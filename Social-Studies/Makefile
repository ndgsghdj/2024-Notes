MD_FILES=Agreement.md SRQ_Evaluative.md Surprise.md SRQ_Evaluative.md HIHS_Prelims_2023.md

PDF_FILES=$(MD_FILES:.md=.pdf)
BUILD_PDF_FILES=$(PDF_FILES:%=build/%)

social_studies.pdf: $(BUILD_PDF_FILES)
		gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=$@ -dBATCH $^
build/%.pdf: %.md
		@mkdir -p $$(dirname $@)
		pandoc -V geometry:margin=1in -c ./github-markdown.css -f gfm -t html -o $@ $?

