# Requirements

You need these only if you run the scripts in [`scripts/`](scripts) yourself, or adapt the skills for your own agent or environment. In the Claude app, Claude sets everything up on its own; just turn on **Code execution and file creation**.

## Python

- **Python 3.8 or later.** The scripts are checked to compile on 3.8 and 3.9 and are tested end to end on 3.13.
- **One third-party package: [`lxml`](https://pypi.org/project/lxml/)** (4.9 or later), used to read and edit Word (.docx) files.

```bash
pip install -r requirements.txt
# or
pip install lxml
```

Everything else comes from the Python standard library (`argparse`, `zipfile`, `re`, `difflib`, `decimal`, `json`, `pathlib`, and others). The scripts don't need Microsoft Word, `python-docx`, or an internet connection.

## What each script needs

| Script | Purpose | Needs |
|---|---|---|
| `jama_count.py`, `gsa_count.py`, `soc_count.py` | Word counts by each journal's rules | Python 3.8+, lxml |
| `table_check.py` | Table format checks | Python 3.8+, lxml |
| `layout_check.py` | Page layout and heading checks | Python 3.8+, lxml |
| `table_format.py` | Writes a copy of the manuscript with journal-style tables | Python 3.8+, lxml |

Each script prints its options with `--help`.

## Input files

- **.docx** (Word 2007 or later, or a .docx exported from Google Docs or LibreOffice) is what the scripts read. Tracked changes are counted as accepted.
- The word counters also accept **.txt** and **.md**. For a PDF, convert it to text first, for example with `pdftotext manuscript.pdf`.

## Optional

- **LibreOffice** (`soffice`) and **Poppler** (`pdftoppm`), only if you want to render a .docx to PDF or images to look at the result, as in the README example. The skills don't need them.
- **python-docx**, only to rebuild the fictional demo manuscript with `examples/make_demo.py`.

## Using the skills outside the Claude app

Each `skills/<name>/SKILL.md` is self-contained: the scripts are embedded at the end, and the instructions tell the agent to write them to a scratch folder before running them. Any agent environment that can read the SKILL.md, write files, and run Python 3.8+ with lxml can use them. The standalone copies in `scripts/` are identical to the embedded ones.
