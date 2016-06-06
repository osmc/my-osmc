# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_myosmc', [dirname(__file__)])
        except ImportError:
            import _myosmc
            return _myosmc
        if fp is not None:
            try:
                _mod = imp.load_module('_myosmc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _myosmc = swig_import_helper()
    del swig_import_helper
else:
    import _myosmc
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_myosmc.DEV_ID_VERO1_swigconstant(_myosmc)
DEV_ID_VERO1 = _myosmc.DEV_ID_VERO1

_myosmc.DEV_ID_VERO2_swigconstant(_myosmc)
DEV_ID_VERO2 = _myosmc.DEV_ID_VERO2

_myosmc.DEV_ID_BCM2835_swigconstant(_myosmc)
DEV_ID_BCM2835 = _myosmc.DEV_ID_BCM2835

_myosmc.DEV_ID_BCM2836_swigconstant(_myosmc)
DEV_ID_BCM2836 = _myosmc.DEV_ID_BCM2836

_myosmc.DEV_ID_APPLETV1_swigconstant(_myosmc)
DEV_ID_APPLETV1 = _myosmc.DEV_ID_APPLETV1

_myosmc.DEV_ID_PC_swigconstant(_myosmc)
DEV_ID_PC = _myosmc.DEV_ID_PC

_myosmc.DEV_ID_UNKNOWN_swigconstant(_myosmc)
DEV_ID_UNKNOWN = _myosmc.DEV_ID_UNKNOWN
class CUtils(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CUtils, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CUtils, name)
    __repr__ = _swig_repr
    __swig_getmethods__["getOSMCVersionShort"] = lambda x: _myosmc.CUtils_getOSMCVersionShort
    if _newclass:
        getOSMCVersionShort = staticmethod(_myosmc.CUtils_getOSMCVersionShort)
    __swig_getmethods__["getOSMCVersionLong"] = lambda x: _myosmc.CUtils_getOSMCVersionLong
    if _newclass:
        getOSMCVersionLong = staticmethod(_myosmc.CUtils_getOSMCVersionLong)
    __swig_getmethods__["getOSMCDevice"] = lambda x: _myosmc.CUtils_getOSMCDevice
    if _newclass:
        getOSMCDevice = staticmethod(_myosmc.CUtils_getOSMCDevice)
    __swig_getmethods__["isVero"] = lambda x: _myosmc.CUtils_isVero
    if _newclass:
        isVero = staticmethod(_myosmc.CUtils_isVero)
    __swig_getmethods__["isRaspberryPi"] = lambda x: _myosmc.CUtils_isRaspberryPi
    if _newclass:
        isRaspberryPi = staticmethod(_myosmc.CUtils_isRaspberryPi)
    __swig_getmethods__["isAppleTV"] = lambda x: _myosmc.CUtils_isAppleTV
    if _newclass:
        isAppleTV = staticmethod(_myosmc.CUtils_isAppleTV)
    __swig_getmethods__["isPC"] = lambda x: _myosmc.CUtils_isPC
    if _newclass:
        isPC = staticmethod(_myosmc.CUtils_isPC)

    def __init__(self):
        this = _myosmc.new_CUtils()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _myosmc.delete_CUtils
    __del__ = lambda self: None
CUtils_swigregister = _myosmc.CUtils_swigregister
CUtils_swigregister(CUtils)

def CUtils_getOSMCVersionShort():
    return _myosmc.CUtils_getOSMCVersionShort()
CUtils_getOSMCVersionShort = _myosmc.CUtils_getOSMCVersionShort

def CUtils_getOSMCVersionLong():
    return _myosmc.CUtils_getOSMCVersionLong()
CUtils_getOSMCVersionLong = _myosmc.CUtils_getOSMCVersionLong

def CUtils_getOSMCDevice():
    return _myosmc.CUtils_getOSMCDevice()
CUtils_getOSMCDevice = _myosmc.CUtils_getOSMCDevice

def CUtils_isVero():
    return _myosmc.CUtils_isVero()
CUtils_isVero = _myosmc.CUtils_isVero

def CUtils_isRaspberryPi():
    return _myosmc.CUtils_isRaspberryPi()
CUtils_isRaspberryPi = _myosmc.CUtils_isRaspberryPi

def CUtils_isAppleTV():
    return _myosmc.CUtils_isAppleTV()
CUtils_isAppleTV = _myosmc.CUtils_isAppleTV

def CUtils_isPC():
    return _myosmc.CUtils_isPC()
CUtils_isPC = _myosmc.CUtils_isPC

class OSMCUtilsException(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OSMCUtilsException, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OSMCUtilsException, name)
    __repr__ = _swig_repr

    def __init__(self, what):
        this = _myosmc.new_OSMCUtilsException(what)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def what(self):
        return _myosmc.OSMCUtilsException_what(self)
    __swig_destroy__ = _myosmc.delete_OSMCUtilsException
    __del__ = lambda self: None
OSMCUtilsException_swigregister = _myosmc.OSMCUtilsException_swigregister
OSMCUtilsException_swigregister(OSMCUtilsException)

class db_operation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, db_operation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, db_operation, name)
    __repr__ = _swig_repr
    __swig_setmethods__["key"] = _myosmc.db_operation_key_set
    __swig_getmethods__["key"] = _myosmc.db_operation_key_get
    if _newclass:
        key = _swig_property(_myosmc.db_operation_key_get, _myosmc.db_operation_key_set)
    __swig_setmethods__["value"] = _myosmc.db_operation_value_set
    __swig_getmethods__["value"] = _myosmc.db_operation_value_get
    if _newclass:
        value = _swig_property(_myosmc.db_operation_value_get, _myosmc.db_operation_value_set)
    __swig_setmethods__["datatype"] = _myosmc.db_operation_datatype_set
    __swig_getmethods__["datatype"] = _myosmc.db_operation_datatype_get
    if _newclass:
        datatype = _swig_property(_myosmc.db_operation_datatype_get, _myosmc.db_operation_datatype_set)
    __swig_setmethods__["query"] = _myosmc.db_operation_query_set
    __swig_getmethods__["query"] = _myosmc.db_operation_query_get
    if _newclass:
        query = _swig_property(_myosmc.db_operation_query_get, _myosmc.db_operation_query_set)

    def __init__(self):
        this = _myosmc.new_db_operation()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _myosmc.delete_db_operation
    __del__ = lambda self: None
db_operation_swigregister = _myosmc.db_operation_swigregister
db_operation_swigregister(db_operation)


_myosmc.DATATYPE_INT_swigconstant(_myosmc)
DATATYPE_INT = _myosmc.DATATYPE_INT

_myosmc.DATATYPE_BOOL_swigconstant(_myosmc)
DATATYPE_BOOL = _myosmc.DATATYPE_BOOL

_myosmc.DATATYPE_STRING_swigconstant(_myosmc)
DATATYPE_STRING = _myosmc.DATATYPE_STRING

_myosmc.MYOSMC_SETTINGS_DB_PATH_swigconstant(_myosmc)
MYOSMC_SETTINGS_DB_PATH = _myosmc.MYOSMC_SETTINGS_DB_PATH
class CSettings(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSettings, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CSettings, name)
    __repr__ = _swig_repr
    __swig_getmethods__["setInt"] = lambda x: _myosmc.CSettings_setInt
    if _newclass:
        setInt = staticmethod(_myosmc.CSettings_setInt)

    def __init__(self):
        this = _myosmc.new_CSettings()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _myosmc.delete_CSettings
    __del__ = lambda self: None
CSettings_swigregister = _myosmc.CSettings_swigregister
CSettings_swigregister(CSettings)

def CSettings_setInt(key, value):
    return _myosmc.CSettings_setInt(key, value)
CSettings_setInt = _myosmc.CSettings_setInt

# This file is compatible with both classic and new-style classes.


