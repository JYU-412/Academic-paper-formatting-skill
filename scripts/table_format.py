#!/usr/bin/env python3
"""Format the tables in a manuscript (.docx) to AMA (JAMA Network, JGA) or APA (JGB,
The Gerontologist, Innovation in Aging, PPAR) conventions. Writes a NEW file; the
original is never touched.

Usage:
    python table_format.py manuscript.docx --style ama -o manuscript_tables.docx
    python table_format.py manuscript.docx --style apa -o manuscript_tables.docx
    python table_format.py manuscript.docx --style asa -o manuscript_tables.docx   # sociology (ASA, Chicago)
Options:
    --decimal-align       align numeric cells on the decimal point with a decimal tab (JHSB requires it;
                          optional elsewhere)
    --round-small-pct     (AMA) round percentages to whole numbers in groups with n < 100
    --include-supplement  also format eTables / supplementary tables
    --no-track            apply text fixes directly instead of as tracked changes
    --author NAME         name shown on tracked changes (default "Table formatter")

What it changes
  Layout (applied directly, listed in the change log):
    - borders: horizontal rules only (top of table, below the header row, bottom);
      vertical lines, inside grid lines, and per-cell side borders removed
    - cell shading, colored text, and highlighting removed
    - header row set to repeat on each page
    - APA only: stub (first) column left-aligned, all other cells centered
  Text (as tracked changes by default, so each one can be accepted or rejected):
    - P values: leading zero dropped (0.04 -> .04, < 0.001 -> <.001); .000 -> <.001
    - hyphens used as minus signs -> true minus sign (U+2212)
    - number separators: AMA removes commas (2,449 -> 2449; 12,450 -> 12 450 with a
      thin space); APA adds commas to 4+ digit counts (2449 -> 2,449; years left alone)
    - optional (--round-small-pct): 30 (62.5) -> 30 (63) where the column's n < 100
What it never changes: numeric values, decimals (except the opt-in rounding),
column or row order, wording, ±, or anything outside tables.
Tracked changes already in the table are left alone; accept or reject them first for
a complete pass. A change log (Markdown) is written next to the output file.
"""
import argparse
import copy
import difflib
import re
import shutil
import sys
import tempfile
import zipfile
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

# A table title: "Table 1", "Table 1.", "Table 1: ...", or "Table 1 Sample ..." (not "Table 1 shows ...")
CAPTION_RE = r'''^(?i:e?table)\s*[A-Z]?\d+(?:\s*$|\s*[.:|—–-]|\s+(?=[A-Z(“"']))'''

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
PVAL_COL = re.compile(r"^\s*\*?p\*?\s*(value)?", re.I)
DATE = "2026-01-01T00:00:00Z"


def q(tag):
    return W + tag


def in_revision(el, stop):
    anc = el.getparent()
    while anc is not None and anc is not stop:
        if anc.tag in (q("ins"), q("del"), q("moveFrom"), q("moveTo")):
            return True
        anc = anc.getparent()
    return False


def cell_text(tc):
    out = []
    for t in tc.iter(q("t")):
        if not in_revision(t, tc) or t.getparent().getparent().tag == q("ins"):
            out.append(t.text or "")
    return "".join(out)


# ---------------- text transforms ----------------
def fix_p(text, style):
    new = text
    new = re.sub(r"(?<![\d.])0\.0{3,}(?!\d)|(?<![\d.])\.0{3,}(?!\d)", "<.001", new)
    new = re.sub(r"([<>=≤≥]\s*)0(\.\d)", r"\1\2", new)
    new = re.sub(r"(?<![\d.])0(\.\d+)", r"\1", new)
    if style == "ama" and re.fullmatch(r"\s*[<>]\s*\.\d+\s*", new):
        new = re.sub(r"([<>])\s+\.", r"\1.", new)
    return new


def fix_minus(text):
    return re.sub(r"(^|[\s(\[,;:/])-(?=\.?\d)", lambda m: m.group(1) + "−", text)


def fix_separators(text, style):
    if style == "ama":  # apa and asa both use commas
        def ama(m):
            digits = m.group(0).replace(",", "")
            if len(digits) <= 4:
                return digits
            groups = []
            while digits:
                groups.insert(0, digits[-3:])
                digits = digits[:-3]
            return " ".join(groups)
        return re.sub(r"(?<![\d.,])\d{1,3}(?:,\d{3})+(?![\d,]|\.\d)", ama, text)

    def apa(m):  # also used for ASA/Chicago, which use commas too
        s = m.group(0)
        n = int(s)
        if 1900 <= n <= 2099 and len(s) == 4:
            return s  # probably a year
        return f"{n:,}"
    return re.sub(r"(?<![\d., ])\d{4,}(?![\d.,])", apa, text)


def round_pct(text):
    """Round the percentage in a 'count (percent)' cell, e.g. 30 (62.5) -> 30 (63).
    Only whole-cell count (percent) patterns are touched, never mean (SD) or other values."""
    m = re.fullmatch(r"(\s*\d[\d,\u2009]*\s*\(\s*)(\d{1,3}\.\d+)(\s*%?\s*\)\s*)", text)
    if not m:
        return text
    count = int(re.sub(r"[^\d]", "", m.group(1)))
    pct = Decimal(m.group(2))
    if pct > 100 or count == 0 and pct != 0:
        return text
    return f"{m.group(1)}{pct.quantize(Decimal('1'), rounding=ROUND_HALF_UP)}{m.group(3)}"


# ---------------- tracked replacement ----------------
class Ids:
    def __init__(self, start):
        self.n = start

    def next(self):
        self.n += 1
        return str(self.n)


def make_run(rpr, text, deleted=False):
    r = etree.Element(q("r"))
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, q("delText") if deleted else q("t"))
    t.text = text
    t.set(XML_SPACE, "preserve")
    return r


def replace_run_text(run, old, new, track, ids, author):
    """Replace the text of a single-text run, marking only the changed characters."""
    if not track:
        ts = run.findall(q("t"))
        ts[0].text = new
        ts[0].set(XML_SPACE, "preserve")
        for t in ts[1:]:
            run.remove(t)
        return
    rpr = run.find(q("rPr"))
    parent = run.getparent()
    pos = parent.index(run)
    pieces = []
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            pieces.append(make_run(rpr, old[i1:i2]))
            continue
        if i2 > i1:
            d = etree.Element(q("del"), {q("id"): ids.next(), q("author"): author, q("date"): DATE})
            d.append(make_run(rpr, old[i1:i2], deleted=True))
            pieces.append(d)
        if j2 > j1:
            ins = etree.Element(q("ins"), {q("id"): ids.next(), q("author"): author, q("date"): DATE})
            ins.append(make_run(rpr, new[j1:j2]))
            pieces.append(ins)
    parent.remove(run)
    for k, el in enumerate(pieces):
        parent.insert(pos + k, el)


def merge_plain_runs(p):
    """Join adjacent runs with identical formatting (outside revisions) so numbers aren't split."""
    runs = [r for r in p.findall(q("r")) if r.find(q("t")) is not None and all(ch.tag in (q("rPr"), q("t")) for ch in r)]
    prev = None
    for r in runs:
        if prev is not None and r.getprevious() is prev:
            a = prev.find(q("rPr"))
            b = r.find(q("rPr"))
            sa = etree.tostring(a) if a is not None else b""
            sb = etree.tostring(b) if b is not None else b""
            if sa == sb:
                pt = prev.findall(q("t"))
                pt[-1].text = "".join(t.text or "" for t in pt) + "".join(t.text or "" for t in r.findall(q("t")))
                pt[-1].set(XML_SPACE, "preserve")
                for t in pt[:-1]:
                    prev.remove(t)
                p.remove(r)
                continue
        prev = r


def transform_cell(tc, funcs, track, ids, author, log, where):
    """Apply text fixes to plain runs in a cell. Runs inside existing tracked changes and runs
    holding tabs, breaks, fields, or drawings are left untouched and counted as skipped."""
    skipped = 0
    for p in tc.iter(q("p")):
        skipped += sum(1 for r in p.iter(q("r")) if in_revision(r, p))
        merge_plain_runs(p)
        for r in list(p.findall(q("r"))):
            ts = r.findall(q("t"))
            if not ts:
                continue
            if any(ch.tag not in (q("rPr"), q("t")) for ch in r):
                skipped += 1
                continue
            old = "".join(t.text or "" for t in ts)
            new = old
            for f in funcs:
                new = f(new)
            if new != old:
                replace_run_text(r, old, new, track, ids, author)
                log.append(f"| {where} | `{old.strip()}` | `{new.strip()}` |")
    return skipped


# ---------------- layout ----------------
def border(tag, val="single", sz="8"):
    el = etree.Element(q(tag))
    el.set(q("val"), val)
    if val != "nil":
        el.set(q("sz"), sz)
        el.set(q("space"), "0")
        el.set(q("color"), "000000")
    return el


def set_child(parent, tag, el, order_before=None):
    old = parent.find(q(tag))
    if old is not None:
        parent.replace(old, el)
    else:
        parent.append(el)


TABS_BEFORE = ("suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
               "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind", "contextualSpacing",
               "mirrorIndents", "suppressOverlap", "jc", "textDirection", "textAlignment", "textboxTightWrap",
               "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange")
# A number, a number with a parenthetical (mean (SD)), or a lone SE in parentheses: (0.03)
NUMERIC_CELL = re.compile(r'''(?:[−\-<>]?\s*(?=[\d., ]*\d)(?:\d[\d, ]*)?(?:\.\d+)?\*{0,3}(?:\s*[\(\[].*[\)\]])?|[\(\[]\s*[−\-]?(?=[\d.,]*\d)(?:\d[\d,]*)?(?:\.\d+)?\s*[\)\]]\*{0,3})\s*''')


def decimal_align(tbl, log, label):
    """Put a decimal tab in each numeric data cell so values line up on the decimal point."""
    n, skipped_int = 0, 0
    rows = tbl.findall(q("tr"))
    grid = [int(g.get(q("w"), 0)) for g in tbl.findall(f"{q('tblGrid')}/{q('gridCol')}")]
    # one tab position per column, so every value in a column lines up; move it left of
    # center when values in that column carry a trailing parenthetical, e.g. 74.2 (6.8)
    trailing = set()
    for ri, tr in enumerate(rows[1:], 1):
        for ci, tc in enumerate(tr.findall(q("tc"))):
            txt = cell_text(tc).strip()
            if ci and NUMERIC_CELL.fullmatch(txt or "x") and re.search(r"\d\S*\s*[\(\[]", txt):
                trailing.add(ci)
    for ri, tr in enumerate(rows):
        if ri == 0:
            continue
        for ci, tc in enumerate(tr.findall(q("tc"))):
            if ci == 0 or not NUMERIC_CELL.fullmatch(cell_text(tc).strip() or "x"):
                continue
            if re.match(r"[\u2212\-<>]?\s*\d[\d,\u2009]*\s*[\(\[][^\)\]]*\.", cell_text(tc).strip()):
                # e.g. 721 (69.9): a decimal tab would align on the percentage's point, not the count
                skipped_int += 1
                continue
            tcw = tc.find(f"{q('tcPr')}/{q('tcW')}")
            width = int(tcw.get(q("w"), 0)) if tcw is not None and tcw.get(q("type")) == "dxa" else (grid[ci] if ci < len(grid) else 1440)
            txt = cell_text(tc).strip()
            # put the decimal point a little left of center when a parenthetical follows
            pos = max(360, int(width * (0.40 if ci in trailing else 0.50)))
            for p in tc.findall(q("p")):
                ppr = p.find(q("pPr"))
                if ppr is None:
                    ppr = etree.Element(q("pPr"))
                    p.insert(0, ppr)
                old = ppr.find(q("tabs"))
                if old is not None:
                    ppr.remove(old)
                tabs = etree.Element(q("tabs"))
                tab = etree.SubElement(tabs, q("tab"))
                tab.set(q("val"), "decimal")
                tab.set(q("pos"), str(pos))
                anchor = None
                for t in TABS_BEFORE:
                    anchor = ppr.find(q(t))
                    if anchor is not None:
                        break
                if anchor is not None:
                    anchor.addprevious(tabs)
                else:
                    ppr.append(tabs)
                jc = ppr.find(q("jc"))
                if jc is not None:
                    jc.set(q("val"), "left")
            n += 1
    log.append(f"- {n} numeric cell(s) aligned on the decimal point (decimal tab)")
    if skipped_int:
        log.append(f"- {skipped_int} cell(s) like \"721 (69.9)\" left as they were: a decimal tab would line up the percentage's decimal point instead of the count. Consider separate n and % columns, or align these by hand.")


def format_layout(tbl, style, log, label):
    changes = []
    tblpr = tbl.find(q("tblPr"))
    if tblpr is None:
        tblpr = etree.SubElement(tbl, q("tblPr"))
        tbl.insert(0, tblpr)
    tb = etree.Element(q("tblBorders"))
    for side, val in (("top", "single"), ("left", "nil"), ("bottom", "single"), ("right", "nil"),
                      ("insideH", "nil"), ("insideV", "nil")):
        tb.append(border(side, val))
    old = tblpr.find(q("tblBorders"))
    # schema order inside tblPr: tblStyle, ..., tblW, jc, ..., tblBorders, shd, tblLayout, tblCellMar, tblLook
    if old is not None:
        tblpr.replace(old, tb)
    else:
        anchor = None
        for t in ("shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"):
            anchor = tblpr.find(q(t))
            if anchor is not None:
                break
        if anchor is not None:
            anchor.addprevious(tb)
        else:
            tblpr.append(tb)
    changes.append("borders set to horizontal rules only (top, below header, bottom)")

    rows = tbl.findall(q("tr"))
    n_shade = n_color = n_side = 0
    for ri, tr in enumerate(rows):
        for ci, tc in enumerate(tr.findall(q("tc"))):
            tcpr = tc.find(q("tcPr"))
            if tcpr is None:
                tcpr = etree.Element(q("tcPr"))
                tc.insert(0, tcpr)
            shd = tcpr.find(q("shd"))
            if shd is not None and (shd.get(q("fill")) or "auto").lower() not in ("auto", "ffffff"):
                tcpr.remove(shd)
                n_shade += 1
            tcb = tcpr.find(q("tcBorders"))
            if tcb is not None:
                for side in ("left", "right", "start", "end", "insideV", "insideH", "top", "bottom", "tl2br", "tr2bl"):
                    el = tcb.find(q(side))
                    if el is not None:
                        tcb.remove(el)
                        n_side += 1
            if ri == 0:
                if tcb is None:
                    tcb = etree.Element(q("tcBorders"))
                    # tcBorders goes after tcW/gridSpan/vMerge, before shd/vAlign
                    anchor = None
                    for t in ("shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"):
                        anchor = tcpr.find(q(t))
                        if anchor is not None:
                            break
                    if anchor is not None:
                        anchor.addprevious(tcb)
                    else:
                        tcpr.append(tcb)
                tcb.append(border("bottom"))
            elif tcb is not None and len(tcb) == 0:
                tcpr.remove(tcb)
            for p in tc.iter(q("p")):
                ppr = p.find(q("pPr"))
                if ppr is not None and ppr.find(q("shd")) is not None:
                    ppr.remove(ppr.find(q("shd")))
                    n_shade += 1
                for rpr in p.iter(q("rPr")):
                    for tag in ("color", "highlight", "shd"):
                        el = rpr.find(q(tag))
                        if el is not None and (tag != "color" or (el.get(q("val")) or "auto").lower() not in ("auto", "000000")):
                            rpr.remove(el)
                            n_color += 1
                if style == "apa":
                    if ppr is None:
                        ppr = etree.Element(q("pPr"))
                        p.insert(0, ppr)
                    jc = ppr.find(q("jc"))
                    want = "left" if ci == 0 else "center"
                    if jc is None:
                        jc = etree.Element(q("jc"))
                        # jc comes late in pPr; before rPr/sectPr/pPrChange
                        anchor = None
                        for t in ("textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"):
                            anchor = ppr.find(q(t))
                            if anchor is not None:
                                break
                        if anchor is not None:
                            anchor.addprevious(jc)
                        else:
                            ppr.append(jc)
                    jc.set(q("val"), want)
    if n_shade:
        changes.append(f"{n_shade} shading setting(s) removed")
    if n_color:
        changes.append(f"{n_color} text color/highlight setting(s) removed")
    if n_side:
        changes.append(f"{n_side} cell-level border(s) removed")
    if style == "apa":
        changes.append("stub column left-aligned, other cells centered")
    if rows:
        trpr = rows[0].find(q("trPr"))
        if trpr is None:
            trpr = etree.Element(q("trPr"))
            anchor = rows[0].find(q("tblPrEx"))
            if anchor is not None:
                anchor.addnext(trpr)
            else:
                rows[0].insert(0, trpr)
        if trpr.find(q("tblHeader")) is None:
            th = etree.Element(q("tblHeader"))
            anchor = None
            for t in ("ins", "del", "trPrChange"):
                anchor = trpr.find(q(t))
                if anchor is not None:
                    break
            if anchor is not None:
                anchor.addprevious(th)
            else:
                trpr.append(th)
            changes.append("header row set to repeat on each page")
    log.append(f"\n**{label}: layout**\n")
    for c in changes:
        log.append(f"- {c}")


def main():
    global etree
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--style", choices=["ama", "apa", "asa"], required=True)
    ap.add_argument("--decimal-align", action="store_true")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--round-small-pct", action="store_true")
    ap.add_argument("--include-supplement", action="store_true")
    ap.add_argument("--no-track", action="store_true")
    ap.add_argument("--author", default="Table formatter")
    a = ap.parse_args()
    from lxml import etree as _et
    etree = _et
    src, dst = Path(a.path), Path(a.output)
    if src.resolve() == dst.resolve():
        sys.exit("Output must be a different file; the original is never overwritten.")
    with zipfile.ZipFile(src) as z:
        xml = z.read("word/document.xml")
    root = etree.fromstring(xml)
    ids = Ids(max([int(x) for x in re.findall(rb'w:id="(\d+)"', xml)] or [0]) + 1000)
    body = root.find(q("body"))

    items = []

    def walk(node):
        for ch in node:
            if ch.tag == q("p"):
                items.append(("p", ch))
            elif ch.tag == q("tbl"):
                items.append(("tbl", ch))
            elif ch.tag == q("sdt"):
                c = ch.find(q("sdtContent"))
                if c is not None:
                    walk(c)
    walk(body)

    how = "applied directly" if a.no_track else 'tracked changes by "' + a.author + '"'
    log = [f"# Table formatting change log ({a.style.upper()} style)\n",
           f"Source: `{src.name}`  \nOutput: `{dst.name}`  \nText changes are {how}; layout changes are applied directly and listed below.\n"]
    in_supp, last_title, n_done, skipped_total = False, None, 0, 0
    for kind, node in items:
        if kind == "p":
            t = "".join(x.text or "" for x in node.iter(q("t"))).strip()
            if re.fullmatch(r"(supplement(ary|al)?( material| online content)?( \d+)?|emethods|eappendix)", t, re.I):
                in_supp = True
            if re.match(CAPTION_RE, t):
                last_title = t[:60]
            continue
        if in_supp and not a.include_supplement:
            continue
        n_done += 1
        label = last_title or f"Table {n_done}"
        format_layout(node, a.style, log, label)
        if a.decimal_align:
            decimal_align(node, log, label)
        rows = node.findall(q("tr"))
        header = [cell_text(tc).strip() for tc in rows[0].findall(q("tc"))] if rows else []
        pcols = {j for j, h in enumerate(header) if PVAL_COL.match(h)}
        col_n = {}
        for j, h in enumerate(header):
            m = re.search(r"\b[nN]\s*=\s*([\d,  ]+)", h)
            if m:
                col_n[j] = int(re.sub(r"[^\d]", "", m.group(1)))
        for r in rows[1:4]:
            tcs = r.findall(q("tc"))
            if tcs and re.match(r"(number of participants|no\. of participants|^n$|total)", cell_text(tcs[0]).strip(), re.I):
                for j, tc in enumerate(tcs[1:], start=1):
                    m = re.fullmatch(r"\s*([\d,]+)\s*", cell_text(tc))
                    if m and j not in col_n:
                        col_n[j] = int(m.group(1).replace(",", ""))
        log.append(f"\n**{label}: text**\n\n| Cell | Before | After |\n|---|---|---|")
        before = len(log)
        for ri, tr in enumerate(rows):
            tcs = tr.findall(q("tc"))
            stub = cell_text(tcs[0]).strip()[:30] if tcs else ""
            for ci, tc in enumerate(tcs):
                if ci == 0:
                    continue  # stub labels are words, leave them
                funcs = []
                if ri == 0:
                    funcs.append(lambda s: fix_separators(s, a.style))
                else:
                    if ci in pcols:
                        funcs.append(lambda s: fix_p(s, a.style))
                    else:
                        funcs.append(fix_minus)
                        funcs.append(lambda s: fix_separators(s, a.style))
                        if a.round_small_pct and a.style == "ama" and col_n.get(ci, 1000) < 100:
                            funcs.append(round_pct)
                where = f"{stub or 'header'} / {header[ci][:25] if ci < len(header) else ci + 1}"
                skipped_total += transform_cell(tc, funcs, not a.no_track, ids, a.author, log, where)
        if len(log) == before:
            log.append("| (no text changes) | | |")

    if n_done == 0:
        sys.exit("No tables found to format.")
    if skipped_total:
        log.append(f"\n> {skipped_total} run(s) were left as they are because they sit inside existing tracked changes or contain tabs, line breaks, or fields. Accept or reject earlier changes and fix tab-aligned cells, then run again for a complete pass.")
    log.append("\nNot changed by this tool (review by hand): ± (use mean (SD) or separate M and SD columns), decimal places other than the opt-in rounding, P values with more than 3 decimals, footnote markers, titles, and notes.")

    tmp = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp / "out.docx", "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
            zout.writestr(item, data)
    shutil.move(str(tmp / "out.docx"), dst)
    log_path = dst.with_suffix(".changes.md")
    log_path.write_text("\n".join(log) + "\n", encoding="utf8")
    n_text = sum(1 for line in log if line.startswith("| ") and "(no text changes)" not in line and "Cell |" not in line and not line.startswith("|---"))
    print(f"Formatted {n_done} table(s): {n_text} text change(s){' (tracked)' if not a.no_track else ''} plus layout changes.")
    print(f"Output: {dst}\nChange log: {log_path}")


if __name__ == "__main__":
    main()
