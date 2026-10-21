#!/usr/bin/env python3
"""Page layout and heading checker for journal manuscripts (.docx).

Usage:
    python layout_check.py manuscript.docx --journal jama   # JAMA Network journals
    python layout_check.py manuscript.docx --journal jga    # Journals of Gerontology Series A
    python layout_check.py manuscript.docx --journal jgb    # Journals of Gerontology Series B
    python layout_check.py manuscript.docx --journal tg     # The Gerontologist
    python layout_check.py manuscript.docx --journal ia     # Innovation in Aging
    python layout_check.py manuscript.docx --journal ppar   # Public Policy & Aging Report
    add --blinded when checking the anonymized file

Checks the file as Word would render it (styles and defaults resolved):
  page: paper size, margins, orientation of text pages
  text: body font and size, line spacing, justification, highlighting
  numbering: page numbers in a header/footer, line numbers
  structure: page breaks before the sections that must start on a new page,
             tables each on their own page (GSA), footnotes/endnotes (GSA bans them)
  headings: detected heading levels and APA 7 level formatting (GSA journals) or
            consistency (JAMA), title case
  file hygiene: unresolved tracked changes, comments, and author names in the
                document properties (for blinded files)
Findings are suggestions to review; rules that a journal does not state are marked "suggested".
"""
import argparse
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

# Journal rules. "req" = stated in the journal's instructions (checked Oct 2026); "sug" = common practice.
RULES = {
    "jama": dict(name="JAMA Network", font=None, sizes=(10, 11, 12), size_src="req", font_src=None,
                 double="req", ragged="req", margins=None, pagenum="req", lines=None, footnotes=None,
                 newpage=["key_points", "abstract", "text", "references", "legends", "tables"], each_table_page=False,
                 apa_headings=False),
    "jga": dict(name="Journals of Gerontology Series A", font="Times New Roman", sizes=(12,), size_src="req", font_src="req",
                double="req", ragged="sug", margins=None, pagenum="sug", lines=None, footnotes="req",
                newpage=["abstract", "references", "legends", "tables"], each_table_page=True, apa_headings=False),
    "jgb": dict(name="Journals of Gerontology Series B", font="Times New Roman", sizes=(12,), size_src="req", font_src="req",
                double="req", ragged="sug", margins=1440, pagenum="sug", lines="none", footnotes="req",
                newpage=["abstract", "references", "legends", "tables"], each_table_page=True, apa_headings=True),
    "tg": dict(name="The Gerontologist", font=None, sizes=(12,), size_src="sug", font_src=None,
               double="sug", ragged="sug", margins=1440, pagenum="sug", lines=None, footnotes="req",
               newpage=["references", "legends", "tables"], each_table_page=True, apa_headings=True),
    "ia": dict(name="Innovation in Aging", font=None, sizes=(12,), size_src="sug", font_src=None,
               double="sug", ragged="sug", margins=1440, pagenum="sug", lines=None, footnotes="req",
               newpage=["abstract", "references", "tables"], each_table_page=True, apa_headings=True),
    "ppar": dict(name="Public Policy & Aging Report", font=None, sizes=(12,), size_src="sug", font_src=None,
                 double="req", ragged="sug", margins=1440, pagenum="sug", lines=None, footnotes="req",
                 newpage=["references", "tables"], each_table_page=True, apa_headings=True),
}

SECTION_PATTERNS = {
    "key_points": r"key points",
    "abstract": r"(structured )?abstract",
    "text": r"(introduction|background)",
    "references": r"(references|bibliography)",
    "legends": r"(figure legends?|figure captions?|figure titles?( and legends)?|table titles and figure captions)",
}
SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at", "by", "in", "of", "off",
               "on", "per", "to", "up", "via", "vs", "vs."}
SHADE_OK = {"auto", "ffffff", "none", ""}


class Styles:
    def __init__(self, root):
        self.root = root
        self.by_id = {}
        self.default_p = None
        self.default_char = None
        if root is None:
            return
        for st in root.findall(W + "style"):
            self.by_id[st.get(W + "styleId")] = st
            if st.get(W + "default") == "1":
                if st.get(W + "type") == "paragraph":
                    self.default_p = st.get(W + "styleId")
                elif st.get(W + "type") == "character":
                    self.default_char = st.get(W + "styleId")
        dd = root.find(W + "docDefaults")
        self.dd_rpr = dd.find(f"{W}rPrDefault/{W}rPr") if dd is not None else None
        self.dd_ppr = dd.find(f"{W}pPrDefault/{W}pPr") if dd is not None else None

    def chain(self, sid):
        out, seen = [], set()
        while sid and sid not in seen and sid in self.by_id:
            seen.add(sid)
            st = self.by_id[sid]
            out.append(st)
            b = st.find(W + "basedOn")
            sid = b.get(W + "val") if b is not None else None
        return out


def first(*vals):
    for v in vals:
        if v is not None:
            return v
    return None


def get_ppr_prop(ppr, styles, pstyle, tag, attr):
    """Resolve a paragraph property: direct -> style chain -> docDefaults."""
    if ppr is not None:
        el = ppr.find(W + tag)
        if el is not None and el.get(W + attr) is not None:
            return el.get(W + attr)
    for st in styles.chain(pstyle or styles.default_p):
        el = st.find(f"{W}pPr/{W}{tag}")
        if el is not None and el.get(W + attr) is not None:
            return el.get(W + attr)
    if styles.dd_ppr is not None:
        el = styles.dd_ppr.find(W + tag)
        if el is not None and el.get(W + attr) is not None:
            return el.get(W + attr)
    return None


def run_props(run, styles, pstyle):
    """Resolve font, size, bold, italic, highlight for a run."""
    rpr = run.find(W + "rPr")
    chains = []
    if rpr is not None and rpr.find(W + "rStyle") is not None:
        chains += styles.chain(rpr.find(W + "rStyle").get(W + "val"))
    chains += styles.chain(pstyle or styles.default_p)

    def look(tag, attr=None):
        cands = [rpr] + [st.find(W + "rPr") for st in chains] + [styles.dd_rpr]
        for c in cands:
            if c is None:
                continue
            el = c.find(W + tag)
            if el is not None:
                if attr is None:
                    v = el.get(W + "val")
                    return v not in ("0", "false", "none")
                if el.get(W + attr) is not None:
                    return el.get(W + attr)
        return None

    font = look("rFonts", "ascii") or look("rFonts", "hAnsi")
    if font is None:
        theme = look("rFonts", "asciiTheme")
        font = f"(theme font: {theme})" if theme else None
    sz = look("sz", "val")
    return dict(font=font, size=int(sz) / 2 if sz else None, b=bool(look("b")), i=bool(look("i")),
                hl=look("highlight", "val"))


def para_text(p):
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
    return "".join(out).replace(" ", " ").strip()


def visible_runs(p):
    runs = []
    for r in p.iter(W + "r"):
        anc, bad = r.getparent(), False
        while anc is not None and anc is not p:
            if anc.tag in (W + "del", W + "moveFrom"):
                bad = True
                break
            anc = anc.getparent()
        if bad:
            continue
        t = "".join((x.text or "") for x in r.findall(W + "t"))
        if t.strip():
            runs.append((r, t))
    return runs


def is_title_case(t):
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", t)
    if not words:
        return True
    for k, w in enumerate(words):
        if k > 0 and w.lower() in SMALL_WORDS:
            continue
        if len(w) >= 4 and w[0].islower():
            return False
        if k == 0 and w[0].islower():
            return False
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--journal", choices=sorted(RULES), required=True)
    ap.add_argument("--blinded", action="store_true", help="this is the anonymized file")
    a = ap.parse_args()
    rules = RULES[a.journal]
    p = Path(a.path)
    if p.suffix.lower() != ".docx":
        sys.exit("layout_check.py reads .docx files only.")
    from lxml import etree
    z = zipfile.ZipFile(p)
    names = z.namelist()
    root = etree.fromstring(z.read("word/document.xml"))
    styles = Styles(etree.fromstring(z.read("word/styles.xml")) if "word/styles.xml" in names else None)
    theme_fonts = {}
    th = [n for n in names if re.match(r"word/theme/theme\d*\.xml", n)]
    if th:
        A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
        tr = etree.fromstring(z.read(th[0]))
        for kind in ("major", "minor"):
            el = tr.find(f".//{A}{kind}Font/{A}latin")
            if el is not None:
                theme_fonts[kind] = el.get("typeface")
    body = root.find(W + "body")
    out = defaultdict(list)

    def add(cat, msg, src=None):
        tag = {"req": " (journal requirement)", "sug": " (suggested; not stated by the journal)"}.get(src, "")
        out[cat].append(msg + tag)

    # ---------- page setup
    sects = list(root.iter(W + "sectPr"))
    sizes, margins_bad, has_pgnum_ref, lnnum = Counter(), [], False, False
    portrait_sections = 0
    for sp in sects:
        pg = sp.find(W + "pgSz")
        if pg is not None:
            w, h = int(pg.get(W + "w", 0)), int(pg.get(W + "h", 0))
            if pg.get(W + "orient") == "landscape" or w > h:
                continue  # landscape pages are fine for wide tables
            portrait_sections += 1
            sizes["US Letter" if (w, h) == (12240, 15840) else ("A4" if abs(w - 11906) < 30 and abs(h - 16838) < 30 else f"{w / 1440:.2f} x {h / 1440:.2f} in")] += 1
        mar = sp.find(W + "pgMar")
        if mar is not None and rules["margins"]:
            vals = {k: int(mar.get(W + k, 0)) for k in ("top", "bottom", "left", "right")}
            if any(abs(v - rules["margins"]) > 20 for v in vals.values()):
                margins_bad.append(", ".join(f"{k} {v / 1440:.2f} in" for k, v in vals.items()))
        if sp.find(W + "lnNumType") is not None:
            lnnum = True
        if sp.findall(W + "footerReference") or sp.findall(W + "headerReference"):
            has_pgnum_ref = True
    if sizes:
        add("Page setup", "Paper size: " + ", ".join(f"{k} ({v} section{'s' if v > 1 else ''})" for k, v in sizes.items()) + ". US Letter or A4 are both accepted by these journals.")
    if margins_bad:
        add("Page setup", f"Margins are not 1 inch on every side: {margins_bad[0]}.", "req" if a.journal == "jgb" else "sug")
    if lnnum and rules["lines"] == "none":
        add("Page setup", "Line numbering is on. JGB Social Sciences asks for no line numbering; turn it off (Layout > Line Numbers > None).", "req")
    elif lnnum:
        add("Page setup", "Line numbering is on. That is fine for review unless the journal says otherwise.")

    # page numbers: look for a PAGE field in headers/footers
    pg_field = False
    for n in names:
        if re.match(r"word/(header|footer)\d*\.xml", n):
            x = z.read(n).decode("utf8", "ignore")
            if re.search(r"instrText[^>]*>\s*PAGE\b|fldSimple[^>]*instr=\"\s*PAGE\b", x):
                pg_field = True
    if not pg_field:
        add("Page setup", "No page numbers found in the header or footer. Insert page numbers (Insert > Page Number)"
            + (", numbered consecutively from the title page." if a.journal == "jama" else "; reviewers cite comments by page."),
            "req" if rules["pagenum"] == "req" else "sug")

    # ---------- body text paragraphs (top-level only, not tables)
    items = []

    def walk(node):
        for ch in node:
            if ch.tag == W + "p":
                items.append(("p", ch))
            elif ch.tag == W + "tbl":
                items.append(("tbl", ch))
            elif ch.tag == W + "sdt":
                c = ch.find(W + "sdtContent")
                if c is not None:
                    walk(c)
    walk(body)

    fonts, fsizes, spacing, just, hl_count = Counter(), Counter(), Counter(), Counter(), 0
    headings = []
    in_refs = False
    in_supp = False
    paras_info = []
    for kind, node in items:
        if kind != "p":
            paras_info.append(("tbl", node, ""))
            continue
        t = para_text(node)
        paras_info.append(("p", node, t))
        if not t:
            continue
        low = t.lower().rstrip(":")
        if re.fullmatch(r"(supplement(ary|al)?( material| online content)?( \d+)?|emethods|eappendix)", low):
            in_supp = True
        if in_supp:
            continue
        ppr = node.find(W + "pPr")
        pstyle = ppr.find(W + "pStyle").get(W + "val") if ppr is not None and ppr.find(W + "pStyle") is not None else None
        runs = visible_runs(node)
        props = [run_props(r, styles, pstyle) for r, _ in runs]
        nwords = len(t.split())
        is_heading_style = bool(pstyle and re.match(r"(heading|title)", pstyle, re.I))
        all_bold = bool(props) and all(pr["b"] for pr in props)
        all_ital = bool(props) and all(pr["i"] for pr in props)
        jc = get_ppr_prop(ppr, styles, pstyle, "jc", "val") or "left"
        if (is_heading_style or all_bold) and nwords <= 14 and not re.match(r"^(table|figure|e?table|e?figure)\s*\d", low):
            headings.append(dict(text=t, jc=jc, b=all_bold or is_heading_style, i=all_ital, style=pstyle,
                                 ends_period=t.endswith(".")))
            if re.fullmatch(SECTION_PATTERNS["references"], low):
                in_refs = True
            continue
        if re.match(r"^(table|figure)\s*\d", low):
            continue
        # body paragraph stats
        for pr in props:
            if pr["font"]:
                fonts[pr["font"]] += 1
            if pr["size"]:
                fsizes[pr["size"]] += 1
            if pr["hl"] and pr["hl"] != "none":
                hl_count += 1
        line = get_ppr_prop(ppr, styles, pstyle, "spacing", "line")
        rule = get_ppr_prop(ppr, styles, pstyle, "spacing", "lineRule") or "auto"
        if line and rule == "auto":
            v = int(line) / 240
            spacing["double" if v >= 1.95 else ("1.5" if v >= 1.45 else ("single" if v <= 1.16 else f"{v:.2f}"))] += 1
        elif line:
            spacing[f"exact/at least {int(line) / 20:.0f} pt"] += 1
        else:
            spacing["single"] += 1
        just[jc] += 1

    # fonts and sizes
    if fonts:
        resolved = Counter()
        for f, k in fonts.items():
            if f.startswith("(theme font:"):
                f2 = theme_fonts.get("major" if "major" in f.lower() else "minor") or f
                resolved[f2] += k
            else:
                resolved[f] += k
        fonts = resolved
        main_font, n = fonts.most_common(1)[0]
        others = [f for f in fonts if f != main_font and fonts[f] > 2]
        if rules["font"] and main_font != rules["font"]:
            add("Text", f"Body font is {main_font}; {rules['name']} asks for 12-point {rules['font']}.", rules["font_src"])
        if others:
            add("Text", f"Mixed body fonts: {', '.join([main_font] + others)}. Use one font throughout (often from pasted text or Zotero fields).")
    if fonts and fsizes:
        out["Text"].insert(0, f"Body text: {fonts.most_common(1)[0][0]}, {fsizes.most_common(1)[0][0]:g} pt (most common).")
    if fsizes:
        main_size = fsizes.most_common(1)[0][0]
        if main_size not in rules["sizes"]:
            add("Text", f"Body text is {main_size:g} pt; use {'/'.join(str(s) for s in rules['sizes'])} pt.", rules["size_src"])
        odd = [f"{s:g} pt" for s in fsizes if s != main_size and fsizes[s] > 5]
        if odd:
            add("Text", f"Some body text is in other sizes ({', '.join(odd)}).")
    if spacing:
        total = sum(spacing.values())
        dbl = spacing.get("double", 0)
        if dbl / total < 0.9:
            add("Text", f"Only {100 * dbl / total:.0f}% of body paragraphs are double spaced (found: " + ", ".join(f"{k} {v}" for k, v in spacing.most_common()) + "). Double space the whole manuscript, including references (Home > Line spacing > 2.0).", rules["double"])
    if just.get("both", 0) + just.get("distribute", 0) > 0:
        add("Text", f"{just.get('both', 0) + just.get('distribute', 0)} body paragraph(s) are justified. Use left alignment with a ragged right margin.", rules["ragged"])
    if hl_count:
        add("Text", f"{hl_count} highlighted run(s) in the body text. Remove highlighting before submission.")

    # ---------- footnotes / endnotes
    for part, label in (("word/footnotes.xml", "footnote"), ("word/endnotes.xml", "endnote")):
        if part in names:
            x = etree.fromstring(z.read(part))
            real = [f for f in x if f.get(W + "type") not in ("separator", "continuationSeparator", "continuationNotice")]
            if real and rules["footnotes"] == "req":
                add("Structure", f"{len(real)} {label}(s) found. GSA journals don't allow footnotes or endnotes; move them to an \"Author Notes\" section (PPAR allows up to 5 short endnotes).", "req")
            elif real:
                add("Structure", f"{len(real)} {label}(s) found. Check the journal's instructions; most medical journals fold notes into the text or the acknowledgments.")

    # ---------- page breaks before sections and tables
    def starts_new_page(idx):
        """True if paragraph idx begins a new page: pageBreakBefore, or a page/section break just before it."""
        kind, node, _ = paras_info[idx]
        if kind == "p":
            ppr = node.find(W + "pPr")
            pstyle = ppr.find(W + "pStyle").get(W + "val") if ppr is not None and ppr.find(W + "pStyle") is not None else None
            v = None
            if ppr is not None and ppr.find(W + "pageBreakBefore") is not None:
                v = ppr.find(W + "pageBreakBefore").get(W + "val", "1")
            else:
                for st in styles.chain(pstyle):
                    el = st.find(f"{W}pPr/{W}pageBreakBefore")
                    if el is not None:
                        v = el.get(W + "val", "1")
                        break
            if v not in (None, "0", "false"):
                return True
            for br in node.iter(W + "br"):
                if br.get(W + "type") == "page":
                    return True
        j = idx - 1
        while j >= 0:
            k2, n2, t2 = paras_info[j]
            if k2 == "tbl":
                return False
            for br in n2.iter(W + "br"):
                if br.get(W + "type") == "page":
                    return True
            if n2.find(f"{W}pPr/{W}sectPr") is not None:
                return True
            if t2:
                return False
            j -= 1
        return False

    wanted = rules["newpage"]
    found_sections = {}
    first_table_idx = None
    caption_idx = []
    for idx, (kind, node, t) in enumerate(paras_info):
        if kind == "p" and t:
            low = t.lower().rstrip(":").strip()
            for key, pat in SECTION_PATTERNS.items():
                if key not in found_sections and re.fullmatch(pat, low):
                    found_sections[key] = idx
            if re.match(r"^table\s*\d+\b", low):
                caption_idx.append(idx)
        if kind == "tbl" and first_table_idx is None:
            first_table_idx = idx
    if "text" in wanted and "text" not in found_sections:
        # no Introduction heading: the first long paragraph is the start of the text
        for idx, (kind, node, t) in enumerate(paras_info):
            if kind == "p" and len(t.split()) >= 40:
                found_sections["text"] = idx
                break
    labels = {"key_points": "Key Points", "abstract": "Abstract", "text": "the main text (Introduction)",
              "references": "References", "legends": "Figure legends/captions", "tables": "Tables"}
    for key in wanted:
        if key == "tables":
            continue
        if key in found_sections and not starts_new_page(found_sections[key]):
            add("Structure", f"{labels[key]} does not start on a new page. Insert a page break before it (Ctrl/Cmd+Enter).", "req" if a.journal in ("jama", "jgb", "jga") else "sug")
    if caption_idx:
        not_new = [paras_info[i][2][:20] for i in caption_idx if not starts_new_page(i)]
        if rules["each_table_page"] and not_new:
            add("Structure", f"{len(not_new)} table(s) don't start on their own page ({', '.join(not_new[:3])}...). GSA journals want each table on a separate page at the end of the file.", "req")
        elif not rules["each_table_page"] and not_new and len(not_new) == len(caption_idx):
            add("Structure", "Tables don't start on a new page after the references/legends. JAMA asks for tables at the end of the manuscript file, starting on a new page.", "req")

    # ---------- headings
    if headings:
        levels = []
        for h in headings:
            if h["b"] and h["jc"] == "center" and not h["i"]:
                lvl = 1
            elif h["b"] and h["i"] and h["jc"] != "center":
                lvl = 3
            elif h["b"] and h["jc"] != "center":
                lvl = 2
            else:
                lvl = 0
            levels.append(lvl)
        summary = "; ".join(f"{h['text'][:28]} [{'L' + str(l) if l else '?'}{', centered' if h['jc'] == 'center' else ''}{', italic' if h['i'] else ''}]" for h, l in zip(headings[:12], levels[:12]))
        add("Headings", f"{len(headings)} heading(s) detected (first 12): {summary}.")
        styled = sum(1 for h in headings if h["style"] and re.match(r"heading", h["style"], re.I))
        if styled < len(headings) / 2:
            add("Headings", "Most headings are bold body text rather than Word Heading styles. Applying Heading 1/2/3 styles keeps formatting consistent and gives editors a navigable outline (suggested).")
        if rules["apa_headings"]:
            main_names = {"introduction", "methods", "method", "results", "discussion", "conclusions", "conclusion",
                          "research design and methods", "background and objectives", "discussion and implications", "implications"}
            for h, l in zip(headings, levels):
                low = h["text"].lower().rstrip(".:")
                if low in main_names and l != 1:
                    add("Headings", f"\"{h['text']}\" looks like a main section heading but isn't formatted as APA Level 1 (centered, bold, Title Case).", "sug")
                if not is_title_case(h["text"].rstrip(".")) and l in (1, 2, 3):
                    add("Headings", f"\"{h['text']}\" is not in Title Case (APA Levels 1-5 use Title Case).", "sug")
            if a.journal == "ia":
                names_present = {h["text"].lower().rstrip(".:") for h in headings}
                for need in ("background and objectives", "research design and methods", "results", "discussion and implications"):
                    if need not in names_present:
                        add("Headings", f"No \"{need.title()}\" heading. Innovation in Aging lists Background and Objectives, Research Design and Methods, Results, and Discussion and Implications as the text headings.", "req")
        else:
            # JAMA: check consistency within tier (same alignment/italics for same-looking headings)
            main_names = {"introduction", "methods", "results", "discussion", "conclusions", "limitations"}
            fmt = {(h["jc"], h["i"]) for h in headings if h["text"].lower().rstrip(".:") in main_names - {"limitations"}}
            if len(fmt) > 1:
                add("Headings", "Main section headings (Introduction, Methods, Results, Discussion, Conclusions) are formatted inconsistently (alignment or italics differ). Give them one style.")
            for h in headings:
                if h["text"].endswith(" ") or re.search(r"\s{2,}", h["text"]):
                    add("Headings", f"Heading \"{h['text'].strip()}\" has extra spaces.")

    # ---------- file hygiene
    doc_x = z.read("word/document.xml").decode("utf8", "ignore")
    n_ins, n_del = doc_x.count("<w:ins "), doc_x.count("<w:del ")
    if n_ins or n_del:
        authors = sorted(set(re.findall(r'<w:(?:ins|del) [^>]*w:author="([^"]+)"', doc_x)))
        add("File", f"{n_ins} tracked insertion(s) and {n_del} deletion(s) are still unresolved (by {', '.join(authors[:5])}). Accept or reject all changes in the submission copy (Review > Accept > Accept All Changes).")
    if "word/comments.xml" in names:
        n_c = len(re.findall(r"<w:comment ", z.read("word/comments.xml").decode("utf8", "ignore")))
        if n_c:
            add("File", f"{n_c} comment(s) remain. Delete all comments in the submission copy (Review > Delete > Delete All Comments in Document).")
    if a.blinded and "docProps/core.xml" in names:
        core = z.read("docProps/core.xml").decode("utf8", "ignore")
        who = [m for m in re.findall(r"<(?:dc:creator|cp:lastModifiedBy)>([^<]+)<", core) if m.strip()]
        if who:
            add("File", f"Document properties name {', '.join(sorted(set(who)))}. For the blinded file, remove personal info (Word: File > Info > Check for Issues > Inspect Document > Document Properties and Personal Information).", "req")

    # ---------- report
    print(f"Layout check for {rules['name']}: {p.name}")
    total = 0
    for cat in ("Page setup", "Text", "Structure", "Headings", "File"):
        msgs = out.get(cat, [])
        if not msgs:
            continue
        print(f"\n[{cat}]")
        for m in msgs:
            total += 1
            print("  - " + m)
    print(f"\n{total} item(s). Requirements are marked; everything else is a suggestion. Confirm against the journal's live instructions.")


if __name__ == "__main__":
    main()
