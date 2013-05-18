
.PHONY: clean all

all: talk.html


%.html: %.rst
	rst2html $^ > $@
	./process.py $@

clean: 
	rm -fr html talk.html
