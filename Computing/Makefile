MD_FILES=$(shell find . -name \*.md)
PDF_FILES=$(MD_FILES:.md=.pdf)
BUILD_PDF_FILES=$(PDF_FILES:%=build/%)

computing.pdf: $(BUILD_PDF_FILES)
		gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=$@ -dBATCH $^
build/%.pdf: %.md
		@mkdir -p $$(dirname $@)
		pandoc -V geometry:margin=1in -c ~/Documents/2024-Notes/markdown.css -f gfm -t html -o $@ $?

.PHONY: clean

clean:
	rm -rf build
