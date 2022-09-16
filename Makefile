date = $(shell date +%Y-%m-%d)

define compile_latex
	cp HEPQIS.tex BY_$(1)/$(2).tex
	cp jheppub.sty JHEP.bst HEPQIS.bib BY_$(1)/
	sed -i 's/TYPE/$(2)/g' BY_$(1)/$(2).tex
	sed -i 's/SUBJECT/$(1)/g' BY_$(1)/$(2).tex
	cd BY_$(1); latexmk -lualatex -logfilewarnings -halt-on-error $(2)
	cp BY_$(1)/$(2).pdf BY_$(1)/BY$(1)_$(2).pdf
	rm -f BY_$(1)/$(2)* BY_$(1)/jheppub.sty BY_$(1)/JHEP.bst BY_$(1)/BY$(1)_$(2).tex BY_$(1)/HEPQIS.bib
endef

define backup
	rsync BY_$(1)/BY$(1)_$(2).pdf BY_$(1)/DRAFTS/draft_$(2)_$(3).pdf
endef

all: hepqis default

default: document copy_draft

document: hep qis

hepqis: make_hepqis.py
	python3 make_hepqis.py

hep:
	$(call compile_latex,HEP,LIST)
	$(call compile_latex,HEP,DETAIL)

qis:
	$(call compile_latex,QIS,LIST)
	$(call compile_latex,QIS,DETAIL)

copy_draft:
	$(call backup,HEP,LIST,$(date))
	$(call backup,HEP,DETAIL,$(date))
	$(call backup,QIS,LIST,$(date))
	$(call backup,QIS,DETAIL,$(date))
	
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