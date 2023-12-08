import commands as cmds
import csv
import os
from Queries.Searchs import query_search as search
from Queries.Inserts import query_insert
from Queries.Deletes import query_delete

def query(command):
    if command.find(cmds.USE) != -1: 
        BDName_start = command.find(cmds.USE) + len(cmds.USE) + 1
        if os.path.exists(cmds.ABS_FILE_PATH + "/" + command[BDName_start:]):
            cmds.BDName = command[BDName_start:]
            SaveDatabaseInRam()
        else:
            print("ERROR: invalid database")
    
    elif command.find(cmds.SELECT) != -1:
        if cmds.BDName != " ":
            return search.query(command)
        else:
            print("ERROR: no database selected")
    elif command.find(cmds.INSERT) != -1:
        if cmds.BDName != " ":
            query_insert.insert(command)
        else:
            print("ERROR: no database selected")
    elif command.find(cmds.DELETE) != -1:
        if command.find(cmds.DATABASE) != -1:
            print("Delete database")
            query_delete.deletedatabase(command)
            #remova-banco
        if command.find(cmds.DELETE_TABLE) != -1:
            print("Delete table")
            query_delete.deletetable(command)
            #remova-aTabela-nomedatabela
        if cmds.DELETE_TABLE not in command and cmds.DATABASE not in command:
            if cmds.BDName != " ":
                print("Remove from table")
                query_delete.delete(command)
            else:
                print("ERROR: no database selected")
    elif command.find(cmds.UPDATE) != -1:
        if cmds.BDName != " ":
            query_insert.update(command)
        else:
            print("ERROR: no database selected")
    elif command.find(cmds.EXIT) != -1:
        cmds.BDName = " "
        print("")
        return False
    return True

def SaveDatabaseInRam():
    script_dir = os.path.dirname("__main__")
    dir_path = os.path.join(script_dir, cmds.BD_FILE_PATH, cmds.BDName)
    if os.path.exists(dir_path) == False:
        os.mkdir(dir_path)

    table_select = []

    with open(dir_path + "/" + cmds.LIST_TABLES_FILE_NAME + ".csv", newline='') as csvfile_list_table:
        reader = csv.DictReader(csvfile_list_table)
        cont_tables = 0
        for row in reader:
            search.data_select.append([])
            search.list_tables.append(row.get('name'))
            with open(dir_path + "/" + row.get('filename'), newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cont = 0
                for row in reader:
                    table_select.append({})
                    table_select[cont] = row.copy()
                    cont += 1
                search.data_select[cont_tables] = table_select.copy()
                table_select.clear()
                cont_tables += 1
