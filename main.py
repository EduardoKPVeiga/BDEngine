from Imports import main_import
from Queries import query_main
import commands as cmds

def main():
    # takes query from user
    answer = None
    while not (answer == cmds.IMPORT or answer == cmds.QUERY or answer == cmds.EXIT):
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