/* (c) 2016 Sam Nazarko
 * email@samnazarko.co.uk */

#include "CUtils.h"
#include "exception"

using namespace std;

/* Returns an OS property from /etc/os-release, e.g. VERSION_ID */

string CUtils::getOSProperty(string property)
{
	ifstream releaseFile;
	string line;
	int offset;
	bool foundLine = false;
	releaseFile.open("/etc/os-releases", fstream::in);
	if (releaseFile.is_open())
	{
		while (!releaseFile.eof())
		{
			getline(releaseFile, line);
			offset = line.find(property, 0);
			if (offset != string::npos)
				/* Next character needs to be an = or we have a substring, i.e. VERSION being a substitute of VERSION_ID, but also a
				 * separate property */
				if (line.at(offset + property.size()) == '=')
				{
					foundLine = true;
					/* Clean up */
					line = line.substr((offset + property.size() +1 ), line.size());
					/* Could erase + remove here */
					if (line.at(0) = '"')
						return line.substr(1, std::distance(line.begin() + 1, line.end() - 1));
					else
						return line;
				}
		}
		releaseFile.close();
		if (! foundLine)
			throw NoOSPropertyException("Could not find the property " + property + " in /etc/os-release");
	}
	else
		throw NoOSPropertyException("Could not open /etc/os-release");
}

/* Returns the value of a /proc/cmdline property, e.g. osmcdev */

string CUtils::getBootOption(string property)
{
	ifstream cmdlineFile;
	string cmdline;
	string buffer;
	cmdlineFile.open("/proc/cmdline", fstream::in);

	if (cmdlineFile.is_open())
	{
		/* Split by spaces */
		getline(cmdlineFile, cmdline);
		istringstream ss(cmdline);
		vector<string> parameters;
		while (ss >> buffer)
			parameters.push_back(buffer);
		cmdlineFile.close();
		for (int i = 0; i < parameters.size(); i++)
		{
			int offset;
			string parameter = parameters.at(i);
			/* Find parameter we want */
			offset = parameter.find(property);
			if (offset != string::npos)
			{
				/* Look for first =, return everything after if it matches */
				if (parameter.at(offset + property.size()) == '=')
					return(parameter.substr((offset + property.size() + 1), parameter.size()));
				else
					/* No equals, just return true */
					return("true");
			}
		}
		/* If we are here, we have not found a matching property */
		throw NoBootOptionException("Could not find the property" + property + " in /proc/cmdline");
	}
	else
		throw NoBootOptionException("Could not open /proc/cmdline");
}

/* Returns the short version string of OSMC,
 * which is the VERSION_ID property retrieved from /etc/os-release, e.g
 * "2016.02-1" */

const char *CUtils::getOSMCVersionShort()
{
	return getOSProperty("VERSION_ID").c_str();
}

/* Returns the long version string of OSMC,
 * which is the VERSION property from /etc/os-release, e.g.
 * "February 2016" */

const char *CUtils::getOSMCVersionLong()
{
	return getOSProperty("VERSION").c_str();
}

/* Returns the device that OSMC is running on */

int CUtils::getOSMCDevice()
{
	string deviceVersion = getBootOption("osmcdev");
	if (deviceVersion == "rbp1")
		return DEV_ID_BCM2835;
	if (deviceVersion == "rbp2")
		return DEV_ID_BCM2836;
	if (deviceVersion == "vero1")
		return DEV_ID_VERO1;
	if (deviceVersion == "vero2")
		return DEV_ID_VERO2;
	/* If we are here, we did get a boot option, but this version of My OSMC does not recognise the device */
	throw UnknownDeviceException("Could not identify the device OSMC is running on. Is My OSMC up to date?");
}

/* Returns true if My OSMC is being invoked on a Vero device */

bool CUtils::isVero()
{
	return getOSMCDevice() & (DEV_ID_VERO1 | DEV_ID_VERO2);
}

/* Returns true if My OSMC is being invoked on a Raspberry Pi device */

bool CUtils::isRaspberryPi()
{
	return (getOSMCDevice() & (DEV_ID_BCM2835 | DEV_ID_BCM2836));
}

/* Returns true if My OSMC is being invoked on an Apple TV device */

bool CUtils::isAppleTV()
{
	return (getOSMCDevice() & (DEV_ID_APPLETV1));
}

bool CUtils::isPC()
{
	return (getOSMCDevice() & (DEV_ID_PC));
}
