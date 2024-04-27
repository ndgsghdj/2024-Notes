MD_FILES=$(shell find . -name \*.md)
HTML_FILES=$(MD_FILES:.md=.html)
BUILD_HTML_FILES=$(HTML_FILES:%=build/%)
CSS_FILE=~/Documents/2024-Notes/pandoc.css
INDEX_FILE=build/index.md
INDEX_HTML_FILE=$(INDEX_FILE:.md=.html)

all: $(BUILD_HTML_FILES)

build/assets/%: assets/%
	@mkdir -p $$(dirname $@)
	cp $? $@

build/%.html: %.md $(CSS_FILE)
	@mkdir -p $$(dirname $@)
	pandoc --standalone $<  -c $(CSS_FILE) -f gfm -t html5 -o $@ $<

$(INDEX_FILE): $(MD_FILES)
	echo "# Index\n" > $(INDEX_FILE)
	for file in $(MD_FILES); do \
		echo "* [$${file%.md}]($${file%.md}.html)" >> $(INDEX_FILE); \
	done
	pandoc --standalone $(INDEX_FILE) -c $(CSS_FILE) -f gfm -t html5 -o $(INDEX_HTML_FILE) $(INDEX_FILE)



.PHONY: all clean

all: $(BUILD_HTML_FILES) $(INDEX_FILE)

clean:
	rm -rf build
