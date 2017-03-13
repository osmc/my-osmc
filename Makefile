all:
	make -C swig
	make -C cpp

clean:
	make -C swig clean
	make -C cpp clean
