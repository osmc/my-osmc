%include exception.i

%{
#define SWIG_FILE_WITH_INIT
static PyObject* m_NoOSPropertyException;
#include "CUtils.h"
%}


%init %{
    m_NoOSPropertyException = PyErr_NewException("_myosmc.NoOSPropertyException", NULL, NULL);
    Py_INCREF(m_NoOSPropertyException);
    PyModule_AddObject(m, "NoOSPropertyException", m_NoOSPropertyException);
%}

%exception {
  try {
    $action
  } catch (NoOSPropertyException &_e) {
    SWIG_Python_Raise(SWIG_NewPointerObj(
            (new NoOSPropertyException(static_cast<const NoOSPropertyException& >(_e))),  
            SWIGTYPE_p_NoOSPropertyException,SWIG_POINTER_OWN),
        "NoOSPropertyException", SWIGTYPE_p_NoOSPropertyException); 
    SWIG_fail;
  } 
}

%include "CUtils.h"
