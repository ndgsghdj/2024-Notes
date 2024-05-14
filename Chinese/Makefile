CSV_FILES = $(wildcard *.csv)
MD_FILES = $(CSV_FILES:.csv=.md)

%.md: %.csv
	csv2md $< > $@
	rm $<

all: $(MD_FILES)

.PHONY: all
