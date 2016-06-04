/* (c) 2016 Sam Nazarko
 * email@samnazarko.co.uk */

#ifndef CSETTINGS_H
#define CSETTINGS_H

#include <string>
#include <sqlite3.h>

typedef struct db_operation
{
    char *key;
    void *value;
    int datatype;
    char *query;
} db_operation;

#define DATATYPE_INT 1
#define DATATYPE_BOOL 2
#define DATATYPE_STRING 3

#define MYOSMC_SETTINGS_DB_PATH "/home/osmc/.myosmc/userdata/osmc_settings.db"

class CSettings
{
public:
    static bool setInt(char *key, int value);
  /*  static bool setBool(char *key, bool value);
    static bool setString(char *key, char *value);
    static int getInt(char *key);
    static bool getBool(char *key);
    static char *getString(char *key);
    static bool isSet(char *key);*/
    //static char[] getSettingList();

private:
    static bool checkDB();
 /*   static bool createDatabase();
    static bool doesDatabaseExist();
    static (void *) executeQuery();*/
};

#endif // CSETTINGS_H
