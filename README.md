# 🧪 PubMed Paper Fetcher

A Python CLI tool to fetch research papers from **PubMed** using a user-specified search query, and filter out authors affiliated with **non-academic institutions** such as **pharmaceutical** or **biotech companies**.

---

## 🚀 Features

- 🔍 Fetches papers from PubMed using Biopython's Entrez API
- 🧠 Filters authors based on affiliation keywords like "pharma", "biotech", "inc", "ltd", etc.
- 📄 Saves results to a CSV file or prints them to the terminal
- 🧾 Typed Python for better readability and maintainability
- 💻 Clean CLI interface using Typer with options for help, debug, and output file
- 📦 Dependency management handled by Poetry
- 🧱 Modular structure separating core logic from CLI

---

## 🗂️ Project Structure

```text
pubmed-paper-fetcher/
├── README.md               # Project documentation
├── pyproject.toml          # Poetry configuration file
├── poetry.lock             # Lock file for dependencies
├── get-papers-list.py      # Optional CLI entry point
├── get_papers/             # Main application module
│   ├── __init__.py
│   ├── cli.py              # CLI interface using Typer
│   └── core.py             # Core logic to query, filter, and export PubMed papers
├── tests/                  # Test directory
│   └── test_core.py        # Unit test placeholder
├── results.csv             # Example output CSV
└── output.csv              # Optional CSV file saved by user

---

```
## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/2020ucp1070/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher

# Install dependencies
poetry install

---

```
 ## 🧭 Step-by-Step Usage Guide

 ```bash
 # Run a query (results printed to console)
poetry run get-papers-list "cancer immunotherapy"

# Save output to CSV
poetry run get-papers-list "mRNA vaccine" --file results.csv

# Enable debug mode
poetry run get-papers-list "gene therapy" --debug

# View help message
poetry run get-papers-list --help

---

```
## ⚙️ Command-Line Options

```bash
-d, --debug                 Show debug output
-f, --file <filename>       Save output to CSV file
-h, --help                  Show help message

---

```
## 🔍 How It Works

```bash
1. User runs the CLI with a search query.
   Example: poetry run get-papers-list "cancer immunotherapy"

2. The CLI passes the query and options to the core logic.

3. Biopython's Entrez module queries the PubMed API and retrieves paper metadata.

4. Author affiliations are scanned for pharma/biotech-related keywords like:
   - "inc", "ltd", "biotech", "pharma", "therapeutics", "gmbh", "llc", etc.

5. If at least one author is affiliated with such organizations, the paper is included.

6. The final result is either:
   - Displayed in the terminal, OR
   - Saved as a CSV file if `--file` is specified.

---

```
## 📦 Tools Used

```bash
- Biopython – for accessing PubMed via Entrez
- Typer – for building the command-line interface
- Pandas – for formatting and exporting CSV output
- Poetry – for managing dependencies and packaging

---


```
## 🤝 Built With Help From

```bash
- Git – version control and project tracking
- GitHub – for hosting and sharing the project
- Markdown – for clean and readable documentation
- Poetry – for dependency and environment management
- ChatGPT – for debugging, suggestions, and code improvements


