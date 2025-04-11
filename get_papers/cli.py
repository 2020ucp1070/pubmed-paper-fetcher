import typer
from get_papers.core import fetch_and_filter_papers
from typing import Optional

app = typer.Typer()

@app.command()
def main(
    query: str,
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Output CSV filename")
):
    fetch_and_filter_papers(query, debug, file)

    # if __name__ == "__main__":
    # app()