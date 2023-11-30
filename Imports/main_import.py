from Imports import mysql_import as mysql
from Imports import csv_import as csv
import commands as cmds

def Import():
    option = None
    while not (option == cmds.FROM_MYSQL or option == cmds.FROM_CSV):
        option = input(">> ")
    if option == cmds.FROM_MYSQL:
        return mysql.Import()
    elif option == cmds.FROM_CSV:
        return csv.Import()
    return True