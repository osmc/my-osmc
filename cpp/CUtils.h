/* (c) 2016 Sam Nazarko
 * email@samnazarko.co.uk */

#ifndef CUTILS_H
#define CUTILS_H

#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <exception>

/* Device definitions. Use a bitmask to make it easy to evaluate across device revisions */

#define DEV_ID_VERO1 1 << 1
#define DEV_ID_VERO2 1 << 2
#define DEV_ID_BCM2835 1 << 3
#define DEV_ID_BCM2836 1 << 4
#define DEV_ID_APPLETV1 1 << 5
#define DEV_ID_PC 1 << 6
#define DEV_ID_UNKNOWN 1 << 31

class CUtils
{
public:
    static const char *getOSMCVersionShort();
    static const char *getOSMCVersionLong();
    static int getOSMCDevice();
    static bool isVero();
    static bool isRaspberryPi();
    static bool isAppleTV();
    static bool isPC();

private:
    static std::string getOSProperty(std::string property);
    static std::string getBootOption(std::string property);
};

/* An exception when CUtils::getOSProperty is unable to retrieve the desired property */

class NoOSPropertyException
{
public:

	NoOSPropertyException(const std::string& what) { this->eMsg = (std::string(what)); }
	const char * what() const throw() { return eMsg.c_str(); }
private:
	std::string eMsg;
};

#endif // CUTILS_H
