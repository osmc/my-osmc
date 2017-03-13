PYVER=2.7
CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CPPFILES:%.cpp=%.o)
WRAPPER = myosmc_wrap.o
OBJNAME = myosmc.o
SONAME = _myosmc.so

CFLAGS += `pkg-config --cflags python2`
LDFLAGS += `pkg-config --libs python2`
LDFLAGS += `pkg-config --libs sqlite3`

all: $(SONAME)

$(SONAME) : $(OBJFILES)
	g++ -fPIC -c $(WRAPPER:%.o=%.cxx) ${LDFLAGS} ${CFLAGS} -o ${WRAPPER} -fPIC
	g++ -shared ${WRAPPER} $^ -o $@ ${LDFLAGS}
	strip ${SONAME}

%.o: %.cpp
	g++ -c $^ ${CFLAGS} -fPIC
clean:
	rm -f *.o
	rm -f ${SONAME}
	rm -f ${WRAPPER}
	rm -f myosmc_wrap.cxx
	rm -f myosmc.py
