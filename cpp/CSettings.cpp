/* (c) 2016 Sam Nazarko
 * email@samnazarko.co.uk */

#include "CSettings.h"
#include <stdio.h>
#include <cstdlib>
#include <iostream>

using namespace std;

/* Verifies that the Settings database exists with all structures. If it does not exist,
 * then this method will try and create it. */
bool CSettings::checkDB()
{
    /* Check if the userdata directory exists */
    sqlite3 *db;
    int rc;
    rc = sqlite3_open(MYOSMC_SETTINGS_DB_PATH, &db);
    if (rc)
        return false;
    sqlite3_stmt *stmt = NULL;

    char *sql = "CREATE TABLE IF NOT EXISTS intSettings  ("
                "key VARCHAR(32) NOT NULL PRIMARY KEY,"
                "value INT(32) NOT NULL"
                ");";
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK)
        return false;
    rc = sqlite3_step(stmt);
    if (rc != SQLITE_DONE)
    	return false;
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return true;
}

/* Performs one shot operation on database without retrieving any data */

/*void CSettings::oneshotDBOperation(char *stmt)
{

// move checkDB in to a functional call here

}*/

/* Performs an operation on the database */

/*void CSettings::*performDBOperation(db_operation operation)
{
    //return ((void*) 5);
}*/

/* Sets an integer of value and associates it with the given key name */
bool CSettings::setInt(char *key, int value)
{
	if (checkDB())
	{
    /* Do we have a value already? If so we need to update it */
    db_operation operation;
    operation.key = key;
    operation.value = (void*) value;
    operation.datatype = DATATYPE_STRING;
    operation.query = "SELECT setting_value FROM intSettings WHERE setting_key = \"test\"";
    checkDB();
    return true;
	}

    //bool performDBOperation()
}

/* Sets an boolean of value and associates it with the given key name */

/*bool CSettings::setBool(char *key, bool value)
{

}*/

/* Sets a string of value and associates it with the given key name */

/*bool CSettings::setString(char *key, char *value)
{

}*/

/* Retrieves the value of the integer mapped to key, if it exists and returns it */

/*int CSettings::getInt(char *key)
{

}*/

/* Retrieves the value of the boolean mapped to key, if it exists and returns it */

/*bool CSettings::getBool(char *key)
{

}*/

/* Retrieves the value of the string mapped to key, if it exists and returns it */

/*char CSettings::*getString(char *key)
{

}

/* Checks if a value is assigned to the key passed */

/*bool CSettings::isSet(char *key)
{

}*/
