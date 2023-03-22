import sys
import re
import pandas as pd
import bibtexparser
from datetime import date
import urllib3
import json

def get_inspirehep_metadata(runtype, label, http):
    url = ''
    if runtype == 'arxiv' and label != 'nan':
        url = 'https://inspirehep.net/api/arxiv/'+ label
    elif runtype == 'doi' and label != 'nan':
        url = 'https://inspirehep.net/api/doi/'+ label
    else:
        return json.loads('{}')

    http_request = http.request('GET', url)
    metadata = json.loads(http_request.data)
    return metadata['metadata']

def get_journal_doi(doi, metadata_doi):
    if doi != 'nan':
        if len(metadata_doi['publication_info']) != 1:
            full_journal_name = ''
            for i in metadata_doi['publication_info']:
                if 'pubinfo_freetext' in i.keys():
                    full_journal_name = i['pubinfo_freetext']
                elif 'journal_title' in i.keys():
                    full_journal_name = i['journal_title']
            return full_journal_name
        elif 'pubinfo_freetext' in metadata_doi['publication_info'][0].keys():
            return metadata_doi['publication_info'][0]['pubinfo_freetext']
        else:
            return metadata_doi['publication_info'][0]['journal_title']
    else:
        return 'nan'

def get_date(runtype, metadata):
    if runtype == 'arxiv' and len(metadata) != 0:
        return metadata['preprint_date']
    elif runtype == 'doi' and len(metadata) != 0:
        if 'imprints' in metadata.keys():
            return metadata['imprints'][0]['date']
        else:
            return 'nan'
    else:
        return 'nan'

def get_inspirehep_date(metadata_arxiv, metadata_doi):
    if len(metadata_arxiv) != 0:
        if 'preprint_date' in metadata_arxiv.keys():
            return metadata_arxiv['preprint_date']
        else:
            return 'nan'
    elif len(metadata_doi) != 0:
        if 'imprints' in metadata_doi.keys():
            return metadata_doi['imprints'][0]['date']
        else:
            return 'nan'
    else:
        return 'nan'

def format_date(date_arxiv, date_doi, journal_name):
    date_vec_arxiv = date_arxiv.split("-")
    date_vec_doi = date_doi.split("-")
    if date_arxiv != 'nan' and date_doi != 'nan':
        # Paper is on arXiv and is in a journal
        if len(date_vec_arxiv) == 3:
            return "Published on arXiv: " + date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), int(date_vec_arxiv[2])).strftime("%d %B %Y") + "; Published in %s" % (journal_name)
        elif len(date_vec_arxiv) == 2:
            return "Published on arXiv: " + date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), 1).strftime("%B %Y") + "; Published in %s" % (journal_name)
    elif date_arxiv != 'nan':
        # Paper is only on arXiv
        if len(date_vec_arxiv) == 3:
            return "Published on arXiv: " + date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), int(date_vec_arxiv[2])).strftime("%d %B %Y") 
        else:
            return "Published on arXiv: " + date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), 1).strftime("%B %Y") 
    elif date_doi != 'nan':
        # Paper is only in a journal
        if len(date_vec_doi) == 3:
            return "Published in %s: " % (journal_name)  + date(int(date_vec_doi[0]), int(date_vec_doi[1]), int(date_vec_doi[2])).strftime("%d %B %Y")
        else:
            return "Published in %s: " % (journal_name) + date(int(date_vec_doi[0]), int(date_vec_doi[1]), 1).strftime("%B %Y")
    else:
        return 'nan'

def get_author_list(metadata_arxiv, metadata_doi):
    if len(metadata_arxiv) != 0:
        if 'authors' in metadata_arxiv.keys():
            author_list = ""
            if len(metadata_arxiv['authors']) == 1:
                return metadata_arxiv['authors'][0]['full_name']
            else:
                for i in metadata_arxiv['authors']:
                    author_list += i['full_name'] + " and "
                return author_list[:-5]
        else:
            return 'nan'
    elif len(metadata_doi) != 0:
        if 'authors' in metadata_doi.keys():
            author_list = ""
            if len(metadata_doi['authors']) == 1:
                return metadata_doi['authors'][0]['full_name']
            else:
                for i in metadata_doi['authors']:
                    author_list += i['full_name'] + " and "
                return author_list[:-5]
        else:
            return 'nan'
    return "nan"

def get_author_url_list(metadata_arxiv, metadata_doi):
    if len(metadata_arxiv) != 0:
        if 'authors' in metadata_arxiv.keys():
            author_list = ""
            if len(metadata_arxiv['authors']) == 1:
                author_name = metadata_arxiv['authors'][0]['full_name']
                if ',' in author_name:
                    author_name = author_name.split(',')[1] + ' ' + author_name.split(',')[0].strip()
                return "<a href=\"%s\"> %s</a>" % (metadata_arxiv['authors'][0]['record']['$ref'].replace('/api',''), author_name)
            else:
                for i in metadata_arxiv['authors']:
                    author_name = i['full_name']
                    if ',' in author_name:
                        author_name = author_name.split(',')[1].strip() + ' ' + author_name.split(',')[0].strip()
                    author_list += "<a href=\"%s\"> %s</a>" % (i['record']['$ref'].replace('/api',''), author_name) + ", "
                return author_list[:-2]
        else:
            return 'nan'
    elif len(metadata_doi) != 0:
        if 'authors' in metadata_doi.keys():
            author_list = ""
            if len(metadata_doi['authors']) == 1:
                author_name = metadata_doi['authors'][0]['full_name']
                if ',' in author_name:
                    author_name = author_name.split(',')[1].strip() + ' ' + author_name.split(',')[0].strip()
                return "<a href=\"%s\"> %s</a>" % (metadata_doi['authors'][0]['record']['$ref'].replace('/api',''), author_name)
            else:
                for i in metadata_doi['authors']:
                    author_name = i['full_name']
                    if ',' in author_name:
                        author_name = author_name.split(',')[1].strip() + ' ' + author_name.split(',')[0].strip()
                    author_list += "<a href=\"%s\"> %s</a>" % (i['record']['$ref'].replace('/api',''), i['full_name']) + ", "
                return author_list[:-2]
        else:
            return 'nan'
    return "nan"

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

    # Sort by Dates
    http = urllib3.PoolManager()
    df["metadata_arxiv"] = df.apply(lambda x: get_inspirehep_metadata('arxiv',str(x['eprint']), http), axis=1)
    df["metadata_doi"] = df.apply(lambda x: get_inspirehep_metadata('doi', str(x['doi']), http), axis=1)
    df["journal_name"] = df.apply(lambda x: get_journal_doi(str(x['doi']), x['metadata_doi']), axis=1)
    df["arxiv_date"] = df.apply(lambda x: get_date('arxiv', x['metadata_arxiv']), axis=1)
    df["doi_date"] = df.apply(lambda x: get_date('doi', x['metadata_doi']), axis=1)
    df["InspireHEP_Date"] = df.apply(lambda x: get_inspirehep_date(x['metadata_arxiv'], x['metadata_doi']), axis=1)
    df["Publish_Info"] = df.apply(lambda x: format_date(str(x['arxiv_date']), str(x['doi_date']), str(x['journal_name'])), axis=1)
    df.sort_values(by=['InspireHEP_Date'], ascending=False, inplace=True)

    # Get author list from metadata and fix formatting
    def fix_author_format(author_str):
        author_list = author_str.split(' and ')
        formatted_author_list = []
        for author in author_list:
            if ',' in author:
                formatted_author_list.append(author.split(',')[1].strip() + ' ' + author.split(',')[0].strip())
        fixed_author = ', '.join(formatted_author_list)
        return fixed_author
  
    df["author_list"] = df.apply(lambda x: get_author_list(x['metadata_arxiv'], x['metadata_doi']), axis=1)
    df["authors_url"] = df.apply(lambda x: get_author_url_list(x['metadata_arxiv'], x['metadata_doi']), axis=1)
    df["authors"] = df["author_list"].apply(lambda x: fix_author_format(x))
    # df["authors_url"] = df["author_url_list"].apply(lambda x: fix_author_format(x))
    
    # Compress dataframe with useful information
    df = df[["ID", "title", "authors", "HEP_Categories", "QIS_Categories", "eprint_url", "doi_url", "HEP_Context", "Methods", "Results_and_Conclusions","HEP_Primary", "HEP_Secondary", "QIS_Primary", "QIS_Secondary", "Publish_Info", "authors_url", "eprint", "doi"]]
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
                    paper[2] = re.sub(r"\\\'z", r"ź", paper[2])

                    if (paper[5] is not None) and (paper[6] is not None):
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">arXiv:%s</a>] [<a href=\"%s\">DOI</a>] <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[1], paper[5], paper[16], paper[6], paper[15], paper[14]))
                    elif paper[5] is not None:
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">arXiv:%s</a>] <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[1], paper[5], paper[16], paper[15], paper[14]))
                    elif paper[6] is not None:
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">DOI</a>] <code>Expand</code><br><em> Authors: %s<br>%s</em> </summary>" % (paper[1], paper[6], paper[15], paper[14]))

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

