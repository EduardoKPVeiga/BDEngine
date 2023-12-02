import commands as cmds
import csv
import os
from Queries.Searchs import query_search as search
from Queries.Inserts import query_insert
from Queries.Deletes import query_delete

def query(command):
    if command.find(cmds.USE) != -1: 
        BDName_start = command.find(cmds.USE) + len(cmds.USE) + 1
        cmds.BDName = command[BDName_start:]
        SaveDatabaseInRam()
    
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
            print("")
        elif command.find(cmds.DELETE_TABLE) != -1:
            print("Delete table")
        else:
            if cmds.BDName != " ":
                print("Remove from table")
                query_delete.delete(command)
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

    with open(dir_path + "/" + cmds.LIST_TABLES_FILE_NAME, newline='') as csvfile_list_table:
        reader = csv.DictReader(csvfile_list_table)
        cont_tables = 0
        for row in reader:
            search.data_select.append([])
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
