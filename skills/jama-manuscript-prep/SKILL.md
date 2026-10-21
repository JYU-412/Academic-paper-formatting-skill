---
name: jama-manuscript-prep
description: Prepare, polish, check, and revise research manuscripts for JAMA Network journals (JAMA, JAMA Network Open, JAMA Internal Medicine, JAMA Psychiatry, JAMA Neurology, JAMA Health Forum, and the other JAMA specialty journals). Use this skill whenever the user wants to write a JAMA-style structured abstract or Key Points, fit a paper to JAMA word or display-item limits, trim text while keeping their voice, check AMA Manual of Style issues, check STROBE/CONSORT/PRISMA or other reporting-guideline compliance, check references, title page or declarations, draft a cover letter, get a mock peer review before submission, respond to reviewer comments, or reformat a rejected paper for another JAMA Network journal, even if they only say "get my paper ready for JAMA" or "help me respond to the reviewers".
---

# JAMA Network Manuscript Prep

A toolkit for getting a research manuscript ready for a JAMA Network journal, and for the revision stage after peer review. The person using this is the author. Their scientific judgment and their writing voice come first: this skill does formatting, checking, condensing, and drafting, and it shows every change so the author stays in control.

## Step 1: Gather the inputs

Every run needs the manuscript (a .docx, .pdf, or pasted text). Before doing anything else, read it in full. If it is a .docx, read it with tracked changes accepted (`pandoc file.docx -t plain --track-changes=accept --wrap=none`), since co-author edits are often still tracked, and run the word counter (Step 3) on it at the same time, since that gives you the section structure.

Then confirm three things, inferring what you can from the manuscript and asking only about what is missing:

1. **Target journal**, e.g., JAMA Network Open or JAMA Internal Medicine.
2. **Article type**, usually Original Investigation or Research Letter.
3. **Study type**, e.g., cohort, cross-sectional, RCT, meta-analysis, qualitative. This decides the reporting guideline and the title/subtitle rules.

Stage-specific inputs, requested only when the chosen feature needs them:
- Reviewer and editor comments (features 17 and 18)
- The rejection letter and the new target journal (feature 18)
- A completed reporting checklist, if the author has one (feature 12)
- Optional: an earlier published paper by the author, if they want extra help matching their voice (features 8 and 10). Otherwise the manuscript itself is the voice reference.

## Step 2: Show the menu and let the author choose

Present this menu, grouped by stage, so the author can pick only what they need right now. Accept numbers, ranges ("1-6"), a stage name ("all of Polishing"), or "everything". If the author's opening message already says what they want ("write my Key Points"), skip the menu and do that.

**Preparing**
1. Journal-specific requirements: pull the current limits and rules for the chosen journal and article type
2. Structured abstract: write or rewrite it with JAMA headings
3. Key Points: write the Question / Findings / Meaning box
4. Section order and completeness check

**Polishing**
5. AMA Manual of Style check
6. Consistency check: numbers across abstract, Key Points, text, and tables
7. Causal language check
8. Clarity edit in the author's voice

**Fitting the limits**
9. Word count and limits dashboard
10. Trim to fit, with every cut tracked
11. Move-to-Supplement suggestions

**Submitting**
12. Reporting guideline checklist mapping
13. Reference check
14. Title page and declarations check
15. Cover letter draft
16. Pre-submission mock review

**Revising**
17. Response-to-reviewers table
18. Retarget to another JAMA Network journal

When several features are chosen, run them in a sensible order: requirements (1) and counts (9) first, because everything else depends on the limits; then checks (4-7, 12-14); then writing and editing (2, 3, 8, 10, 11); then submission pieces (15, 16). Running edits after the checks means the edits can fix what the checks found.

## Step 3: Get the current journal requirements

The JAMA Network journals share most rules, but limits differ by journal and article type, and they change over time. Before applying any limit:

1. Use the **JAMA Network format reference** section below. It holds the shared rules as of October 2026 and the URL pattern for each journal's Instructions for Authors.
2. Fetch the target journal's live Instructions for Authors page and check the numbers for the chosen article and study type. If the live page differs from the reference file, the live page wins; tell the author what changed.
3. If the page can't be fetched, use the reference file and say so in the output, so the author knows to double-check.

For tables, also write the **Table checker** at the end of this file to the scratchpad as `table_check.py` and run `python table_check.py manuscript.docx --style ama`. It checks every Word table for vertical lines, shading, values aligned with tabs or stacked with line breaks, empty cells, mixed decimal places, percentages with decimals in groups under 100, hyphens used as minus signs, ±, P value format, and footnote markers.

For counts, write the script in the **Word counter** section at the end of this file to the scratchpad as `jama_count.py` and run it (it needs `lxml`; install with `pip install lxml --break-system-packages` if missing). It reads .docx files with tracked changes accepted, so unaccepted co-author insertions are counted and tracked deletions are not. It reports the main text, abstract, and Key Points word counts, title length, tables and figures, and references, compared with the limits you pass in:

```bash
python jama_count.py manuscript.docx --text-limit 3000 --abstract-limit 350 --kp-limit 100 --display-limit 5 --ref-limit 75
```

It accepts .docx, .md, and .txt. For a PDF, extract the text first (`pdftotext -layout`) and run it on the .txt. If the draft has no Introduction heading, it treats the long paragraphs before Methods as the Introduction. If its section detection looks wrong for an unusual layout, say so and count that section by hand rather than trusting a bad number.

## How to do each feature

Detailed instructions for every feature are in the **Feature playbook** section below. Read the entries for the features the author chose. A few principles apply throughout:

**Never invent content.** Abstracts, Key Points, cover letters, and responses to reviewers are built only from what the manuscript, the reviewer comments, or the author says. If something needed is missing (a sample size, a CI, the registry number), leave a clearly marked placeholder like `[CI NEEDED]` and list it at the end. A made-up number in a submitted paper is far worse than a gap.

**Keep the author's voice.** Before editing or trimming, note the author's habits from the manuscript: sentence length, hedging style ("suggests" vs "indicates"), how they open paragraphs, first person or not, preferred terms. Edit within those habits. Cut words and redundancy before rewriting sentences; when a sentence has to be rewritten, make it sound like the author's other sentences, not like a generic editor. The author should read the result and recognize it as theirs.

**Show every change.** For edits and trims, give the revised text and a change log that lists what was cut or changed and why, with the word savings. For checks, list each issue with its location (section and a short quote of the sentence), the problem, and a suggested fix. The author decides what to accept.

**Flag, don't fix, the science.** If a check turns up something substantive (a primary outcome missing from the abstract, a mismatch between Methods and Results, an unreported limitation), raise it as a question for the author. Don't change the science or the conclusions to make a check pass.

**References are checked, not generated.** JAMA Network policy says AI tools should not be used to generate or format references. Feature 13 reports problems; the author fixes them in their reference manager.

## Output

Match the output to what was asked:

- **Checks and the dashboard** (1, 4-7, 9, 12-14): a short report in the reply, grouped by severity: must fix before submission, should fix, optional. Put a one-line verdict at the top ("Over the main-text limit by 412 words; abstract and Key Points within limits").
- **New text** (2, 3, 15): the text itself, ready to paste, followed by its word count and any placeholders.
- **Edits** (8, 10, 11): the revised section(s) followed by the change log. When the author gave a .docx and asks for the whole manuscript back, edit a copy of the file with tracked changes using the docx skill, so they can accept or reject each change in Word.
- **Mock review** (16): a reviewer-style report (summary, major comments, minor comments). If the gerontology-paper-review skill is available and the paper is on aging or a related topic, use it for this step.
- **Response to reviewers** (17): a table with the comment, the response, and the change made with its location in the revised manuscript.

End with a short list of open items: placeholders to fill, decisions only the author can make, and anything that needs checking against the live journal page.

## A note on AI disclosure

JAMA Network journals require authors to disclose use of AI tools in manuscript preparation and to take responsibility for the content. When the author uses this skill for writing or editing (features 2, 3, 8, 10, 15, 17), remind them once, briefly, at the end of the output, that they may need to disclose it in the Acknowledgment or Methods per the journal's current policy. Don't repeat this on every output in the same session.

## JAMA Network format reference

Compiled October 2026 from the Instructions for Authors pages of JAMA Network Open and JAMA Internal Medicine. The JAMA Network journals share one instructions template, so most rules below apply across the network. **Always check the live page for the target journal before applying a number**, because limits differ by journal and are revised.

### Contents
1. Instructions for Authors URLs
2. Article type limits
3. Study types: subtitle and reporting guideline
4. Title and title page
5. Key Points
6. Structured abstracts
7. Main text structure
8. Tables and figures
9. References
10. Supplement
11. Style rules that come up most
12. Other required items
13. AI policy

---

### 1. Instructions for Authors URLs

Pattern: `https://jamanetwork.com/journals/<slug>/pages/instructions-for-authors`

| Journal | Slug |
|---|---|
| JAMA | jama |
| JAMA Network Open | jamanetworkopen |
| JAMA Internal Medicine | jamainternalmedicine |
| JAMA Cardiology | jamacardiology |
| JAMA Dermatology | jamadermatology |
| JAMA Health Forum | jama-health-forum |
| JAMA Neurology | jamaneurology |
| JAMA Oncology | jamaoncology |
| JAMA Ophthalmology | jamaophthalmology |
| JAMA Otolaryngology–Head & Neck Surgery | jamaotolaryngology |
| JAMA Pediatrics | jamapediatrics |
| JAMA Psychiatry | jamapsychiatry |
| JAMA Surgery | jamasurgery |

The page is long and organized into collapsible topics. The article type table near the top gives the limits; the "Format My Manuscript" and "Requirements for Reporting" topics give the rules.

### 2. Article type limits

As listed for JAMA Network Open and JAMA Internal Medicine (Oct 2026):

| Article type | Main text | Abstract | Key Points | Tables + figures | References |
|---|---|---|---|---|---|
| Original Investigation | 3000 words | Structured, ≤350 words | Required, 75-100 words | ≤5 total | 50-75 (per study type entries) |
| Research Letter | 800 words | None | None | ≤2 small | ≤10 |
| Systematic Review (no meta-analysis) | 3000 words | Structured, ≤350 words | Required | ≤5 | 50-75 |
| Meta-analysis | 3000 words | Structured, ≤350 words | Required | ≤5 | 50-75 |
| Special Communication | 3000 words | Structured, ≤350 words | — | ≤4 | ≤50 |
| Narrative Review (specialty journals; presubmission inquiry) | 2000-3500 words | 3-part, ≤300 words | None | ≤5 | 50-75 |
| Consensus Statement (JAMA Network Open) | 3500 words | Structured, ≤350 words | — | ≤5 | 50-75 |

**What the main-text count excludes:** abstract, tables, figures, acknowledgments, references, and online-only (supplemental) material. The title page word count should also exclude the title, abstract, acknowledgment, references, tables, and figure legends. Key Points sit outside the main text too.

**Research Letter specifics:** sections Introduction, Methods, Results, Discussion; Supplement only for brief essential Methods, never extra results or discussion.

**Flagship JAMA** has its own article types and may differ (it has historically listed a different reference cap for Original Investigations). Always fetch the JAMA page when JAMA itself is the target.

### 3. Study types: subtitle and reporting guideline

A study type is required for research papers. Most specialty journals and JAMA Network Open list these:

| Study type | Subtitle required | Reporting guideline |
|---|---|---|
| Randomized clinical trial (incl. parallel, crossover, equivalence/noninferiority, cluster) | "A Randomized Clinical Trial" | CONSORT (2025); flow diagram counts toward display limit; protocol + SAP; trial registration |
| Nonrandomized clinical trial | "A Nonrandomized Clinical Trial" | TREND; trial flow diagram; protocol; registration |
| Meta-analysis | Include "A Meta-analysis" | PRISMA (trials) or MOOSE (observational) |
| Systematic review without meta-analysis | "A Systematic Review" | Relevant parts of PRISMA or MOOSE; PRISMA-style flow diagram in Supplement; evidence quality ratings table |
| Cohort, case-control, cross-sectional | None (do not put design in title) | STROBE |
| Case series | None | Case series reporting guideline linked from the journal page |
| Economic evaluation, decision analytical model | None | CHEERS |
| Comparative effectiveness research | None | ISPOR good research practices |
| Genetic association study | None | STREGA |
| Diagnostic/prognostic study | None | STARD or TRIPOD |
| Quality improvement study | None | SQUIRE |
| Survey study | None | AAPOR best practices; response rate generally ≥60% with nonresponder characterization |
| Qualitative / mixed methods | None | SRQR or COREQ |

Clinical trials: registry name, ID, and URL go at the end of the abstract. Secondary analyses of a trial cite the parent trial's registration rather than registering separately.

### 4. Title and title page

- Title ≤100 characters including spaces for research reports; subtitles ≤60 characters.
- Concise, specific, informative. **Not allowed:** overly general titles, declarative titles (stating the result), titles giving the direction of results, question titles.
- Trials and meta-analyses (and, for specialty journals, systematic reviews) put the study type in the subtitle. Other research types do **not** include study type or design in the title or subtitle.
- JAMA Internal Medicine adds: depending on context, avoid specific locations (state, country) and specific years in the title.
- No abbreviations in the title.
- **Title page** (first page): title; full names, highest academic degrees, and affiliations of all authors (with new affiliations if changed); corresponding author's name and full contact information; manuscript word count.

### 5. Key Points

Required for research and review manuscripts (not Research Letters). Placed as a separate section called "Key Points" **before** the abstract. 75-100 words total.

- **Question:** one sentence, focused question based on the hypothesis or purpose.
- **Findings:** 1-2 sentences. Name the design (eg, "In this cohort study of 12 450 adults..."). Primary outcome only; don't emphasize secondary outcomes. Basic numbers only. State whether results were statistically significant; **no** P values, CIs, or measures of variance.
- **Meaning:** one sentence, the key conclusion and implication from the primary finding.

Official research example pattern: "In this randomized clinical trial that included 980 adults, the proportion achieving an effective antibody response was 84% with adjuvant vs 2% without adjuvant, a significant difference."

### 6. Structured abstracts

No information in the abstract that isn't in the main text. No abbreviations. Phrases rather than full sentences are allowed. ≤350 words.

#### Reports of original data (Original Investigation)
Headings, in this order. **At submission, Design, Setting, and Participants are kept as separate headings** (editors combine them later).

1. **Importance:** 1-2 sentences on the clinical (or other) importance of the question.
2. **Objective:** the precise objective ("To determine whether..."); main objective first, only key secondary ones; state an a priori hypothesis if tested.
3. **Design:** basic design with the specific study type; years of the study and follow-up duration; date of analysis for studies completed >3 years ago; study name if any; blinding where relevant.
4. **Setting:** e.g., multicenter, population-based, primary care, referral center.
5. **Participants:** clinical disorders, key eligibility criteria, key sociodemographic features; number eligible, how selected, number who refused or were excluded; sampling terms (random, population-based, referred, consecutive, volunteer, convenience sample); matching characteristics; proportion completing follow-up.
6. **Intervention(s)** (trials) **or Exposure(s)** (observational): essential features, method, duration; nonproprietary names.
7. **Main Outcome(s) and Measure(s):** primary outcome as planned before data collection; say so if main planned outcomes aren't reported; say if the hypothesis was formed during or after data collection.
8. **Results:** **first sentence gives the number of participants and summary demographics (eg, sex and age).** Main outcomes quantified with final analyzed sample; absolute numbers or rates with uncertainty (CIs); absolute numbers alongside any ratio measures; mean (SD) for normal data, median (IQR or range) otherwise; P values only after the comparison and CI, never alone; ITT results for RCTs; withdrawals for adverse effects in intervention studies; response rates for surveys; sensitivity, specificity, likelihood ratios for diagnostic studies.
9. **Conclusions and Relevance:** only conclusions directly supported by results; equal emphasis on positive and negative findings; a relevance statement on implications for practice or policy, without speculation or overgeneralization.
10. **Trial Registration:** trials only. Registry name, ID, URL.

#### Meta-analysis
Importance; Objective; Data Sources; Study Selection; Data Extraction and Synthesis; Main Outcome(s) and Measure(s); Results; Conclusions and Relevance. ≤350 words.

#### Systematic review (no meta-analysis)
Importance; Objective; Evidence Review; Findings; Conclusions and Relevance. ≤350 words.

#### Narrative review / Special Communication (3-part)
Importance; Observations; Conclusions and Relevance. ≤300 words for Narrative Reviews; Special Communications use ≤350 on JAMA Network Open.

### 7. Main text structure

Original Investigation: Introduction, Methods, Results, Discussion (including Limitations), Conclusions. Each manuscript should clearly state:
- objective or hypothesis
- design and methods: study type, setting, dates, participants with inclusion/exclusion criteria and participation or response rates, data sources and how selected
- essential features of interventions or exposures
- main outcome measures
- main results
- discussion placing results in context of published literature, with study limitations
- conclusions and implications for practice or policy

Data should be as timely as possible (the "Timeliness of Data" policy). Older data needs a reason.

Manuscript file order: title page, Key Points, abstract, text, references, then figure legends and tables. Each starts on a new page; pages numbered from the title page. Word document only (not PDF). 10-, 11-, or 12-point font, double spaced, ragged right margin.

Systematic reviews have suggested section lengths: Introduction 150-250, Methods 150-250, Results 1000-1250, Discussion ~1000 words, Conclusions 2-3 sentences.

### 8. Tables and figures

Display-item limit counts tables and figures together (≤5 for Original Investigations, including the CONSORT diagram for trials).

General:
- Only what's needed to support the argument and to report all outcomes listed in Methods.
- Every table and figure numbered and cited in text in order; brief descriptive title (10-15 words).
- Data consistent across text, tables, figures, supplement.
- Primary outcomes must have exact values with uncertainty in text or a table **and** in the abstract, not only in a figure.
- Don't duplicate data between figures and tables.

Tables: see **Table formatting (JAMA Network)** below for the full checklist, and run the table checker on every .docx.

Figures:
- No pie charts, 3-D graphs, or stacked bars (except ordinal distributions).
- Bars only for frequency data; point estimates with error bars (both directions) for summary data.
- Ratio measures (OR, HR, RR) plotted on a log scale with actual (not log-transformed) values.
- Survival plots as step functions with numbers at risk below the x-axis.
- Axes labeled with units; all symbols defined; ≤4 panels unless justified; footnotes with letters.
- Figures with labels/arrows need a second unlabeled version.
- AI-created or AI-manipulated clinical images are not permitted unless part of the research methods.

### 8a. Table formatting (JAMA Network)

From the JAMA Network Instructions for Authors (Tables, Table Creation, Table Footnotes), checked October 2026. Run the **table checker** (end of this file) with `--style ama` on every .docx; it flags most of these automatically.

**Construction**
- Build tables with Word's table menu (Insert → Table, or paste from Word or Excel). Never set up columns with tabs, spaces, or hard returns; such tables have to be retyped.
- Each piece of data in its own cell, one row of data per row of cells. No values stacked in one cell with line breaks.
- Single spaced, 10- or 12-point font; don't shrink the font to fit. Minimum 2 columns.
- Don't draw extra lines or rules; the grid shows cell outlines. No vertical rules, shading, or colored text in the submitted file (JAMA re-creates tables in house style).
- **Alignment, including decimal alignment, is imposed in production.** Don't try to align numbers on the decimal point with tabs or spaces; just put each value in its own cell. To show an indent (subcategories under a variable), add 2 spaces.
- Avoid empty cells: use NA (not applicable or not available) and define it in a footnote. For a value that spans several rows (e.g., an overall P value for a categorical variable), merge the cells vertically.
- The primary comparison reads horizontally, across columns (e.g., groups as columns, characteristics as rows).
- Tables go at the end of the manuscript file, each numbered and cited in order. Not as images, not as separate uploads.
- A table that runs onto a second page repeats its title and column headings, followed by "(continued)".

**Content and numbers**
- Title: "Table 1. Descriptive phrase", preferably 10-15 words. Don't put data sources or years in parentheses in the title; use a footnote.
- Frequencies as No. (%) in the same cell: 1385 (56.6). Include numerators and denominators with percentages. Percentages alone only for samples above about 10 000.
- **No decimal places in percentages when the sample size is less than 100** (xx%, not xx.x%). Apply this per group: a column for a group of 72 gets whole-number percentages.
- Variability in the same cell: mean (SD), median (IQR). Not ± (AMA style is mean (SD)).
- Use a consistent number of decimal places for comparable values in a column (e.g., all ages to 1 decimal; all means and SDs of the same scale to the same precision). Report no more precision than the measurement supports.
- P values (AMA Manual of Style): no leading zero; 2 digits in general, 3 when P < .01; smallest <.001, largest >.99. Never .000.
- Use a true minus sign (−) for negative values; give ranges or CIs with negative limits using "to" (−0.4 to −0.2).
- Numbers: no comma in 4-digit numbers (2449); thin space for 5+ digits (12 450).
- Laboratory values in conventional units; give the SI conversion factor in a footnote.
- Regression tables: focus on the primary results and give unadjusted and adjusted estimates for the primary exposure; put full models in an eTable.
- Units in column or row headings, not repeated in every cell.

**Footnotes**
- Superscript lowercase letters (a, b, c), ordered by where the item appears in the table (left to right, top to bottom). Every letter has a note and every note has a letter.
- When a reference number and a footnote letter follow the same entry, the reference number comes first, then a comma, then the letter.
- List abbreviations in the footnotes and explain empty or NA cells.
- Explain when numbers don't sum to group totals or percentages don't add to 100% (e.g., missing data, rounding).
- Name the statistical tests used for the P values in a footnote. JAMA tables generally report exact P values rather than significance asterisks.

### 9. References

- AMA style, numbered in order of first citation (not alphabetical), superscript arabic numerals in text, tables, and legends.
- List all authors up to 6; if more than 6, list the first 3 followed by "et al".
- Journal abbreviations per PubMed. Include the issue number in parentheses after the volume.
- Example: `Youngster I, Russell GH, Pindar C, Ziv-Baran T, Sauk J, Hohmann EL. Oral, capsulized, frozen fecal microbiota transplantation for relapsing Clostridium difficile infection. JAMA. 2014;312(17):1772-1778.`
- **AI tools should not be used to generate or format references**; use a reference manager. (So this skill only checks references.)
- Personal communications and unpublished data have their own rules on the journal page.

### 10. Supplement

- One Word document, pages numbered, first page lists each element with number and title.
- Elements named and numbered in order of citation: eTable 1, eFigure 1, eMethods, eAppendix, etc. Cited in the main text as, e.g., "eTable 2 in Supplement 1".
- Not edited by the journal; must not repeat main-article material; amount should be limited and justified.
- Supplemental text: Times New Roman, 10 point, single spaced.
- Trial protocols and statistical analysis plans go in as a separate supplement.

### 11. Style rules that come up most

See the AMA style checklist for the fuller list. Highlights from the Instructions for Authors:
- No abbreviations in title or abstract; limit them in text; expand at first mention.
- Conventional units for lab values, with SI conversion in parentheses at first mention (or a conversion paragraph at the end of Methods).
- Nonproprietary drug and device names; trade name once only if essential; no ™/® symbols.
- Gene names and symbols per HGNC / NCBI.

### 12. Other required items

- **Data Sharing Statement** for research papers (questions also asked in the submission system).
- **Conflict of interest disclosures** and **Funding/Support** with **Role of the Funder/Sponsor**.
- **Data access statement**: who had full access to the data and takes responsibility for integrity and analysis.
- **Author contributions** per ICMJE criteria.
- **Ethics approval and informed consent** statement (or waiver with reason) in Methods.
- **Reporting of race and ethnicity**: who classified it, the categories, and why it was assessed (see the journal's "Reporting Demographic Information" section).
- **Cover letter:** JAMA Internal Medicine and most specialty journals ask for one; JAMA Network Open recommends one. Contents: corresponding author's full contact information and whether related papers from the same study have been published, posted (preprints), or submitted.
- **Previous reviews:** if the paper was reviewed at another journal, authors are encouraged to upload those comments with their responses.

### 13. AI policy

- Authors must review and take responsibility for all AI-generated content.
- Use of AI in manuscript preparation must be disclosed per the journal's "Use of AI in Publication and Research" section (typically name, version, manufacturer, and what it was used for).
- AI-generated content in the paper itself is discouraged unless part of the research methods.
- Opinion pieces, Letters to the Editor, and some narrative article types prohibit AI drafting altogether at some journals (e.g., JAMA Internal Medicine Viewpoints, Inside Story, Letters). Check before using this skill on those.

## AMA style checklist (AMA Manual of Style, 11th ed)

The items JAMA copy editors and reviewers flag most often. Use for features 5 (style check), 7 (causal language), and 13 (references). When a rule here conflicts with the target journal's live Instructions for Authors, the journal page wins.

### Numbers
- Arabic numerals for all numbers, including 1-9, except at the start of a sentence (spell out or recast), in common expressions ("one of the most"), and ordinals "first" through "ninth".
- Numbers with 5+ digits use a thin space as the thousands separator: 12 450, 1 204 377. Four-digit numbers have no separator: 4500. (In a Word draft a regular space is fine; flag commas.)
- Ranges: repeat the % sign or unit on both numbers ("10% to 20%", not "10-20%"). Use "to" in text when either number is negative. Mixed range styles across the paper are worth flagging.
- Percentages: no space before %; no decimals when the denominator is under 100; give numerators and denominators where possible: 45 of 120 (37.5%).
- Use "No. (%)" formatting in tables.

### Statistics
- P values: italic capital *P*, no leading zero, spaces around the operator: *P* = .04, *P* < .001. Smallest reported is *P* < .001; never *P* = .000 or *P* = 0.0001. Two digits generally; three digits when between .001 and .01 (*P* = .004). Flag *P* = .05 interpretation issues and "trend toward significance" for nonsignificant results.
- P values never stand alone: give the effect estimate and CI first.
- Confidence intervals: "OR, 1.45; 95% CI, 1.12-1.88" format. Use "to" instead of a hyphen when either limit is negative: "−0.2 to 1.8".
- Mean (SD), not mean ± SD. Median (IQR), with IQR given as a range: 54 (45-63).
- "Statistically significant" only for formal tests; don't use "significant" loosely to mean "important".
- Report absolute measures alongside relative ones (rates or absolute risk differences with ORs/HRs).
- Name the statistical software and version in Methods, and the significance threshold and whether tests were 2-sided.

### Abbreviations
- None in the title, Key Points, or abstract. (Very common units like mg and standard statistical abbreviations such as CI, OR, HR are accepted in JAMA abstracts in practice, but study-specific abbreviations are not. Flag anything coined by the authors.)
- Expand at first use in the text; after that use consistently. If a term is used fewer than ~3 times, spell it out every time.
- "eg," and "ie," (no periods, followed by comma); "vs" (no period); "et al" (no period).

### Terminology and inclusive language
- Person-first language: "patients with diabetes", not "diabetics"; "people with obesity" rather than "obese people".
- Age: "older adults" or "persons aged 65 years or older", not "the elderly", "seniors", or "aged". Give ages in years ("aged 70 years").
- Sex vs gender: sex for biological attributes, gender for identity/social roles; say how each was determined. "Women/men" for gender; "female/male" as adjectives for sex.
- Race and ethnicity: capitalize Black and White; avoid "Caucasian" and the collective "minorities" without specifying groups; avoid "non-White" as a single category where possible; list "other" categories explicitly if they make up a substantial share. Methods should say who classified race and ethnicity, the categories used, and why they were assessed.
- "Participants" or "patients" rather than "subjects".
- "Data" is plural ("data were").
- Prefer "outcome" over "endpoint" in text unless describing a trial's prespecified end point.
- Use "sex" not "gender" for animals and biological variables.

### Causal language (feature 7)
JAMA Network journals have a "Use of Causal Language" policy: causal terms are reserved for designs that support causal inference (generally randomized trials, or observational studies explicitly using causal inference methods with stated assumptions). For observational designs, flag:
- Verbs: "caused", "led to", "resulted in", "reduced", "increased", "improved", "prevented", "protects", "drives", "determines".
- Nouns: "effect", "impact", "influence", "benefit", "harm" when describing an association.
- Phrases: "risk factor for" can be fine; "contributes to" is borderline; "the effect of X on Y" is causal.

Suggested replacements: "was associated with", "was linked with", "the association between X and Y", "was associated with higher/lower...". Also flag overreach in Conclusions and Relevance and in Key Points Meaning: recommendations for practice from a single cross-sectional study, or generalization beyond the sample.

Don't swap words mechanically if the authors used a formal causal design (target trial emulation, instrumental variables, regression discontinuity, difference-in-differences). In that case check that the assumptions are stated and the language matches the design.

### Units and drugs
- Conventional units for lab values with SI in parentheses at first mention (or a conversion paragraph at end of Methods); in tables, a conversion factor in the footnote.
- Time units: spell out in text (hours, days); abbreviations in tables are OK (h, d, wk, mo, y).
- Nonproprietary drug names; no ™ or ®.

### Titles and headings
- Title case for titles and headings (AMA capitalizes major words, including prepositions of 4+ letters).
- Title ≤100 characters with spaces; no declarative or question titles; no study design in title except trial/meta-analysis/systematic review subtitles; no abbreviations.

### References (feature 13 — check only)
Check, don't rewrite:
- Cited in numerical order of first appearance; every number in text appears in the list and vice versa; no gaps or duplicates.
- Superscript numerals, placed outside periods and commas, inside colons and semicolons. Ranges with hyphen: ^1-3^; series with commas, no spaces: ^1,4,7^.
- Up to 6 authors listed; 7 or more → first 3 + "et al".
- Journal names abbreviated per PubMed (NLM catalog), italicized, no periods in abbreviations ("JAMA Netw Open").
- Format: Author AA, Author BB. Title in sentence case. *Journal*. Year;Vol(Issue):pages. doi:xx
- Page ranges in full (1772-1778, not 1772-8).
- Online references need an accessed date and URL.
- Flag preprints, references older than ~10 years for key background claims, and self-citation heavy lists as optional notes, not errors.
- Count against the article type's reference limit.

## Feature playbook

How to carry out each menu item. Read only the entries for the features the author chose. All of them assume you have read the full manuscript, confirmed journal / article type / study type, and checked the current limits (see Step 3 and the JAMA Network format reference).

### Contents
Preparing: 1 Requirements · 2 Abstract · 3 Key Points · 4 Section check
Polishing: 5 AMA style · 6 Consistency · 7 Causal language · 8 Clarity edit
Limits: 9 Dashboard · 10 Trim · 11 Move to Supplement
Submitting: 12 Reporting guideline · 13 References · 14 Title page and declarations · 15 Cover letter · 16 Mock review
Revising: 17 Response to reviewers · 18 Retarget

---

### 1. Journal-specific requirements
Fetch the live Instructions for Authors page for the target journal (URL pattern in the JAMA Network format reference). Produce a compact card for this manuscript, not a copy of the page:
- Article type and study type, and the required subtitle (if any)
- Limits: main text, abstract, Key Points, tables + figures, references, title characters
- Required elements: abstract headings to use, reporting guideline and checklist, trial registration, protocol/SAP, data sharing statement, other declarations
- Anything specific to this journal that differs from the JAMA Network format reference (call it out)
- Date checked and URL

### 2. Structured abstract
1. Pick the heading set for the study type (the JAMA Network format reference section 6). Keep Design, Setting, and Participants as separate headings at submission.
2. Pull every fact from the manuscript text and tables. The abstract can contain nothing that isn't in the main text.
3. Results: first sentence gives N and summary demographics (age with mean (SD) or median (IQR), sex as No. (%)). Then the primary outcome with absolute numbers/rates and the effect estimate with 95% CI; then key secondary results only if space allows. P values only after CIs, if at all.
4. Conclusions and Relevance: what the primary result supports, plus one relevance statement. Match the strength of language to the design (feature 7 rules). No new claims.
5. No abbreviations. Spell out everything except standard statistical terms (CI, OR, HR).
6. Count words (≤350 unless the journal says otherwise). If over, cut from Importance, Setting, and secondary results first; never cut the N, primary estimate, or CI.
7. If the author already has an abstract, revise it rather than starting over, preserving their phrasing where it already meets the rules, and give a short change log.

Output: the abstract with bold headings, its word count, placeholders list.

### 3. Key Points
- Question: one sentence, a real question, mirroring the Objective.
- Findings: "In this [study type] of/including [N] [population], ..." then the primary result with basic numbers, and whether it was statistically significant. No P values, CIs, or SDs. 1-2 sentences.
- Meaning: one sentence, the implication of the primary finding, worded no more strongly than the abstract's Conclusions and Relevance.
- 75-100 words total; count and report it.
- Offer 2 variants of Meaning when the right strength of claim is a judgment call (e.g., one more cautious, one more practice-oriented), and say which matches the abstract.

### 4. Section order and completeness
Check against the JAMA Network format reference sections 4-8a (run the table checker for section 8a):
- Order: title page → Key Points → abstract → Introduction → Methods → Results → Discussion (with Limitations) → Conclusions → Acknowledgments/declarations → References → figure legends → tables.
- Methods contents: study type and setting, dates, participants and eligibility, data sources, exposures/interventions, outcomes, covariates, statistical analysis (software, version, 2-sided tests, α), ethics/consent statement, reporting guideline named.
- Results open with the participant flow and characteristics.
- Discussion has a Limitations section; Conclusions short.
- Each table and figure cited in order.
Report what's missing or out of order, by section.

### 5. AMA Manual of Style check
Run the table checker (`--style ama`) and fold its findings into the report. Then go through the AMA style checklist and section 8a (table formatting) against the manuscript. Report issues as a table: Location | Text (short quote) | Issue | Suggested fix. Group repeated issues ("P values written with leading zeros: 14 instances, e.g., ...") instead of listing each one. Don't flag things that are fine; a short list of real issues beats a long noisy one.

### 6. Consistency check
Build a small fact table from the manuscript: N (screened, eligible, enrolled, analyzed), demographics, primary and key secondary estimates with CIs, follow-up duration, study dates. Then find every place each fact appears (Key Points, abstract, Results text, tables, figure legends, Discussion) and flag mismatches, rounding inconsistencies, percentages that don't match numerator/denominator (recompute them), and Ns that don't add up through the flow. Also check that every outcome listed in Methods is reported in Results, and that the primary outcome is the same everywhere.
Output: list of mismatches with each location and value, plus "verified consistent" for key facts that checked out.

### 7. Causal language
Use the AMA style checklist "Causal language". Scan title, Key Points, abstract, Introduction (aims), Results, Discussion, and Conclusions. For each hit, give location, quote, and a replacement that keeps the author's sentence structure. Pay most attention to Key Points Meaning and Conclusions and Relevance, where overreach is most visible to editors. If the design supports causal claims, say so and check the assumptions are stated instead.

### 8. Clarity edit in the author's voice
1. Build a short voice profile from the manuscript (and from an earlier paper if provided): typical sentence length, hedging words, transitions they use, first-person use, recurring phrasings, US vs UK spelling. Show it to the author in 3-5 bullets so they can correct it.
2. Edit for clarity only: fix ambiguity, dangling modifiers, buried subjects, long noun stacks, unclear antecedents, unnecessary passive voice where it hides the actor, and grammar. Don't swap the author's vocabulary for synonyms. Don't add flourish.
3. Output the edited section and a change log (original → revised → reason). For a full .docx, offer tracked changes.

### 9. Word count and limits dashboard
Run the word counter with the journal's limits. Present a table: Item | Count | Limit | Status (✓ / over by N / under). Items: main text, abstract, Key Points, title characters, subtitle characters, tables + figures, references, and per-section main-text counts (Introduction, Methods, Results, Discussion, Conclusions). Add a line suggesting where cuts would hurt least, based on section proportions (e.g., Introduction >15% of text or Discussion >35% is usually where to look).

### 10. Trim to fit
1. Get the target: the overage from the dashboard, or a number the author gives. Ask whether any sections are off-limits.
2. Cut in this order, stopping when the target is met:
   - Redundancy: repeated statements of the aim, results repeated from tables in full, Discussion restating Results.
   - Wordy phrases: "in order to" → "to", "it is important to note that" → delete, "a total of", "was found to be", "due to the fact that", "in the present study".
   - Excess background in the Introduction (keep: what's known, the gap, the aim).
   - Methods details that belong in the Supplement (see feature 11): full covariate definitions, variable coding, sensitivity-analysis specifications.
   - Discussion paragraphs comparing with many individual studies → one sentence summarizing the literature with grouped citations.
3. Keep the author's voice: delete before rewriting; when combining sentences, use the author's own phrasing from those sentences.
4. Never cut: the primary result, CIs, limitations that reviewers would expect, ethics statements, required reporting items.
5. Output: the revised section(s), new word counts per section, and a change log grouped by type with words saved. Offer tracked changes in .docx for the full manuscript.

### 11. Move-to-Supplement suggestions
List candidates with what each would save (words or display items): detailed Methods (variable definitions, imputation, sensitivity-analysis specs) → eMethods; secondary tables and stratified results → eTables; extra figures → eFigures; full covariate lists → eTable. Suggest which of the main tables/figures to merge or move if over the display limit, keeping the primary outcome in the main paper. Give the in-text citation wording to use (e.g., "eTable 2 in Supplement 1"). Remind the author the Supplement must not repeat main-text content.

### 12. Reporting guideline checklist mapping
Pick the guideline from the study type (the JAMA Network format reference section 3). Use the current official checklist items (fetch from equator-network.org or the guideline's own site if you don't have them reliably; STROBE has 22 items; CONSORT 2025 is the current CONSORT version). For each item: Item | Reported? (Yes / Partly / No) | Location (section, page or paragraph) | What's missing. Output a table the author can copy into the journal's checklist file, plus a short list of the "No" and "Partly" items to fix first.

### 13. Reference check
Check only (JAMA Network says not to use AI to generate or format references). Use the AMA style checklist "References":
- Every in-text citation number appears in the list and vice versa; numbered in order of first citation; no duplicates.
- Author lists (6 or fewer full; 7+ → 3 + et al), journal abbreviations, issue numbers, page ranges, DOIs, accessed dates for websites.
- Count against the article type limit.
Report problems by reference number. Don't produce a reformatted list.

### 14. Title page and declarations
Check: title (≤100 characters, not declarative or a question, no abbreviations, study type subtitle only for trials/meta-analyses/systematic reviews); author names with highest degrees and affiliations; corresponding author contact block; word count on title page; Key Points present (if required). Declarations: conflict of interest disclosures, funding and role of funder, data access and responsibility statement, author contributions, data sharing statement, ethics approval and consent (in Methods), trial registration (trials), AI use disclosure, acknowledgments of nonauthor contributors with permission. List what's missing; for the title, offer 2-3 alternatives within the limit that keep the author's key terms.

### 15. Cover letter draft
Ask (or infer) the corresponding author's details, and whether there are related publications, preprints, or prior submissions of this work. Draft a one-page letter in the author's register:
- Title, article type, journal.
- 2-3 sentences on the question, the design and sample, and the main finding (with the primary estimate).
- 1-2 sentences on why it fits this journal's readership and scope (from the journal's "About" or scope statement, fetched if possible).
- Required statements: not under consideration elsewhere; related papers/preprints disclosed; all authors approved; conflicts disclosed; reporting guideline followed; data sharing.
- Optional: suggested or excluded reviewers, if the author provides them.
Use placeholders for anything not supplied.

### 16. Pre-submission mock review
Read the manuscript as a JAMA Network reviewer and statistical reviewer would. If the topic is aging, life course, cognitive health, or place and health, and the gerontology-paper-review skill is available, load it and follow it. Otherwise produce:
- Summary of the study in 3-4 sentences.
- Editor's view: is it a fit for this journal; is the question important for a general medical readership; what would make an editor desk-reject.
- Major comments (design, confounding, selection, measurement, missing data, analysis choices, overinterpretation, generalizability).
- Minor comments.
- Statistical review points (model specification, multiple comparisons, sensitivity analyses, reporting of effect sizes).
- Top 3 things to fix before submission.
Be direct and specific; reference sections and tables.

### 17. Response-to-reviewers table
Inputs: decision letter with editor and reviewer comments; the revised manuscript or a description of the changes made.
1. Split comments into individual numbered points (Editor 1.1, Reviewer 1.1, 1.2, ...). Quote each comment in full; don't paraphrase it.
2. For each, draft a response in the author's voice: thank briefly once per reviewer (not every point), answer directly, describe the change and where it is (section, page/line). If the author disagrees, write a respectful, evidence-based rebuttal and mark it [AUTHOR TO CONFIRM].
3. Where the author hasn't said what they changed, write [DESCRIBE CHANGE] rather than inventing one; list these at the end.
4. Output as a table (Comment | Response | Change and location) or as the alternating comment/response letter format, whichever the author prefers. Also draft the short cover note to the editor.
5. Re-run the dashboard (feature 9) on the revised manuscript, since revisions often push the paper over the limit.

### 18. Retarget to another JAMA Network journal
Inputs: the new target journal and, if available, the rejection letter.
1. Fetch the new journal's requirements (feature 1) and list every difference from the previous journal: limits, article types, abstract style, scope.
2. If there was a review, separate comments worth addressing before resubmission from ones specific to the first journal.
3. Apply format changes (abstract headings, Key Points, word and display limits via feature 10/11, title/subtitle rules).
4. Reframe the Introduction's first paragraph and the relevance statement for the new journal's readership, keeping the author's wording where possible.
5. Draft a new cover letter (feature 15). If the prior reviews were constructive, suggest including them with responses, which JAMA Network journals encourage.

## Word counter

Write this to the scratchpad as `jama_count.py` before running it.

```python
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
```

## Table checker

Write this to the scratchpad as `table_check.py` before running it. Use `--style ama` for JAMA Network journals.

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
