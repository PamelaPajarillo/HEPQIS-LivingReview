import sys
import re
import pandas as pd
import bibtexparser
import requests
from datetime import date

def get_inspirehep_date(arxiv, doi):
    url = ''
    if arxiv != 'nan':
        url = 'https://labs.inspirehep.net/api/arxiv/'+arxiv
    else:
        url = 'https://labs.inspirehep.net/api/doi/'+doi
    
    r = requests.get(url)
    if 'metadata' in r.json():
        metadata = r.json()['metadata']
        if arxiv != 'nan':
            return metadata['preprint_date']
        else:
            return metadata['imprints'][0]['date']
    
def format_date(inspirehep_date, arxiv):
    date_vec = inspirehep_date.split("-")
    if len(date_vec) == 3:
        if arxiv != 'nan':
            return "Published on arXiv: " + date(int(date_vec[0]), int(date_vec[1]), int(date_vec[2])).strftime("%d %B %Y") 
        else:
            return "Published in Journal: " + date(int(date_vec[0]), int(date_vec[1]), int(date_vec[2])).strftime("%d %B %Y")
    else:
        if arxiv != 'nan':
            return "Published on arXiv: " + date(int(date_vec[0]), int(date_vec[1]), 1).strftime("%B %Y") 
        else:
            return "Published in Journal: " + date(int(date_vec[0]), int(date_vec[1]), 1).strftime("%B %Y")

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

    # Check to make sure each paper's categories are valid
    def check_categories(categories, category_list):
        for category in categories.split('\'')[1::2]:
            if category not in category_list:
                return False
        return True
    
    # Check to make sure each paper has at least one valid HEP category and at least one valid QIS category
    exit_condition = False
    df["HEP_Check"] = df["HEP_Categories"].str.contains('|'.join(categories_hep), case=False)
    df["QIS_Check"] = df["QIS_Categories"].str.contains('|'.join(categories_qis), case=False)
    df["HEP_Category_Check"] = df["HEP_Categories"].apply(lambda x: check_categories(x, categories_hep))
    df["QIS_Category_Check"] = df["QIS_Categories"].apply(lambda x: check_categories(x, categories_qis))
    check_hep = df[~df["HEP_Check"] | ~df["HEP_Category_Check"]]
    check_qis = df[~df["QIS_Check"]| ~df["QIS_Category_Check"]]
    if len(check_hep) > 0:
        print("The following papers have invalid HEP categories:")
        print(check_hep[['ID']])
        exit_condition = True
    if len(check_qis) > 0:
        print("The following papers have invalid QIS categories:")
        print(check_qis[['ID']])
        exit_condition = True

    # Stop if there are any invalid categories
    if exit_condition:
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
    
    # Parse out primary category and secondary categories
    def sort_categories(categories, primary = False):
        if primary:
            return categories.split('; ')[0]
        else:
            return categories.split('; ')[1] if len(categories.split('; ')) > 1 else 'N/A'
    
    df["HEP_Primary"] = df["HEP_Categories"].apply(lambda x: sort_categories(x, primary = True))
    df["HEP_Secondary"] = df["HEP_Categories"].apply(lambda x: sort_categories(x, primary = False))
    df["QIS_Primary"] = df["QIS_Categories"].apply(lambda x: sort_categories(x, primary = True))
    df["QIS_Secondary"] = df["QIS_Categories"].apply(lambda x: sort_categories(x, primary = False))

    # Fix author format
    def fix_author_format(author_str):
        author_list = author_str.split(' and ')
        formatted_author_list = []
        for author in author_list:
            if ',' in author:
                formatted_author_list.append(author.split(',')[1].strip() + ' ' + author.split(',')[0].strip())
            elif 'others' in author:
                formatted_author_list.append("et al.")        
        fixed_author = ', '.join(formatted_author_list)
        fixed_author = fixed_author.replace(', et al.', ' et al.')
        return fixed_author
    
    df["authors"] = df["author"].apply(lambda x: fix_author_format(x))
    
    # Sort by Dates
    df["InspireHEP_Date"] = df.apply(lambda x: get_inspirehep_date(str(x['eprint']), str(x['doi'])), axis=1)
    df["Date"] = df.apply(lambda x: format_date(str(x['InspireHEP_Date']), str(x['eprint'])), axis=1)
    df["InspireHEP_Date"] = pd.to_datetime(df['InspireHEP_Date'])
    df.sort_values(by='InspireHEP_Date', ascending=False, inplace=True)
    
    # Compress dataframe with useful information
    df = df[["ID", "title", "authors", "HEP_Categories", "QIS_Categories", "eprint_url", "doi_url", "HEP_Context", "Methods", "Results_and_Conclusions","HEP_Primary", "HEP_Secondary", "QIS_Primary", "QIS_Secondary", "Date"]]
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
        if (category != 'Reviews') and (category != 'Whitepapers'):
            OUTPUT_FILE_MAIN.write("* [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-) [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-) **%s**  \n" % (category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category))
            OUTPUT_FILE_RUN.write("## **%s** [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-)\n" % (category, category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower()))
            OUTPUT_FILE_RUN.write("%s\n\n" % df_csv.loc[df_csv['Category'] == category]['Description'].values[0])
    OUTPUT_FILE_MAIN.write("\n\n")
    OUTPUT_FILE_RUN.write("\n\n")
    
def write_papers_to_md(df, output_file, categories_main, categories_sub, main_type, sub_type):

    # Indices of table to check for LaTeX formatting and change to Markdown
    text_check = [7, 8, 9]

    # Get Categories
    for main_category in categories_main:

        # Print Title of Main Category
        if (main_category != 'Reviews') and (main_category != 'Whitepapers'):
            output_file.write("##  **%s** [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-)\n\n" % (main_category, main_category.replace(" ", "-").lower(), main_type, main_category.replace(" ", "-").lower()))
        elif (main_category == 'Reviews'):
            output_file.write("## **Reviews and Whitepapers**\n\n")

        # Retrieve papers by checking for substring in categories
        df_main = df.loc[df['%s_Primary' % main_type].str.contains(main_category, case=False)]
        
        for sub_category in categories_sub:
            
            # Retrieve papers by checking for substring in categories
            df_sub = df_main.loc[df['%s_Primary' % sub_type].str.contains(sub_category, case=False)]
            papers = df_sub.values.tolist()

            if len(papers) > 0:
                # Print Title of Main Category
                if (sub_category != 'Reviews') and (sub_category != 'Whitepapers'):
                    output_file.write("###  **%s** [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-)\n\n" % (sub_category, sub_category.replace(" ", "-").lower(), main_type, main_category.replace(" ", "-").lower()))
                else:
                    output_file.write("###  **%s**\n\n" % (sub_category))

                # Formatting and write to file
                for paper in papers:

                    output_file.write("<details>\n")

                    # Fix Author Names with Special Characters
                    paper[2] = re.sub(r"\\~a", r"ã", paper[2])
                    paper[2] = re.sub(r"\\'a", r"á", paper[2])
                    paper[2] = re.sub(r"\\'e", r"é", paper[2])
                    paper[2] = re.sub(r"\\`e", r"è", paper[2])
                    paper[2] = re.sub(r"\\'\\i\{\}", r"í", paper[2])
                    paper[2] = re.sub(r"\\\"o", r"ö", paper[2])
                    paper[2] = re.sub(r"\\\'o", r"ó", paper[2])
                    paper[2] = re.sub(r"\\~n", r"ñ", paper[2])
                    paper[2] = re.sub(r"\\\"u", r"ü", paper[2])
                    paper[2] = re.sub(r"\\\'u", r"ú", paper[2])

                    if (paper[5] is not None) and (paper[6] is not None):
                        output_file.write("<summary> <a href=\"%s\"> %s</a> [<a href=\"%s\">DOI</a>] <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[5], paper[1], paper[6], paper[2], paper[14]))
                    elif paper[5] is not None:
                        output_file.write("<summary> <a href=\"%s\"> %s</a> <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[5], paper[1], paper[2], paper[14]))
                    elif paper[6] is not None:
                        output_file.write("<summary> <a href=\"%s\"> %s</a> <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[6], paper[1], paper[2], paper[14]))

                    # Reformat LaTeX to Markdown
                    for i in text_check:
                        paper[i] = re.sub(r"(\\textbf{)(.*?)\}", r"<strong>\2</strong>", paper[i])
                        paper[i] = re.sub(r"(\\textit{)(.*?)\}", r"<em>\2</em>", paper[i])
                        paper[i] = re.sub(r"(\\underline{)(.*?)\}", r"<u>\2</u>", paper[i])
                    
                    # Write brief description and summary of paper
                    output_file.write("\n\n+ <em><strong>HEP Context:</strong></em> <em>%s</em>\n+ <em><strong>Methods:</strong></em> <em>%s</em>\n+ <em><strong>Results and Conclusions:</strong></em> <em>%s</em>" % (paper[7].strip('\"'), paper[8].strip('\"'), paper[9].strip('\"')))
                    output_file.write("</details>\n\n")
                
                output_file.write("\n\n")

def write_categories_to_tex(OUTPUT_FILE_MAIN, subcategories, df_csv, run_type):
    if run_type == 'HEP':
        OUTPUT_FILE_MAIN.write("\subsection{High Energy Physics Categories}  \n")
    elif run_type == 'QIS':
        OUTPUT_FILE_MAIN.write("\subsection{Quantum Information Science Categories}  \n")
    
    for category in subcategories:
        if (category != 'Reviews') and (category != 'Whitepapers'):
            OUTPUT_FILE_MAIN.write("\subsubsection{%s}  \n" % (category))
            OUTPUT_FILE_MAIN.write("%s\n\n" % df_csv.loc[df_csv['Category'] == category]['Description'].values[0])

    OUTPUT_FILE_MAIN.write("\n\n")

def write_papers_to_tex(df, file, categories_main, categories_sub, main_type, sub_type):
    # Get Categories and Subcategories
    if main_type == 'HEP':
        file.write("\section{High Energy Physics in Quantum Information Science}\n\n")
    elif main_type == 'QIS':
        file.write("\section{Quantum Information Science in High Energy Physics}\n\n")
    
    for main_category in categories_main:
        # Print Title of Main Category
        if (main_category != 'Reviews') and (main_category != 'Whitepapers'):
            file.write("\subsection{%s}\n\n" % main_category)
        elif (main_category == 'Reviews'):
            file.write("\subsection{Reviews and Whitepapers}\n\n")

        # Retrieve papers by checking for substring in categories
        df_main = df.loc[df['%s_Primary' % main_type].str.contains(main_category, case=False)]
        
        for sub_category in categories_sub:
            
            # Retrieve papers by checking for substring in categories
            df_sub = df_main.loc[df['%s_Primary' % sub_type].str.contains(sub_category, case=False)]
            papers = df_sub.values.tolist()

            if len(papers) > 0:
                
                file.write("\subsubsection{%s}\n\n" % sub_category)

                # Formatting and write to file
                for paper in papers:

                    file.write("\paragraph{%s~\cite{%s}}\n\n" % (paper[1], paper[0]))
                    file.write("\\textit{Authors: %s; %s} \n\n\\begin{itemize}\n\t\item \\textbf{HEP Context: }%s\n\t\item \\textbf{Methods: }%s\n\t\item \\textbf{Results and Conclusions: }%s\n\end{itemize}" % (paper[2], paper[14], paper[7], paper[8], paper[9]))
            
                file.write("\n\n")

