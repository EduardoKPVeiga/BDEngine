from Imports import mysql_import as mysql
from Imports import csv_import as csv
import commands as cmds

def Import():

    option = None
    while not (option == cmds.from_mysql_cmds or option == cmds.from_postgres_cmds or option == cmds.from_csv_cmds):
        option = input(">> ")
    if option == cmds.from_mysql_cmds:
        mysql.Import()
    elif option == cmds.from_csv_cmds:
        csv.Import()
    return