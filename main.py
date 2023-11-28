from Imports import main_import
import commands as cmds

def main():
    # takes query from user
    answer = None
    while not (answer == cmds.import_cmds or answer == cmds.query_cmds or answer == cmds.exit_cmds):
        print("Select action (" + cmds.import_cmds + ", " + cmds.query_cmds + ", " + cmds.exit_cmds + "):")
        answer = input(">> ")
    if (answer == cmds.import_cmds):
        if main_import.Import() == False:
            return False
    elif (answer == cmds.query_cmds):
        print("query")
    elif (answer == cmds.exit_cmds):
        print("exit")
        return False
    
    return True

if __name__ == "__main__":
    main_success = False
    while main_success == False:
        main_success = main()