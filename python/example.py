#!/bin/python2

# (c) 2016 Sam Nazarko
# email@samnazarko.co.uk

import os
import myosmc

# Get the short version of OSMC

#try:
#    print myosmc.CUtils_getOSMCVersionShort()
#except myosmc.OSMCUtilsException as e:
#    print e.what()

# Save an integer setting

myosmc.CSettings_setInt("updateHour", 15)


# Get a string setting or update it

# See if a key is set, and what kind of setting it is, bool etc

