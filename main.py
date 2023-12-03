from Imports import main_import
from Queries import query_main
import commands as cmds
import csv
import os

def main():
    # takes query from user
    answer = None
    while not (answer == cmds.IMPORT or answer == cmds.INSERT or answer == cmds.QUERY or answer == cmds.EXIT):
        print("Select action (" + cmds.IMPORT + ", " + cmds.QUERY + ", " + cmds.EXIT + "):")
        answer = input(">> ")
    if (answer == cmds.IMPORT):
        return main_import.Import()
    elif (answer == cmds.QUERY):
        query_running = True
        while query_running:
            command = input("(" + cmds.BDName + ") " + ">> ")
            query_running = query_main.query(command)
    elif (answer == cmds.EXIT):
        print("Bye.")
        return False
    return True

if __name__ == "__main__":
    main_running = True
    while main_running == True:
        main_running = main()

def write_csv(cursor, colum_names:list, bdname:str, table_name:str) -> bool:
    path_for_file = os.path.join(cmds.ABS_FILE_PATH, bdname)
    table_data = []

    for row in cursor:
        table_data.append(row)

    # headers = cursor.column_names
    if os.path.exists(path_for_file) == False:
        os.mkdir(path_for_file)

    path_for_file = os.path.join(path_for_file, table_name + '.csv')

    with open(path_for_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colum_names)
        writer.writeheader()
        writer.writerows(table_data)