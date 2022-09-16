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

# ***** ---------------------------------------------------------------------------------------
# ***** MARKDOWN FILES ------------------------------------------------------------------------
# ***** ---------------------------------------------------------------------------------------
# Output Markdown Files
OUTPUT_FILE_MAIN = open("README.md","w")
OUTPUT_FILE_HEP = open("BY_HEP/README.md","w")
OUTPUT_FILE_QIS = open("BY_QIS/README.md","w")
OUTPUT_FILE_HEP_CATEGORIES = open("BY_HEP/CATEGORIES.md","w")
OUTPUT_FILE_QIS_CATEGORIES = open("BY_QIS/CATEGORIES.md","w")

# ***** MAIN MD -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("#  **A Living Review of Quantum Information Science in High Energy Physics**\n\n")
OUTPUT_FILE_MAIN.write("*Inspired by <a href=\"https://iml-wg.github.io/HEPML-LivingReview/\">\"A Living Review of Machine Learning for High Energy Physics\"</a>, the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*\n\n")
OUTPUT_FILE_MAIN.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics. The papers listed are in no particular order. \n\n")
OUTPUT_FILE_MAIN.write("The repository is organized in two ways: \n* [![MAIN_TO_HEP](https://img.shields.io/badge/Link_to-HEP-5BC0EB)](/BY_HEP#readme) **By High Energy Physics (HEP) Topics** \n* [![MAIN_TO_HEP](https://img.shields.io/badge/Link_to-QIS-9BC53D)](/BY_QIS#readme) **By Quantum Information Science (QIS) Topics** \n\n")
OUTPUT_FILE_MAIN.write("These are then organized by subtopics listed below. \n\n")

# ***** HEP CATEGORIES -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("##  **High Energy Physics (HEP) Topics**\n\n")
OUTPUT_FILE_HEP_CATEGORIES.write("#  **Descriptions of HEP Topics**\n\n")
OUTPUT_FILE_HEP_CATEGORIES.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions) is not functioning properly. Please refer to the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_HEP/BYHEP_DETAIL.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_HEP](https://img.shields.io/badge/Link_to-HEP_-5BC0EB)](/BY_HEP#readme) ⟵ Click the following for the living review organized by HEP topics  \n")
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_QIS](https://img.shields.io/badge/Link_to-QIS_-9BC53D)](/BY_QIS#readme) ⟵ Click the following for the living review organized by QIS topics  \n")
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_MAIN](https://img.shields.io/badge/Link_to-Main-FDE74C)](/../../#readme) ⟵ Click the following to go to the main living review page  \n\n")
list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_HEP_CATEGORIES, categories_hep, df_csv_hep, "HEP")

# ***** QIS CATEGORIES -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("##  **Quantum Information Science (QIS) Topics**\n\n")
OUTPUT_FILE_QIS_CATEGORIES.write("#  **Descriptions of QIS Topics**\n\n")
OUTPUT_FILE_QIS_CATEGORIES.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions) is not functioning properly. Please refer to the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_QIS/BYQIS_DETAIL.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_HEP](https://img.shields.io/badge/Link_to-HEP_-5BC0EB)](/BY_HEP#readme) ⟵ Click the following for the living review organized by HEP topics  \n")
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_QIS](https://img.shields.io/badge/Link_to-QIS_-9BC53D)](/BY_QIS#readme) ⟵ Click the following for the living review organized by QIS topics  \n")
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_MAIN](https://img.shields.io/badge/Link_to-Main-FDE74C)](/../../#readme) ⟵ Click the following to go to the main living review page  \n\n")
list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_QIS_CATEGORIES, categories_qis, df_csv_qis, "QIS")

OUTPUT_FILE_MAIN.close()
OUTPUT_FILE_HEP_CATEGORIES.close()
OUTPUT_FILE_QIS_CATEGORIES.close()

# ***** BY HEP MD -----------------------------------------------------------------------
OUTPUT_FILE_HEP.write("#  **A Living Review of Quantum Information Science in High Energy Physics Organized by HEP Topics**\n\n")
OUTPUT_FILE_HEP.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_HEP/BYHEP_DETAIL.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_HEP.write("[![BY_QIS](https://img.shields.io/badge/Link_to-QIS-9BC53D)](/BY_QIS#readme) ⟵ Click the following for the living review organized by QIS topics  \n")
OUTPUT_FILE_HEP.write("[![HEP_TO_MAIN](https://img.shields.io/badge/Link_to-Main-FDE74C)](/../../#readme) ⟵ Click the following to go to the main living review page  \n\n")

OUTPUT_FILE_HEP.write("## **PDF Versions** \n")
OUTPUT_FILE_HEP.write("[![HEP_LIST](https://img.shields.io/badge/Download_PDF-List-ffcce7)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_HEP/BYHEP_LIST.pdf) ⟵ PDF of list of references  \n")
OUTPUT_FILE_HEP.write("[![HEP_DETAIL](https://img.shields.io/badge/Download_PDF-Detail-81b7df)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_HEP/BYHEP_DETAIL.pdf) ⟵ PDF of references with detailed descriptions  \n")

write_papers_to_md(df, OUTPUT_FILE_HEP, categories_hep, categories_qis, "HEP", "QIS")
OUTPUT_FILE_HEP.close()

# ***** BY QIS MD -----------------------------------------------------------------------
OUTPUT_FILE_QIS.write("#  **A Living Review of Quantum Information Science in High Energy Physics Organized by QIS Topics**\n\n")
OUTPUT_FILE_QIS.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_QIS/BYQIS_DETAIL.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_QIS.write("[![QIS_TO_HEP](https://img.shields.io/badge/Link_to-HEP-5BC0EB)](/BY_HEP#readme) ⟵ Click the following for the living review organized by QIS topics  \n")
OUTPUT_FILE_QIS.write("[![QIS_TO_MAIN](https://img.shields.io/badge/Link_to-Main-FDE74C)](/../../#readme) ⟵ Click the following to go to the main living review page  \n\n")

OUTPUT_FILE_QIS.write("## **PDF Versions** \n")
OUTPUT_FILE_QIS.write("[![QIS_LIST](https://img.shields.io/badge/Download_PDF-List-ffcce7)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_QIS/BYQIS_LIST.pdf) ⟵ PDF of list of references  \n")
OUTPUT_FILE_QIS.write("[![QIS_DETAIL](https://img.shields.io/badge/Download_PDF-Detail-81b7df)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/BY_QIS/BYQIS_DETAIL.pdf) ⟵ PDF of references with detailed descriptions  \n")

write_papers_to_md(df, OUTPUT_FILE_QIS, categories_qis, categories_hep, "QIS", "HEP")
OUTPUT_FILE_QIS.close()

# ***** ------------------------------------------------------------------------------------
# ***** LATEX FILES ------------------------------------------------------------------------
# ***** ------------------------------------------------------------------------------------
# Output LaTeX Files
# OUTPUT_FILE_MAIN = open("HEPQIS_MAIN.tex","w")
OUTPUT_FILE_HEP_LIST = open("BY_HEP/BYHEP_LIST.tex","w")
OUTPUT_FILE_HEP_DETAIL = open("BY_HEP/BYHEP_DETAIL.tex","w")

OUTPUT_FILE_QIS_LIST = open("BY_QIS/BYQIS_LIST.tex","w")
OUTPUT_FILE_QIS_DETAIL = open("BY_QIS/BYQIS_DETAIL.tex","w")

# ***** MAIN LATEX FILES -----------------------------------------------------------------------

# OUTPUT_FILE_MAIN.close()

# ***** BY HEP LATEX FILES -----------------------------------------------------------------------
write_papers_to_tex(df, OUTPUT_FILE_HEP_LIST, OUTPUT_FILE_HEP_DETAIL, categories_hep, categories_qis, "HEP", "QIS")
OUTPUT_FILE_HEP_LIST.close()
OUTPUT_FILE_HEP_DETAIL.close()

# ***** BY QIS LATEX FILES -----------------------------------------------------------------------
write_papers_to_tex(df, OUTPUT_FILE_QIS_LIST, OUTPUT_FILE_QIS_DETAIL, categories_qis, categories_hep, "QIS", "HEP")
OUTPUT_FILE_QIS_LIST.close()
OUTPUT_FILE_QIS_DETAIL.close()