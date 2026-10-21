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

Run multiple features in this order: requirements (1) and counts (10) first, then checks (5-8, 13-16), then writing and edits (2-4, 9, 11, 12), then 17-18.

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


def check_table(idx, tbl, title, styles_root, style, allow_asterisks=False):
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
    if style == "apa":
        nocomma = [c for r in rows[1:] for c in r[1:] if re.search(r"(?<![\d.,])\d{4,}(?![\d.,])", c) and not re.search(r"\b(19|20)\d\d\b", c)]
        if nocomma:
            issues["Numbers"].append(f"{len(nocomma)} cell(s) have 4+ digit numbers without commas (e.g., \"{nocomma[0].strip()[:20]}\"). APA style uses commas (2,449).")

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
    if style == "apa" and pcols:
        hdr = header[min(pcols)]
        if hdr and not re.match(r"^\s*p\b", hdr):
            issues["P values"].append(f"P value column headed \"{hdr}\": APA uses an italic lowercase p.")

    # --- footnote markers
    syms = re.findall(r"[†‡§¶]", alltext)
    if syms:
        issues["Notes"].append(f"Symbol footnote markers ({' '.join(sorted(set(syms)))}) found. Use superscript lowercase letters (a, b, c) for footnotes{'; asterisks only for significance levels' if style == 'apa' else ''}.")
    if style == "ama" and not allow_asterisks and re.search(r"\d\*|\*\s*$", alltext):
        issues["Notes"].append("Asterisks found next to values. JAMA Network tables mark footnotes with superscript letters and generally report exact P values rather than significance asterisks.")

    # --- title
    if not title:
        issues["Title"].append("No \"Table N.\" title found just above this table.")
    else:
        words_n = len(re.sub(r"^table\s+\d+\.?\s*", "", title, flags=re.I).split())
        if style == "ama" and words_n > 15:
            issues["Title"].append(f"Title is {words_n} words; JAMA asks for a brief descriptive phrase, preferably 10-15 words.")
        if re.search(r"\((?:[A-Z][a-z]+ )+(?:Study|Survey)[^)]*\d{4}\)", title):
            issues["Title"].append("Title includes a data source/year in parentheses; consider moving it to a table note.")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--style", choices=["ama", "apa"], required=True)
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
            report.append((n, title, check_table(n, node, title, styles_root, a.style, a.allow_asterisks)))
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
