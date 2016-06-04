#!/bin/python2

# (c) 2016 Sam Nazarko
# email@samnazarko.co.uk

import os
import myosmc

# Get the short version of OSMC

try:
    print myosmc.CUtils_getOSMCVersionShort()
except myosmc.NoOSPropertyException as e:
    print e.what()

