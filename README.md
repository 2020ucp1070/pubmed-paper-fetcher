@@ -9,11 +9,35 @@ A Python CLI tool to fetch PubMed papers matching a search query and filter out
 - Saves results to CSV or prints to console
 - CLI with options for debug and output file
 - Modular structure
 - Typed Python
 - Typed Python for better readability and maintainability
 - Poetry for dependency management
 
 ## Project Structure
 
 pubmed-paper-fetcher/
 │
 ├── README.md                # Project documentation
 ├── pyproject.toml           # Poetry configuration file
 ├── poetry.lock              # Lock file for dependencies
 │
 ├── get-papers-list.py       # Entry point to run the CLI (optional)
 │
 ├── get_papers/              # Main Python package
 │   ├── __init__.py
 │   ├── cli.py               # CLI interface using Typer
 │   └── core.py              # Core logic to fetch, process, and export PubMed data
 │
 ├── tests/                   # Test suite
 │   └── test_core.py         # Unit test placeholder
 │
 ├── results.csv              # Example or generated output (optional)
 └── output.csv               # User-generated CSV output (optional)
 
 
 ## Installation
 
 > Make sure [Poetry](https://python-poetry.org/docs/#installation) is installed.
 
 ```bash
 git clone https://github.com/yourusername/pubmed-paper-fetcher.git
 cd pubmed-paper-fetcher
 @@ -29,10 +53,41 @@ poetry run get-papers-list "cancer therapy"
 Options:
 - `-d` or `--debug`: Show debug output
 - `-f <filename>` or `--file <filename>`: Save to CSV file
 - `-h` or `--help`: Show help message
 - `-h` or `--help`: Show usage instructions and available options
 
 Example with output:
  poetry run get-papers-list "mRNA vaccine" --file results.csv
 
 
 ## How It Works
  1. The user runs the CLI command with a search query.
    Example: poetry run get-papers-list "cancer immunotherapy"
 
 2. The CLI passes the query and options (like --debug or --file) to the core logic.
 
 3. The program uses Biopython's Entrez module to query the PubMed API and fetch paper metadata.
 
 4. Author affiliations are scanned for pharmaceutical/biotech-related keywords
    (e.g., "inc", "ltd", "biotech", "pharma", "therapeutics", etc.)
 
 5. Papers with at least one non-academic author are collected.
 
 6. The results are output to:
    - The terminal (by default), OR
    - A CSV file if --file <filename> is specified.
 
 
 ## Tools Used
 
 - [Biopython](https://biopython.org/)
 - [Poetry](https://python-poetry.org/)
 - [Typer](https://typer.tiangolo.com/)# pubmed-paper-fetcher
 - pandas for outputting to CSV
 
 ## Built With Help From
 - Git for version control and project tracking
 - Poetry for managing dependencies and creating CLI executables
 - ChatGPT (LLM) to resolve errors & doubts in Python coding 
 - GitHub for hosting and version collaboration
 - Markdown for clean project documentation
 
