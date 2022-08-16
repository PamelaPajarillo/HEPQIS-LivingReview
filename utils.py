import sys
import re
import pandas as pd
import bibtexparser

def get_dataframe(bib_file, csv_file, categories_hep, categories_qis):

    # Read CSV and convert to dataframe
    csv_entries = pd.read_csv(csv_file)
    df_csv = pd.DataFrame(csv_entries)

    # Read BibTeX and convert to dataframe
    with open(bib_file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    df_bib = pd.DataFrame(bib_database.entries)
    df_bib['title'] = df_bib['title'].str.strip('{}')
    df = df_csv.merge(df_bib, on='ID')

    # Check to make sure all papers are in the CSV and BIB files
    check_bib = df_bib[~df_bib['ID'].isin(df_csv['ID'])]
    check_csv = df_csv[~df_csv['ID'].isin(df_bib['ID'])]
    if len(check_bib) > 0:
        print("The following papers are in the BIB file but not the CSV file:")
        print(check_bib[['ID']])
        sys.exit(1)
    if len(check_csv) > 0:
        print("The following papers are in the CSV file but not the BIB file:")
        print(check_csv[['ID']])
        sys.exit(1)

    # Check to make sure each paper has at least one HEP category and at least one QIS category
    df["HEP_Check"] = df["Categories"].str.contains('|'.join(categories_hep), case=False)
    df["QIS_Check"] = df["Categories"].str.contains('|'.join(categories_qis), case=False)
    check_hep = df[~df["HEP_Check"]]
    check_qis = df[~df["QIS_Check"]]
    if len(check_hep) > 0:
        print("The following papers do not have at least one HEP category:")
        print(check_hep[[['ID']]])
        sys.exit(1)
    if len(check_qis) > 0:
        print("The following papers do not have at least one QIS category:")
        print(check_qis[[['ID']]])
        sys.exit(1)

    # Check and Make URLs 
    def fetch_eprint_url(entry_str,check):
        # Look at eprint
        if not check:
            return 'https://arxiv.org/abs/' + str(entry_str)

    def fetch_doi_url(entry_str,check):
        # Look at eprint
        if not check:
            return 'https://doi.org/'+ str(entry_str)

    df["eprint_check"] = df["eprint"].isnull()
    df["doi_check"] = df["doi"].isnull()
    df["eprint_url"] = df.apply(lambda x: fetch_eprint_url(x.eprint, x.eprint_check), axis = 1)
    df["doi_url"] = df.apply(lambda x: fetch_doi_url(x.doi, x.doi_check), axis = 1)

    # Compress dataframe with useful information
    df = df[["ID", "title", "Categories", "Description", "eprint_url", "doi_url", "HEP Context", "Methods" , "Results and Conclusions", "HEP_Check", "QIS_Check"]]

    return df

def get_categories(csv_file):
    categories = []
    # Read CSV and convert to dataframe
    csv_entries = pd.read_csv(csv_file)
    df_csv = pd.DataFrame(csv_entries)
    categories = df_csv['Category'].tolist()
    
    return categories, df_csv

def list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_RUN, subcategories, df_csv, run_type):
    for category in subcategories:
        if (category != 'Reviews') and (category != 'Whitepapers') and (category != 'Uncategorized by %s - TEMPORARY' % run_type):
            OUTPUT_FILE_MAIN.write("* [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-) [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-) **%s**  \n" % (category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category))
            OUTPUT_FILE_RUN.write("## **%s** [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-)\n" % (category, category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower()))
            OUTPUT_FILE_RUN.write("%s\n\n" % df_csv.loc[df_csv['Category'] == category]['Description'].values[0])
    OUTPUT_FILE_MAIN.write("\n\n")
    OUTPUT_FILE_RUN.write("\n\n")
    
def write_papers_to_md(output_file, categories, df, run_type):

    # Indices of table to check for LaTeX formatting and change to Markdown
    text_check = [3, 6, 7, 8]

    # Get Categories
    for entry in categories:

        # Print Title of Main Category
        if (entry != 'Reviews') and (entry != 'Whitepapers') and (entry != 'Uncategorized by %s - TEMPORARY' % run_type):
            output_file.write("##  **%s** [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-)\n\n" % (entry, entry.replace(" ", "-").lower(), run_type, entry.replace(" ", "-").lower()))
        else:
            output_file.write("##  **%s**\n\n" % (entry))

        # Retrieve papers by checking for substring in categories
        df_cat = df.loc[df['Categories'].str.contains(entry, case=False)]
        cat_papers = df_cat.values.tolist()
        
        # Formatting and write to file
        for paper in cat_papers:
            output_file.write("<details>\n")
            if (paper[4] is not None) and (paper[5] is not None):
                output_file.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>] <code>Expand</code> </summary>" % (paper[4], paper[1], paper[5]))
            elif paper[4] is not None:
                output_file.write("<summary> <a href=\"%s\"> %s</a> <code>Expand</code> </summary>" % (paper[4], paper[1]))
            elif paper[5] is not None:
                output_file.write("<summary> <a href=\"%s\"> %s</a> <code>Expand</code> </summary>" % (paper[5], paper[1]))

            # Reformat LaTeX to Markdown
            for i in text_check:
                paper[i] = re.sub(r"(\\textbf{)(.*?)\}", r"<strong>\2</strong>", paper[i])
                paper[i] = re.sub(r"(\\textit{)(.*?)\}", r"<em>\2</em>", paper[i])
                paper[i] = re.sub(r"(\\underline{)(.*?)\}", r"<u>\2</u>", paper[i])
            
            # Write brief description and summary of paper
            output_file.write("\n\n+ <em><strong>HEP Context:</strong></em> <em>%s</em>\n+ <em><strong>Methods:</strong></em> <em>%s</em>\n+ <em><strong>Results and Conclusions:</strong></em> <em>%s</em>" % (paper[6].strip('\"'), paper[7].strip('\"'), paper[8].strip('\"')))
            output_file.write("\n\n%s\n\n" % paper[3].strip('\"'))
            output_file.write("</details>\n\n")
        
        output_file.write("\n\n")

def write_papers_to_tex(list_file, brief_file, detail_file, categories, df, df_csv):
    # Get Categories and Subcategories
    for entry in categories:
        # Print Title of Main Category
        list_file.write("\section{%s}\n\n" % entry)
        brief_file.write("\section{%s}\n\n" % entry)
        detail_file.write("\section{%s}\n\n" % entry)

        # Print Description of Main Category
        if str(entry) in set(df_csv['Category']):
            detail_file.write("\\textit{%s}\n\n" % df_csv.loc[df_csv['Category'] == entry]['Description'].values[0])
        
        # Retrieve papers by checking for substring in categories
        df_cat = df.loc[df['Categories'].str.contains(entry, case=False)]
        cat_papers = df_cat.values.tolist()

        # Formatting and write to file
        if len(cat_papers) != 0:
            list_file.write("\\begin{itemize}\n")
        for paper in cat_papers:
            list_file.write("   \item %s~\cite{%s}\n" % (paper[1], paper[0]))
            brief_file.write("\subsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
            brief_file.write("\\begin{itemize}\n\t\item \\textbf{HEP Context: }%s\n\t\item \\textbf{Methods: }%s\n\t\item \\textbf{Results and Conclusions: }%s\n\end{itemize}" % (paper[6], paper[7], paper[8]))
            detail_file.write("\subsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
            detail_file.write("%s\n" % (paper[3]))
    
        if len(cat_papers) != 0:
            list_file.write("\end{itemize}\n")
        list_file.write("\n\n")
        brief_file.write("\n\n")
        detail_file.write("\n\n")