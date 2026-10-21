# Changelog

## 1.3.1 (2026-10-21)

- Removed Annual Review of Sociology (invitation only).

## 1.3.0 (2026-10-21)

- New `sociology-manuscript-prep` skill for 18 sociology and demography journals (ASR, AJS, Social Forces, Socius, ESR, BJS, JHSB, Social Science & Medicine and SSM journals, Sociology of Health & Illness, Demography, PDR, PRPR, ALCR, Social Science Research, RSSM, Sociological Methodology, SMR, Sociology of Race and Ethnicity). Each journal is marked verified or confirm.
- New `soc_count.py`: choose what counts toward the limit (`--count text,notes,refs,...`), counts Word footnotes/endnotes, flags notes over a word limit, keywords out of range, and long titles.
- Layout checker: 18 sociology journals added (e.g., ASR page numbers removed, JHSB no Word notes and no Introduction heading, PRPR ALL CAPS Level 1 headings and no line numbers, SSM line numbers).
- Table checker and formatter: new `--style asa`; new `--decimal-align` (formatter sets decimal tabs; checker flags unaligned numeric cells).
- Fixed: the table checker embedded in v1.2 had lost the `--allow-asterisks` option used for JGA.

## 1.2.0 (2026-10-21)

- New layout checker (`layout_check.py`): paper size, margins, body font and size, line spacing, justification, highlighting, page and line numbers, page breaks before required sections and tables, footnotes and endnotes, detected heading levels (APA 7 levels for GSA journals), leftover tracked changes and comments, and author names in document properties for blinded files. Journal requirements and suggestions are labeled separately.
- New table formatter (`table_format.py`): writes a new .docx with horizontal rules only, no shading or colored text, a repeating header row, and APA alignment; fixes P values, minus signs, and number separators as tracked changes; optional rounding of percentages for groups under 100 (AMA); writes a change log. Never changes values or the original file.
- Table checker: flags APA table titles that aren't split into a bold number line and an italic title line.
- New menu items in both skills: page layout and heading check, and format my tables.

## 1.1.0 (2026-10-21)

- New table checker (`table_check.py`, also embedded in both skills): vertical lines, shading, colored text, tab- or space-aligned values, stacked values, empty cells, mixed decimal places, percentages with decimals in groups under 100 (AMA), hyphen minus signs, ±, comma use in large numbers, P value format (leading zeros, .000, extra decimals), symbol footnote markers, and title length.
- New table and number formatting sections: JAMA Network table rules (construction, alignment, decimals, footnotes) and APA 7 plus GSA/OUP table rules (borders, headings, alignment, decimals, CIs, notes order), including how each journal family handles decimal alignment.

## 1.0.0 (2026-10-20)

First public release.

- `jama-manuscript-prep`: 18 features for JAMA Network journals, from requirements and Key Points to response to reviewers. Limits checked against the JAMA Network Open and JAMA Internal Medicine Instructions for Authors, October 2026.
- `gsa-manuscript-prep`: 20 features for JGA (Biological and Medical Sciences), JGB (Psychological and Social Sciences), The Gerontologist, Innovation in Aging, and Public Policy & Aging Report, including keywords, the Translational Significance statement, and an anonymization check. Limits checked October 2026.
- Word counters read Word files with tracked changes accepted, apply each journal's counting rule, and count long paragraphs before Methods as the Introduction when a draft has no Introduction heading.
