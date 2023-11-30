import commands as cmds
from Queries.Searchs import query_search as search

def query(command):
    if command.find(cmds.USE) != -1:
        BDName_start = command.find(cmds.USE) + len(cmds.USE) + 1
        cmds.BDName = command[BDName_start:]
    
    elif command.find(cmds.SELECT) != -1:
        if cmds.BDName != " ":
            search.query(command)
        else:
            print("ERROR: no database selected")

    elif command.find(cmds.INSERT) != -1:
        if cmds.BDName != " ":
            print("Insert")
        else:
            print("ERROR: no database selected")
    
    elif command.find(cmds.DELETE) != -1:
        if command.find(cmds.DATABASE) != -1:
            print("Delete database")
        elif command.find(cmds.DELETE_TABLE) != -1:
            print("Delete table")
        else:
            if cmds.BDName != " ":
                print("Remove from table")
            else:
                print("ERROR: no database selected")
    
    elif command.find(cmds.EXIT) != -1:
        cmds.BDName = " "
        print("")
        return False
    return True