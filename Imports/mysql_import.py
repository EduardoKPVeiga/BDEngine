from Connections import mysql_connection as mysqlc
import os

def Import():

    print("")
    host = input('Host: ')
    database = input('Database: ')
    user = input('User: ')
    password = input('Password: ')
    print("")

    print("Connecting to database...\n")
    if mysqlc.connect(host, database, user, password):
        print("Connected.")
    else:
        print("\nReturning to main menu...\n")
        return True

    print("")
    filename = input('Filename: ')
    os.system("mysqldump -u " + user + " --password=" + password + " -h " + host + " --xml " + database + " > Files/" + filename + ".xml")
    return True