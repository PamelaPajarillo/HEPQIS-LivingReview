from utils import *

# Input Files
CSV_FILE = 'HEPQIS.csv'
BIB_FILE = 'HEPQIS.bib'
CATEGORIES_CSV_HEP = 'BY_HEP/CATEGORIES.csv'
CATEGORIES_CSV_QIS = 'BY_QIS/CATEGORIES.csv'

# Get categories from CSV file
categories_hep, df_csv_hep = get_categories(CATEGORIES_CSV_HEP)
categories_qis, df_csv_qis = get_categories(CATEGORIES_CSV_QIS)

# Get dataframe of BibTeX and CSV
df = get_dataframe(BIB_FILE, CSV_FILE, categories_hep, categories_qis)

# Check to make sure each paper has at least one HEP category and at least one QIS category
##### TODO #####

# ***** ---------------------------------------------------------------------------------------
# ***** MARKDOWN FILES ------------------------------------------------------------------------
# ***** ---------------------------------------------------------------------------------------
# Output Markdown Files
OUTPUT_FILE_MAIN = open("README.md","w")
OUTPUT_FILE_HEP = open("BY_HEP/README.md","w")
OUTPUT_FILE_QIS = open("BY_QIS/README.md","w")

# ***** MAIN MD -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("#  **A Living Review of Quantum Information Science in Particle Physics**\n\n")
OUTPUT_FILE_MAIN.write("*Inspired by \"A Living Review of Machine Learning for Particle Physics\", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*\n\n")
OUTPUT_FILE_MAIN.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics. The papers listed are in no particular order. \n\n")
OUTPUT_FILE_MAIN.write("The repository is organized in two ways: \n* <a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/tree/main/BY_HEP\"><img src=\"https://img.shields.io/badge/Link to-HEP-5BC0EB\"/></a> **By High Energy Physics (HEP) Topics** \n* <a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/tree/main/BY_QIS\"><img src=\"https://img.shields.io/badge/Link to-QIS-9BC53D\"/></a> **By Quantum Information Science (QIS) Topics** \n\n")

OUTPUT_FILE_MAIN.write("#  **High Energy Physics (HEP) Topics**\n\n")
OUTPUT_FILE_MAIN.write("To be written\n\n")

OUTPUT_FILE_MAIN.write("#  **Quantum Information Science (QIS) Topics**\n\n")
OUTPUT_FILE_MAIN.write("To be written\n\n")

OUTPUT_FILE_MAIN.write("#  **Resources**\n\n")
OUTPUT_FILE_MAIN.write("To be written\n\n")

OUTPUT_FILE_MAIN.write("#  **Contributing**\n\n")
OUTPUT_FILE_MAIN.write("To be written\n\n")
OUTPUT_FILE_MAIN.close()

# ***** BY HEP MD -----------------------------------------------------------------------
OUTPUT_FILE_HEP.write("#  **A Living Review of Quantum Information Science in Particle Physics Organized by HEP Topics**\n\n")
OUTPUT_FILE_HEP.write('\n**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to the <a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_HEP/BYHEP_DETAIL.pdf\"> PDF version found here </a> ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_HEP.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/tree/main/BY_QIS\"><img src=\"https://img.shields.io/badge/Link to-QIS-9BC53D\"/></a> ⟵ Click the following for the living review organized by QIS topics  \n")
OUTPUT_FILE_HEP.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview\"><img src=\"https://img.shields.io/badge/Link to-Main-FDE74C\"/></a> ⟵ Click the following to go to the main living review page  \n\n")

OUTPUT_FILE_HEP.write("## **PDF Versions** \n")
OUTPUT_FILE_HEP.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_HEP/BYHEP_LIST.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-List-ffcce7\"/></a> ⟵ PDF of list of references  \n")
OUTPUT_FILE_HEP.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_HEP/BYHEP_BRIEF.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-Brief-daf2dc\"/></a> ⟵ PDF of references with short descriptions (HEP context, methods, results and conclusions)  \n")
OUTPUT_FILE_HEP.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_HEP/BYHEP_DETAIL.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-Detail-81b7df\"/></a> ⟵ PDF of references with detailed descriptions  \n")

write_papers_to_md(OUTPUT_FILE_HEP, categories_hep, df)
OUTPUT_FILE_HEP.close()

# ***** BY QIS MD -----------------------------------------------------------------------
OUTPUT_FILE_QIS.write("#  **A Living Review of Quantum Information Science in Particle Physics Organized by QIS Topics**\n\n")
OUTPUT_FILE_QIS.write('\n**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to the <a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_QIS/BYQIS_DETAIL.pdf\"> PDF version found here </a> ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_QIS.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/tree/main/BY_HEP\"><img src=\"https://img.shields.io/badge/Link to-HEP-5BC0EB\"/></a> ⟵ Click the following for the living review organized by HEP topics  \n")
OUTPUT_FILE_QIS.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview\"><img src=\"https://img.shields.io/badge/Link to-Main-FDE74C\"/></a>  ⟵ Click the following to go to the main living review page  \n\n")

OUTPUT_FILE_QIS.write("## **PDF Versions** \n")
OUTPUT_FILE_QIS.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_QIS/BYQIS_LIST.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-List-ffcce7\"/></a> ⟵ PDF of list of references  \n")
OUTPUT_FILE_QIS.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_QIS/BYQIS_BRIEF.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-Brief-daf2dc\"/></a> ⟵ PDF of references with short descriptions (HEP context, methods, results and conclusions)  \n")
OUTPUT_FILE_QIS.write("<a href=\"https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/BY_QIS/BYQIS_DETAIL.pdf\"><img src=\"https://img.shields.io/badge/Download PDF-Detail-81b7df\"/></a> ⟵ PDF of references with detailed descriptions  \n")

write_papers_to_md(OUTPUT_FILE_QIS, categories_qis, df)
OUTPUT_FILE_QIS.close()

# ***** ------------------------------------------------------------------------------------
# ***** LATEX FILES ------------------------------------------------------------------------
# ***** ------------------------------------------------------------------------------------
# Output LaTeX Files
OUTPUT_FILE_HEP_LIST = open("BY_HEP/BYHEP_LIST.tex","w")
OUTPUT_FILE_HEP_BRIEF = open("BY_HEP/BYHEP_BRIEF.tex","w")
OUTPUT_FILE_HEP_DETAIL = open("BY_HEP/BYHEP_DETAIL.tex","w")

OUTPUT_FILE_QIS_LIST = open("BY_QIS/BYQIS_LIST.tex","w")
OUTPUT_FILE_QIS_BRIEF = open("BY_QIS/BYQIS_BRIEF.tex","w")
OUTPUT_FILE_QIS_DETAIL = open("BY_QIS/BYQIS_DETAIL.tex","w")

# ***** BY HEP LATEX FILES -----------------------------------------------------------------------
write_papers_to_tex(OUTPUT_FILE_HEP_LIST, OUTPUT_FILE_HEP_BRIEF, OUTPUT_FILE_HEP_DETAIL, categories_hep, df, df_csv_hep)

# ***** BY QIS LATEX FILES -----------------------------------------------------------------------
write_papers_to_tex(OUTPUT_FILE_QIS_LIST, OUTPUT_FILE_QIS_BRIEF, OUTPUT_FILE_QIS_DETAIL, categories_qis, df, df_csv_qis)
