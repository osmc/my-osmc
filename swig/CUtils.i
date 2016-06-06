%include exception.i

%{
#define SWIG_FILE_WITH_INIT
static PyObject* m_OSMCUtilsException;
#include "CUtils.h"
%}


%init %{
    m_OSMCUtilsException = PyErr_NewException("_myosmc.OSMCUtilsException", NULL, NULL);
    Py_INCREF(m_OSMCUtilsException);
    PyModule_AddObject(m, "OSMCUtilsException", m_OSMCUtilsException);
%}

%exception {
  try {
    $action
  } catch (OSMCUtilsException &_e) {
    SWIG_Python_Raise(SWIG_NewPointerObj(
            (new OSMCUtilsException(static_cast<const OSMCUtilsException& >(_e))),
            SWIGTYPE_p_OSMCUtilsException,SWIG_POINTER_OWN),
        "OSMCUtilsException", SWIGTYPE_p_OSMCUtilsException);
    SWIG_fail;
  }
}

%include "CUtils.h"
