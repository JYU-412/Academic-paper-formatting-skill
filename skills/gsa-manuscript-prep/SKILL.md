---
name: gsa-manuscript-prep
description: Prepare, polish, check, and revise manuscripts for the Gerontological Society of America journals (Journals of Gerontology Series A (Biological or Medical Sciences), Series B (Psychological or Social Sciences), The Gerontologist, Innovation in Aging, and Public Policy & Aging Report). Use whenever the user wants a GSA-style abstract, keywords, Translational Significance statement, word-limit check or trim, APA/AMA style or ageist-language check, anonymization check, reporting-guideline check, cover letter, mock review, response to reviewers, or to reformat a paper for one of these journals, even if they just say "get this ready for JGB" or "submit to The Gerontologist".
---

# GSA Journals Manuscript Prep

A toolkit for getting a manuscript ready for a Gerontological Society of America journal, and for the revision stage. The user is the author: their science and their voice come first. This skill formats, checks, condenses, and drafts, and it shows every change so the author stays in control.

## Step 1: Gather the inputs

Every run needs the manuscript (.docx, .pdf, or pasted text). Read it in full first. If it is a .docx, read it with tracked changes accepted (`pandoc file.docx -t plain --track-changes=accept --wrap=none`), since co-author edits are often still tracked.

Confirm, inferring what you can and asking only about what is missing:
1. **Journal, and section where there is one.** JGA has Biological Sciences and Medical Sciences; JGB has Psychological Sciences and Social Sciences. Each section has its own limits, abstract headings, and submission site.
2. **Article type**, e.g., Research Article, Research Report, Review, Viewpoint, Policy Analysis.
3. **Study design**, e.g., quantitative observational, qualitative, mixed methods, trial, review. This sets the word limit for some journals (qualitative and mixed methods get more words at JGB Social Sciences and The Gerontologist) and the reporting guideline.
4. **Reference style.** It is fixed by the journal except at Innovation in Aging, which accepts APA 7 or AMA 11.

Stage-specific inputs only when needed: reviewer comments (19), rejection letter and new target (20), author surnames (16, to check anonymization), an earlier paper by the author if they want extra voice matching (9, 11).

## Step 2: Show the menu

Present this menu so the author picks only what they need. Accept numbers, ranges, a stage name, or "everything". If the opening message already says what they want, skip the menu and do it.

**Preparing**
1. Journal requirements card for the chosen journal, section, and article type
2. Structured abstract with the journal's headings
3. Journal-specific statement: Innovation and Translational Significance (Innovation in Aging), Implications section (The Gerontologist, PPAR)
4. Keywords (3-5, GSA rules)
5. Section order and completeness check

**Polishing**
6. Style check: APA 7 or AMA 11, plus GSA language rules (ageist terms, age ranges, demographics)
6b. Page layout and heading check (font, spacing, margins, page and line numbers, page breaks, APA heading levels, footnotes, leftover tracked changes and comments)
6c. Format my tables: edit a copy of the file so its tables follow APA/GSA (or AMA for JGA) style, with text fixes as tracked changes
7. Consistency check: numbers across abstract, text, and tables
8. Causal language check
9. Clarity edit in the author's voice

**Fitting the limits**
10. Word count and limits dashboard
11. Trim to fit, with every cut tracked
12. Move-to-Supplement suggestions

**Submitting**
13. Reporting guideline checklist mapping
14. Reference check (check only)
15. Title page and required statements (Funding, Conflict of Interest, Data Availability, ethics, AI disclosure)
16. Anonymization check for the blinded file
17. Cover letter draft
18. Pre-submission mock review

**Revising**
19. Response-to-reviewers table
20. Retarget to another GSA journal (or between a GSA journal and a JAMA Network journal)

Run multiple features in this order: requirements (1) and counts (10) first, then checks (5-8, 6b, 13-16), table formatting (6c) only when the author asks for it, then writing and edits (2-4, 9, 11, 12), then 17-18.

## Step 3: Get the current requirements

Limits below were checked against the journals' Instructions to Authors in October 2026. Before applying a number, fetch the live page for the target journal (URLs below). If it differs, the live page wins; tell the author. If it can't be fetched, use this file and say so.

For counts, write the script in the **Word counter** section at the end of this file to the scratchpad as `gsa_count.py` and run it. It reads tracked changes as accepted and supports each journal's counting rule:

```bash
python gsa_count.py manuscript.docx --mode text --text-limit 5000 --abstract-limit 250 --display-limit 5 --ref-limit 50 --authors "Surname1;Surname2"
```

- `--mode text`: main text only (JGB, The Gerontologist, Innovation in Aging)
- `--mode text+front`: title page + abstract + main text (JGA Biological and Medical Sciences)
- `--mode text+refs`: main text + references (PPAR)
- `--statement-limit 100` for Innovation in Aging's Translational Significance statement

It also flags ageist terms, keyword problems, first-person words, and author names in the blinded file. If the draft has no Introduction heading, it treats the long paragraphs before Methods as the Introduction. If its section detection looks wrong, say so and count that part by hand.

For page layout and headings, write the **Layout checker** at the end of this file to the scratchpad as `layout_check.py` and run `python layout_check.py manuscript.docx --journal jgb` (or `jga`, `tg`, `ia`, `ppar`; add `--blinded` for the anonymized file). It resolves Word styles the way Word renders them and reports paper size, 1-inch margins, body font and size (12-pt Times New Roman at JGA and JGB), double spacing, justification, page and line numbers (JGB Social: no line numbers), page breaks before the abstract, references, captions, and each table, footnotes (not allowed), APA heading levels, leftover tracked changes and comments, and author names in the document properties.

To **format** tables (feature 6c, only when the author asks), write the **Table formatter** to the scratchpad as `table_format.py` and run `python table_format.py manuscript.docx --style apa -o manuscript_tables.docx` (`--style ama` for JGA). It writes a new file and a `.changes.md` log; the original is never touched.

For tables, write the **Table checker** at the end of this file to the scratchpad as `table_check.py` and run `python table_check.py manuscript.docx --style apa` (or `--style ama --allow-asterisks` for JGA). It checks every Word table for vertical lines, shading, values aligned with tabs or stacked with line breaks, empty cells, mixed decimal places, hyphens used as minus signs, ±, comma use in large numbers, P value format, and footnote markers.

## Journal reference

### Instructions to Authors URLs
| Journal | Instructions | Submission site |
|---|---|---|
| JGA Biological Sciences | https://academic.oup.com/biomedgerontology/pages/General_Instructions_1 | mc.manuscriptcentral.com/jgbs |
| JGA Medical Sciences | https://academic.oup.com/biomedgerontology/pages/General_Instructions_2 | mc.manuscriptcentral.com/jgms |
| JGB Psychological Sciences | https://academic.oup.com/psychsocgerontology/pages/General_Instruction_2 | mc.manuscriptcentral.com/jgps |
| JGB Social Sciences | https://academic.oup.com/psychsocgerontology/pages/General_Instruction_1 | mc.manuscriptcentral.com/jgss |
| The Gerontologist | https://academic.oup.com/gerontologist/pages/Instructions_To_Authors | mc.manuscriptcentral.com/tg |
| Innovation in Aging | https://academic.oup.com/innovateage/pages/Author_Guidelines | ScholarOne |
| Public Policy & Aging Report | https://academic.oup.com/ppar/pages/Instructions_To_Authors | mc.manuscriptcentral.com/ppar |

### Main research article at a glance
| | Text limit | What counts | Abstract | Refs | Tables + figures | Ref style | Review |
|---|---|---|---|---|---|---|---|
| JGA Biological | Original Article 5800 | title page + abstract + text | 250, unstructured | 50 | 5 (recommended) | AMA 11, numbered in parentheses | not stated |
| JGA Medical | Research Article 5200 | title page + abstract + text | 250, structured | 50 | 5 (recommended) | AMA 11, numbered in parentheses | not stated |
| JGB Psychological | Research Article 5000 | text only | 250, structured | 50 (75 meta-analysis) | 5 | APA 7 | single-blind |
| JGB Social | Quantitative 5000; qualitative or mixed 6000 | text only | 250, structured | 50 | 5 | APA 7, DOIs required | double-blind |
| The Gerontologist | Quantitative 6000; qualitative, mixed, intervention, humanities 7000 | text (exclusions not stated; confirm) | 250, structured | 50 | 5 | APA 7 | double-anonymized |
| Innovation in Aging | Original Research 6000 | text only | 250, structured | 50 | 5 | APA 7 or AMA 11 | double-anonymized (since Feb 4, 2026) |
| PPAR | Policy Analysis 3500 | text + references | not stated | not stated | not stated (excluded from count) | APA 7 | editor review |

"Text only" excludes the title page, abstract, keywords, references, and tables and figures. JGA counts the title page and abstract inside the limit and may return papers more than 10% over (Medical Sciences). Exceeding any limit needs prior Editor-in-Chief permission, noted in the cover letter.

### Abstract headings
- **JGB (both sections):** Objectives; Methods; Results; Discussion. No references. Summarize sample demographics.
- **The Gerontologist and Innovation in Aging:** Background and Objectives; Research Design and Methods; Results; Discussion and Implications. Summarize sample demographics. The Gerontologist's Forum uses a 200-word unstructured abstract; its humanities and arts papers use 250 unstructured words covering question, data source, method, and conclusion. Innovation in Aging's Meeting Reports and Invited Articles are unstructured; Research Letters, Viewpoints, and Innovation Notes have none.
- **JGA Medical Sciences:** Background; Methods; Results; Conclusions. 250 words, not negotiable.
- **JGA Biological Sciences:** unstructured, 250 words: purpose, basic procedures (participants or animals, methods), main findings, conclusions.
- **PPAR:** no abstract requirement stated; check the live page or call for papers.

### Other article types
- **JGA Biological:** Research Report 2500 (25 refs, 3 elements); Research Letter 1000 excluding references (10 refs, 1 element, ≤5 authors, no abstract or supplement); Reviews in Depth 7000 (100 refs, 5); Research Practice 3800; Perspective 2000-3000 (no abstract, 40 refs, 1-2 elements); Editorial 1200; Letter to the Editor 750. Commentary, Symposium Report, and Workshop Report are by invitation.
- **JGA Medical:** Research Report 2800 (20 refs, 3); Research Letter 1000 excluding references (10 refs, 1, ≤5 authors); Review 6000 (100 refs, 5); Research Practice 3800 (40 refs); Perspective about 3000 (40 refs); Editorial 1200; Letter 750.
- **JGB Psychological:** Research Report 2500 (30 refs, 3); New Directions in Aging Research 5000 (50, 3; by invitation); Viewpoint 800 (10 refs, 1 element, ≤5 authors). Sample size must be justified in the text (e.g., power analysis). Meta-analyses must be registered in PROSPERO and follow PRISMA. Authors suggest reviewers.
- **JGB Social:** Research Report 2500 (30, 3); Theoretical or Methodological Article 5000 (50, 3); Viewpoint 800. The section does not publish systematic, scoping, or meta-analytic reviews or experimental studies.
- **The Gerontologist:** Forum 5000 (200-word unstructured abstract); Measurement 6000; Review 8000 (75 refs, 10 elements; PROSPERO or OSF registration; PRISMA or PRISMA-ScR checklist in the supplement). Book reviews, guest editorials, and On Film and Digital Media pieces are invited only. **Every manuscript must address practice and/or policy implications** in a section that interprets results rather than restating them.
- **Innovation in Aging:** Research Report 3000 (30, 3); Scholarly Review 8000 (75, 5); Meeting Report 5000 (30, 3); Research Letter 1000 (10, 1); Viewpoint 800; Innovation Note 800; Invited Article 6000. Research Letters, Viewpoints, and Innovation Notes allow ≤5 authors and no supplement. Fully open access with an article processing charge (3625 USD listed; 20% GSA member discount; LMIC waivers).
- **PPAR:** Policy Spotlight 1500 with ≤1 table, figure, or graphic; Point-Counterpoint 1500, responding to an earlier article. Issues are themed. Unsolicited proposals go to the editorial office first and must propose topics and authors for at least 4 Policy Analysis articles. Write for a well-educated, non-specialist audience with little jargon. All articles must address practice and/or policy implications. Footnotes are not allowed; endnotes are discouraged (≤5 short ones, no references in them). Acknowledgments are 30-40 words on a page after the title page.

### Innovation in Aging extras
- **Innovation and Translational Significance statement:** ≤100 words, below the abstract, for an interdisciplinary audience. It says how the work is innovative and how it can be translated or applied to improve outcomes in later life, covering the main issue, approach, and outcome.
- Text headings: Background and Objectives, Research Design and Methods, Results, Discussion and Implications.
- The anonymized file avoids first-person language and refers to the authors' own work in the third person.
- Optional cover letter ≤300 words on innovation, contribution to understanding aging or the life course, and translational significance.

### File layout and anonymization
- **JGB Social:** separate (non-blinded) title page file; the anonymized manuscript opens with an anonymous title page giving title, word count, reference count, and element count.
- **JGB Psychological:** single-blind, but anonymous and non-anonymous versions are both uploaded, each with the supplement.
- **The Gerontologist:** exactly two main files, anonymized and non-anonymized. The anonymized file removes names, contacts, funding, acknowledgments, and self-identifying details; self-references become "Anonymized for Review". The supplement goes inside both files.
- **Innovation in Aging:** title page as a separate file (with funding, conflicts, data availability, acknowledgments, CRediT roles); acknowledgments optional on their own page; then the anonymized main document. Self-citations are referred to in the third person, with references shown in full.
- **JGA:** title page with word count and number of data elements; supplement as a single PDF (eTable 1, eFigure 1, eMethods) for Biological Sciences.
- **PPAR:** upload a complete version with author details; it is the version editors review.

### Rules shared by all five journals
- **Keywords:** 3-5, chosen from the submission system's list, none repeating the title, and not generic terms like "older adults" or "aging". At least 3 are needed to proceed in the system.
- **Age language (GSA Reframing Aging, which overrides other style guides):** "older adults" for people aged 65 and older, with a specific age range when describing research or recommendations ("older adults aged 75 to 85 years"). Never "aged", "elder(s)", "elderly", or "seniors". People-first language ("persons with dementia"); for disability, person-first and identity-first are both acceptable until the group's preference is known. Justify any culturally specific term that departs from this.
- **Demographics:** report them in full and explain why they were collected and why any groups were excluded. JGB, The Gerontologist, and Innovation in Aging ask how race and ethnicity, sex, gender, gender identity, and sexual orientation were assessed, with categories and who assigned them.
- **No footnotes:** use an "Author Notes" section instead.
- **Abbreviations:** minimize; define at first mention only.
- **Format:** Word only (no PDF), 12-pt Times New Roman, double spaced, 1-inch margins (JGB Social: no line numbers).
- **Tables:** editable Word tables, each on its own page at the end, Arabic numerals, no vertical lines, color, or shading. Notes go in this order: general note beginning "*Note.*", then lettered footnotes (a, b, c), then asterisk P values (*p < .05). Tables longer than 2 pages go to the supplement.
- **Figures:** separate files, 300 DPI (600 for black and white at JGB), 83 mm single-column or ≤170 mm wide, ≥8-pt sans-serif text, legible at 100%. Captions go on a separate page after the references. **Alt text for every figure, directly under its legend, beginning "Alt text:".** A graphical abstract is optional (landscape, ≤170 mm, 300 DPI, separate file).
- **Funding:** separate "Funding" section before Acknowledgments, beginning "This work was supported by…", with full agency names (no abbreviations), grant numbers in parentheses (JGA, JGB) or brackets (The Gerontologist, Innovation in Aging, PPAR), agencies separated by semicolons with "and" before the last. If none, "None reported" (Innovation in Aging, The Gerontologist).
- **Conflict of Interest:** for all authors; "None reported" (Innovation in Aging) or "We have no conflict of interest to declare" (The Gerontologist, PPAR).
- **Data Availability:** JGB, The Gerontologist, and Innovation in Aging require it to state (1) whether data, analytic methods, or materials are available for replication, (2) where, and (3) whether the study was preregistered, with reasons if not shared. JGB Psychological and The Gerontologist put the data and preregistration paragraphs in Acknowledgments and want a preregistration link in the main text. Cite public datasets in the references with a DOI (JGA: tag them "[dataset]"). The Gerontologist asks qualitative researchers for coding examples and interview guides.
- **Ethics:** IRB approval and number (or say none was required, and why), plus animal care approval and number for animal studies.
- **AI disclosure:** AI tools can't be authors. Any AI use in writing, images, or analysis is disclosed in the **Methods** (or similar section): which tool and how. Authors remain responsible for all content.
- **Reporting guidelines:** EQUATOR, e.g., STROBE (observational), CONSORT (trials, registered before enrollment), PRISMA or PRISMA-ScR (reviews), SRQR or COREQ, Levitt et al. 2018 JARS-Qual (qualitative), JARS-Mixed (mixed methods), STARD or TRIPOD (diagnostic or prognostic).
- **Revisions** are due within 3 months, or they are treated as new submissions.
- **Cover letter:** optional and not shared with reviewers. It covers innovation, timeliness, broad interest, and any word-limit permission; JGB Psychological also wants the contribution relative to the authors' earlier papers on the same data.

## Style reference

### APA 7 (JGB, The Gerontologist, Innovation in Aging, PPAR)
- In-text citations by author and year; for 3+ authors, first author et al.; multiple works in alphabetical order separated by semicolons. Reference list alphabetical, hanging indent, not numbered, DOIs as https://doi.org/... Up to 20 authors listed.
- Statistical symbols italicized: *M*, *SD*, *b*, *t*, *F*, *p*, *r*, *n*, *N* (Greek letters such as β are not italicized). *p* = .032 (no leading zero for values that cannot exceed 1: *p*, *r*, standardized β; leading zero for others: 0.45). Report exact *p* to 2-3 decimals, *p* < .001 as the floor. 95% CI [0.12, 0.45] with square brackets.
- Numbers 10 and above as numerals; below 10 as words except for measurements, statistics, ages, times, percentages, and sample sizes. Numbers with 4+ digits use commas (2,449). "%" after numerals, "percent" after words.
- Serial comma; "e.g.," and "i.e.," inside parentheses only.
- Headings: Level 1 centered bold; Level 2 flush-left bold; Level 3 flush-left bold italic.

### AMA 11 (JGA; Innovation in Aging if chosen)
- At JGA, references are numbered in order of first citation, **in parentheses, not superscript**: "...as shown previously (3,4)". List up to 6 authors, else 3 + et al; Index Medicus journal abbreviations; DOIs required.
- *P* = .04, *P* < .001; 95% CI, 1.12-1.88; mean (SD); median (IQR). No comma in 4-digit numbers (2449); thin space for 5+ digits.
- No abbreviations in the title or abstract beyond standard statistical ones.

### Table and number formatting

Combines APA 7 table setup (apastyle.apa.org) with the GSA/OUP table rules in the Instructions to Authors, checked October 2026. GSA rules win where they differ. Run the **table checker** (end of this file) on every .docx: `--style apa` for JGB, The Gerontologist, Innovation in Aging (APA option), and PPAR; `--style ama --allow-asterisks` for JGA, and `--style ama` for Innovation in Aging papers using AMA.

**Construction (all five journals)**
- Editable Word tables made with the table feature, never tabs, spaces, or images. Each table on its own page at the end of the main file (after references), numbered in Arabic numerals in order of citation. Tables longer than 2 pages go to the supplement.
- **No vertical lines, colored text, or shading** (GSA). APA uses horizontal rules only: top and bottom of the table, below the column headings, and above column spanners; optionally above a totals row.
- Same font as the paper; body may be single, 1.5, or double spaced.
- Each value in its own cell; put different statistics (e.g., M and SD) in different columns, or the journal's combined form consistently.
- Long tables repeat the heading row on each page; wide tables go on a landscape page.

**Titles and headings (APA journals)**
- Table number in bold ("**Table 1**"), then the title on the next line in *italic Title Case*. JGB asks for a concise title that names the content and population.
- Every column has a heading, including the stub (leftmost) column ("Variable" or "Characteristic"). Column headings centered, sentence case. Give units in parentheses in the column heading (JGB), e.g., "Age (years)".
- Put group sizes in the column headings, e.g., "Dementia (*n* = 209)".

**Alignment and decimals**
- APA: stub column entries left-aligned; all other cells centered; left-align text-heavy cells for readability. **Neither APA nor the GSA journals require decimal alignment**, and OUP typesets tables. If you want decimal alignment, use Word's decimal tab inside the cells, never spaces. What matters is a consistent number of decimal places within a column.
- APA decimals: round as much as precision allows, generally 2 decimals for statistics such as correlations, proportions, and inferential tests; give means and SDs of the same measure to the same precision. Exact *p* to 2 or 3 decimals; *p* < .001 as the floor; never *p* = .000.
- Leading zero: omit it for values that cannot exceed 1 (*p*, *r*, standardized β, proportions); keep it otherwise (0.45 kg).
- Percentages: numerals with %, or put "%" in the column heading and omit it from cells. Whole numbers are clearer for small groups.
- Numbers of 1,000 or more use commas (2,449).
- Negative values use a true minus sign (−.08).
- CIs: 95% CI [LL, UL] in square brackets, or separate *LL* and *UL* columns under a "95% CI" spanner.
- Italicize statistical symbols in headings and notes (*M*, *SD*, *n*, *p*, *b*, *t*, *F*); Greek letters are not italic.
- Empty cells: use an em dash (—) for not applicable or redundant cells, and define it in the note.

**Notes (APA and GSA order)**
1. General note, beginning with italic *Note.*, explaining abbreviations, units, data source, and anything that applies to the whole table.
2. Specific notes, marked with superscript lowercase letters (a, b, c).
3. Probability note: asterisks for significance levels, \*p < .05. \*\*p < .01. \*\*\*p < .001. Asterisks are used **only** for significance levels.
- Define every abbreviation unless it is explained in the note. No symbol markers (†, ‡).

**JGA (AMA 11) differences**
- Tables follow AMA conventions for statistics: mean (SD) and No. (%) in one cell, P values without leading zeros (.04, <.001). Notes follow JGA's stated order: a general note beginning "Note.", then superscript-letter footnotes, then asterisk P values (*p < .05), so asterisks are allowed at JGA. For number style (commas in 4-digit numbers), match a recent JGA article, since the instructions don't say.

### Causal language (all journals)
For observational designs, flag causal verbs and nouns ("led to", "caused", "resulted in", "reduced", "improved", "effect of", "impact", "protects", "drives") and suggest "was associated with" or "the association between". Look hardest at the abstract's Discussion/Conclusions, the Translational Significance statement, Implications sections, and policy recommendations. If the design supports causal inference (trial, target trial emulation, instrumental variables, difference-in-differences), check that assumptions are stated instead.

## How to do each feature

Principles that apply to all of them:
- **Never invent content.** Build abstracts, statements, keywords, cover letters, and responses only from the manuscript, the reviewer comments, or what the author says. Use marked placeholders like `[IRB NUMBER NEEDED]` and list them at the end.
- **Keep the author's voice.** Note their sentence length, hedging words, transitions, and preferred terms before editing. Delete before rewriting; when a sentence must change, reuse the author's own phrasing.
- **Show every change.** Edits come with a change log (original, revised, reason, words saved). Checks list location, a short quote, the issue, and a fix. The author decides.
- **Flag, don't fix, the science.** Mismatches between Methods and Results, missing outcomes, or unstated limitations are questions for the author.
- **References are checked, not generated.** Point the author to their reference manager (e.g., switch the Zotero style to APA 7 or AMA 11) rather than retyping references.

**1. Requirements card.** Fetch the live page. Give: journal and section, article type, text limit and what counts toward it, abstract (words and headings), keywords, statement or Implications requirement, references and style, elements, file layout and anonymization, required statements, reporting guideline, anything new vs this file, date checked.

**2. Abstract.** Use the journal's headings exactly. Every fact must be in the main text. First Results sentence (or Methods for JGB) gives N and demographics (age with mean (SD) or range, sex or gender, race and ethnicity where reported). Report the main estimates with uncertainty in the journal's style (APA or AMA). The last section matches the design's strength (feature 8 rules); for The Gerontologist and Innovation in Aging, "Discussion and Implications" should name a practice, policy, or research implication. 250 words maximum; cut from background and secondary results first, never the N or main estimate.

**3. Statement or Implications.** Innovation in Aging: draft a ≤100-word Innovation and Translational Significance statement in plain language (what is new, and how it can be applied to improve later-life outcomes), not a second abstract; offer 2 versions. The Gerontologist and PPAR: check that an Implications section (or a clearly labeled part of the Discussion) states specific practice or policy implications instead of restating results; draft one from the Discussion if missing.

**4. Keywords.** Suggest 5-7 candidates drawn from the paper's concepts, none repeating title words, none generic ("older adults", "aging"), and tell the author to choose 3-5 from the submission system's list.

**5. Section order.** Run the table checker for table construction. Check against the journal's layout: title page (separate file where required), abstract, keywords, statement (Innovation in Aging), main text headings (Innovation in Aging lists Background and Objectives, Research Design and Methods, Results, and Discussion and Implications for the text itself; the others use Introduction, Methods, Results, Discussion), Funding, Conflict of Interest, Data Availability, Acknowledgments, Author Notes, References, tables, figure captions with alt text, supplement. Methods should include design, sample and eligibility, measures, analysis (software and version), ethics statement, reporting guideline, and how demographics were assessed.

**6. Style check.** Run the table checker and fold its findings into the report. Then check the style reference above, including **Table and number formatting**, plus the GSA rules (ageist terms, age ranges, demographics, footnotes, abbreviations, table note order, alt text, funding wording). Report as a table (location | quote | issue | fix), grouping repeated issues.

**6b. Page layout and heading check.** Run the layout checker with the journal code (`jga`, `jgb`, `tg`, `ia`, `ppar`; `--blinded` for the anonymized file). Report must-fix items (marked "journal requirement": double spacing, 12-pt Times New Roman at JGA and JGB, 1-inch margins and no line numbers at JGB Social, no footnotes, abstract, references, captions, and each table on a new page, document properties cleared in the blinded file) and suggestions. For APA journals, show the detected headings and their levels and propose the APA 7 levels: Level 1 centered bold Title Case for the main sections the journal lists (JGB: Introduction, Methods, Results, Discussion), Level 2 flush-left bold Title Case, Level 3 flush-left bold italic Title Case, Levels 4-5 indented and run in with a period. Innovation in Aging uses Background and Objectives, Research Design and Methods, Results, and Discussion and Implications. Always tell the author to accept or reject tracked changes and delete comments in the submission copy if any remain. Don't edit layout unless asked; if asked, edit a copy with the docx skill.

**6c. Format my tables.** Use only when the author asks for tables to be formatted (or accepts an offer after a check). (1) Run the table checker and show the findings. (2) Suggest resolving tracked changes inside tables first; the formatter leaves those runs alone. (3) Run `python table_format.py manuscript.docx --style apa -o <name>_tables.docx` (`--style ama` for JGA; `--include-supplement` for supplementary tables). (4) What it does: horizontal rules only (top, below header, bottom), no shading or colored text, header row repeats, APA alignment (stub left, other cells centered); tracked text fixes for P values (0.04 to .04, 0.000 to <.001), minus signs, and number separators (APA: 2449 to 2,449; AMA at JGA: commas removed). It never changes values, decimals, wording, or order. (5) Re-run the checker on the output and list what remains by hand: the APA title layout (bold **Table 1** on its own line, italic title below), the *Note.* / lettered / asterisk note order, ±, mixed decimals, an italic lowercase *p* column heading, and empty cells (em dash, defined in the note). (6) Deliver the formatted .docx and the change log, and remind the author to review the tracked changes before accepting.

**7. Consistency check.** Build a fact table (Ns through the sample flow, demographics, main estimates and CIs, dates) and check every place each appears: abstract, statement, text, tables, figure captions. Recompute percentages from counts.

**8. Causal language.** As in the style reference.

**9. Clarity edit.** Show a 3-5 bullet voice profile first so the author can correct it. Edit only for clarity and grammar; give the edited text plus a change log.

**10. Dashboard.** Run the counter with the right mode and limits. Table: item | count | limit | status, plus per-section counts and where cuts would hurt least (Introduction >20% or Discussion >35% of text are usual places). Note for JGA that the title page and abstract eat into the limit.

**11. Trim to fit.** Target the overage (with about a 2% buffer). Cut in order: redundancy (aims restated, Results repeating tables, Discussion repeating Results), wordy phrases ("in order to", "it is important to note that", "a total of", "the present study"), excess background, Methods details that belong in the supplement, and literature comparisons that list studies one by one. Never cut the main result, its uncertainty, expected limitations, ethics, or required statements. For a .docx, deliver a copy with suggested cuts as Word comments (or tracked changes if the author asks), using the docx skill.

**12. Move to supplement.** List candidates with words or elements saved (detailed measures, coding, sensitivity analyses, secondary tables). Use the journal's naming (Supplementary Table 1 for APA journals; eTable 1 for JGA) and remind the author the supplement can't repeat main text. Note: Research Letters, Viewpoints, and Innovation Notes allow no supplement.

**13. Reporting guideline.** Pick the guideline by design. Map each item: item | reported (Yes / Partly / No) | location | what's missing. For JGB Psychological, also check the sample-size justification.

**14. Reference check.** Check in-text citations against the list (both directions), style (APA: alphabetical, et al rules, DOIs; AMA at JGA: numbered in parentheses, in citation order), the reference limit, datasets cited with DOIs, and duplicates. Report problems by reference; don't reformat the list.

**15. Title page and statements.** Check the title (concise; The Gerontologist cites APA's suggestion of ≤12 words), author block, corresponding author, counts required on the title page (JGA, JGB), and each required statement against the shared rules above, including the exact "This work was supported by…" wording, the 3-part Data Availability statement, and the AI disclosure in Methods. Draft missing statements with placeholders.

**16. Anonymization check.** Run the counter with `--authors` on the blinded file. Also look for institution names, grant numbers, IRB names that identify the institution (replace with "[institution blinded]"), acknowledgments, funding, file metadata (tell the author to clear Word's document properties), and self-citations (third person, or "Anonymized for Review" at The Gerontologist). Innovation in Aging: flag first-person language. Ethics statements that name the IRB can say "the authors' institutional review board" in the blinded file.

**17. Cover letter.** Draft from the manuscript: the question, design and sample, main finding, and why it fits this journal's audience (innovation, timeliness, broad interest; translational significance for Innovation in Aging, ≤300 words). Include word-limit permission if granted, related papers on the same data (JGB Psychological asks), and that it isn't under review elsewhere.

**18. Mock review.** If the gerontology-paper-review skill is available, load it and follow it with the target journal in mind. Otherwise write a reviewer report: summary, fit with the journal (e.g., JGB Social Sciences won't take reviews; The Gerontologist wants practice or policy implications; PPAR wants policy relevance for non-specialists), major comments, minor comments, statistical points, and the top 3 fixes.

**19. Response to reviewers.** Number each comment (Editor 1, Reviewer 1.1...) and quote it in full. Draft responses in the author's voice with the change and its location; use [DESCRIBE CHANGE] where the author hasn't said, and [AUTHOR TO CONFIRM] for rebuttals. Rerun the dashboard on the revised file. Remind the author of the 3-month revision window.

**20. Retarget.** List every difference between the old and new journal: limit and what counts, abstract headings, statement, keywords, reference style (APA vs AMA is the big one between JGB/TG/IA and JGA or JAMA), anonymization, required statements. Apply the format changes, then reframe the introduction's opening and the implications for the new audience. Draft a new cover letter.

## Output
- Checks and the dashboard: a short report grouped as must fix, should fix, optional, with a one-line verdict at the top.
- New text: ready to paste, with its word count and placeholders.
- Edits: the revised text and change log; for a .docx, an edited copy with comments or tracked changes.
- End with open items: placeholders, decisions only the author can make, anything to confirm on the live page.

GSA journals require AI use to be disclosed in the Methods (tool and how it was used). When this skill writes or edits text (features 2-4, 9, 11, 17, 19), remind the author once per session.

## Word counter

Write this to the scratchpad as `gsa_count.py` before running it (it needs `lxml`; install with `pip install lxml --break-system-packages` if missing).

```python
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
```

## Table checker

Write this to the scratchpad as `table_check.py` before running it. Use `--style apa` for JGB, The Gerontologist, Innovation in Aging (APA), and PPAR; `--style ama --allow-asterisks` for JGA.

```python
#!/usr/bin/env python3
"""Table formatting checker for journal manuscripts (.docx).

Usage:
    python table_check.py manuscript.docx --style ama   # JAMA Network, JGA (AMA 11)
    python table_check.py manuscript.docx --style apa   # JGB, The Gerontologist, Innovation in Aging, PPAR (APA 7)
    python table_check.py manuscript.docx --style ama --allow-asterisks   # JGA (AMA; asterisk P notes allowed)

Checks every Word table before the Supplement (add --include-supplement to check
eTables too) and reports, per table:
  - construction: vertical lines, cell shading, colored text, tabs/multiple spaces or
    line breaks used to align values inside cells, empty cells, tables pasted as images
  - numbers: mixed decimal places within a column, hyphens used as minus signs,
    "±" instead of mean (SD), percentages with decimals when the group n is < 100 (AMA)
  - P values: leading zeros, "P = .000", "P < 0.05" style thresholds, uppercase/lowercase
  - notes: symbol footnote markers (*, †, ‡) where letters are required, missing "Note." (APA)
  - titles: missing or long titles (AMA: 10-15 words)
Reads tracked changes as accepted. Findings are suggestions to review, not automatic fixes.
"""
import argparse
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NUM = re.compile(r"(?<![\w.])[−\-]?\d+(?:,\d{3})*(?:\.(\d+))?")
PVAL_COL = re.compile(r"^\s*\*?p\*?\s*(value)?", re.I)


def text_of(node):
    out = []
    for el in node.iter(W + "t", W + "tab", W + "br"):
        anc, bad = el.getparent(), False
        while anc is not None and anc is not node:
            if anc.tag in (W + "del", W + "moveFrom"):
                bad = True
                break
            anc = anc.getparent()
        if bad:
            continue
        if el.tag == W + "tab":
            out.append("\t")
        elif el.tag == W + "br":
            out.append("\n")
        else:
            out.append(el.text or "")
    return "".join(out)


def border_on(el):
    if el is None:
        return False
    v = el.get(W + "val")
    return v not in (None, "nil", "none")


def style_borders(styles_root, style_id):
    """Return the set of borders ('left','right','insideV') switched on by a table style."""
    on = set()
    if styles_root is None or not style_id:
        return on
    seen = set()
    while style_id and style_id not in seen:
        seen.add(style_id)
        st = styles_root.find(f"{W}style[@{W}styleId='{style_id}']")
        if st is None:
            break
        b = st.find(f"{W}tblPr/{W}tblBorders")
        if b is not None:
            for side in ("left", "right", "insideV", "start", "end"):
                if border_on(b.find(W + side)):
                    on.add(side)
        based = st.find(W + "basedOn")
        style_id = based.get(W + "val") if based is not None else None
    return on


def has_decimal_tab(tc):
    for t in tc.iter(W + "tab"):
        if t.getparent().tag == W + "tabs" and t.get(W + "val") == "decimal":
            return True
    return False


def check_table(idx, tbl, title, styles_root, style, allow_asterisks=False, decimal_align=False):
    issues = defaultdict(list)
    tblpr = tbl.find(W + "tblPr")
    # --- vertical lines
    vert = set()
    sid = tblpr.find(W + "tblStyle").get(W + "val") if tblpr is not None and tblpr.find(W + "tblStyle") is not None else None
    vert |= style_borders(styles_root, sid)
    tb = tblpr.find(W + "tblBorders") if tblpr is not None else None
    if tb is not None:
        for side in ("left", "right", "insideV", "start", "end"):
            el = tb.find(W + side)
            if el is not None:
                (vert.add if border_on(el) else vert.discard)(side)
    cell_vert = 0
    shaded = 0
    colored = 0
    for tc in tbl.iter(W + "tc"):
        tcb = tc.find(f"{W}tcPr/{W}tcBorders")
        if tcb is not None and any(border_on(tcb.find(W + s)) for s in ("left", "right", "start", "end")):
            cell_vert += 1
        shd = tc.find(f"{W}tcPr/{W}shd")
        if shd is not None and (shd.get(W + "fill") or "auto").upper() not in ("AUTO", "FFFFFF", ""):
            shaded += 1
        for c in tc.iter(W + "color"):
            if (c.get(W + "val") or "auto").upper() not in ("AUTO", "000000"):
                colored += 1
                break
    if vert or cell_vert:
        issues["Construction"].append("Vertical lines found (table style or cell borders). Neither AMA/JAMA nor APA/GSA journals use vertical rules; keep only horizontal lines.")
    if shaded:
        issues["Construction"].append(f"{shaded} shaded cell(s). Remove shading (GSA journals ban shading; JAMA re-creates tables in house style).")
    if colored:
        issues["Construction"].append(f"{colored} cell(s) with colored text. Use black text only.")

    # --- grid of cell texts
    rows = []
    for tr in tbl.iter(W + "tr"):
        row = []
        for tc in tr.findall(W + "tc"):
            row.append(text_of(tc))
        rows.append(row)
    if not rows:
        return issues
    n_cols = max(len(r) for r in rows)

    tab_cells = [c for r in rows for c in r if "\t" in c or re.search(r"\S {3,}\S", c)]
    if tab_cells:
        issues["Construction"].append(f"{len(tab_cells)} cell(s) use tabs or runs of spaces to position text (e.g., \"{tab_cells[0].strip()[:40]}\"). Put each value in its own cell; use cell alignment or an indent instead.")
    br_cells = [c for r in rows for c in r if "\n" in c.strip()]
    if br_cells:
        issues["Construction"].append(f"{len(br_cells)} cell(s) stack several values with line breaks (e.g., \"{br_cells[0].strip()[:40].replace(chr(10), ' / ')}\"). Use one row per value so data stay in separate cells.")
    header0 = [c.strip() for c in rows[0]]
    pcols0 = {j for j, h in enumerate(header0) if PVAL_COL.match(h)}
    empty = 0
    p_spans = 0
    for r in rows[1:]:
        data = [(j, c) for j, c in enumerate(r) if j > 0]
        filled = [j for j, c in data if c.strip()]
        if not filled:
            continue  # section/category row with no data
        if all(j in pcols0 for j in filled):
            continue  # category row that carries only the overall P value
        for j, c in data:
            if not c.strip():
                if j in pcols0:
                    p_spans += 1
                else:
                    empty += 1
    if p_spans and style == "ama":
        issues["Construction"].append(f"{p_spans} empty P value cell(s) under category rows. JAMA: when a value applies to several rows (e.g., an overall P value), merge the cells vertically or place the P value on the category row only.")
    if empty:
        if style == "ama":
            issues["Construction"].append(f"{empty} empty data cell(s) in rows that have other values. JAMA asks to avoid empty cells: use NA (defined in a footnote) or merge cells vertically for values spanning rows.")
        else:
            issues["Construction"].append(f"{empty} empty data cell(s) in rows that have other values. Use an em dash (—) or NA for not applicable/not available and define it in the table note, or merge cells for values spanning rows.")

    # --- header row and column roles
    header = [c.strip() for c in rows[0]] + [""] * (n_cols - len(rows[0]))
    pcols = {j for j, h in enumerate(header) if PVAL_COL.match(h)}

    # group n from header like "(n = 72)" or "n = 72", or a "Number of participants" row
    col_n = {}
    for j, h in enumerate(header):
        m = re.search(r"\b[nN]\s*=\s*([\d,]+)", h)
        if m:
            col_n[j] = int(m.group(1).replace(",", ""))
    for r in rows[1:4]:
        if r and re.match(r"(number of participants|no\. of participants|^n$|^n\b|total)", r[0].strip(), re.I):
            for j, c in enumerate(r[1:], start=1):
                m = re.fullmatch(r"\s*([\d,]+)\s*", c)
                if m and j not in col_n:
                    col_n[j] = int(m.group(1).replace(",", ""))

    # --- decimals per column (skip stub and P columns)
    mixed = []
    for j in range(1, n_cols):
        if j in pcols:
            continue
        dec_counts = defaultdict(int)
        for r in rows[1:]:
            if j >= len(r):
                continue
            c = r[j]
            if "%" in c:
                continue  # percentages checked separately
            m = NUM.search(c.replace("−", "-"))
            if m and m.group(0) and not re.fullmatch(r"\s*[\d,]+\s*\(.*\)\s*", c):
                d = len(m.group(1)) if m.group(1) else 0
                if "." in c or d:
                    dec_counts[d] += 1
        if len(dec_counts) > 1:
            label = header[j][:30] or f"column {j + 1}"
            mixed.append(f"{label} ({', '.join(f'{k} dp x{v}' for k, v in sorted(dec_counts.items()))})")
    if mixed:
        issues["Numbers"].append("Mixed decimal places among continuous values in the same column: " + "; ".join(mixed) + ". Use the same number of decimals for comparable values (e.g., all means and SDs to 1 decimal); differences are fine only between rows measured on different scales.")

    pct_dec = defaultdict(int)
    for r in rows[1:]:
        for j, c in enumerate(r[1:], start=1):
            for m in re.finditer(r"\(\s*\d+\.(\d+)\s*%?\s*\)|\b\d+\.(\d+)\s*%", c):
                if j in col_n and col_n[j] < 100:
                    pct_dec[j] += 1
    if pct_dec and style == "ama":
        cols = ", ".join(header[j][:30] if "=" in header[j] else f"{header[j][:25] or 'column ' + str(j + 1)} (n = {col_n[j]})" for j in pct_dec)
        issues["Numbers"].append(f"Percentages with decimals in groups with n < 100: {cols}. JAMA Network: \"Do not use decimal places (ie, xx%, not xx.xx%) if the sample size is less than 100.\"")
    elif pct_dec:
        cols = ", ".join(header[j][:30] if "=" in header[j] else f"{header[j][:25] or 'column ' + str(j + 1)} (n = {col_n[j]})" for j in pct_dec)
        issues["Numbers"].append(f"Percentages with decimals in small groups ({cols}). Consider whole-number percentages when n < 100.")

    hyphen_neg = [c.strip() for r in rows[1:] for c in r[1:] if re.search(r"(^|[\s(\[,;])-\d", c)]
    if hyphen_neg:
        issues["Numbers"].append(f"{len(hyphen_neg)} cell(s) use a hyphen as a minus sign (e.g., \"{hyphen_neg[0][:30]}\"). Use the true minus sign (−, U+2212), and write ranges with negative values with \"to\" (−0.4 to −0.2).")
    pm = [c for r in rows for c in r if "±" in c]
    if pm:
        issues["Numbers"].append(f"{len(pm)} cell(s) use ±. Report mean (SD) (AMA/JAMA) or separate M and SD columns (APA), and say which measure of variability is shown.")
    commas = [c for r in rows[1:] for c in r[1:] if re.search(r"\b\d{1,3},\d{3}\b", c)]
    if commas and style == "ama":
        issues["Numbers"].append(f"{len(commas)} cell(s) use commas in numbers (e.g., \"{commas[0].strip()[:20]}\"). AMA style: no comma in 4-digit numbers (2449); a thin space for 5+ digits (12 450).")
    if style in ("apa", "asa"):
        nocomma = [c for r in rows[1:] for c in r[1:] if re.search(r"(?<![\d.,])\d{4,}(?![\d.,])", c) and not re.search(r"\b(19|20)\d\d\b", c)]
        if nocomma:
            issues["Numbers"].append(f"{len(nocomma)} cell(s) have 4+ digit numbers without commas (e.g., \"{nocomma[0].strip()[:20]}\"). {'APA' if style == 'apa' else 'ASA (Chicago-based)'} style uses commas (2,449).")

    # --- P values anywhere in the table
    alltext = "\n".join(c for r in rows for c in r)
    lead = re.findall(r"(?<![\d.])0\.\d+", "\n".join(rows[i][j] for i in range(1, len(rows)) for j in range(len(rows[i])) if j in pcols))
    lead += re.findall(r"[pP]\s*[<=>≤]\s*0\.\d+", alltext)
    if lead:
        issues["P values"].append(f"{len(lead)} P value(s) with a leading zero (e.g., \"{lead[0]}\"). Both AMA and APA drop the leading zero: .04, <.001.")
    pcells = [rows[i][j] for i in range(1, len(rows)) for j in range(len(rows[i])) if j in pcols]
    if re.search(r"[pP]\s*[=<]\s*0?\.000\b", alltext) or any(re.fullmatch(r"\s*[<=]?\s*0?\.0+\s*", c) for c in pcells):
        issues["P values"].append("A P value is shown as .000. Report it as <.001.")
    if style == "ama":
        two_dec = [c.strip() for i in range(1, len(rows)) for j, c in enumerate(rows[i]) if j in pcols and re.fullmatch(r"\s*[<>=]?\s*0?\.\d{4,}\s*", c)]
        if two_dec:
            issues["P values"].append(f"P values with more than 3 decimals (e.g., \"{two_dec[0]}\"). AMA: 2 digits in general, 3 when P < .01, <.001 as the floor.")
    if style == "asa":
        stars = re.search(r"\d\*", alltext)
        if stars and not re.search(r"(one|two)[- ]tailed", (title or "") + alltext, re.I):
            issues["Notes"].append("Significance asterisks are used; ASA journals ask you to state in the note whether tests are one- or two-tailed (e.g., \"*p < .05, **p < .01, ***p < .001 (two-tailed tests)\"). Don't mark p < .10 as significant.")
    if decimal_align:
        numeric_cells = 0
        aligned = 0
        for tr_i, tr in enumerate(tbl.iter(W + "tr")):
            if tr_i == 0:
                continue
            for ci, tc in enumerate(tr.findall(W + "tc")):
                if ci == 0:
                    continue
                txt = text_of(tc).strip()
                if re.fullmatch(r"[\u2212\-<>]?\s*\d[\d,]*(\.\d+)?(\*{0,3})?(\s*\(.*\))?\s*", txt):
                    numeric_cells += 1
                    if has_decimal_tab(tc):
                        aligned += 1
        if numeric_cells and aligned < numeric_cells:
            issues["Construction"].append(f"{numeric_cells - aligned} of {numeric_cells} numeric cell(s) are not aligned on the decimal point. JHSB asks to align numbers by decimal; the table formatter's --decimal-align option sets decimal tabs in each cell.")
    if style == "apa" and pcols:
        hdr = header[min(pcols)]
        if hdr and not re.match(r"^\s*p\b", hdr):
            issues["P values"].append(f"P value column headed \"{hdr}\": APA uses an italic lowercase p.")

    # --- footnote markers
    syms = re.findall(r"[†‡§¶]", alltext)
    if syms:
        issues["Notes"].append(f"Symbol footnote markers ({' '.join(sorted(set(syms)))}) found. Use superscript lowercase letters (a, b, c) for footnotes{'; asterisks only for significance levels' if style in ('apa', 'asa') else ''}. (PRPR is an exception: it uses \u2020 for p < .10.)")
    if style == "ama" and not allow_asterisks and re.search(r"\d\*|\*\s*$", alltext):
        issues["Notes"].append("Asterisks found next to values. JAMA Network tables mark footnotes with superscript letters and generally report exact P values rather than significance asterisks.")

    # --- title
    if not title:
        issues["Title"].append("No \"Table N.\" title found just above this table.")
    else:
        words_n = len(re.sub(r"^table\s+\d+\.?\s*", "", title, flags=re.I).split())
        if style == "ama" and words_n > 15:
            issues["Title"].append(f"Title is {words_n} words; JAMA asks for a brief descriptive phrase, preferably 10-15 words.")
        if style == "apa" and re.match(r"^table\s*\d+[.:]?\s+\S", title, re.I):
            issues["Title"].append("APA puts the table number on its own line in bold (**Table 1**) and the title on the next line in italic Title Case, with no period after the number.")
        if re.search(r"\((?:[A-Z][a-z]+ )+(?:Study|Survey)[^)]*\d{4}\)", title):
            issues["Title"].append("Title includes a data source/year in parentheses; consider moving it to a table note.")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--style", choices=["ama", "apa", "asa"], required=True)
    ap.add_argument("--decimal-align", action="store_true", help="flag numeric cells not aligned on the decimal point (JHSB)")
    ap.add_argument("--include-supplement", action="store_true")
    ap.add_argument("--allow-asterisks", action="store_true", help="JGA: asterisk P value notes are allowed")
    a = ap.parse_args()
    p = Path(a.path)
    if p.suffix.lower() != ".docx":
        sys.exit("table_check.py reads .docx files only.")
    from lxml import etree
    with zipfile.ZipFile(p) as z:
        root = etree.fromstring(z.read("word/document.xml"))
        styles_root = etree.fromstring(z.read("word/styles.xml")) if "word/styles.xml" in z.namelist() else None
    body = root.find(W + "body")

    items = []

    def walk(node):
        for ch in node:
            if ch.tag == W + "p":
                items.append(("p", text_of(ch).strip(), ch))
            elif ch.tag == W + "tbl":
                items.append(("tbl", "", ch))
            elif ch.tag == W + "sdt":
                c = ch.find(W + "sdtContent")
                if c is not None:
                    walk(c)
    walk(body)

    in_supp, last_title, n, caption_titles, report = False, None, 0, [], []
    since_title = 99
    for kind, txt, node in items:
        if kind == "p":
            if re.fullmatch(r"(supplement(ary|al)?( material| online content)?( \d+)?|emethods|eappendix)", txt, re.I):
                in_supp = True
            if re.match(r"^(e?table)\s*\d+[.:]?\s", txt, re.I) or re.fullmatch(r"(e?table)\s*\d+[.:]?", txt, re.I):
                last_title, since_title = txt, 0
                if not txt.lower().startswith("e"):
                    caption_titles.append(txt)
            elif txt:
                since_title += 1
                if since_title == 1 and last_title and re.fullmatch(r"(e?table)\s*\d+", last_title, re.I):
                    last_title = last_title + " " + txt  # APA: number line, then title line
        else:
            if in_supp and not a.include_supplement:
                continue
            n += 1
            title = last_title if since_title <= 2 else None
            report.append((n, title, check_table(n, node, title, styles_root, a.style, a.allow_asterisks, a.decimal_align)))
            last_title, since_title = None, 99

    if len(caption_titles) > n and not a.include_supplement:
        report.append((None, None, {"Construction": [f"{len(caption_titles)} table titles but only {n} Word table(s) before the Supplement: a table may be pasted as an image or typed with tabs. Tables must be editable Word tables."]}))

    if not report:
        print("No tables found before the Supplement.")
        return
    total = 0
    for num, title, issues in report:
        head = f"Table {num}" if num else "Document"
        print(f"\n=== {head}: {title or ''}".rstrip())
        if not any(issues.values()):
            print("  No issues found.")
        for cat in ("Construction", "Numbers", "P values", "Notes", "Title"):
            for msg in issues.get(cat, []):
                total += 1
                print(f"  [{cat}] {msg}")
    print(f"\n{total} item(s) to review. These are checks, not fixes; confirm each against the journal's instructions.")


if __name__ == "__main__":
    main()
```

## Layout checker

Write this to the scratchpad as `layout_check.py` before running it. Use `--journal jga`, `jgb`, `tg`, `ia`, or `ppar`.

```python
#!/usr/bin/env python3
"""Page layout and heading checker for journal manuscripts (.docx).

Usage:
    python layout_check.py manuscript.docx --journal jama   # JAMA Network journals
    python layout_check.py manuscript.docx --journal jga    # Journals of Gerontology Series A
    python layout_check.py manuscript.docx --journal jgb    # Journals of Gerontology Series B
    python layout_check.py manuscript.docx --journal tg     # The Gerontologist
    python layout_check.py manuscript.docx --journal ia     # Innovation in Aging
    python layout_check.py manuscript.docx --journal ppar   # Public Policy & Aging Report
    Sociology and demography: asr, ajs, sf, socius, esr, bjs, jhsb, ssm, shi, demography,
    pdr, prpr, alcr, ssr, rssm, smx (Sociological Methodology), smr, sre
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

# Sociology and demography journals (checked Oct 2026 where pages were reachable; "sug" where not stated)
def _soc(name, **kw):
    base = dict(name=name, font=None, sizes=(12,), size_src="sug", font_src=None, double="sug", ragged="sug",
                margins=None, pagenum="sug", lines=None, footnotes=None, newpage=["references"],
                each_table_page=False, apa_headings=False, word_notes=None, no_intro_heading=False,
                caps_l1=False)
    base.update(kw)
    return base


RULES.update({
    "asr": _soc("American Sociological Review", font="Times New Roman", size_src="req", font_src="req", double="req",
                margins=1440, pagenum="none", word_notes="sug", newpage=["references"]),
    "jhsb": _soc("Journal of Health and Social Behavior", font="Times New Roman", size_src="req", font_src="req",
                 double="req", margins=(1440, 14400), margin_src="req", word_notes="req", no_intro_heading=True,
                 newpage=["text", "notes", "references", "tables"], each_table_page=True),
    "sre": _soc("Sociology of Race and Ethnicity", font="Times New Roman", size_src="req", font_src="req",
                double="req", margins=(1440, 2160), margin_src="req", word_notes="req",
                newpage=["text", "notes", "references", "tables"], each_table_page=True),
    "smx": _soc("Sociological Methodology", font="Times New Roman", size_src="req", font_src="req", double="req",
                margins=1800, margin_src="req", word_notes="sug"),
    "smr": _soc("Sociological Methods & Research", size_src="req", double="req", margins=1800, margin_src="req"),
    "socius": _soc("Socius", double="req", pagenum="req"),
    "ajs": _soc("American Journal of Sociology", sizes=(11, 12), size_src="req", double="req", margins=1440,
                newpage=["references", "tables"]),
    "sf": _soc("Social Forces", newpage=["references", "tables"], each_table_page=True),
    "esr": _soc("European Sociological Review", double="req", pagenum="req"),
    "bjs": _soc("British Journal of Sociology", double="req", newpage=["references", "tables"], each_table_page=True),
    "demography": _soc("Demography", size_src="req", double="req", ragged="req", margins=1440, margin_src="req",
                       pagenum="req", newpage=["references", "tables"], each_table_page=True),
    "prpr": _soc("Population Research and Policy Review", size_src="req", double="req", ragged="req", margins=1440,
                 margin_src="req", pagenum="req", lines="none", caps_l1=True, newpage=["text", "references", "tables"], each_table_page=True),
    "ssm": _soc("Social Science & Medicine (and SSM journals)"),
    "shi": _soc("Sociology of Health & Illness", double="req"),
    "pdr": _soc("Population and Development Review"),
    "alcr": _soc("Advances in Life Course Research", pagenum="sug", lines="sug"),
    "ssr": _soc("Social Science Research", pagenum="sug", lines="sug"),
    "rssm": _soc("Research in Social Stratification and Mobility", pagenum="sug", lines="sug"),
})
for _r in RULES.values():
    for k, v in dict(word_notes=None, no_intro_heading=False, caps_l1=False).items():
        _r.setdefault(k, v)

SECTION_PATTERNS = {
    "key_points": r"key points",
    "abstract": r"(structured )?abstract",
    "text": r"(introduction|background)",
    "references": r"(references|bibliography|literature cited)",
    "notes": r"(notes|endnotes)",
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
            m = rules["margins"]
            lo, hi = (m if isinstance(m, tuple) else (m, m))
            if any(v < lo - 20 or v > hi + 20 for v in vals.values()):
                margins_bad.append(", ".join(f"{k} {v / 1440:.2f} in" for k, v in vals.items()))
        if sp.find(W + "lnNumType") is not None:
            lnnum = True
        if sp.findall(W + "footerReference") or sp.findall(W + "headerReference"):
            has_pgnum_ref = True
    if sizes:
        add("Page setup", "Paper size: " + ", ".join(f"{k} ({v} section{'s' if v > 1 else ''})" for k, v in sizes.items()) + ". US Letter or A4 are both accepted by these journals.")
    if margins_bad:
        m = rules["margins"]
        lo, hi = (m if isinstance(m, tuple) else (m, m))
        want = (f"{lo / 1440:g} inch" if lo == hi else f"at least {lo / 1440:g} inch" if hi >= 14400
                else f"between {lo / 1440:g} and {hi / 1440:g} inches")
        add("Page setup", f"Margins should be {want} on every side; found {margins_bad[0]}.",
            "req" if a.journal == "jgb" or rules.get("margin_src") == "req" else "sug")
    if lnnum and rules["lines"] == "none":
        add("Page setup", f"Line numbering is on. {rules['name']} asks for no line numbering; turn it off (Layout > Line Numbers > None).", "req")
    elif not lnnum and rules["lines"] in ("req", "sug"):
        add("Page setup", "No line numbers. Turn them on (Layout > Line Numbers > Continuous).", rules["lines"])
    elif lnnum:
        add("Page setup", "Line numbering is on. That is fine for review unless the journal says otherwise.")

    # page numbers: look for a PAGE field in headers/footers
    pg_field = False
    for n in names:
        if re.match(r"word/(header|footer)\d*\.xml", n):
            x = z.read(n).decode("utf8", "ignore")
            if re.search(r"instrText[^>]*>\s*PAGE\b|fldSimple[^>]*instr=\"\s*PAGE\b", x):
                pg_field = True
    if pg_field and rules["pagenum"] == "none":
        add("Page setup", f"Page numbers found. {rules['name']} asks authors to remove page numbers (the system renumbers the file).", "req")
    if not pg_field and rules["pagenum"] != "none":
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
            if real and rules.get("word_notes"):
                add("Structure", f"{len(real)} Word {label}(s) found. {rules['name']} wants notes typed in a separate NOTES section after the text (superscript numbers in the text), not Word's built-in note function.", rules["word_notes"])
            elif real and rules["footnotes"] == "req":
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
    labels = {"notes": "Notes", "key_points": "Key Points", "abstract": "Abstract", "text": "the main text (Introduction)",
              "references": "References", "legends": "Figure legends/captions", "tables": "Tables"}
    for key in wanted:
        if key == "tables":
            continue
        if key in found_sections and not starts_new_page(found_sections[key]):
            add("Structure", f"{labels[key]} does not start on a new page. Insert a page break before it (Ctrl/Cmd+Enter).", "req" if a.journal in ("jama", "jgb", "jga", "jhsb", "prpr", "demography") else "sug")
    if caption_idx:
        not_new = [paras_info[i][2][:20] for i in caption_idx if not starts_new_page(i)]
        if rules["each_table_page"] and not_new:
            add("Structure", f"{len(not_new)} table(s) don't start on their own page ({', '.join(not_new[:3])}...). {rules['name']} wants each table on a separate page at the end of the file.", "req" if a.journal in ("jga", "jgb", "tg", "ia", "ppar", "jhsb", "sf", "demography", "prpr", "bjs") else "sug")
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
        if rules.get("no_intro_heading") and any(h["text"].lower().rstrip(".:") == "introduction" for h in headings):
            add("Headings", "Remove the \"Introduction\" heading: JHSB text starts with the full title and goes straight into the introduction, followed by Background, Data and Methods, Results, Discussion.", "req")
        if rules.get("caps_l1"):
            for h in headings:
                low = h["text"].lower().rstrip(".:")
                if low in ("introduction", "background", "data and methods", "results", "discussion and conclusion", "discussion", "conclusion", "references") and h["text"] != h["text"].upper():
                    add("Headings", f"\"{h['text']}\": PRPR Level 1 headings are 14-pt bold ALL CAPS on their own line.", "req")
        if rules["apa_headings"]:
            main_names = {"introduction", "methods", "method", "results", "discussion", "conclusions", "conclusion",
                          "research design and methods", "background and objectives", "discussion and implications", "implications",
                          "background", "data and methods", "findings", "discussion and conclusion"}
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
            main_names = {"introduction", "methods", "results", "discussion", "conclusions", "limitations",
                          "background", "data and methods", "findings", "conclusion"}
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
```

## Table formatter

Write this to the scratchpad as `table_format.py` before running it. Use `--style apa` (or `--style ama` for JGA). Run it only when the author asks for tables to be formatted.

```python
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
NUMERIC_CELL = re.compile(r"[\u2212\-<>]?\s*\d[\d,\u2009]*(\.\d+)?(\*{0,3})?(\s*[\(\[].*[\)\]])?\s*")


def decimal_align(tbl, log, label):
    """Put a decimal tab in each numeric data cell so values line up on the decimal point."""
    n = 0
    rows = tbl.findall(q("tr"))
    grid = [int(g.get(q("w"), 0)) for g in tbl.findall(f"{q('tblGrid')}/{q('gridCol')}")]
    for ri, tr in enumerate(rows):
        if ri == 0:
            continue
        for ci, tc in enumerate(tr.findall(q("tc"))):
            if ci == 0 or not NUMERIC_CELL.fullmatch(cell_text(tc).strip() or "x"):
                continue
            tcw = tc.find(f"{q('tcPr')}/{q('tcW')}")
            width = int(tcw.get(q("w"), 0)) if tcw is not None and tcw.get(q("type")) == "dxa" else (grid[ci] if ci < len(grid) else 1440)
            txt = cell_text(tc).strip()
            # put the decimal point a little left of center when a parenthetical follows
            pos = max(360, int(width * (0.40 if "(" in txt or "[" in txt else 0.50)))
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

    log = [f"# Table formatting change log ({a.style.upper()} style)\n",
           f"Source: `{src.name}`  \nOutput: `{dst.name}`  \nText changes are {'applied directly' if a.no_track else 'tracked changes by \"' + a.author + '\"'}; layout changes are applied directly and listed below.\n"]
    in_supp, last_title, n_done, skipped_total = False, None, 0, 0
    for kind, node in items:
        if kind == "p":
            t = "".join(x.text or "" for x in node.iter(q("t"))).strip()
            if re.fullmatch(r"(supplement(ary|al)?( material| online content)?( \d+)?|emethods|eappendix)", t, re.I):
                in_supp = True
            if re.match(r"^e?table\s*\d+", t, re.I):
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
```
