#!/usr/bin/env python3
"""Word count, limits, and GSA compliance scan for gerontology manuscripts.

Usage:
  python gsa_count.py manuscript.docx --text-limit 5000 --abstract-limit 250 \
      --display-limit 5 --ref-limit 50 [--mode text|text+front|text+refs] \
      [--statement-limit 100] [--authors "Smith;Lee"] [--json]

--mode text        main text only (JGB, The Gerontologist, Innovation in Aging)
--mode text+front  title page + abstract + main text (JGA Biological and Medical Sciences)
--mode text+refs   main text + references (Public Policy & Aging Report)

Reads .docx with tracked changes ACCEPTED (insertions counted, deletions ignored),
or .md/.txt. Main text = Introduction through Discussion/Implications/Conclusions.
Also scans for ageist terms, first-person language, author names (anonymization),
and keyword rules. Section detection relies on standard headings; check the
"sections found" line and count by hand if it looks wrong.
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
    ("statement", r"(innovation\s+and\s+)?translational\s+significance(\s+statement)?"),
    ("abstract", r"(structured\s+)?abstract"),
    ("introduction", r"(introduction|background)"),
    ("methods", r"(methods?|research\s+design\s+and\s+methods|materials\s+and\s+methods|design\s+and\s+methods|the\s+present\s+study)"),
    ("results", r"results?"),
    ("discussion", r"(discussion|discussion\s+and\s+implications|general\s+discussion)"),
    ("implications", r"(implications|policy\s+implications|practice\s+implications|implications\s+for\s+(policy|practice|research)(\s+and\s+(policy|practice|research))?)"),
    ("limitations", r"(strengths\s+and\s+)?limitations?"),
    ("conclusions", r"conclusions?"),
    ("backmatter", r"(funding|conflicts?\s+of\s+interest|data\s+availability(\s+statement)?|acknowledge?ments?|"
                   r"author\s+notes|author\s+contributions?|article\s+information|declarations?|ethics(\s+statement)?)"),
    ("references", r"(references|bibliography|literature\s+cited)"),
    ("legends", r"(figure\s+legends?|figure\s+captions?|table\s+titles\s+and\s+figure\s+captions|figure\s+titles?(\s+and\s+legends)?)"),
    ("tables", r"tables?(\s*/\s*figures)?"),
    ("supplement", r"(supplement(ary|al)?(\s+(material|materials|online\s+content|appendix))?(\s*\d+)?|appendix|online\s+supplement)"),
]
MAIN = ["introduction", "methods", "results", "discussion", "implications", "limitations", "conclusions"]
ABS_SUB = ["background and objectives", "research design and methods", "results", "discussion and implications",
           "objectives", "objective", "methods", "discussion", "background", "conclusions", "conclusion"]
AGEIST = [r"\belderly\b", r"\belders?\b", r"\bseniors?\b", r"\bsenior citizens?\b", r"\bthe aged\b", r"\bgeriatric (patients|people|population)\b"]
FIRST_PERSON = r"\b(we|our|us|ours|ourselves|I|my)\b"


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
        if re.match(r"^(innovation and )?translational significance(\s+statement)?\s*:", low):
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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--text-limit", type=int)
    ap.add_argument("--abstract-limit", type=int, default=250)
    ap.add_argument("--statement-limit", type=int, default=None, help="Innovation in Aging: 100")
    ap.add_argument("--display-limit", type=int)
    ap.add_argument("--ref-limit", type=int)
    ap.add_argument("--mode", choices=["text", "text+front", "text+refs"], default="text")
    ap.add_argument("--authors", default="", help="semicolon-separated surnames to flag (anonymized file)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

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
    front_w = sw.get("front", 0) + words(title or "")
    stmt_w = sw.get("statement", 0)
    raw_refs = [l for l in by.get("references", []) if l.strip()]
    numbered = [l for l in raw_refs if re.match(r"^\s*\[?\d{1,3}[.)\]]\s+\S", l)]
    apa = [l for l in raw_refs if re.search(r"\((19|20)\d\d[a-z]?\)|\(n\.d\.\)", l)]
    ref_lines = numbered if numbered else (apa if apa else raw_refs)
    n_refs = len(ref_lines)

    all_text = "\n".join(norm(v) for k, v in items if k == "p")
    pre_supp = all_text.split("\nSupplement")[0] if "\nSupplement" in all_text else all_text
    cap_tables = set(re.findall(r"^Table\s+(\d+)\b", pre_supp, flags=re.M | re.I))
    figs = set(re.findall(r"^Figure\s+(\d+)\b", pre_supp, flags=re.M | re.I))
    n_t = max(len(cap_tables), n_tbl)
    n_f = len(figs)

    if a.mode == "text+front":
        counted, label = main_w + abs_w + front_w, "Title page + abstract + text"
    elif a.mode == "text+refs":
        counted, label = main_w + sum(words(l) for l in ref_lines), "Text + references"
    else:
        counted, label = main_w, "Main text"

    def st(c, lim):
        return "-" if lim is None else ("OK" if c <= lim else f"OVER by {c - lim}")

    rows = [(label, counted, a.text_limit), ("Abstract", abs_w, a.abstract_limit)]
    if a.statement_limit:
        rows.append(("Translational Significance", stmt_w, a.statement_limit))
    rows += [("Tables + figures", n_t + n_f, a.display_limit), ("References", n_refs, a.ref_limit)]

    warn = []
    miss = [s for s in ["introduction", "methods", "results", "discussion"] if s not in by]
    if miss:
        warn.append("Sections not detected: " + ", ".join(miss) + " (check headings or count by hand)")
    if "abstract" not in by:
        warn.append("No Abstract heading found.")
    if a.statement_limit and "statement" not in by:
        warn.append("No Translational Significance statement found (Innovation in Aging requires one, <=100 words, below the abstract).")
    kw = ", ".join(by.get("keywords", []))
    if not kw:
        warn.append("No Keywords line found (3-5 required by all GSA journals).")
    else:
        kws = [k.strip().lower() for k in re.split(r"[;,]", kw) if k.strip()]
        if not 3 <= len(kws) <= 5:
            warn.append(f"{len(kws)} keywords; GSA journals require 3-5.")
        tl = (title or "").lower()
        bad = [k for k in kws if k in tl or k in ("older adults", "aging", "ageing", "elders", "older adult")]
        if bad:
            warn.append("Keywords that repeat the title or are banned generic terms: " + ", ".join(bad))
    body = " ".join(" ".join(by.get(s, [])) for s in MAIN + ["abstract", "statement"]) + " " + (title or "")
    for pat in AGEIST:
        hits = re.findall(pat, body, flags=re.I)
        if hits:
            warn.append(f"Ageist term '{hits[0]}' x{len(hits)} (GSA bans elderly/elder(s)/seniors/the aged; use 'older adults' with an age range).")
    fp = re.findall(FIRST_PERSON, " ".join(" ".join(by.get(s, [])) for s in MAIN))
    if fp:
        warn.append(f"First-person words x{len(fp)} (Innovation in Aging asks authors to avoid first person in the anonymized file; other GSA journals allow it).")
    for name in [n.strip() for n in a.authors.split(";") if n.strip()]:
        c = len(re.findall(r"\b" + re.escape(name) + r"\b", all_text))
        if c:
            warn.append(f"Author name '{name}' appears {c} time(s): remove or anonymize self-citations in the blinded file.")
    if sw.get("front", 0) > 0 and a.mode != "text+front":
        warn.append(f"{sw['front']} words before the first heading treated as title page (not counted).")

    res = {"title": title, "title_words": words(title or ""), "rows": [{"item": r[0], "count": r[1], "limit": r[2], "status": st(r[1], r[2])} for r in rows],
           "tables": n_t, "figures": n_f, "by_section": {s: sw[s] for s in MAIN if s in sw},
           "sections_found": [n for n, _ in sections if n not in ("front",)], "warnings": warn}
    if a.json:
        print(json.dumps(res, indent=2))
        return
    print(f"Title ({res['title_words']} words; APA suggests <=12): {title}\n")
    print(f"{'Item':30} {'Count':>7} {'Limit':>7}  Status")
    print("-" * 60)
    for r in res["rows"]:
        print(f"{r['item']:30} {r['count']:>7} {('-' if r['limit'] is None else r['limit']):>7}  {r['status']}")
    print(f"  (tables: {n_t}, figures: {n_f})\n")
    print("Main text by section:")
    for s, w in res["by_section"].items():
        print(f"  {s:13} {w:>6}  ({100 * w / main_w if main_w else 0:4.1f}%)")
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
