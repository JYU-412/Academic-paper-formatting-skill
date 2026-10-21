#!/usr/bin/env python3
"""Word count, limits, and compliance scan for sociology and demography manuscripts.

Usage:
  python soc_count.py manuscript.docx --count text,notes,refs --text-limit 15000 \
      --abstract-limit 200 --kw-min 4 --kw-max 5 [--display-limit N] [--ref-limit N] \
      [--authors "Smith;Lee"] [--json]

--count lists the parts that count toward the journal's limit (comma separated):
  text      main text (Introduction/Background through Discussion/Conclusion)
  abstract  the abstract
  notes     a NOTES/ENDNOTES section plus Word footnotes and endnotes
  refs      the reference list
  appendix  appendices in the main file
  tables    words inside tables
Examples: ASR "text,notes,refs"; Social Forces "text,notes,refs"; ESR "text,notes,refs";
BJS "abstract,text,notes,refs,appendix"; JHSB "text,notes,refs"; Demography and PRPR "text".

Reads .docx with tracked changes ACCEPTED (insertions counted, deletions ignored),
or .md/.txt. Also checks keywords count, author names in a blinded file, and notes
longer than --note-max words (ASR and Sociological Methodology: 100).
Section detection relies on standard headings; check the "sections found" line.
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

HEADINGS = [
    ("keywords", r"key\s*words?"),
    ("statement", r"(research\s+)?highlights|relevance\s+statement"),
    ("abstract", r"(structured\s+)?abstract"),
    ("introduction", r"(introduction|background|theoretical\s+background|literature\s+review|theory(\s+and\s+hypotheses)?|prior\s+research)"),
    ("methods", r"(methods?|data|data\s+and\s+methods?|data,\s+measures,?\s+and\s+methods?|measures|analytic\s+(strategy|approach)|research\s+design\s+and\s+methods|materials\s+and\s+methods|design\s+and\s+methods|the\s+present\s+study)"),
    ("results", r"(results?|findings)"),
    ("discussion", r"(discussion|discussion\s+and\s+(implications|conclusions?)|general\s+discussion|conclusion\s+and\s+discussion)"),
    ("implications", r"(implications|policy\s+implications|practice\s+implications|implications\s+for\s+(policy|practice|research)(\s+and\s+(policy|practice|research))?)"),
    ("limitations", r"(strengths\s+and\s+)?limitations?"),
    ("conclusions", r"conclusions?"),
    ("backmatter", r"(funding|conflicts?\s+of\s+interest|data\s+availability(\s+statement)?|acknowledge?ments?|"
                   r"author\s+notes|author\s+contributions?|article\s+information|declarations?|ethics(\s+statement)?)"),
    ("notes", r"(notes|endnotes|footnotes)"),
    ("references", r"(references|bibliography|literature\s+cited|works\s+cited)"),
    ("appendix", r"(appendix(\s+[a-z0-9]+)?(\s*[.:].*)?|appendices)"),
    ("legends", r"(figure\s+legends?|figure\s+captions?|table\s+titles\s+and\s+figure\s+captions|figure\s+titles?(\s+and\s+legends)?)"),
    ("tables", r"tables?(\s*/\s*figures)?"),
    ("supplement", r"(supplement(ary|al)?(\s+(material|materials|online\s+content|appendix))?(\s*\d+)?|online\s+supplement|online\s+appendix)"),
]
MAIN = ["introduction", "methods", "results", "discussion", "implications", "limitations", "conclusions"]
ABS_SUB = ["background and objectives", "research design and methods", "results", "discussion and implications",
           "objectives", "objective", "methods", "discussion", "background", "conclusions", "conclusion"]
TABLE_WORDS = [0]
PARTS = ("text", "abstract", "notes", "refs", "appendix", "tables")


def words(t):
    return len(t.split())


def norm(t):
    return re.sub(r"\s+", " ", t.replace("\u00a0", " ")).strip()


def classify(line):
    t = norm(line).strip("#*_ ").rstrip(":").strip()
    if not t or len(t) > 90:
        return None, t
    for name, pat in HEADINGS:
        if re.fullmatch(pat, t, flags=re.IGNORECASE):
            return name, t
    return None, t


def para_text(p):
    out = []
    for el in p.iter():
        if el.tag == W + "t":
            # skip text inside moved-from or deleted containers
            anc = el.getparent()
            bad = False
            while anc is not None and anc is not p:
                if anc.tag in (W + "del", W + "moveFrom"):
                    bad = True
                    break
                anc = anc.getparent()
            if not bad and el.text:
                out.append(el.text)
        elif el.tag in (W + "tab",):
            out.append(" ")
    return "".join(out)


def read_docx(path):
    from lxml import etree
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    items = []  # ("p", text) or ("tbl", n_words)

    def walk(node):
        for ch in node:
            if ch.tag == W + "p":
                items.append(("p", para_text(ch)))
            elif ch.tag == W + "tbl":
                items.append(("tbl", sum(words(para_text(p)) for p in ch.iter(W + "p"))))
            elif ch.tag == W + "sdt":
                c = ch.find(W + "sdtContent")
                if c is not None:
                    walk(c)
    walk(body)
    return items


def read_text(path):
    items, in_tbl = [], False
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().startswith("|"):
            if not in_tbl:
                items.append(("tbl", 0))
            in_tbl = True
            continue
        in_tbl = False
        items.append(("p", line))
    return items


def by_len(section):
    return len(section[1])


def split(items):
    title, sections, cur = None, [["front", []]], "front"
    abs_seen, n_tbl_main = set(), 0
    for kind, val in items:
        if kind == "tbl":
            if cur not in ("supplement",):
                n_tbl_main += 1
                TABLE_WORDS[0] += val
            if cur == "references":
                cur = "displays"
                sections.append(["displays", []])
            continue
        text = norm(val)
        if not text:
            continue
        name, clean = classify(text)
        low = clean.lower()
        if title is None and name is None and cur == "front":
            title = clean
            continue
        # inline "Keywords: a; b; c" line: record it, then the next lines belong to no section
        # until a real heading appears (keeps them out of the abstract count)
        if re.match(r"^key\s*words?\s*:", low):
            sections.append(["keywords", [re.sub(r"^key\s*words?\s*:\s*", "", text, flags=re.I)]])
            cur = "between"
            sections.append(["between", []])
            continue
        if re.match(r"^((research )?highlights|relevance statement)\s*:", low):
            sections.append(["statement", [re.sub(r"^[^:]+:\s*", "", text)]])
            cur = "statement"
            continue
        # abstract subheadings stay inside the abstract the first time they appear
        if cur == "abstract" and low in ABS_SUB and low not in abs_seen and name not in ("keywords", "statement", "introduction"):
            abs_seen.add(low)
            continue
        if cur == "abstract" and re.match(r"^[A-Za-z][A-Za-z ,()]{0,45}:\s", text):
            sections[-1][1].append(re.sub(r"^[^:]+:\s*", "", text))
            continue
        # captions or supplement items end the reference list
        if cur == "references" and re.match(r"^(e?table|e?figure|supplementary (table|figure))\s*\d", low):
            cur = "displays"
            sections.append(["displays", []])
        if name:
            cur = name
            sections.append([name, []])
            continue
        if cur == "keywords":
            # a Keywords heading holds one line of keywords; anything after it is unsectioned
            if by_len(sections[-1]) >= 1:
                cur = "between"
                sections.append(["between", []])
        sections[-1][1].append(text)
    # No Introduction heading (common in drafts): treat long paragraphs before Methods
    # that sit outside the abstract and keywords as the Introduction.
    names = [n for n, _ in sections]
    if "introduction" not in names and "methods" in names:
        mi = names.index("methods")
        for i in range(mi):
            n, lines = sections[i]
            if n in ("front", "between"):
                move = [l for l in lines if words(l) >= 40]
                if move:
                    sections[i] = [n, [l for l in lines if words(l) < 40]]
                    sections.insert(i + 1, ["introduction", move])
                    break
    return title, sections, n_tbl_main


def word_notes(path):
    """Words in Word's own footnotes and endnotes (not separators)."""
    if Path(path).suffix.lower() != ".docx":
        return 0, 0
    from lxml import etree
    n_notes, n_words = 0, 0
    with zipfile.ZipFile(path) as z:
        for part in ("word/footnotes.xml", "word/endnotes.xml"):
            if part not in z.namelist():
                continue
            root = etree.fromstring(z.read(part))
            for f in root:
                if f.get(W + "type") in ("separator", "continuationSeparator", "continuationNotice"):
                    continue
                n_notes += 1
                n_words += words(" ".join(para_text(p) for p in f.iter(W + "p")))
    return n_notes, n_words


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--count", default="text", help="parts counted toward the limit: " + ",".join(PARTS))
    ap.add_argument("--text-limit", type=int)
    ap.add_argument("--abstract-limit", type=int)
    ap.add_argument("--kw-min", type=int)
    ap.add_argument("--kw-max", type=int)
    ap.add_argument("--display-limit", type=int)
    ap.add_argument("--ref-limit", type=int)
    ap.add_argument("--note-max", type=int, help="maximum words per note (ASR, Sociological Methodology: 100)")
    ap.add_argument("--title-max-words", type=int, help="Socius, SMR: 20")
    ap.add_argument("--authors", default="", help="semicolon-separated surnames to flag (anonymized file)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    parts = [x.strip() for x in a.count.split(",") if x.strip()]
    bad = [x for x in parts if x not in PARTS]
    if bad:
        sys.exit(f"Unknown --count part(s): {', '.join(bad)}. Use: {', '.join(PARTS)}")

    p = Path(a.path)
    if not p.exists():
        sys.exit(f"File not found: {p}")
    if p.suffix.lower() == ".docx":
        items = read_docx(p)
    elif p.suffix.lower() in (".md", ".txt"):
        items = read_text(p)
    else:
        sys.exit("Use .docx, .md, or .txt (extract PDFs with pdftotext first).")

    title, sections, n_tbl = split(items)
    by = {}
    for n, lines in sections:
        by.setdefault(n, []).extend(lines)
    sw = {n: sum(words(l) for l in ls) for n, ls in by.items()}
    main_w = sum(sw.get(s, 0) for s in MAIN)
    abs_w = sw.get("abstract", 0)
    raw_refs = [l for l in by.get("references", []) if l.strip()]
    numbered = [l for l in raw_refs if re.match(r"^\s*\[?\d{1,3}[.)\]]\s+\S", l)]
    yearish = [l for l in raw_refs if re.search(r"(\((19|20)\d\d[a-z]?\)|\b(19|20)\d\d[a-z]?\.|\bn\.d\.|forthcoming)", l, re.I)]
    ref_lines = numbered if numbered else (yearish if yearish else raw_refs)
    n_refs = len(ref_lines)
    ref_w = sum(words(l) for l in ref_lines)
    note_lines = [l for l in by.get("notes", []) if l.strip()]
    wn_count, wn_words = word_notes(p)
    notes_w = sum(words(l) for l in note_lines) + wn_words
    table_w = TABLE_WORDS[0]

    all_text = "\n".join(norm(v) for k, v in items if k == "p")
    pre_supp = all_text.split("\nSupplement")[0] if "\nSupplement" in all_text else all_text
    cap_tables = set(re.findall(r"^Table\s+([\dIVXL]+)\b", pre_supp, flags=re.M | re.I))
    figs = set(re.findall(r"^Figure\s+([\dIVXL]+)\b", pre_supp, flags=re.M | re.I))
    n_t = max(len(cap_tables), n_tbl)
    n_f = len(figs)

    contrib = {"text": main_w, "abstract": abs_w, "notes": notes_w, "refs": ref_w,
               "appendix": sw.get("appendix", 0), "tables": table_w}
    counted = sum(contrib[x] for x in parts)
    label = " + ".join(parts)

    def st(c, lim):
        return "-" if lim is None else ("OK" if c <= lim else f"OVER by {c - lim}")

    rows = [(f"Counted ({label})", counted, a.text_limit), ("Abstract", abs_w, a.abstract_limit),
            ("Tables + figures", n_t + n_f, a.display_limit), ("References", n_refs, a.ref_limit)]

    warn = []
    miss = [s for s in ["methods", "results", "discussion"] if s not in by]
    if miss:
        warn.append("Sections not detected: " + ", ".join(miss) + " (check headings or count by hand)")
    if "abstract" not in by:
        warn.append("No Abstract heading found (some journals want the abstract on the title page or in the portal; check).")
    kw = ", ".join(by.get("keywords", []))
    kws = [k.strip() for k in re.split(r"[;,]", kw) if k.strip()]
    if a.kw_min or a.kw_max:
        if not kws:
            warn.append("No Keywords line found.")
        elif (a.kw_min and len(kws) < a.kw_min) or (a.kw_max and len(kws) > a.kw_max):
            warn.append(f"{len(kws)} keywords; this journal asks for {a.kw_min or 0}-{a.kw_max or '?'}.")
    if a.note_max:
        long_notes = [l for l in note_lines if words(l) > a.note_max]
        if long_notes:
            warn.append(f"{len(long_notes)} note(s) over {a.note_max} words (e.g., \"{long_notes[0][:50]}...\").")
    if wn_count:
        warn.append(f"{wn_count} Word footnote/endnote(s) ({wn_words} words) found. Some journals want notes in a separate NOTES section instead of Word's note function (JHSB says so explicitly); others want footnotes only (SMR, Demography, PRPR).")
    if a.title_max_words and title and words(title) > a.title_max_words:
        warn.append(f"Title is {words(title)} words; limit {a.title_max_words}.")
    for name in [n.strip() for n in a.authors.split(";") if n.strip()]:
        c = len(re.findall(r"\b" + re.escape(name) + r"\b", all_text))
        if c:
            warn.append(f"Author name '{name}' appears {c} time(s): cite your own work in the third person or as the journal directs in the blinded file.")
    if sw.get("front", 0) > 0:
        warn.append(f"{sw['front']} words before the first heading treated as title page (not counted).")

    res = {"title": title, "title_words": words(title or ""), "parts": contrib, "counted_parts": parts,
           "rows": [{"item": r[0], "count": r[1], "limit": r[2], "status": st(r[1], r[2])} for r in rows],
           "tables": n_t, "figures": n_f, "by_section": {s: sw[s] for s in MAIN if s in sw},
           "sections_found": [n for n, _ in sections if n not in ("front",)], "warnings": warn}
    if a.json:
        print(json.dumps(res, indent=2))
        return
    print(f"Title ({res['title_words']} words): {title}\n")
    print(f"{'Item':40} {'Count':>7} {'Limit':>7}  Status")
    print("-" * 70)
    for r in res["rows"]:
        print(f"{r['item']:40} {r['count']:>7} {('-' if r['limit'] is None else r['limit']):>7}  {r['status']}")
    print(f"  (tables: {n_t}, figures: {n_f})\n")
    print("Parts: " + ", ".join(f"{k} {v}" for k, v in contrib.items()))
    print("Main text by section:")
    for s_, w in res["by_section"].items():
        print(f"  {s_:13} {w:>6}  ({100 * w / main_w if main_w else 0:4.1f}%)")
    seen = []
    for n in res["sections_found"]:
        if not seen or seen[-1] != n:
            seen.append(n)
    print("\nSections found: " + " > ".join(seen))
    if warn:
        print("\nWarnings:")
        for w in warn:
            print("  - " + w)


if __name__ == "__main__":
    main()
