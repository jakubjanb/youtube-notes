.PHONY: metadata new-note validate build build-all update-index clean

PYTHON ?= python3
TITLE ?=
DOMAIN ?= other
SUBDOMAIN ?=
URL ?=
TEX ?=

metadata:
	$(PYTHON) youtube-metadata-collector/scripts/create_youtube_metadata.py "$(URL)" --domain "$(DOMAIN)" --subdomain "$(SUBDOMAIN)" --output-dir sources/youtube/metadata

new-note:
	$(PYTHON) scripts/new_note.py "$(TITLE)" --domain "$(DOMAIN)"

validate:
	$(PYTHON) scripts/validate_metadata.py --notes notes --sources sources/youtube/metadata examples/sample-note/metadata.yaml

build:
	$(PYTHON) scripts/build_latex.py "$(TEX)"

build-all:
	$(PYTHON) scripts/build_latex.py --all notes examples

update-index:
	$(PYTHON) scripts/update_index.py --notes notes --knowledge-base knowledge-base

clean:
	find . \( -name '*.aux' -o -name '*.bbl' -o -name '*.bcf' -o -name '*.blg' -o -name '*.fdb_latexmk' -o -name '*.fls' -o -name '*.log' -o -name '*.out' -o -name '*.run.xml' -o -name '*.synctex.gz' -o -name '*.toc' \) -delete
