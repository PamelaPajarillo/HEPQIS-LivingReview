from utils import *

# Output Markdown File
out_md = open("README.md","w")

# Title
out_md.write("#  **A Living Review of Quantum Information Science in Particle Physics**\n\n")

# Abstract
out_md.write("*Inspired by \"A Living Review of Machine Learning for Particle Physics\", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*\n\n")

# Intro
out_md.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics.  \n\n")

# Input Files
csv_file = 'HEPQIS.csv'
bib_file = 'HEPQIS.bib'
txt_file = 'CATEGORIES.txt'

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

# Parse CATEGORIES.txt
categories = []
with open(txt_file) as cat_file:
    categories = cat_file.read().splitlines() 
            
# Get Categories and Subcategories
for entry in categories:
    # Parse main category and subcategory
    maincategory = entry.split(", ")[0]
    subcategories = entry.split(", ")[1:]    

    # Print Title of Main Category
    out_md.write("##  **%s**\n\n" % maincategory.strip('\''))

    # Retrieve papers by checking for substring in categories
    df_cat = df.loc[df['Categories'].str.contains(maincategory, case=False)]
    cat_papers = df_cat.values.tolist()

    # Formatting and write to file
    for paper in cat_papers:
        out_md.write("<details>\n")
        if (paper[4] is not None) and (paper[5] is not None):
            out_md.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>]</summary>" % (paper[4], paper[1], paper[5]))
        elif (paper[4] is not None):
            out_md.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[4], paper[1]))
        elif (paper[5] is not None):
            out_md.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[5], paper[1]))

        out_md.write("%s\n" % paper[3].strip('\"'))
        out_md.write("</details>\n")
    
    out_md.write("\n\n")
    for subentry in subcategories:
        out_md.write("###  **%s**\n\n" % subentry.strip('\''))

        # Retrieve papers by checking for substring in categories
        df_subcat = df.loc[df['Categories'].str.contains(subentry, case=False)]
        cat_papers = df_subcat.values.tolist()
        # Formatting and write to file
        for paper in cat_papers:
            out_md.write("<details>\n")
            if (paper[4] is not None) and (paper[5] is not None):
                out_md.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>]</summary>" % (paper[4], paper[1], paper[5]))
            elif (paper[4] is not None):
                out_md.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[4], paper[1]))
            elif (paper[5] is not None):
                out_md.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[5], paper[1]))

            out_md.write("%s\n" % paper[3].strip('\"'))
            out_md.write("</details>\n")
        out_md.write("\n")
