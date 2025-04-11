from Bio import Entrez
import pandas as pd
import re
from typing import List, Optional

Entrez.email = "danitha200204@gmail.com"

def fetch_and_filter_papers(query: str, debug: bool = False, file: Optional[str] = None):
    search = Entrez.esearch(db="pubmed", term=query, retmax=10)
    record = Entrez.read(search)
    ids = record["IdList"]
    
    papers = []
    
    for pid in ids:
        fetch = Entrez.efetch(db="pubmed", id=pid, rettype="medline", retmode="text")
        data = fetch.read()
        
        title_match = re.search(r"TI  - (.+)", data)
        date_match = re.search(r"DP  - (.+)", data)
        author_matches = re.findall(r"FAU - (.+)", data)
        affil_matches = re.findall(r"AD  - (.+)", data)
        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", data)
        
        non_academic_authors = []
        company_affiliations = []

        for affil in affil_matches:
            if any(word in affil.lower() for word in ["inc", "ltd", "pharma", "therapeutics", "biotech"]):
                company_affiliations.append(affil)
                match = re.search(r"(.+?),", affil)
                if match:
                    non_academic_authors.append(match.group(1).strip())

        papers.append({
            "PubmedID": pid,
            "Title": title_match.group(1) if title_match else "",
            "Publication Date": date_match.group(1) if date_match else "",
            "Non-academic Author(s)": "; ".join(set(non_academic_authors)),
            "Company Affiliation(s)": "; ".join(set(company_affiliations)),
            "Corresponding Author Email": email_match.group(0) if email_match else ""
        })

    df = pd.DataFrame(papers)

    if file:
        df.to_csv(file, index=False)
        print(f"Saved to {file}")
    else:
        print(df.to_string(index=False))