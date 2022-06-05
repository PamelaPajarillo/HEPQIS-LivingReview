import pandas as pd
import bibtexparser

def get_dataframe(bib_file, csv_file):

    # Read CSV and convert to dataframe
    csv_entries = pd.read_csv(csv_file)
    df_csv = pd.DataFrame(csv_entries)

    # Read BibTeX and convert to dataframe
    with open(bib_file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    df_bib = pd.DataFrame(bib_database.entries)
    df_bib['title'] = df_bib['title'].str.strip('{}')
    df = df_csv.merge(df_bib, on='ID')

    def fetch_eprint_url(entry_str,check):
        # Look at eprint
        if not check:
            return 'https://arxiv.org/abs/' + str(entry_str)

    def fetch_doi_url(entry_str,check):
        # Look at eprint
        if not check:
            return 'https://doi.org/'+ str(entry_str)

    # Check and Make URLs 
    df["eprint_check"] = df["eprint"].isnull()
    df["doi_check"] = df["doi"].isnull()
    df["eprint_url"] = df.apply(lambda x: fetch_eprint_url(x.eprint, x.eprint_check), axis = 1)
    df["doi_url"] = df.apply(lambda x: fetch_doi_url(x.doi, x.doi_check), axis = 1)

    # Compress dataframe with useful information
    df = df[["ID", "title", "Categories", "Description", "eprint_url", "doi_url"]]

    return df

def get_categories(txt_file):
    categories = []
    with open(txt_file) as cat_file:
        categories = cat_file.read().splitlines() 
    return categories