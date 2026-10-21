#!/usr/bin/env python3
"""Word count and limits dashboard for JAMA Network manuscripts.

Usage:
    python jama_count.py manuscript.docx [--text-limit 3000] [--abstract-limit 350]
        [--kp-limit 100] [--display-limit 5] [--ref-limit 75] [--title-limit 100]
        [--subtitle-limit 60] [--json]

Accepts .docx, .md, or .txt. Splits the manuscript into sections by heading,
counts words the way Word does (whitespace-separated tokens), and compares
against the limits given. Main text = Introduction through Conclusions
(including Limitations). Everything else (title page, Key Points, abstract,
acknowledgments, references, legends, tables, supplement) is excluded,
matching JAMA Network's definition. Word files are read with tracked changes
accepted: insertions are counted, deletions are not.

Heuristic: section detection relies on standard headings. Always eyeball the
"sections found" list; if a section is missing or merged, count it by hand.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# Canonical section name -> regex matched against a whole heading line
HEADINGS = [
    ("key_points", r"key\s+points"),
    ("abstract", r"(structured\s+)?abstract"),
    ("introduction", r"(introduction|background)"),
    ("methods", r"(methods?|materials\s+and\s+methods|study\s+design\s+and\s+methods)"),
    ("results", r"results?"),
    ("discussion", r"discussion"),
    ("limitations", r"(strengths\s+and\s+)?limitations?"),
    ("conclusions", r"conclusions?"),
    ("acknowledgments", r"(acknowledge?ments?|article\s+information|author\s+contributions?|"
                        r"conflicts?\s+of\s+interest(\s+disclosures?)?|funding(/support)?|"
                        r"role\s+of\s+the\s+funder(/sponsor)?|data\s+sharing\s+statement|declarations?)"),
    ("references", r"(references|bibliography|literature\s+cited)"),
    ("legends", r"(figure\s+legends?|figure\s+titles?(\s+and\s+legends)?|legends?)"),
    ("tables", r"tables?"),
    ("supplement", r"(supplement(ary|al)?(\s+(material|online\s+content|appendix))?(\s*\d+)?|appendix|emethods)"),
]
MAIN_TEXT = ["introduction", "methods", "results", "discussion", "limitations", "conclusions"]

ABSTRACT_HEADINGS = ["Importance", "Objective", "Design", "Setting", "Participants",
                     "Exposure", "Exposures", "Intervention", "Interventions",
                     "Main Outcomes and Measures", "Main Outcome and Measure",
                     "Main Outcomes and Measure", "Main Outcome and Measures",
                     "Results", "Conclusions and Relevance", "Trial Registration",
                     "Design, Setting, and Participants", "Data Sources", "Study Selection",
                     "Data Extraction and Synthesis", "Evidence Review", "Findings", "Observations"]
ALLOWED_ABBREV = {"CI", "OR", "HR", "RR", "SD", "IQR", "US", "UK", "AOR", "aOR", "aHR", "II", "III", "IV"}


def words(text):
    return len(text.split())


def classify_heading(line):
    """Return canonical section name if the line is a heading, else None."""
    t = line.strip().strip("#*_ ").rstrip(":").strip()
    if not t or len(t) > 80:
        return None
    for name, pat in HEADINGS:
        if re.fullmatch(pat, t, flags=re.IGNORECASE):
            return name
    return None


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def para_text(p):
    """Paragraph text with tracked changes accepted: insertions kept, deletions dropped."""
    out = []
    for el in p.iter(W + "t", W + "tab"):
        anc, bad = el.getparent(), False
        while anc is not None and anc is not p:
            if anc.tag in (W + "del", W + "moveFrom"):
                bad = True
                break
            anc = anc.getparent()
        if not bad:
            out.append(" " if el.tag == W + "tab" else (el.text or ""))
    return "".join(out)


def read_docx(path):
    """Return paragraphs as (text, style) plus ('<TABLE>', '') markers, tracked changes accepted."""
    import zipfile
    from lxml import etree
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    paras = []

    def walk(node):
        for ch in node:
            if ch.tag == W + "p":
                st = ch.find(f"{W}pPr/{W}pStyle")
                paras.append((para_text(ch), st.get(W + "val") if st is not None else ""))
            elif ch.tag == W + "tbl":
                paras.append(("<TABLE>", ""))
            elif ch.tag == W + "sdt":
                c = ch.find(W + "sdtContent")
                if c is not None:
                    walk(c)
    walk(root.find(W + "body"))
    return paras, 0, 0


def read_text(path):
    raw = Path(path).read_text(encoding="utf-8", errors="replace")
    paras = []
    for line in raw.splitlines():
        style = "Heading" if line.lstrip().startswith("#") else ""
        paras.append((line, style))
    # markdown tables: count blocks of lines starting with |
    n_tables, in_table = 0, False
    for line in raw.splitlines():
        if line.strip().startswith("|"):
            if not in_table:
                n_tables += 1
            in_table = True
        else:
            in_table = False
    return paras, n_tables, 0


def split_sections(paras):
    """Walk paragraphs; return title, list of (section, [texts]) in order, and main-text table count."""
    title = None
    seen_first = False
    sections = [("front", [])]
    n_tables = 0
    for text, style in paras:
        cur = sections[-1][0]
        if text == "<TABLE>":
            if cur != "supplement":
                n_tables += 1
            if cur == "references":
                sections.append(("displays", []))
            continue
        text = text.replace("\u00a0", " ").strip()
        if not text:
            continue
        name = classify_heading(text)
        if not seen_first:
            seen_first = True
            # the first non-empty paragraph is the title unless it is a section heading
            if name is None:
                title = text.strip("#*_ ").strip()
                continue
        # table/figure captions end the reference list
        if cur == "references" and re.match(r"^(e?table|e?figure)\s*\d", text, flags=re.I):
            sections.append(("displays", []))
        if name:
            sections.append((name, []))
        else:
            sections[-1][1].append(text)
    # No Introduction heading (common in drafts): treat long paragraphs between the
    # front matter / abstract and Methods as the Introduction.
    names = [n for n, _ in sections]
    if "introduction" not in names and "methods" in names:
        mi = names.index("methods")
        for i in range(mi):
            n, lines = sections[i]
            if n in ("front", "abstract", "key_points"):
                if n == "abstract" or n == "key_points":
                    # an abstract runs until its last labeled part; long unlabeled paragraphs after
                    # "Conclusions and Relevance"/"Trial Registration" belong to the Introduction
                    cut = next((j for j, l in enumerate(lines) if re.match(r"^(conclusions and relevance|trial registration)\b", l, re.I)), None)
                    if cut is None:
                        continue
                    keep, move = lines[:cut + 1], [l for l in lines[cut + 1:]]
                else:
                    keep = [l for l in lines if words(l) < 40]
                    move = [l for l in lines if words(l) >= 40]
                if move:
                    sections[i] = (n, keep)
                    sections.insert(i + 1, ("introduction", move))
                    break
    return title, sections, n_tables


def count_refs(lines):
    """Count reference entries: numbered lines, else non-empty lines."""
    numbered = [l for l in lines if re.match(r"^\s*\[?\d{1,3}[\.\)\]]\s+\S", l)]
    return len(numbered) if numbered else len([l for l in lines if l.strip()])


def count_display_items(all_text, n_docx_tables):
    all_text = re.split(r"\n(?:Supplement|eAppendix|Online Supplement)", all_text)[0]
    tables = set(re.findall(r"^\s*Table\s+(\d+)\b", all_text, flags=re.MULTILINE | re.IGNORECASE))
    figures = set(re.findall(r"^\s*Figure\s+(\d+)\b", all_text, flags=re.MULTILINE | re.IGNORECASE))
    n_tables = max(len(tables), n_docx_tables)
    return n_tables, len(figures)


def strip_abstract_labels(text):
    for h in sorted(ABSTRACT_HEADINGS, key=len, reverse=True):
        text = re.sub(r"\b" + re.escape(h) + r"\s*:", " ", text)
    return text


def find_abbreviations(text):
    toks = re.findall(r"\b[A-Za-z]*[A-Z][A-Za-z0-9-]*[A-Z][A-Za-z0-9-]*\b", text)
    return sorted({t for t in toks if t not in ALLOWED_ABBREV and not t.istitle() and len(t) >= 2})


def status(count, limit):
    if limit is None:
        return "-"
    if count <= limit:
        return "OK"
    return f"OVER by {count - limit}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--text-limit", type=int, default=3000)
    ap.add_argument("--abstract-limit", type=int, default=350)
    ap.add_argument("--kp-limit", type=int, default=100)
    ap.add_argument("--display-limit", type=int, default=5)
    ap.add_argument("--ref-limit", type=int, default=None)
    ap.add_argument("--title-limit", type=int, default=100)
    ap.add_argument("--subtitle-limit", type=int, default=60)
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    a = ap.parse_args()

    path = Path(a.path)
    if not path.exists():
        sys.exit(f"File not found: {path}")
    if path.suffix.lower() == ".docx":
        paras, n_docx_tables, table_words = read_docx(path)
    elif path.suffix.lower() in {".md", ".txt"}:
        paras, n_docx_tables, table_words = read_text(path)
    else:
        sys.exit("Unsupported file type. Use .docx, .md, or .txt (extract PDFs with pdftotext first).")

    title, sections, n_main_tables = split_sections(paras)
    n_docx_tables = max(n_docx_tables, n_main_tables)
    by_name = {}
    for name, lines in sections:
        by_name.setdefault(name, []).extend(lines)

    sec_words = {name: sum(words(l) for l in lines) for name, lines in by_name.items()}
    main_words = sum(sec_words.get(s, 0) for s in MAIN_TEXT)
    abstract_text = " ".join(by_name.get("abstract", []))
    kp_text = " ".join(by_name.get("key_points", []))
    abstract_words = words(strip_abstract_labels(abstract_text))
    kp_words = words(re.sub(r"\b(Question|Findings|Meaning)\s*:", " ", kp_text))
    n_refs = count_refs(by_name.get("references", [])) if "references" in by_name else None
    all_text = "\n".join(t.replace("\u00a0", " ").strip() for t, _ in paras if t != "<TABLE>")
    n_tab, n_fig = count_display_items(all_text, n_docx_tables)

    main_title, subtitle = (title or ""), None
    if title and ":" in title:
        main_title, subtitle = [s.strip() for s in title.split(":", 1)]

    warnings = []
    missing = [s for s in ["introduction", "methods", "results", "discussion"] if s not in by_name]
    if missing:
        warnings.append("Sections not detected (count by hand or check headings): " + ", ".join(missing))
    if "abstract" not in by_name:
        warnings.append("No 'Abstract' heading found; abstract count is 0.")
    if "key_points" not in by_name:
        warnings.append("No 'Key Points' heading found (required for Original Investigations).")
    if kp_text and re.search(r"\bP\s*[=<>]|\b95%\s*CI\b|\bCI\b", kp_text):
        warnings.append("Key Points contain a P value or CI; JAMA Key Points should report basic numbers only.")
    abbrevs = find_abbreviations(strip_abstract_labels(abstract_text) + " " + (title or ""))
    if abbrevs:
        warnings.append("Possible abbreviations in title/abstract (JAMA disallows): " + ", ".join(abbrevs))
    if title and title.rstrip().endswith("?"):
        warnings.append("Title is a question; JAMA Network does not allow question titles.")
    if sec_words.get("front", 0) > 0:
        warnings.append(f"{sec_words['front']} words before the first heading were treated as title page and not counted.")

    rows = [
        ("Main text (Intro-Conclusions)", main_words, a.text_limit),
        ("Abstract", abstract_words, a.abstract_limit),
        ("Key Points", kp_words, a.kp_limit),
        ("Title characters (full)", len(title or ""), a.title_limit),
    ]
    if subtitle is not None:
        rows.append(("Subtitle characters", len(subtitle), a.subtitle_limit))
    rows += [
        ("Tables + figures", n_tab + n_fig, a.display_limit),
        ("References", n_refs if n_refs is not None else 0, a.ref_limit),
    ]
    per_section = [(s, sec_words.get(s, 0)) for s in MAIN_TEXT if s in by_name]

    result = {
        "file": str(path),
        "title": title,
        "rows": [{"item": r[0], "count": r[1], "limit": r[2], "status": status(r[1], r[2])} for r in rows],
        "tables": n_tab, "figures": n_fig,
        "main_text_by_section": {s: w for s, w in per_section},
        "sections_found": [n for n, _ in sections if n != "front"],
        "warnings": warnings,
    }
    if a.json:
        print(json.dumps(result, indent=2))
        return

    print(f"File: {path.name}")
    print(f"Title: {title}")
    print()
    print(f"{'Item':34} {'Count':>7} {'Limit':>7}  Status")
    print("-" * 64)
    for r in result["rows"]:
        lim = "-" if r["limit"] is None else r["limit"]
        print(f"{r['item']:34} {r['count']:>7} {lim:>7}  {r['status']}")
    print(f"  (tables: {n_tab}, figures: {n_fig})")
    print()
    print("Main text by section:")
    for s, w in per_section:
        pct = 100 * w / main_words if main_words else 0
        print(f"  {s:14} {w:>6} words  ({pct:4.1f}%)")
    print()
    print("Sections found, in order: " + " > ".join(result["sections_found"]))
    if warnings:
        print()
        print("Warnings:")
        for w in warnings:
            print("  - " + w)


if __name__ == "__main__":
    main()
