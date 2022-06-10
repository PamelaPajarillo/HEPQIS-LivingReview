FILENAME = HEPQIS
FILENAME_BRIEF = HEPQIS_BRIEF
FILENAME_DETAIL = HEPQIS_DETAIL
FILENAME_LIST = HEPQIS_LIST

date = $(shell date +%Y-%m-%d)
output_brief_file = draft_brief_$(date).pdf
output_detail_file = draft_detail_$(date).pdf
output_list_file = draft_list_$(date).pdf

LATEX = lualatex
BIBTEX = bibtex

all: default

default: document copy_draft

document: brief detail list
	
brief:
	cp HEPQIS.tex BRIEF.tex
	sed -i 's/INPUTFILE/BRIEF/g' BRIEF.tex
	latexmk -$(LATEX) -logfilewarnings -halt-on-error BRIEF
	cp BRIEF.pdf $(FILENAME_BRIEF).pdf
	rm -f BRIEF*

detail:
	cp HEPQIS.tex DETAIL.tex
	sed -i 's/INPUTFILE/DETAIL/g' DETAIL.tex
	latexmk -$(LATEX) -logfilewarnings -halt-on-error DETAIL
	cp DETAIL.pdf $(FILENAME_DETAIL).pdf
	rm -f DETAIL*

list:
	cp HEPQIS.tex LIST.tex
	sed -i 's/INPUTFILE/LIST/g' LIST.tex
	latexmk -$(LATEX) -logfilewarnings -halt-on-error LIST
	cp LIST.pdf $(FILENAME_LIST).pdf
	rm -f LIST*

copy_draft:
	rsync $(FILENAME_BRIEF).pdf $(output_brief_file)
	rsync $(FILENAME_DETAIL).pdf $(output_detail_file)
	rsync $(FILENAME_LIST).pdf $(output_list_file)

clean:
	rm -f *.aux *.bak *.bbl *.blg *.dvi *.idx *.lof *.log *.lot *.toc \
		*.glg *.gls *.glo *.xdy *.nav *.out *.snm *.vrb *.mp \
		*.synctex.gz *.run.xml *.bcf *.brf *.fls *.fdb_latexmk

realclean: clean
	rm -f *.ps *.pdf

final:
	if [ -f *.aux ]; \
		then make clean; \
	fi
	make document