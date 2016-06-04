ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all:
	cp $(ROOT_DIR)/../cpp/_myosmc.so .
	cp $(ROOT_DIR)/../swig/myosmc.py .

clean:
	rm -f _myosmc.so
	rm -f myosmc.py
	rm -f myosmc.pyc
