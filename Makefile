MD_FILES=$(shell find . -name \*.md)
HTML_FILES=$(MD_FILES:.md=.html)
BUILD_HTML_FILES=$(HTML_FILES:%=docs/%)
CSS_FILE=~/Documents/2024-Notes/pandoc.css

SRC_DIRS := $(shell find . -type d -not -path "./docs/*" -not -path "./.*" -not -path "./.venv/*")

all: $(BUILD_HTML_FILES) 

docs/assets/%: assets/%
	@mkdir -p $$(dirname $@)
	cp $? $@

docs/%.html: %.md $(CSS_FILE)
	@mkdir -p $$(dirname $@)
	cp $(CSS_FILE) docs/
	pandoc --standalone --mathjax $<  -c ../pandoc.css -f gfm -t html5 -o $@ $<

.PHONY: all clean index_md

index_md:
	pandoc --standalone --mathjax index.md -c ./pandoc.css -f gfm -t html5 -o docs/index.html index.md

all: $(BUILD_HTML_FILES)

clean:
	rm -rf docs

