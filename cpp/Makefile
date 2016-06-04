PYVER=2.7
CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CPPFILES:%.cpp=%.o)
WRAPPER = myosmc_wrap.o
OBJNAME = myosmc.o
SONAME = _myosmc.so

all: $(SONAME)

$(SONAME) : $(OBJFILES)
	g++ -fPIC -c $(WRAPPER:%.o=%.cxx) -I/usr/include/python$(PYVER) -o ${WRAPPER} -fPIC
	g++ -shared ${WRAPPER} $^ -o $@ -lsqlite3

%.o: %.cpp
	g++ -c $^ -I/usr/include/python$(PYVER) -fPIC
clean:
	rm -f *.o
	rm -f ${SONAME}
	rm -f ${WRAPPER}
	rm -f myosmc_wrap.cxx
	rm -f myosmc.py
