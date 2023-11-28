from Connections import mysql_connection as mysqlc
import os

def Import():

    print("")
    host = input('Host: ')
    database = input('Database: ')
    user = input('User: ')
    password = input('Password: ')
    print("")

    print("Connecting to database...")
    mysqlc.connect(host, database, user, password)
    print("Connected.")

    print("")
    filename = input('Filename: ')
    os.system("mysqldump -u " + user + " --password=" + password + " -h " + host + " --xml " + database + " > Files/" + filename + ".xml")
    return