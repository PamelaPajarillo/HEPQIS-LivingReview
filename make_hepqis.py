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

OUTPUT_FILE_MAIN.write("[![DOWNLOAD_PDF](https://img.shields.io/badge/Download-PDF_Version-81b7df)](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/HEPQIS.pdf) \n\n\n")

OUTPUT_FILE_MAIN.write("*Inspired by <a href=\"https://iml-wg.github.io/HEPML-LivingReview/\">\"A Living Review of Machine Learning for High Energy Physics\"</a>, the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*\n\n")
OUTPUT_FILE_MAIN.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics. The papers are listed in reverse chronological order. \n\n")

OUTPUT_FILE_MAIN.write("The repository is organized in two ways: \n* [![MAIN_TO_HEP](https://img.shields.io/badge/Link_to-Living_Review_by_HEP-5BC0EB)](/BY_HEP#readme) \n* [![MAIN_TO_HEP](https://img.shields.io/badge/Link_to-Living_Review_by_QIS-9BC53D)](/BY_QIS#readme)\n\n")
OUTPUT_FILE_MAIN.write("These are then organized by subtopics listed below. \n\n")

# ***** HEP CATEGORIES -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("##  **High Energy Physics (HEP) Topics**\n\n")
OUTPUT_FILE_HEP_CATEGORIES.write("#  **Descriptions of HEP Topics**\n\n")
OUTPUT_FILE_HEP_CATEGORIES.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions) is not functioning properly. Please refer to Section 1.1 in the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/HEPQIS.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_HEP](https://img.shields.io/badge/Link_to-Living_Review_by_HEP_-5BC0EB)](/BY_HEP#readme) \t\n")
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_QIS](https://img.shields.io/badge/Link_to-Living_Review_by_QIS_-9BC53D)](/BY_QIS#readme) \t\n")
OUTPUT_FILE_HEP_CATEGORIES.write("[![HEPCAT_TO_MAIN](https://img.shields.io/badge/Link_to-Living_Review_Home_-FDE74C)](/../../#readme) \n\n")
list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_HEP_CATEGORIES, categories_hep, df_csv_hep, "HEP")

# ***** QIS CATEGORIES -----------------------------------------------------------------------
OUTPUT_FILE_MAIN.write("##  **Quantum Information Science (QIS) Topics**\n\n")
OUTPUT_FILE_QIS_CATEGORIES.write("#  **Descriptions of QIS Topics**\n\n")
OUTPUT_FILE_QIS_CATEGORIES.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions) is not functioning properly. Please refer to Section 1.2 in the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/HEPQIS.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_HEP](https://img.shields.io/badge/Link_to-Living_Review_by_HEP_-5BC0EB)](/BY_HEP#readme) \t\n")
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_QIS](https://img.shields.io/badge/Link_to-Living_Review_by_QIS_-9BC53D)](/BY_QIS#readme) \t\n")
OUTPUT_FILE_QIS_CATEGORIES.write("[![QISCAT_TO_MAIN](https://img.shields.io/badge/Link_to-Living_Review_Home_-FDE74C)](/../../#readme) \n\n")
list_subcategories_to_md(OUTPUT_FILE_MAIN, OUTPUT_FILE_QIS_CATEGORIES, categories_qis, df_csv_qis, "QIS")

OUTPUT_FILE_MAIN.close()
OUTPUT_FILE_HEP_CATEGORIES.close()
OUTPUT_FILE_QIS_CATEGORIES.close()

# ***** BY HEP MD -----------------------------------------------------------------------
OUTPUT_FILE_HEP.write("#  **A Living Review of Quantum Information Science in High Energy Physics Organized by HEP Topics**\n\n")
OUTPUT_FILE_HEP.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to Section 2 in the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/HEPQIS.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_HEP.write("[![BY_QIS](https://img.shields.io/badge/Link_to-Living_Review_by_QIS-9BC53D)](/BY_QIS#readme) \t\n")
OUTPUT_FILE_HEP.write("[![HEP_TO_MAIN](https://img.shields.io/badge/Link_to-Living_Review_Home_-FDE74C)](/../../#readme) \n\n")

write_papers_to_md(df, OUTPUT_FILE_HEP, categories_hep, categories_qis, "HEP", "QIS")
OUTPUT_FILE_HEP.close()

# ***** BY QIS MD -----------------------------------------------------------------------
OUTPUT_FILE_QIS.write("#  **A Living Review of Quantum Information Science in High Energy Physics Organized by QIS Topics**\n\n")
OUTPUT_FILE_QIS.write('**⚠️⚠️⚠️ Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to Section 3 in the [PDF version found here](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/PamelaPajarillo/HEPQIS-LivingReview/main/HEPQIS.pdf) ⚠️⚠️⚠️**\n\n')
OUTPUT_FILE_QIS.write("[![QIS_TO_HEP](https://img.shields.io/badge/Link_to-Living_Review_by_HEP-5BC0EB)](/BY_HEP#readme) \t\n")
OUTPUT_FILE_QIS.write("[![QIS_TO_MAIN](https://img.shields.io/badge/Link_to-Living_Review_Home_-FDE74C)](/../../#readme) \n\n")

write_papers_to_md(df, OUTPUT_FILE_QIS, categories_qis, categories_hep, "QIS", "HEP")
OUTPUT_FILE_QIS.close()

# ***** ------------------------------------------------------------------------------------
# ***** LATEX FILES ------------------------------------------------------------------------
# ***** ------------------------------------------------------------------------------------
# Output LaTeX Files
OUTPUT_FILE_CATEGORIES = open("INTRODUCTION.tex","w")
OUTPUT_FILE_CATEGORIES.write('\section{Introduction}\n\n')
OUTPUT_FILE_CATEGORIES.write('The purpose of this note is to collect references for quantum information science as applied to particle and nuclear physics.  The papers are listed in reverse chronological order).  In order to be as useful as possible, this document will continually change. Please check back \\footnote[2]{See \href{https://github.com/PamelaPajarillo/HEPQIS-LivingReview}{https://github.com/PamelaPajarillo/HEPQIS-LivingReview}.} regularly.  You can simply download the .bib file to get all of the latest references.  Suggestions are most welcome.')
OUTPUT_FILE_HEP = open("BYHEP.tex","w")
OUTPUT_FILE_QIS = open("BYQIS.tex","w")

# ***** MAIN LATEX FILES -----------------------------------------------------------------------
write_categories_to_tex(OUTPUT_FILE_CATEGORIES, categories_hep, df_csv_hep, "HEP")
write_categories_to_tex(OUTPUT_FILE_CATEGORIES, categories_qis, df_csv_qis, "QIS")
write_papers_to_tex(df, OUTPUT_FILE_HEP, categories_hep, categories_qis, "HEP", "QIS")
write_papers_to_tex(df, OUTPUT_FILE_QIS, categories_qis, categories_hep, "QIS", "HEP")
OUTPUT_FILE_CATEGORIES.close()
OUTPUT_FILE_HEP.close()
OUTPUT_FILE_QIS.close()