from Imports import main_import
import commands as cmds

def main():
    # takes query from user
    answer = None
    while not (answer == cmds.import_cmds or answer == cmds.query_cmds or answer == cmds.exit_cmds):
        answer = input(">> ")
    if (answer == cmds.import_cmds):
        main_import.Import()
    elif (answer == cmds.query_cmds):
        print("query")
    elif (answer == cmds.exit_cmds):
        print("exit")
        return False
    
    return True

if __name__ == "__main__":
    main()