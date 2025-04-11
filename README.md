# PubMed Paper Fetcher

A Python CLI tool to fetch PubMed papers matching a search query and filter out non-academic authors affiliated with pharmaceutical or biotech companies.

## Features

- Fetches papers using PubMed API (via Biopython)
- Filters authors based on affiliations
- Saves results to CSV or prints to console
- CLI with options for debug and output file
- Modular structure
- Typed Python
- Poetry for dependency management

## Installation

```bash
git clone https://github.com/yourusername/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer therapy"
```

Options:
- `-d` or `--debug`: Show debug output
- `-f <filename>` or `--file <filename>`: Save to CSV file
- `-h` or `--help`: Show help message

## Tools Used

- [Biopython](https://biopython.org/)
- [Poetry](https://python-poetry.org/)
- [Typer](https://typer.tiangolo.com/)# pubmed-paper-fetcher
