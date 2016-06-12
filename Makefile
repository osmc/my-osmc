all:
	make -C swig
	make -C cpp
	make -C python


clean:
	make -C swig clean
	make -C cpp clean
	make -C python clean
