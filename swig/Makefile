ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all:
	swig -verbose -python -c++ -globals myosmc -I$(ROOT_DIR)/../cpp myosmc.i
	cp myosmc_wrap.cxx $(ROOT_DIR)/../cpp
	cp myosmc.py $(ROOT_DIR)/../cpp
clean:
	rm -f myosmc_wrap.cxx
	rm -f myosmc.py*
