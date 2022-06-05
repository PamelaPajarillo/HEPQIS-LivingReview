from utils import *

# Output Markdown File
OUTPUT_FILE = open("README.md","w")

# Title
OUTPUT_FILE.write("#  **A Living Review of Quantum Information Science in Particle Physics**\n\n")

# Abstract
OUTPUT_FILE.write("*Inspired by \"A Living Review of Machine Learning for Particle Physics\", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*\n\n")

# Intro
OUTPUT_FILE.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics.  \n\n")

# Input Files
CSV_FILE = 'HEPQIS.csv'
BIB_FILE = 'HEPQIS.bib'
TXT_FILE = 'CATEGORIES.txt'

# Get dataframe of BibTeX and CSV
df = get_dataframe(BIB_FILE, CSV_FILE)

# Parse CATEGORIES.txt
categories = get_categories(TXT_FILE)
            
# Get Categories and Subcategories
for entry in categories:
    # Parse main category and subcategory
    maincategory = entry.split(", ")[0]
    subcategories = entry.split(", ")[1:]

    # Print Title of Main Category
    OUTPUT_FILE.write("##  **%s**\n\n" % maincategory.strip('\''))

    # Retrieve papers by checking for substring in categories
    df_cat = df.loc[df['Categories'].str.contains(maincategory, case=False)]
    cat_papers = df_cat.values.tolist()

    # Formatting and write to file
    for paper in cat_papers:
        OUTPUT_FILE.write("<details>\n")
        if (paper[4] is not None) and (paper[5] is not None):
            OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>]</summary>" % (paper[4], paper[1], paper[5]))
        elif paper[4] is not None:
            OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[4], paper[1]))
        elif paper[5] is not None:
            OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[5], paper[1]))

        OUTPUT_FILE.write("%s\n" % paper[3].strip('\"'))
        OUTPUT_FILE.write("</details>\n")
    
    OUTPUT_FILE.write("\n\n")
    for subentry in subcategories:
        OUTPUT_FILE.write("###  **%s**\n\n" % subentry.strip('\''))

        # Retrieve papers by checking for substring in categories
        df_subcat = df.loc[df['Categories'].str.contains(subentry, case=False)]
        cat_papers = df_subcat.values.tolist()
        # Formatting and write to file
        for paper in cat_papers:
            OUTPUT_FILE.write("<details>\n")
            if (paper[4] is not None) and (paper[5] is not None):
                OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>]</summary>" % (paper[4], paper[1], paper[5]))
            elif paper[4] is not None:
                OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[4], paper[1]))
            elif paper[5] is not None:
                OUTPUT_FILE.write("<summary> <a href=\"%s\"> %s</a></summary>" % (paper[5], paper[1]))

            OUTPUT_FILE.write("%s\n" % paper[3].strip('\"'))
            OUTPUT_FILE.write("</details>\n")
        OUTPUT_FILE.write("\n\n")
