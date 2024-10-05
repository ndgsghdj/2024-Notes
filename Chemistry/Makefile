MD_FILES = $(wildcard *.md)
PDF_FILES=$(MD_FILES:.md=.pdf)
BUILD_PDF_FILES=$(PDF_FILES:%=build/%)


chemistry.pdf: $(BUILD_PDF_FILES)
		gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=$@ -dBATCH $^
build/%.pdf: %.md
		@mkdir -p $$(dirname $@)
		pandoc -f latex+raw_tex -L mhchem.lua -c ~/Documents/2024-Notes/pandoc.css -f gfm -t html -o $@ $?

.PHONY: clean

clean:
	rm -rf build
