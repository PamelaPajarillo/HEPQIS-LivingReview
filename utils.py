import sys
import re
import pandas as pd
from datetime import date
import urllib3
import json
import yaml

def format_pub_info(run, date_arxiv, date_doi, eprint, eprint_url, doi, doi_url):
    date_vec_arxiv = date_arxiv.split("-")
    date_vec_doi = date_doi.split("-")

    str_arxiv = ''
    str_doi = ''

    if date_arxiv != 'nan':
        # Prefix 
        if run == 'md':
            str_arxiv = "\n+ <strong>Posted on <a href=\"%s\">arXiv:%s</a>:</strong> " % (eprint_url, eprint)
        elif run == 'tex':
            str_arxiv = "\item \\textbf{Posted on arXiv:} "
        # Append Date
        if len(date_vec_arxiv) == 3:
            str_arxiv += date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), int(date_vec_arxiv[2])).strftime("%d %B %Y")
        elif len(date_vec_arxiv) == 2:
            str_arxiv += date(int(date_vec_arxiv[0]), int(date_vec_arxiv[1]), 1).strftime("%B %Y")
        else:
            str_arxiv += date(int(date_vec_arxiv[0]), 1, 1).strftime("%Y")
    
    if date_doi != 'nan':
        # Prefix
        if run == 'md':
            str_doi = "\n+ <strong>Published in <a href=\"%s\">%s</a>:</strong> " % (doi_url, doi)
        elif run == 'tex':
            str_doi = "\item \\textbf{Published in %s:} " % (doi)
        # Append Date
        if len(date_vec_doi) == 3:
            str_doi += date(int(date_vec_doi[0]), int(date_vec_doi[1]), int(date_vec_doi[2])).strftime("%d %B %Y")
        elif len(date_vec_doi) == 2:
            str_doi += date(int(date_vec_doi[0]), int(date_vec_doi[1]), 1).strftime("%B %Y")
        else:
            str_doi += date(int(date_vec_doi[0]), 1, 1).strftime("%Y")
            
    if str_arxiv != '' and str_doi != '':
        return str_arxiv + ' ' +  str_doi
    elif str_arxiv != '' and str_doi == '':
        return str_arxiv
    elif str_arxiv == '' and str_doi != '':
        return str_doi
    else:
        return ''

def get_dataframe(yaml_file, categories_hep, categories_qis):
    
    # Load the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(data)

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

    def get_inspirehep_metadata(label, http):
        url = 'https://inspirehep.net/api/literature/' + str(label)
        http_request = http.request('GET', url)
        metadata = json.loads(http_request.data)
        return metadata

    def get_doi_metadata(label, http):
        if label != 'nan':
            url = 'https://inspirehep.net/api/doi/' + str(label)
            http_request = http.request('GET', url)
            metadata = json.loads(http_request.data)
            return metadata['metadata']
        else:
            return json.loads('{}')

    def get_author_list(metadata):
        author_list = ''
        if 'authors' in metadata['metadata'].keys():
            for i in metadata['metadata']['authors']:
                author_list += i['full_name'] + " and "
            author_list = author_list[:-5]
        else:
            author_list =  'nan'
        
        # Fix Formatting
        author_list = author_list.split(' and ')
        formatted_author_list = []
        for author in author_list:
            if ',' in author:
                formatted_author_list.append(author.split(',')[1].strip() + ' ' + author.split(',')[0].strip())
        fixed_author = ', '.join(formatted_author_list)
        return fixed_author

    def get_author_url_list(metadata):
        author_list = ''
        for i in metadata['metadata']['authors']:
            author_name = i['full_name']
            if ',' in author_name:
                author_name = author_name.split(',')[1].strip() + ' ' + author_name.split(',')[0].strip()
            author_list += "<a href=\"%s\"> %s</a>" % (i['record']['$ref'].replace('/api',''), author_name) + ", "
        return author_list[:-2]
    
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
    
    def get_bibtex(metadata, http):
        url = metadata["links"]["bibtex"]
        bibtex_request = http.request('GET', url)
        return bibtex_request.data.decode('utf-8')
            
    # Read InspireHEP entry
    http = urllib3.PoolManager()
    df["metadata"] = df.apply(lambda x: get_inspirehep_metadata(x["ID"], http), axis=1)
    df["inspirehep_url"] = "https://inspirehep.net/literature/" + df["ID"]
    df["title"] = df["metadata"].apply(lambda x: x['metadata']['titles'][0]['title'])
    df["authors"] = df["metadata"].apply(lambda x: get_author_list(x))
    df["authors_url"] = df["metadata"].apply(lambda x: get_author_url_list(x))
    df["eprint"] = df["metadata"].apply(lambda x: x['metadata']['arxiv_eprints'][0]['value'] if 'arxiv_eprints' in x['metadata'].keys() else 'nan')
    df["doi"] = df["metadata"].apply(lambda x: x['metadata']['dois'][0]['value'] if 'dois' in x['metadata'].keys() else 'nan')
    df["eprint_url"] = df["eprint"].apply(lambda x: "https://arxiv.org/abs/" + x if x != 'nan' else 'nan')
    df["doi_url"] = df["doi"].apply(lambda x: "https://doi.org/" + x if x != 'nan' else 'nan')
    df["arxiv_date"] = df["metadata"].apply(lambda x: x['metadata']['preprint_date'] if 'preprint_date' in x['metadata'].keys() else 'nan')
    df["doi_date"] = df["metadata"].apply(lambda x: x['metadata']['imprints'][0]['date'] if 'imprints' in x['metadata'].keys() else (x['metadata']['publication_info'][0]['year'] if 'publication_info' in x['metadata'].keys() and 'journal_title' in x['metadata']['publication_info'][0] else 'nan'))
    df["metadata_doi"] = df.apply(lambda x: get_doi_metadata(x['doi'], http), axis=1)
    df["journal_name"] = df.apply(lambda x: get_journal_doi(x['doi'], x['metadata_doi']), axis=1)
    df["Publish_Info_md"] = df.apply(lambda x: format_pub_info('md', str(x['arxiv_date']), str(x['doi_date']), str(x['eprint']), str(x['eprint_url']), str(x['journal_name']), str(x['doi_url'])), axis=1)
    df["Publish_Info_latex"] = df.apply(lambda x: format_pub_info('tex', str(x['arxiv_date']), str(x['doi_date']), str(x['eprint']), str(x['eprint_url']), str(x['journal_name']), str(x['doi_url'])), axis=1)
    df["bibtex_tag"] = df["metadata"].apply(lambda x: x['metadata']['texkeys'][0])
    df["bibtex"] = df["metadata"].apply(lambda x: get_bibtex(x, http))
    
    # Compress dataframe with useful information
    df = df[["ID", "title", "authors", "authors_url", "eprint", "doi", "eprint_url", "doi_url", "inspirehep_url", "Publish_Info_md", "Publish_Info_latex",
             "HEP_Primary", "HEP_Secondary", "QIS_Primary", "QIS_Secondary", "HEP_Context", "QIS_Methods", "Results_and_Conclusions", "bibtex_tag", "bibtex"]]
    return df

def get_categories(yaml_file):
    # Read YAML file
    df_categories = {}
    list_categories = {}
    with open(yaml_file, 'r') as file:
        data = yaml.load_all(file, Loader=yaml.FullLoader)

        # Convert the YAML data to a Pandas DataFrame
        for idx, d in enumerate(data):
            df_categories[idx] = pd.DataFrame.from_dict(d)
            list_categories[idx] = df_categories[idx]['Category'].tolist()
    
    return df_categories[0], list_categories[0], df_categories[1], list_categories[1]

def list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_RUN, subcategories, df_csv, run_type):
    for category in subcategories:
        if (category != 'Reviews') and (category != 'Whitepapers'):
            OUTPUT_FILE_MAIN.write("* [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-) [![Descriptions-%s](https://img.shields.io/badge/Link_to-Description-0066CC)](/BY_%s/CATEGORIES.md#%s-) **%s**  \n" % (category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower(), category))
            OUTPUT_FILE_RUN.write("## **%s** [![Papers-%s](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_%s/README.md#%s-)\n" % (category, category.replace(" ", "-").lower(), run_type, category.replace(" ", "-").lower()))
            if str(df_csv.loc[df_csv['Category'] == category]['Description'].values[0]) != '':
                OUTPUT_FILE_RUN.write("%s\n\n" % df_csv.loc[df_csv['Category'] == category]['Description'].values[0])
    OUTPUT_FILE_MAIN.write("\n\n")
    OUTPUT_FILE_RUN.write("\n\n")
    
def write_papers_to_md(df, output_file, categories_main, categories_sub, main_type, sub_type):

    # Indices of table to check for LaTeX formatting and change to Markdown
    text_check = [15, 16, 17]

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

                    if (str(paper[4]) != 'nan') and (str(paper[5]) != 'nan'):
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">arXiv</a>] [<a href=\"%s\">DOI</a>] [<a href=\"%s\">INSPIRE</a>] <code>Expand</code> </summary>" % (paper[1], paper[6], paper[7], paper[8]))
                    elif str(paper[4]) != 'nan':
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">arXiv</a>] [<a href=\"%s\">INSPIRE</a>] <code>Expand</code><br> </summary>" % (paper[1], paper[6], paper[8]))
                    elif str(paper[5])!= 'nan':
                        output_file.write("<summary> <b>%s</b> [<a href=\"%s\">DOI</a>] [<a href=\"%s\">INSPIRE</a>] <code>Expand</code><br> </summary>" % (paper[1], paper[7], paper[8]))

                    # Reformat LaTeX to Markdown
                    for i in text_check:
                        if paper[i] is not None:
                            paper[i] = re.sub(r"(\\textbf{)(.*?)\}", r"<strong>\2</strong>", paper[i])
                            paper[i] = re.sub(r"(\\textit{)(.*?)\}", r"<em>\2</em>", paper[i])
                            paper[i] = re.sub(r"(\\underline{)(.*?)\}", r"<u>\2</u>", paper[i])
                    
                    # Write brief description and summary of paper
                    output_file.write("\n\n+ <strong>Authors:</strong> %s%s" % (paper[3], paper[9]))
                    if (str(paper[15]) != ''):
                        output_file.write("\n+ <strong>HEP Context:</strong> %s" % (paper[15].strip('\"')))
                    if (str(paper[16]) != ''):
                        output_file.write("\n+ <strong>QIS Methods:</strong> %s" % (paper[16].strip('\"')))
                    if (str(paper[17]) != ''):
                        output_file.write("\n+ <strong>Results and Conclusions:</strong> %s" % (paper[17].strip('\"')))
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
            if str(df_csv.loc[df_csv['Category'] == category]['Description'].values[0]) != '':
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

                    # Fix Author Names with Special Characters
                    paper[2] = re.sub(r"ã", r"\~{a}", paper[2])
                    paper[2] = re.sub(r"á", r"\'{a}", paper[2])
                    paper[2] = re.sub(r"é", r"\`{e}", paper[2])
                    paper[2] = re.sub(r"é", r"\'{e}", paper[2])
                    paper[2] = re.sub(r"í", r"\'{i}", paper[2])
                    paper[2] = re.sub(r"ö", r"\"{o}", paper[2])
                    paper[2] = re.sub(r"ó", r"\'{o}", paper[2])
                    paper[2] = re.sub(r"ñ", r"\~{n}", paper[2])
                    paper[2] = re.sub(r"ü", r"\"{u}", paper[2])
                    paper[2] = re.sub(r"ú", r"\'{u}", paper[2])
                    paper[2] = re.sub(r"ź", r"\'{z}", paper[2])

                    file.write("\paragraph{%s~\cite{%s}}\n" % (paper[1], paper[18]))
                    file.write("\\begin{itemize}\n")
                    file.write("\t\item \\textbf{Authors:} %s\n\t%s\n" % (paper[2], paper[10]))
                    if (str(paper[15]) != ''):
                        file.write("\t\item \\textbf{HEP Context:} %s\n" % (paper[15]))
                    
                    if (str(paper[16]) != ''):
                        file.write("\t\item \\textbf{QIS Methods:} %s\n\t" % (paper[16]))

                    if (str(paper[17]) != ''):
                        file.write("\t\item \\textbf{Results and Conclusions:} %s\n" % (paper[17]))
                    
                    file.write("\end{itemize}\n\n")
                file.write("\n\n")

def write_bib(df, OUTPUT_FILE_BIB):
    for paper in df.values.tolist():
        OUTPUT_FILE_BIB.write("%s\n" % paper[19])