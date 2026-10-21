---
name: sociology-manuscript-prep
description: Prepare, polish, check, and revise manuscripts for major sociology and demography journals (American Sociological Review, American Journal of Sociology, Social Forces, Socius, European Sociological Review, British Journal of Sociology, Journal of Health and Social Behavior, Social Science & Medicine, SSM - Population Health, SSM - Mental Health, Sociology of Health & Illness, Demography, Population and Development Review, Population Research and Policy Review, Advances in Life Course Research, Social Science Research, Research in Social Stratification and Mobility, Sociological Methodology, Sociological Methods & Research, Sociology of Race and Ethnicity). Use for abstracts, highlights, keywords, word limits and trims, ASA/Chicago/APA/Harvard style, table and layout checks, table formatting, anonymization, data statements, cover letters, mock reviews, and reviewer responses, even if the user just says "get this ready for ASR" or "submit to Demography".
---

# Sociology Journals Manuscript Prep

A toolkit for getting a manuscript ready for a sociology or demography journal, and for the revision stage. The user is the author: their science and their voice come first. This skill formats, checks, condenses, and drafts, and it shows every change so the author stays in control.

## Step 1: Gather the inputs

Every run needs the manuscript (.docx, .pdf, or pasted text). Read it in full first. If it is a .docx, read it with tracked changes accepted (`pandoc file.docx -t plain --track-changes=accept --wrap=none`), since co-author edits are often still tracked.

Confirm, inferring what you can and asking only about what is missing:
1. **Journal** (see the journal reference below). For the SSM family, which journal: *Social Science & Medicine* (and which of its seven editorial offices), *SSM - Population Health*, or *SSM - Mental Health*.
2. **Article type**, e.g., article, research note, brief report, comment, data visualization (Socius), review. (Annual Review of Sociology is invitation-only and not covered.)
3. **Design**: quantitative, qualitative, mixed methods, computational, review. It changes the reporting expectations and data-sharing rules (several journals exempt interview and ethnographic data).
4. **Stage**: first submission (several journals accept "format-free" first submissions: Social Forces, ESR) or final/accepted version (journal style required).

Stage-specific inputs only when needed: reviewer comments (19), rejection letter and new target (20), author surnames (16, anonymization), an earlier paper by the author for voice matching (9, 11).

## Step 2: Show the menu

Present this menu so the author picks only what they need. Accept numbers, ranges, a stage name, or "everything". If the opening message already says what they want, skip the menu and do it.

**Preparing**
1. Journal requirements card for the chosen journal and article type
2. Abstract within the journal's limit and conventions
3. Journal-specific extras: Highlights (Demography; required at SSM, SSM-MH, and RSSM, encouraged at SSM-PH, ALCR, and SSR), the SSM editorial office, Relevance to Demography statement, Data Availability / replication statement (ESR, Social Forces, SMR, PRPR, AJS data-openness statement), running head (JHSB)
4. Keywords (count and rules per journal)
5. Section order and completeness check

**Polishing**
6. Style check: ASA 7, Chicago author-date, APA 7 variant, or Harvard, per journal
6b. Page layout and heading check (font, spacing, margins, page and line numbers, page breaks, notes, headings, leftover tracked changes and comments)
6c. Format my tables: edit a copy of the file so its tables follow the journal's style, with text fixes as tracked changes (optional decimal alignment)
7. Consistency check: numbers across abstract, text, and tables
8. Causal language check
9. Clarity edit in the author's voice

**Fitting the limits**
10. Word count and limits dashboard (each journal's own counting rule)
11. Trim to fit, with every cut tracked
12. Move-to-supplement suggestions

**Submitting**
13. Reporting standards check (sample, measures, missing data, models, robustness; EQUATOR guideline where relevant, e.g., STROBE, CONSORT, PRISMA, SRQR/COREQ)
14. Reference check (check only)
15. Title page and required statements (funding, conflicts, ethics, data availability, author contributions, AI disclosure)
16. Anonymization check for the blinded file
17. Cover letter draft
18. Pre-submission mock review

**Revising**
19. Response-to-reviewers memo
20. Retarget to another journal in this list (or to a JAMA Network or GSA journal)

Run multiple features in this order: requirements (1) and counts (10) first, then checks (5-8, 6b, 13-16), table formatting (6c) only when the author asks, then writing and edits (2-4, 9, 11, 12), then 17-18.

## Step 3: Get the current requirements

The journal notes below were compiled in October 2026. Each entry is marked **[verified]** (read from the journal's own author page that month) or **[confirm]** (the official page could not be read; details come from secondary sources or are missing). Before applying a number, fetch the live author page (URLs below). If it differs, the live page wins; tell the author. For [confirm] journals, always tell the author which details still need checking, and never present them as certain.

Tools (write each from the end of this file to the scratchpad before running; they need `lxml`, `pip install lxml --break-system-packages` if missing):

- **Word counter** `soc_count.py`. Journals differ in what counts, so pass the parts with `--count`:
  ```bash
  python soc_count.py manuscript.docx --count text,notes,refs --text-limit 15000 --abstract-limit 200 --kw-min 4 --kw-max 5 --note-max 100 --authors "Surname1;Surname2"
  ```
  Parts: `text`, `abstract`, `notes` (a NOTES section plus Word footnotes/endnotes), `refs`, `appendix`, `tables`. The journal table gives each journal's `--count`. It reads tracked changes as accepted and treats long paragraphs before the first section as the introduction when there is no Introduction heading (JHSB and many sociology papers have none).
- **Table checker** `table_check.py --style asa` for ASA journals and most sociology journals; `--style apa` for Demography, PRPR, SSM-PH, ALCR, RSSM, SSR, and the SSM journals; add `--decimal-align` for JHSB and SRE.
- **Layout checker** `layout_check.py --journal <code>` (codes in the journal table; add `--blinded` for the anonymized file).
- **Table formatter** `table_format.py --style asa|apa -o <name>_tables.docx [--decimal-align]`, only when the author asks (feature 6c).

## Journal reference

### Author page URLs and codes
| Journal | Code | Author instructions | Status |
|---|---|---|---|
| American Sociological Review | asr | https://journals.sagepub.com/author-instructions/ASR | verified |
| American Journal of Sociology | ajs | https://www.journals.uchicago.edu/journals/ajs/instruct and https://ajs.uchicago.edu/for-authors/further-guides-for-submission/ | verified |
| Social Forces | sf | https://academic.oup.com/sf/pages/author-guidelines | verified |
| Socius | socius | https://journals.sagepub.com/author-instructions/SRD | verified |
| European Sociological Review | esr | https://academic.oup.com/esr/pages/General_Instructions | verified |
| British Journal of Sociology | bjs | https://lse.ac.uk/sociology/british-journal-of-sociology/notes-to-contributors (Wiley page also) | verified (LSE page) |
| Journal of Health and Social Behavior | jhsb | https://journals.sagepub.com/author-instructions/HSB | verified |
| Social Science & Medicine; SSM - Population Health; SSM - Mental Health | ssm | https://www.sciencedirect.com/journal/social-science-and-medicine/publish/guide-for-authors (and /ssm-population-health/, /ssm-mental-health/) | verified |
| Sociology of Health & Illness | shi | https://onlinelibrary.wiley.com/page/journal/14679566/homepage/forauthors.html | verified |
| Demography | demography | https://www.populationassociation.org/demography/for-authors/preparing-manuscripts and /editorial-policy | verified |
| Population and Development Review | pdr | https://onlinelibrary.wiley.com/page/journal/17284457/homepage/forauthors.html | verified |
| Population Research and Policy Review | prpr | https://sda-demography.org/PRPR-journal/Preparing-Manuscripts and /Article-Types | verified |
| Advances in Life Course Research | alcr | https://www.sciencedirect.com/journal/advances-in-life-course-research/publish/guide-for-authors | verified |
| Social Science Research | ssr | https://www.sciencedirect.com/journal/social-science-research/publish/guide-for-authors | verified |
| Research in Social Stratification and Mobility | rssm | https://www.sciencedirect.com/journal/research-in-social-stratification-and-mobility/publish/guide-for-authors | verified |
| Sociological Methodology | smx | https://www.sagepub.com/docs/default-source/msg/SMX | verified |
| Sociological Methods & Research | smr | https://www.sagepub.com/docs/default-source/msg/SMR | verified |
| Sociology of Race and Ethnicity | sre | https://journals.sagepub.com/author-instructions/sre (plus the SRE Manuscript Preparation Guidelines PDF linked there) | verified |

Elsevier and Wiley author pages may block automated reading. If they can't be fetched, say so and ask the author to open the page or paste the relevant section; don't route around the block.

### Main article at a glance
| Journal | Length limit and what counts | `--count` | Abstract | Keywords | Reference style | Review |
|---|---|---|---|---|---|---|
| ASR [verified] | 15,000 words: text, notes, references (not tables/figures) | text,notes,refs | 150-200 words | 4-5, on title page | ASA 7 | anonymous; $25 fee (ASA student members exempt) |
| AJS [verified] | No limit; referees may need more time over 18,000; give the word count (text, notes, references) in the cover letter | text,notes,refs | ~150 words | not stated | AJS author-date (Chicago-based) | double-blind; $30 fee (sole-author grad students exempt) |
| Social Forces [verified] | 10,000 words: text, endnotes, references; ≤10 tables and figure panels | text,notes,refs | no limit stated; no references | not stated | Chicago 17 author-date (any readable style at first submission) | double-anonymized; $50 fee ($20 student-only) |
| Socius [verified] | 10,000 words of main text at first submission; title ≤20 words; data visualizations: 1 figure + ~500 words | text | ≤200 words | yes (number not stated) | ASA 7 | double-blind; $25 fee; APC on acceptance ($1,000 ASA member / $2,000 non-member; student rates) |
| ESR [verified] | ~8,000 words including endnotes and references, excluding tables and figures | text,notes,refs | ≤200 words | required | author-year, year in parentheses: (Gans, 1962) | double-blind |
| BJS [verified, LSE page] | ~8,000 words including abstract, notes, bibliography, appendices; research notes ≤2,500; review essays 5,000-5,500 | abstract,text,notes,refs,appendix | ≤300 words | 6 | Harvard: Smith, A.J. 1992 *Title*, London: Routledge. | double-blind |
| JHSB [verified] | 10,000 words: all text, notes, references (title page gives the count excluding tables and figures); commentaries 3,000 | text,notes,refs | <150 words, must state sample size, design, data source | not stated | ASA 7 | anonymous; $25 fee (ASA student members exempt) |
| Social Science & Medicine [verified] | Research articles and critical reviews ≤9,000 words including abstract, tables, figures, references, and printed appendices (shorter preferred); systematic and scoping reviews ≤15,000; commentaries invited | abstract,text,tables,refs,appendix | ≤250 words, concise and factual (no required headings) | 1-7 | Elsevier name-date: (Allan and Jones, 2019); list "Van der Geer, J., Handgraaf, T., 2020. Title. J. Abbrev. 163, 51–59." | double-anonymized; 3-5 Highlights ≤85 characters required |
| SSM - Population Health [verified] | Research articles ≤9,000 words including abstract, tables, figures, references; reviews ≤12,000 | abstract,text,tables,refs | ≤250 words | 1-7 | APA 7 | double-anonymized; Highlights and graphical abstract encouraged; open access (APC) |
| SSM - Mental Health [verified] | Full-length articles ≤9,000 words including abstract, tables, figures, references; reviews ≤15,000; short communications 2,000-4,000; Practitioner's Corner ≤2,500 (invited); letters 400-750 without references | abstract,text,tables,refs | ≤250 words | 1-7 | Elsevier name-date (as SSM) | **single-anonymized**; Highlights required; open access (APC) |
| Sociology of Health & Illness [verified] | Original articles ≤9,000 words including tables, figures, notes, and bibliography (each half-page table or figure counts as 250 words); review articles ≤8,000 excluding notes and bibliography; commentaries ≤2,500 (invited); book reviews ~800 | text,notes,refs (+250 per half-page table/figure) | 100-200 words, with its word count | not stated | Harvard: (Light 1998); list "Nettleton, S. and Burrows, R. (2003) Title, *Journal*, 23, 2, 165-185" | double-blind; self-citations as "Anon" |
| Demography [verified] | Research articles 8,000 words of main text (excludes abstract, keywords, footnotes, acknowledgments); ≤8 tables + figures; ~75 references; online appendix up to 15 more tables/figures and 2,500 words. Research notes 4,000 / 4 / ~15. Commentaries 2,000 / 4 / ~15 | text | ≤200 words; plus 3-5 Highlights ≤85 characters each | ≤5 | APA-based with journal rules | external review; $50 submission fee (sole students exempt); $1,000 editorial fee on acceptance (waivers possible) |
| PDR [verified] | Research articles typically 8,000-10,000 words; Notes and Commentary and Data and Perspectives take shorter papers; long book reviews 1,500-2,000 (invited) | text,notes,refs | required (length not stated) | not stated | any consistent style at first submission (free format) | double-anonymized |
| PRPR [verified] | Research articles 8,000-10,000 words of main text (excludes title, abstract, keywords, references, tables, figures, supplements); Brief Reports ≤3,500 and ≤5 tables/figures; Research Reviews ≤6,000 with exactly 3 tables/figures; Comments ≤3,000 (invited) | text | 150-250 words, one paragraph | 4-6 | APA 7 with PRPR rules | blinded title page in file |
| Advances in Life Course Research [verified] | no length limit stated | text | ≤250 words | 1-7 | APA 7 | double-anonymized; Highlights encouraged |
| Social Science Research [verified] | no word limit (editors may ask for cuts); quantitative research articles only | text | ≤250 words | 1-7 | **numbered** [1], in order of appearance | double-anonymized; Highlights encouraged |
| RSSM [verified] | no word limit stated | text | ≤250 words | 1-6 | APA 7 | double-anonymized; Highlights required |
| Sociological Methodology [verified] | generally ≤10,000 words | text,notes,refs (confirm) | 150-200 words | 4-5 | ASA 7 | anonymous; $25 fee (ASA student members exempt) |
| SMR [verified] | no fixed limit; typical ~10,000 words; ≤6 main-text tables/figures; title ≤20 words | text | ≤150 words, no parenthetical citations | not stated | ASA (datasets in DataCite style with DOI, repository, version) | double-anonymized |
| Sociology of Race and Ethnicity [verified] | ≤10,000 words including abstract, text, notes, references, tables, figures, and appendices (Pedagogy section ≤3,000); over-length papers are rejected | abstract,text,notes,refs,tables,appendix | <250 words: problem, theoretical and methodological approach, key findings | required (number not stated) | ASA | anonymous |

### Journal notes

**American Sociological Review [verified].** Separate files: cover letter, abstract, title page (title, acknowledgments, author names and affiliations, grant numbers, keywords, word count, corresponding author contact), and the anonymized manuscript (no title page, no author information, no abstract needed). Self-citation in the third person ("Smith (1992) concluded", not "I concluded"); don't cite your own dissertation, drafts, or unpublished papers. Times New Roman 12, double spaced throughout including notes and references, margins at least 1 inch, **remove page numbers** (the system renumbers). Generally 3 heading levels. Put "insert Table 1 here" placeholders in the text. Notes: superscript Arabic numerals, separate NOTES section, **each note ≤100 words**. REFERENCES section; list all authors (no et al. in the list). Tables: descriptive title, headings for all rows and columns, "Note:" for general notes, a, b, c for specific notes, \*p < .05, \*\*p < .01, \*\*\*p < .001, state one- or two-tailed, don't mark p < .10 as significant. Figures: Excel, Word, PowerPoint, .wmf, .emf, or 300-dpi .tiff. Appendixes lettered (Appendix A). Equations numbered at the right margin. ASR does not consider papers it previously rejected. Comments on recent articles ≤3,000 words. ORCID required for the corresponding author.

**American Journal of Sociology [verified].** No word limit (be concise); give the word count (text, notes, references) in the cover letter. Abstract ~150 words, required (papers without one aren't reviewed), pasted in the portal and in the manuscript. Cover page with the acknowledgment note as a separate file; remove personal notes about data collection, grants, and awards; list informal commenters in the acknowledgment note; revision memos must also be anonymous. Don't over-strip self-citations: cite your own work where any author would, and put unpublished supporting material in a reviewer appendix. Serif font ≥11 pt (12 preferred), double spaced, ≥1-inch margins. Order: abstract, text, references, notes (if endnotes), tables, figures. **Tables and figures at the back**, not in the text. Footnotes or endnotes are both fine; the acknowledgment note is marked with an asterisk on the cover sheet and substantive notes start at 1. Author-date citations; reference list alphabetical with full author names, headline-style capitalization, article and chapter titles in quotation marks; three authors get a comma before "and"; more than three use et al. in text; web pages go in notes, with access dates. Tables numbered separately (no 2a/2b), appendix tables A1, A2; avoid bold or italics to mark cells and avoid the word "panel". Alt text required for figures. Required at first submission: a **data-openness statement** (whether data will be deposited in the AJS Dataverse; interview and ethnographic data usually exempt), whether code will be shared, and a **novelty statement** if the paper overlaps with your other work. Don't suggest reviewers (suggestions are ignored). Preregistration optional. No gold open access; green OA is supported.

**Social Forces [verified].** 10,000 words including text, endnotes, and references; ≤10 tables and figure panels. Format-free first submission (any readable reference style), tables and figures in line with the text preferred at first submission; journal style (Chicago 17 author-date) at final submission, with tables at the end on separate pages and **no vertical lines**. Title page holds title, authors, affiliations, contact details, acknowledgments, and the abstract (no references in it). Accept all tracked changes before uploading. Remove reference-manager field codes. Don't use abbreviations in headings, tables, or figures. Notes only for substantive comments. Alt text for every figure, under the legend, beginning "Alt text:". Supplements ≤10 pages, 2 MB per file, mostly tables and figures, not copyedited. **Data availability statement required**; data and code sharing strongly encouraged; cite data and software in the references. Funding with full agency names and grant numbers in acknowledgments; conflicts disclosed at submission; ethics approval or exemption stated in Methods. **AI use must be disclosed in the cover letter and in the Methods or Acknowledgements.** The cover letter must disclose related preprints, dissertations, or papers and how this one differs.

**Socius [verified].** Original research and data visualizations. ≤10,000 words of main text at first submission (contact the office before exceeding), title ≤20 words, abstract ≤200 words. Separate title page file (with 150-word author bios); anonymize the manuscript, cite unpublished unsearchable own work as "Author", and **remove your name from the file properties**. Letter size, double spaced, page numbers starting after the title page. ASA 7. Avoid italics for emphasis. Results must be in the paper or supplement, never "available upon request". Cite datasets with a persistent identifier. Funding under a separate heading ("This research received no specific grant..." if none). Fees: $25 submission; APCs on acceptance by ASA membership status.

**European Sociological Review [verified].** ~8,000 words including endnotes and references, excluding tables and figures; longer papers judged on whether the contribution justifies the length; Data Briefs by proposal. Abstract ≤200 words; keywords required. Double-blind: names, affiliations, acknowledgments, and funding on a separate title page; self-citations must not reveal authorship, and "Author A" redaction is **not** allowed; supplements and replication files anonymous, with file properties cleared. Double spaced, page numbers, **no more than two levels of subheadings**. Format-free first submission. References: author-year with the year in parentheses, e.g., (Gans, 1962). Endnotes, numbered continuously. Alt text for figures. **Data Availability statement required in the endmatter**; papers with statistical or computational methods submitted from 1 January 2025 must deposit a **replication package** in a third-party repository (with a readme) as a condition of publication, and the initial submission must say whether the paper meets this or claims an exemption. 50-100 word author biographies; cover letter; funding statement beginning "This work was supported by...".

**British Journal of Sociology [verified, LSE page].** Articles ~8,000 words including notes and bibliography (the title-page count covers abstract, text, notes, bibliography, and appendices); research notes ≤2,500. Abstract ≤300 words; 6 keywords. Title page as a separate PDF with only title, word count, and date. Double spaced; **British spelling**, single quotation marks, "per cent", dates like 12 December 1972. Harvard citations; Bibliography placed after the Notes, alphabetical, repeat the author's name for multiple works; no op. cit./ibid. Tables and figures on separate sheets with their position marked, **numbered with Roman numerals**, minimal lines and no boxes; appendix items AI, AII. Acknowledgments as note 1, marked after the title. Appendices go after the text and before Notes and Bibliography. Confirm data and AI policies on the Wiley page.

**Journal of Health and Social Behavior [verified].** 10,000 words (title page reports a word count covering text, notes, and references, excluding tables and figures); commentaries ≤3,000. Abstract <150 words and must state **sample size, design, and data source**. Anonymized title page: title, total word count, number of tables, number of figures, and a **running head <55 characters**; author names, acknowledgments, and grants added only at acceptance (title footnote marked with an asterisk). Times New Roman 12, double spaced throughout, ≥1-inch margins. Text starts on a new page with the full title, **no Introduction heading**; headings Background, Data and Methods, Results (or Findings), Discussion, References; generally 3 levels. Notes: superscript numerals in a separate NOTES section before the references; **don't use Word's note function**. Order after the text: notes, references, tables, figures, appendices, each in its own section. Tables each on a separate page with "Table 1 about here" placeholders, no abbreviations for variable names or headings, **align numbers by decimal**, "Note:" and a, b, c notes, \*p < .05, \*\*p < .01, \*\*\*p < .001 with one- or two-tailed stated. Figures in black ink, legible at 2-9/16 or 5-5/16 inch width, no abbreviations. $25 fee.

**Social Science & Medicine [verified].** Choose one of seven **editorial offices** at submission: Medical Anthropology, Health Economics, Social Epidemiology, Health Psychology, Medical Sociology, Health Policy, or Health Geography. Each has its own scope (for example, Medical Sociology requires deep engagement with sociological theory and mainly takes qualitative work; Social Epidemiology mainly takes quantitative and mixed methods; Health Psychology requires psychological theory and is wary of cross-sectional self-report studies), so check fit before submitting. Qualitative papers should follow the SSM Guidelines for Qualitative Papers. Limits in the table. **Double-anonymized**: a separate title page (authors, affiliations, corresponding author's email, acknowledgments, which appear only there) and an anonymized manuscript with no identifying information in the text or supplements. Word (.docx) or LaTeX, single-column; a PDF is not an acceptable source file. Abstract ≤250 words, concise and factual, stating main findings with their statistical significance and the conclusions, with no undefined abbreviations and any cited reference given in full. 1-7 English keywords (avoid multiword phrases with "and" or "of"). **Highlights required**: 3-5 bullets, each ≤85 characters including spaces, in a separate editable file with "highlights" in the file name. Tables: editable text, not images; numbered in order of citation, cited in the text, caption above, notes below the body; **no vertical rules or shading**; don't duplicate results given elsewhere. Appendix items numbered Table A.1, Fig. A.1, Eq. (A.1). References: Elsevier name-date; in text (Allan, 2020a, 2020b; Allan and Jones, 2019), et al. for three or more; list alphabetical then chronological, journal names abbreviated per LTWA, with DOIs. **Generative AI declaration** in a new section before the references ("Declaration of generative AI and AI-assisted technologies in the manuscript preparation process"), plus disclosure in figure captions for AI-generated images. Data: Option C, so deposit data in a repository and cite it, or state why it can't be shared. Declaration of competing interests (Word file) and CRediT author statement. The official guide doesn't set font, spacing, margins, or page or line numbers; double spacing with page and line numbers is a sensible default.

**SSM - Population Health [verified].** Shares SSM's general approach and Elsevier conventions; welcomes replication studies, methodological studies, instrument validation, opinion pieces, and reviews. Limits in the table (reviews ≤12,000, not 15,000). **APA 7 references** (not the SSM name-date style). Highlights and a graphical abstract are encouraged, not required. Double-anonymized with a separate title page; abstract ≤250; 1-7 keywords; same table rules as SSM; Option C data; generative AI declaration as for SSM. Open access with an APC.

**SSM - Mental Health [verified].** Social science of mental and behavioral health (medical anthropology and critical social science; psychiatric epidemiology and population mental health). Article types and limits in the table. **Single-anonymized** review, so the title page and author details can stay in the manuscript. Highlights required (3-5, ≤85 characters); graphical abstract encouraged. Abstract ≤250; 1-7 keywords; footnotes allowed but sparing, numbered consecutively; acknowledgments in a separate section just before the references (not on the title page or in a footnote). Elsevier name-date references as for SSM. Data: Option B (sharing encouraged). Same table rules and generative AI declaration as SSM. Open access with an APC.

**Sociology of Health & Illness [verified].** Original articles (empirical or conceptual; literature reviews with systematic or narrative methods count here and must discuss the reviewed work conceptually) ≤9,000 words **including tables, figures, notes, and bibliography**, with each half-page table or figure counted as 250 words. Review articles (agenda-setting reviews of a field of medical sociology) ≤8,000 words excluding notes and bibliography; contact the co-chief editors first. Commentaries ≤2,500 (invited); book reviews ~800. Abstract 100-200 words that stands on its own, followed by its word count and a word count of the main body. **Double-blind**: remove names, affiliations, acknowledgments, ethics information, and other identifiers; replace self-citations with "Anon" in the text and the reference list; the main text is headed only by the title. Separate title page with word count, resubmission status, ethics approval, ORCID, co-author details, CRediT contributions, funding, **data availability statement** (required, even if data can't be shared), conflicts of interest, patient consent, and permissions. Harvard references: (Light 1998), Jameson (2005), et al. for more than two authors; list alphabetical, e.g., Nettleton, S. and Burrows, R. (2003) E-scaped medicine? Information, reflexivity and health, *Critical Social Policy*, 23, 2, 165-185. Notes few and brief, numbered in the text, placed at the end of the text before the bibliography. **Double line spacing**. House style: British spelling (-ise), no contractions except in verbatim transcripts, no sentence starting with a numeral, dates as 5 January 2003, shortest page ranges (22-4, 105-6), non-sexist language per the BSA guidelines. Generative AI use must be described in detail (tool, purpose, effect on arguments, how outputs were checked) in the Methods or acknowledgments. First-submission references can be in any consistent style, but revisions must follow journal format.

**Demography [verified].** Limits in the table (main text excludes abstract, keywords, footnotes, acknowledgments). Abstract ≤200 words summarizing results and why they matter (population and methods only if they are the contribution); **3-5 Highlights**, complete sentences ≤85 characters; ≤5 keywords; a **Relevance to Demography statement** (editors only) and a pre-submission author attestation form. Order: title, highlights, abstract, keywords, main text, references, tables and figures. Double spaced, 12 pt, 1-inch margins, left aligned (not justified), **page numbers from the title page**. Headings in title case, unnumbered, starting with "Introduction": primary bold 14 pt, secondary bold 12 pt, tertiary italic 12 pt; subheads only when there are two or more. Numbers: spell out one through nine; numerals for 10 and above, ages, and millions; leading zero for values that can exceed 1; en dashes for ranges; Merriam-Webster spelling. References APA-based: (Author Year) with no comma, et al. for three or more, page numbers for quotations, hanging indent, DOIs for online-only journals; don't cite sources in footnotes; **no endnotes**. Tables: each on its own page at the end, title-case column headings, horizontal rules only; notes in the order general notes, sources, lettered notes, significance markers; **CIs or SEs strongly encouraged and asterisks discouraged**. Figures: separate EPS or PDF ≥300 dpi, sans-serif ≥6 pt, title beneath the figure, colorblind-friendly, **alt text** (~200 characters); refer to panels as "panel a of Figure 1". Online appendix as a separate PDF (Table A1, Figure A1), with its own reference list. Accepted papers need a Reproducibility and Data Availability statement. Preprints allowed (tell the office; don't update during review).

**Population and Development Review [verified].** Population Council journal published by Wiley. Papers typically run 8,000-10,000 words. Sections open to submissions: **Research Articles** (theory and application, policy analysis, sociographic studies, critical assessments of research; most papers), **Notes and Commentary** (current population questions and policy), and **Data and Perspectives** (new statistics and their interpretation); the last two take shorter papers. Long book reviews (1,500-2,000 words) and review essays are invited. **Free-format first submission**: one file or several, with abstract, introduction, methods, results, and conclusions; figure and table legends; any consistent reference style. **Double-anonymized**: anonymize the manuscript (papers that reveal authorship aren't sent for review) and give a separate title page with data availability, funding, conflict of interest, ethics approval, patient consent, and permission statements. Confirm authorship in the cover letter. A data availability statement is published with every accepted paper. **AI disclosure** (Wiley): in the acknowledgments for drafting, editing, translation, or formatting help; in the Methods for research uses; in figure captions for generated or edited visuals. Revised papers must follow journal formatting.

**Population Research and Policy Review [verified].** Detailed, strict house style (manuscripts lacking it are returned):
- Main file starts with a **de-identified title page**: 14-pt bold title, "Abstract" heading, abstract, keywords (bold italic label); no author information, running head, JEL codes, or declarations; page break; text starts on page 2. Blinded self-citations as "(Blinded for Review)", omitted from the reference list.
- Word file, 1-inch margins, black text, page numbers from the title page, **no running head or line numbers**; 12-pt Times New Roman, Arial, or similar; double spaced; left justified; first-line indent 0.5 inch; 0 pt before and after paragraphs.
- Headings: Level 1 14-pt bold ALL CAPS on its own line; Level 2 12-pt bold italic Headline Case; Level 3 12-pt bold sentence case ending with a period, run in, indented. Required Level 1 headings for research articles: Introduction, Background, Data and Methods, Results, Discussion and Conclusion.
- Footnotes: 10 pt, single spaced, Word's footnote tool; no endnotes; not just for citations.
- Numbers per APA (words for zero to nine, with exceptions); en dashes for ranges; leading zeros except for values that can't exceed 1. Exact p values when p > .001.
- References APA 7 with PRPR rules: single spaced, 0.5-inch hanging indent, every reference with a DOI or URL hyperlink (https://doi.org/...), no reference-manager field codes. **Don't use LLMs to find or format references** (treated as a research-integrity violation).
- Tables: Word table function, APA format, no vertical lines, decimal tabs, no text under 9 pt; title 12-pt bold Headline Case on the same line as the number; panels A, B and models numbered; SEs in separate parenthetical cells; full model tables; notes beginning italic *Note.* in 10 pt: general, specific (a, b), probability (†, \*, \*\*, \*\*\* with italic p); one table per page after the references, with "[Insert Table 1 about here]" centered after first mention.
- Figures: APA format, title 12-pt bold on the same line as the number, legible in grayscale, black text ≥8 pt, note pointing to the associated table for estimate figures.
- Either an Appendix (in the main file, ≤2 pages, items numbered with the main text) or an Online Supplement (separate file titled ONLINE SUPPLEMENT, items Table S1...), not both.
- Declarations entered in the submission system only: author contributions (CRediT, even for sole authors), competing interests, ethics approval (suggested wording for public de-identified data: "This study used de-identified publicly available data and thus it was exempt from institutional ethics approval."), data availability, funding.

**Advances in Life Course Research [verified].** Interdisciplinary life course research: empirical, theoretical, methodological, and review articles on events, transitions, or whole life segments. No word limit or article-type list in the guide. **Double-anonymized** with a separate title page; abstract ≤250 words; 1-7 keywords; Highlights encouraged (3-5, ≤85 characters); **APA 7 references**; tables editable, no vertical rules or shading, notes below; Option B data (sharing encouraged); Elsevier generative AI declaration before the references; CRediT and competing-interest declarations.

**Social Science Research [verified].** Quantitative research articles that test and advance social science theory, plus papers that significantly advance quantitative methods. **Desk-rejected as out of scope:** theoretical papers, syntheses, or commentaries; qualitative studies; studies relying mainly on simulated data; reviews (except meta-analyses); descriptive or exploratory studies; research notes; evaluations of specific policies or programs; and, usually, nonexperimental studies of convenience samples (some discretion for hard-to-reach populations). Check fit before anything else. **No word limit**, but write concisely; editors may ask for cuts. Double-anonymized with a separate title page; abstract ≤250 words; 1-7 keywords; Highlights encouraged (3-5, ≤85 characters). **References are numbered**: square brackets in the text ("as demonstrated [3,6]. Barnaby and Jones [8] found..."), numbered in order of appearance, journal names abbreviated per LTWA, which is unusual for sociology, so convert author-date drafts. Tables: editable, no vertical rules or shading, notes below. Option B data (sharing encouraged); Elsevier generative AI declaration before the references; CRediT and competing-interest declarations.

**Research in Social Stratification and Mobility [verified].** Official journal of ISA RC28. No word limit stated. Double-anonymized with a separate title page; abstract ≤250 words; **1-6 keywords**; **Highlights required** (3-5, ≤85 characters); **APA 7 references**; footnotes allowed but sparing, numbered consecutively; tables editable, no vertical rules or shading; Option B data; Elsevier generative AI declaration, CRediT, and competing-interest declarations.

**Sociological Methodology [verified].** Generally ≤10,000 words. Abstract 150-200 words without identifying information; 4-5 keywords on the title page. Blinded manuscript; third-person self-citation. Double spaced throughout, Times New Roman 12, **1.25-inch margins**, Word or LaTeX (with PDF), generally 3 heading levels, editable equations. ASA 7; REFERENCES alphabetical, all authors listed, DOIs for datasets. Tables in Word or Excel with significance asterisks (one- or two-tailed stated); figures in grayscale. Notes in a separate ENDNOTES section, each ≤100 words. Lettered appendices. $25 fee.

**Sociological Methods & Research [verified].** No target length (typical ~10,000 words); ≤6 essential tables/figures in the main text; title ≤20 words; abstract ≤150 words without parenthetical citations. Double-anonymized: third-person self-citation, or "(Author(s), date)" with an entry alphabetized under "A"; replace IRB and funding details with "[Anonymized for peer review]". Double spaced, 12 pt, **1.25-inch margins**, **footnotes only (no endnotes)**; Word, LaTeX (Overleaf template), or PDF. ASA references; datasets in DataCite style with DOI, repository, and version; incomplete references are returned. Tables: label and title above, notes below; figures: label and title below; readable in greyscale, colorblind-friendly. Online supplement as separate PDFs named "ONLINE SUPPLEMENT". **Anonymized code and materials required at submission** (anonymous repository link preferred), an **availability statement** required, open data and code in a trusted repository before acceptance ("upon request" not accepted), and a **preregistration statement** for all manuscripts (preregistration mandatory for new RCT submissions from July 2026). Generative AI allowed for readability, **disclosed in the backmatter** with the tool and purpose; no statement needed if none was used.

**Sociology of Race and Ethnicity [verified].** ASA section journal (Sage); papers that break the length or format rules are **rejected**. ≤10,000 words **including abstract, text, notes, references, tables, figures, and appendices**; Pedagogy section ≤3,000 (long or landscape tables may prompt a request to cut). **Double spaced throughout** (notes and references included), **Times New Roman 12**, margins **1 to 1.5 inches**, .doc or .docx. Abstract <250 words covering the research problem, theoretical and methodological approach, and key findings and arguments. Text starts on a **new page headed by the full title**; then, in order, Notes, References, tables, figures, appendices. Generally three heading levels. Anonymized: cite your own work in the third person ("Smith (1992) concluded"); blind or remove working papers. ASA citations as in the style reference. **Notes** in a separate NOTES section after the text, superscript numerals, and **don't use Word's footnote function**. REFERENCES: complete, all authors listed (no et al.), first names and middle initials, repeated names given in full. **Tables**: each on a separate page with "Table 1 about here" in the text; descriptive title; no abbreviated variable names or headings; **align numbers by decimal**; "Note:" plus a, b, c notes; \*p < .05, \*\*p < .01, \*\*\*p < .001 with one- or two-tailed stated; editable, not images. Figures in black ink, no abbreviations, legible at 2-9/16 or 5-5/16 inches wide. Appendices lettered with titles ("APPENDIX A. Variable Names and Definitions"). Separate title page (title, short title, abstract, keywords, author names, emails, mailing addresses, affiliations, bios, acknowledgments); a cover letter with author bios uploaded as a supplementary file. Revisions: no highlighted, colored, or bold text, and the response letter is anonymous and pasted into the portal. Personal acknowledgments and funding (with the "no specific grant" wording if none) go on the title page; AI tools can't be authors (Sage).

## Style reference

### ASA style, 7th edition (ASR, JHSB, Socius, SRE, Sociological Methodology, SMR)
- **In-text citations:** (Author Year) with no comma; page numbers after a colon with no space: (Ramirez and Weiss 1979:239-40). Two authors: both names. Three authors: all three at first citation, then et al. Four or more: et al. throughout. Multiple citations separated by semicolons, in consistent alphabetical or date order. "forthcoming" for accepted work; "n.d." for undated work. Cite data files by author and date.
- **References** (heading REFERENCES; alphabetical; double spaced; hanging indent): list all authors (no et al.), invert only the first author's name, full first names where available. Same author, several works: by year; same year: 2020a, 2020b by title.
  - Journal article: Lastname, Firstname, and Firstname Lastname. Year. "Article Title in Title Case." *Journal Name* Volume(Issue):pages. doi:10.xxxx/xxxxx.
  - Book: Lastname, Firstname. Year. *Book Title*. City, ST: Publisher.
  - Chapter: Lastname, Firstname. Year. "Chapter Title." Pp. 1-20 in *Book Title*, edited by F. Lastname. City, ST: Publisher.
  - Datasets: include a persistent identifier (DOI).
  - Page ranges: full numbers under 100 and for ranges starting at a multiple of 100 (100-108); otherwise drop repeated leading digits (321-28).
- **Notes:** superscript Arabic numerals, a separate NOTES (or ENDNOTES) section; ASR and Sociological Methodology limit each to 100 words; JHSB says not to use Word's note function.
- **Tables:** descriptive title; headings for all rows and columns; "Note:" for general notes; a, b, c for specific notes; \*p < .05, \*\*p < .01, \*\*\*p < .001 and say whether tests are one- or two-tailed; don't mark p < .10 as significant. Placeholders in the text ("Table 1 about here"). JHSB: align numbers by decimal; no abbreviated variable names.
- **Language (ASA 7):** capitalize racial and ethnic terms (Black, White); avoid "Afro-American", "Negro", "Oriental"; singular "they" is acceptable; prefer active voice; past tense for literature reviews.

### Chicago author-date (Social Forces) and AJS
- Social Forces: Chicago 17 author-date. (Author Year) with no comma; page numbers only for quotations or specific notes or tables; et al. for more than three authors; 1975a, 1975b; reference list alphabetical with first names spelled out.
- AJS house style: author-date; headline-style capitalization; article and chapter titles in quotation marks; comma before "and" for three authors in the list; web pages cited in notes with access dates; inclusive page numbers for chapters.

### APA-based (Demography, PRPR, SSM - Population Health, ALCR, RSSM; SSM tables)
- Social Science Research is the exception among the Elsevier sociology journals: numbered references in square brackets, in order of appearance.
- Demography: (Author Year) without comma; et al. for three or more; numbers rule as in the Demography note; no endnotes.
- PRPR: APA 7 with the PRPR rules above (DOIs as hyperlinks; single-spaced reference list).
- APA statistics conventions apply in tables: italic statistical symbols, no leading zero for values that can't exceed 1, exact p values (p < .001 floor).

### Harvard and Elsevier name-date (BJS, SHI, ESR variant, SSM, SSM - Mental Health)
- BJS: Riley (1983) in text; et al. for four or more authors; bibliography entry "Smith, A.J. 1992 *Sociology Today*, London: Routledge." Repeat author names; no ibid.
- ESR: (Gans, 1962), with a comma and the year in parentheses in the list.
- SHI: (Light 1998), et al. for more than two authors; "Nettleton, S. and Burrows, R. (2003) Title, *Journal*, 23, 2, 165-185"; British spelling.
- SSM and SSM - Mental Health (Elsevier name-date): (Allan, 2020a, 2020b; Allan and Jones, 2019), with a comma before the year and et al. for three or more; "Van der Geer, J., Handgraaf, T., Lupton, R.A., 2020. The art of writing a scientific article. J. Sci. Commun. 163, 51–59. https://doi.org/..."; journal names abbreviated per LTWA.

### Causal language (all journals)
For observational designs, flag causal verbs and nouns ("led to", "caused", "resulted in", "reduced", "increased", "effect of", "impact") and suggest "was associated with" or "the association between". If the design supports causal inference (experiments, natural experiments, fixed effects with stated assumptions, IV, RD, difference-in-differences, target trial emulation), check that the identification assumptions are stated instead. Look hardest at the abstract, highlights, and discussion.

### Table and number formatting (sociology)
- Build tables with Word's table tool, never tabs or spaces; each value in its own cell; no vertical lines (Social Forces, Demography, PRPR, and the Elsevier journals state this); no shading (stated by the Elsevier journals).
- Significance asterisks are standard in ASA journals (with one- or two-tailed stated) but **discouraged at Demography**, which prefers CIs or SEs. PRPR adds † for p < .10.
- Decimal alignment: **required at JHSB and SRE** ("align numbers by decimal") and PRPR ("decimal tabs"); optional elsewhere. Use the table formatter's `--decimal-align`, which puts a decimal tab in each numeric cell. Keep decimal places consistent within a column.
- Standard errors in parentheses below or beside coefficients, stated in the note; give model fit statistics and N for each model.
- Numbering: Arabic in most journals; **Roman numerals at BJS**; no 2a/2b at AJS (appendix tables A1, A2).
- Placement: ASR, JHSB, PRPR, Demography want placeholders in the text ("Table 1 about here"); AJS and Social Forces (final) want tables at the end; Social Forces and ESR prefer inline at first submission.

## How to do each feature

Principles that apply to all of them:
- **Never invent content.** Build abstracts, highlights, statements, keywords, cover letters, and responses only from the manuscript, the reviewer comments, or what the author says. Use marked placeholders like `[DATA DOI NEEDED]` and list them at the end.
- **Keep the author's voice.** Note sentence length, hedging words, transitions, and preferred terms before editing. Delete before rewriting; reuse the author's own phrasing.
- **Show every change.** Edits come with a change log (original, revised, reason, words saved). Checks list location, a short quote, the issue, and a fix. The author decides.
- **Flag, don't fix, the science.** Mismatches between methods and results, missing robustness checks, or unstated limitations are questions for the author.
- **References are checked, not generated.** Point the author to their reference manager (Zotero styles exist for ASA, Chicago author-date, APA 7, and most of these journals). PRPR explicitly bans using LLMs to find or format references.
- **Say what's unverified.** For [confirm] journals, every requirements card and dashboard names the items to confirm.

**1. Requirements card.** Fetch the live page. Give: journal, article type, length limit and what counts (and the `--count` to use), abstract, keywords, extras (highlights, relevance statement, data/replication statement, running head), reference style, tables/figures rules and placement, notes rules, file layout and anonymization, required statements, fees, anything new vs this file, verification status, date checked.

**2. Abstract.** Follow the journal's limit and any content rule (JHSB: sample size, design, data source; Demography: results and why they matter, methods only if they're the contribution; SMR: no parenthetical citations; ASR and Socius: purpose, methods, findings). No references unless allowed. Count words.

**3. Journal-specific extras.** Highlights (Demography, and SSM, SSM-MH, and RSSM where required; encouraged at SSM-PH, ALCR, and SSR: 3-5 bullets, ≤85 characters each, including spaces; count characters; SSM wants them in a separate file named with "highlights"). SSM editorial office (recommend one of the seven from the paper's methods and theory). Relevance to Demography statement (editors only: why the paper matters to population studies). Data availability or replication statement (ESR, Social Forces, SMR, PRPR, Demography at acceptance; AJS data-openness and code statements at first submission). JHSB running head (<55 characters including spaces). Draft from the manuscript only.

**4. Keywords.** Respect the journal's count (ASR, Sociological Methodology 4-5; BJS 6; Demography ≤5; PRPR 4-6; SSM journals, ALCR, and SSR 1-7, RSSM 1-6, avoiding multiword phrases with "and" or "of"). Avoid repeating title words where the journal says so (PRPR).

**5. Section order.** Check the journal's order and heading conventions (JHSB: no Introduction heading; PRPR required Level 1 headings; Demography starts with "Introduction"; ESR ≤2 subheading levels; ASR, JHSB, Soc Methodology ~3 levels; AJS order abstract, text, references, notes, tables, figures; BJS order text, appendices, notes, bibliography). Methods should cover data source and sample derivation, measures, missing data, and analytic strategy.

**6. Style check.** Apply the journal's reference and citation style from the style reference, plus number, language, and table rules. Run the table checker. Report as a table (location | quote | issue | fix), grouping repeated issues.

**6b. Page layout and heading check.** Run `layout_check.py --journal <code>` (`--blinded` for the anonymized file). Report must-fix items marked "journal requirement" (e.g., ASR: remove page numbers; JHSB: no Word notes, no Introduction heading, text starts on a new page; PRPR: ALL CAPS Level 1, no line numbers, page numbers from the title page; Demography: left aligned, page numbers; Socius and ESR: page numbers; SSM: page and line numbers, no notes) and suggestions. Tell the author to resolve tracked changes and comments, and to clear file properties in the blinded file (Socius and ESR require it). Don't edit layout unless asked; if asked, edit a copy with the docx skill.

**6c. Format my tables.** Only when asked. (1) Run the table checker and show the findings. (2) Suggest resolving tracked changes inside tables first. (3) Run `python table_format.py manuscript.docx --style asa -o <name>_tables.docx` (`--style apa` for Demography, PRPR, SSM-PH, ALCR, RSSM, SSR, and the SSM journals), adding `--decimal-align` for JHSB, SRE, and PRPR (or if the author wants it), and `--include-supplement` for appendix tables if wanted. (4) It sets horizontal rules only, removes shading and colored text, repeats the header row, and makes tracked fixes to P values (leading zeros, .000), minus signs, and comma separators; it never changes values, decimals, wording, or order. (5) Re-run the checker on the output and list what remains by hand (titles, note wording such as "Note:" vs *Note.*, one- or two-tailed statement, Roman numerals at BJS, asterisks at Demography). (6) Deliver the .docx and the change log.

**7. Consistency check.** Fact table (Ns through the sample derivation, descriptives, key coefficients and SEs or CIs, years) checked across abstract, highlights, text, tables, and figures. Recompute percentages from counts.

**8. Causal language.** As in the style reference.

**9. Clarity edit.** Show a 3-5 bullet voice profile first. Edit for clarity and grammar only; give the edited text and a change log. Respect British spelling at BJS.

**10. Dashboard.** Run `soc_count.py` with the journal's `--count` and limits, plus `--note-max 100` for ASR and Sociological Methodology and `--title-max-words 20` for Socius and SMR. Table: item | count | limit | status, per-section counts, and where cuts would hurt least.

**11. Trim to fit.** Target the overage with a ~2% buffer. Cut redundancy, wordy phrases, long literature reviews that list studies one by one, results that repeat tables, and methods details that belong in an appendix or supplement. Notes and references count at ASR, Social Forces, ESR, JHSB, and BJS, so trimming long notes and unneeded references helps there. For a .docx, deliver a copy with suggested cuts as Word comments (or tracked changes if asked).

**12. Move to supplement.** Use the journal's naming (Appendix A at ASR and JHSB; Table A1 at Demography and AJS; Table S1 in a PRPR online supplement; "online supplement" at SMR). Socius forbids "results available upon request"; anything discussed must be in the paper or supplement.

**13. Reporting standards.** Check that data source, sample derivation and exclusions, measures, missing data handling, model specification, robustness checks, and limitations are reported. For trials, reviews, and qualitative studies, map the relevant EQUATOR guideline.

**14. Reference check.** Check citations against the list (both directions), the journal style (ASA: all authors listed, colon page numbers; Chicago; APA; Harvard), DOIs (required for datasets at ASR, Socius, SMR; for all references at PRPR), and duplicates. Report problems; don't rewrite the list.

**15. Title page and statements.** Check the journal's title page contents (ASR: title, acknowledgments, authors, grants, keywords, word count, contact; JHSB: anonymized title page with counts and running head; PRPR: de-identified title page inside the main file; BJS: title, word count, date only; Demography: highlights and keywords) and each required statement: funding, conflicts, ethics (PRPR suggested wording for public de-identified data), data availability, CRediT (PRPR, ESR), AI disclosure (Social Forces: cover letter and Methods or Acknowledgements; SMR: backmatter). Draft missing statements with placeholders.

**16. Anonymization check.** Run `soc_count.py --authors` and `layout_check.py --blinded`. Check for self-identifying citations (ASR, JHSB, Soc Methodology: third person; SMR: "(Author(s), date)" allowed; ESR: "Author A" not allowed; AJS: don't over-strip, use a reviewer appendix; Socius: "Author" for unsearchable work), IRB and funder names, acknowledgments, file properties, and identifying details in supplements and replication files (ESR, SMR).

**17. Cover letter.** Include what the journal asks for: AJS word count and novelty statement; Social Forces related papers and AI use; Demography preprint status; ASR contact details and full title. Explain fit with the journal's audience.

**18. Mock review.** If the gerontology-paper-review skill is available and the paper is on aging, life course, or health, load it with the target journal in mind. Otherwise: summary, fit (ASR: methods quality, general sociological appeal, breadth; Demography: relevance to population studies; JHSB: medical sociology contribution), major and minor comments, methods and robustness points, top 3 fixes.

**19. Response to reviewers.** Number and quote each comment; respond in the author's voice with the change and its location; [DESCRIBE CHANGE] and [AUTHOR TO CONFIRM] placeholders. Keep the memo anonymous where the journal requires (AJS). Rerun the dashboard.

**20. Retarget.** List every difference: what counts toward the limit, abstract, keywords, extras, reference style (ASA vs Chicago vs APA vs Harvard is usually the biggest job), notes rules, tables placement, anonymization, statements, fees. Apply format changes, reframe the opening and contribution for the new audience, and draft a new cover letter. ASR does not consider papers it previously rejected.

## Output
- Checks and the dashboard: a short report grouped as must fix, should fix, optional, with a one-line verdict at the top.
- New text: ready to paste, with word or character counts and placeholders.
- Edits: revised text and change log; for a .docx, an edited copy with comments or tracked changes.
- End with open items: placeholders, author decisions, and anything marked [confirm].

Several of these journals require disclosure of AI use (Social Forces, SMR; Sage, OUP, Elsevier, and Wiley all have policies). When this skill writes or edits text (features 2-4, 9, 11, 17, 19), remind the author once per session to check the journal's AI disclosure rule.

## Word counter

Write this to the scratchpad as `soc_count.py` before running it. Pass the journal's `--count` from the journal table.

```python
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
```

## Table checker

Write this to the scratchpad as `table_check.py` before running it. Use `--style asa` for ASA journals and most sociology journals, `--style apa` for Demography, PRPR, SSM-PH, ALCR, RSSM, SSR, and the SSM journals; add `--decimal-align` for JHSB and SRE.

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

Write this to the scratchpad as `layout_check.py` before running it. Use `--journal` with the code from the journal table.

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

Write this to the scratchpad as `table_format.py` before running it. Run it only when the author asks for tables to be formatted.

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
