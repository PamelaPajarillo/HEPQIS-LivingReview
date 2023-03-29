import os

import requests

update_journal = False

myfile = open("HEPQIS.tex")
myfile_out = open("README.md","w")

myfile_out.write("#  **A Living Review of Quantum Information Science in Particle Physics**\n\n")

myfile_out.write("*Inspired by \"A Living Review of Machine Learning for Particle Physics\", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  This repository will be updated as often as possible.  Suggestions are most welcome.*\n\n")

# myfile_out.write("[![download](https://img.shields.io/badge/download-review-blue.svg)](https://iml-wg.github.io/HEPML-LivingReview/review/hepml-review.pdf)\n\n")

myfile_out.write("The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics.  \n\n")

###This bit is slightly modified from Kyle Cranmer https://github.com/cranmer/inspire_play
def summarize_record(recid):
    url = 'https://labs.inspirehep.net/api/arxiv/'+str(recid)
    max_authors = 5
    r = requests.get(url)
    mini_dict = {'recid':recid}
    if 'metadata' in r.json():
        data = r.json()['metadata']
        mini_dict.update({'title':data['titles'][0]['title']})
        if len(data['authors'])>max_authors:
            #mini_dict.update({'authors':[a['full_name'] for a in data['authors'][:max_authors]]+['et. al.']})
            mini_dict.update({'authors':"; ".join([a['full_name'] for a in data['authors'][:max_authors]]+['et. al.'])})
        else:
            mini_dict.update({'authors':[a['full_name'] for a in data['authors']]})

        if 'collaborations' in data:
            mini_dict.update({'collaboration': data['collaborations'][0]['value']})

        mini_dict.update({'arxiv_eprint': data['arxiv_eprints'][0]['value']})
        mini_dict.update({'url': 'https://arxiv.org/abs/'+data['arxiv_eprints'][0]['value']})
        mini_dict.update({'creation_date': data['legacy_creation_date']})

        if 'journal_title' in data:
            mini_dict.update({'journal_title':data['publication_info'][0]['journal_title']})
        if 'journal_volume' in data:
            mini_dict.update({'journal_volume':data['publication_info'][0]['journal_volume']})
        if 'page_start' in data:
            mini_dict.update({'page_start':data['publication_info'][0]['page_start']})
        if 'journal_year' in data:
            mini_dict.update({'journal_year':data['publication_info'][0]['year']})

        if 'dois' in data:
            mini_dict.update({'doi': data['dois'][0]['value']})
    return mini_dict

def convert_from_bib(myline):
    #Not the most elegant way, but quick and dirty.  Files are not big, so this doesn't take long.

    myline = myline.replace(" ","").replace("\n","")

    myfile_bib = open("HEPQIS.bib")
    mylines = []
    for line in myfile_bib:
        mylines+=[line]
        pass
    myentry = []
    for i in range(len(mylines)):
        if myline in mylines[i]:
            j = i+1
            myentry+=[mylines[i]]
            while "@" not in mylines[j]:
                myentry+=[mylines[j]]
                j+=1
                pass
            pass
        pass
    myentry_dict = {}
    for entry in myentry:
        entry_cleaned = entry.replace("\"{","").replace("}\",","").replace("},","")
        entry_cleaned = entry_cleaned.replace(" =","=")
        entry_cleaned = entry_cleaned.replace("= ","=")
        first_entry = entry_cleaned.split("=")[0]
        if "title" in first_entry and not "booktitle" in first_entry:
            myentry_dict["title"] = entry_cleaned.split("title")[1].split("=")[1].split("\n")[0]
            pass
        elif "eprint" in first_entry:
            myentry_dict["eprint"] = entry_cleaned.split("eprint")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
            if "{" in myentry_dict["eprint"]:
                myentry_dict["eprint"] = myentry_dict["eprint"][1:]
                pass
        elif "doi" in first_entry:
            myentry_dict["doi"] = entry_cleaned.split("doi")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        elif "url" in first_entry:
            myentry_dict["url"] = entry_cleaned.split("url")[1].split("=")[1].split("\n")[0].replace("\"","").replace(",","").replace("\'","").replace(" ","")
        else:
            #print(entry_cleaned)
            pass
        pass

    if "eprint" in myentry_dict and 'doi' not in myentry_dict and update_journal:
        #check inspire
        inspire_dict = summarize_record(myentry_dict['eprint'])
        if 'doi' in inspire_dict:
            print("Updating journal ref for ",myline)
            myentry_dict['doi'] = inspire_dict['doi']

            #print(inspire_dict)

            myfile_bib_copy = open("HEPQIS_copy.bib","w")
            myfile_bib = open("HEPQIS.bib")
            for line in myfile_bib:
                myfile_bib_copy.write(line)
                if myentry_dict['eprint'] in line and "eprint" in line:
                    if "journal_title" in inspire_dict:
                        myfile_bib_copy.write("      journal=\""+inspire_dict['journal_title']+"\",\n")
                    if "journal_volume" in inspire_dict:
                        myfile_bib_copy.write("      volume=\""+inspire_dict['journal_volume']+"\",\n")
                    if "page_start" in inspire_dict:
                        myfile_bib_copy.write("      pages=\""+inspire_dict['page_start']+"\",\n")
                    if "doi" in inspire_dict:
                        myfile_bib_copy.write("      doi=\""+inspire_dict['doi']+"\",\n")
                        pass
                    pass
                pass
            os.system("mv HEPQIS_copy.bib HEPQIS.bib")
            #exit(1)

    if "title" not in myentry_dict:
        print(myline)
        print(myentry)
        print("We are in trouble ! ")
    if "eprint" in myentry_dict:
        paper=""
        if "doi" in myentry_dict:
            paper=f" [[DOI](https://doi.org/{myentry_dict['doi']})]"
        elif "url" in myentry_dict:
            paper=f" [[url]({myentry_dict['url']})]"
        return "["+myentry_dict["title"]+"](https://arxiv.org/abs/"+myentry_dict["eprint"]+")"+paper
    elif "doi" in myentry_dict:
        return "["+myentry_dict["title"]+"](https://doi.org/"+myentry_dict["doi"]+")"
    elif "url" in myentry_dict:
        return "["+myentry_dict["title"]+"]("+myentry_dict["url"]+")"
    else:
        return myentry_dict["title"]
    return myline

itemize_counter = 0
for line in myfile:

    if "author" in line:
        continue

    if "\\item \\textbf{" in line:
        line = line[0:line.find("}")]+line[line.find("}")+1:-1]
    line = line.replace("\\textbf{","")

    if "textit{" in line:
        continue

    if "item" in line:
        if "begin{itemize}" in line:
            itemize_counter+=1
        elif "end{itemize}" in line:
            itemize_counter-=1
        else:
            #print(itemize_counter,line)
            if (itemize_counter==1):
                hascites = len(line.split("cite"))
                if (hascites==1):
                    if "Experimental" not in line:
                        myfile_out.write("* "+line.replace(r"\item","")+"\n")
                    else:
                        myfile_out.write("*  Experimental results. *This section is incomplete as there are many results that directly and indirectly (e.g. via flavor tagging) use modern machine learning techniques.  We will try to highlight experimental results that use deep learning in a critical way for the final analysis sensitivity.*\n\n")
                else:
                    myfile_out.write("* "+line.replace(r"\item","").split(r"~\cite")[0]+".\n\n")
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        myfile_out.write("    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                    pass
                pass
            elif "cite" in line:
                mybuffer = ""
                for j in range(itemize_counter-1):
                     mybuffer+="    "
                     pass
                if (":~" in line):
                    myfile_out.write(mybuffer+"* "+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].replace("}","").split(",")
                    for cite in mycites:
                        myfile_out.write(mybuffer+"    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                else:
                    myfile_out.write(mybuffer+"* "+line.split(r"~\cite{")[0].split(r"\item")[1]+"\n\n")
                    mycites = line.split(r"~\cite{")[1].split("}")[0].split(",")
                    for cite in mycites:
                        myfile_out.write(mybuffer+"    * "+convert_from_bib(cite)+"\n")
                        pass
                    myfile_out.write("\n")
                    pass
                pass
