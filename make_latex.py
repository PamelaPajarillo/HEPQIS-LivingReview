from utils import *

# Output Markdown File
OUTPUT_FILE_LIST = open("HEPQIS_LIST.tex","w")
OUTPUT_FILE_BRIEF = open("HEPQIS_BRIEF.tex","w")
OUTPUT_FILE_DETAIL = open("HEPQIS_DETAIL.tex","w")

# Input Files
CSV_FILE = 'HEPQIS.csv'
BIB_FILE = 'HEPQIS.bib'
TXT_FILE = 'CATEGORIES.txt'

# Get dataframe of BibTeX and CSV
df = get_dataframe(BIB_FILE, CSV_FILE)

# Parse CATEGORIES.txt
categories = get_categories(TXT_FILE)

# Make dataframe for descriptions of categories
# Read CSV and convert to dataframe
csv_entries = pd.read_csv('CATEGORIES.csv')
df_csv = pd.DataFrame(csv_entries)
      
# Get Categories and Subcategories
for entry in categories:
    # Parse main category and subcategory
    maincategory = entry.split(", ")[0]
    subcategories = entry.split(", ")[1:]

    # Print Title of Main Category
    OUTPUT_FILE_LIST.write("\section{%s}\n\n" % maincategory.strip('\''))
    OUTPUT_FILE_BRIEF.write("\section{%s}\n\n" % maincategory.strip('\''))
    OUTPUT_FILE_DETAIL.write("\section{%s}\n\n" % maincategory.strip('\''))

    # Print Description of Main Category
    if str(maincategory) in set(df_csv['Category']):
        OUTPUT_FILE_DETAIL.write("\\textit{%s}\n\n" % df_csv.loc[df_csv['Category'] == maincategory]['Description'].values[0])
    
    # Retrieve papers by checking for substring in categories
    df_cat = df.loc[df['Categories'].str.contains(maincategory, case=False)]
    cat_papers = df_cat.values.tolist()

    # Formatting and write to file
    if len(cat_papers) != 0:
        OUTPUT_FILE_LIST.write("\\begin{itemize}\n")
    for paper in cat_papers:
        OUTPUT_FILE_LIST.write("   \item %s~\cite{%s}\n" % (paper[1], paper[0]))
        OUTPUT_FILE_BRIEF.write("\subsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
        OUTPUT_FILE_BRIEF.write("\\begin{itemize}\n\t\item \\textbf{HEP Context: }%s\n\t\item \\textbf{Methods: }%s\n\t\item \\textbf{Results and Conclusions: }%s\n\end{itemize}" % (paper[6], paper[7], paper[8]))
        OUTPUT_FILE_DETAIL.write("\subsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
        OUTPUT_FILE_DETAIL.write("%s\n" % (paper[3]))
   
    if len(cat_papers) != 0:
        OUTPUT_FILE_LIST.write("\end{itemize}\n")
    OUTPUT_FILE_LIST.write("\n\n")
    OUTPUT_FILE_BRIEF.write("\n\n")
    OUTPUT_FILE_DETAIL.write("\n\n")
    
    for subentry in subcategories:
        OUTPUT_FILE_LIST.write("\subsection{%s}\n\n" % subentry.strip('\''))
        OUTPUT_FILE_BRIEF.write("\subsection{%s}\n\n" % subentry.strip('\''))
        OUTPUT_FILE_DETAIL.write("\subsection{%s}\n\n" % subentry.strip('\''))

        # Print Description of Main Category
        if str(subentry) in set(df_csv['Category']):
            OUTPUT_FILE_DETAIL.write("\\textit{%s}\n\n" % df_csv.loc[df_csv['Category'] == subentry]['Description'].values[0])

        # Retrieve papers by checking for substring in categories
        df_subcat = df.loc[df['Categories'].str.contains(subentry, case=False)]
        cat_papers = df_subcat.values.tolist()
        # Formatting and write to file
        if len(cat_papers) != 0:
            OUTPUT_FILE_LIST.write("\\begin{itemize}\n")
        for paper in cat_papers:
            OUTPUT_FILE_LIST.write("   \item %s~\cite{%s}\n" % (paper[1], paper[0]))
            OUTPUT_FILE_BRIEF.write("\subsubsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
            OUTPUT_FILE_BRIEF.write("\\begin{itemize}\n\t\item \\textbf{HEP Context: }%s\n\t\item \\textbf{Methods: }%s\n\t\item \\textbf{Results and Conclusions: }%s\n\end{itemize}" % (paper[6], paper[7], paper[8]))
            OUTPUT_FILE_DETAIL.write("\subsubsection{%s~\cite{%s}}\n" % (paper[1], paper[0]))
            OUTPUT_FILE_DETAIL.write("%s\n" % (paper[3]))
        
        if len(cat_papers) != 0:
            OUTPUT_FILE_LIST.write("\end{itemize}\n")
        OUTPUT_FILE_LIST.write("\n\n")
        OUTPUT_FILE_DETAIL.write("\n\n")

