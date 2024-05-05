MD_FILES=$(shell find . -name \*.md)
HTML_FILES=$(MD_FILES:.md=.html)
BUILD_HTML_FILES=$(HTML_FILES:%=docs/%)
CSS_FILE=~/Documents/2024-Notes/pandoc.css
INDEX_FILE=docs/index/index.md
INDEX_HTML_FILE=$(INDEX_FILE:.md=.html)

all: $(BUILD_HTML_FILES)

docs/assets/%: assets/%
	@mkdir -p $$(dirname $@)
	cp $? $@

docs/%.html: %.md $(CSS_FILE)
	@mkdir -p $$(dirname $@)
	cp $(CSS_FILE) docs/
	pandoc --standalone --mathjax=https://cdnjs.cloudflare.com/ajax/libs/mathjax-mhchem/3.3.2 $<  -c ../pandoc.css -f gfm -t html5 -o $@ $<

.PHONY: all clean

all: $(BUILD_HTML_FILES)

clean:
	rm -rf docs
