import xml.etree.ElementTree as ET
import commands as cmds

def query(command):
    list_words = command.split()

    if list_words[1].find(")") != -1:
        if list_words[1].find("(") == -1:
            print("ERROR: incorrect setence")
            return True

    if list_words[1].find("(") != -1:
        if list_words[1].find(")") == -1:
            print("ERROR: incorrect setence")
            return True

        else:
            columns = list_words[1].split(",")
            columns[0] = columns[0].replace("(", "")
            columns[len(columns) - 1] = columns[len(columns) - 1].replace(")", "")

            for j in columns:
                print(j)

    else:
        print("ALL")
        
    return True