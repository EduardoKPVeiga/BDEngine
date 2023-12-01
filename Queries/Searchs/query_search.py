import commands as cmds
import csv
import numpy as np

BDxml_tree = 0
BDxml_root = 0

data_select = []
list_tables = []
columns = []

def query(command):
    global data_select
    global columns

    if command.find(" " + cmds.FROM + " ") == -1:
        print("ERROR: incorrect setence")
        return True
    
    list_words = command.split()

    table_name = ""
    getTableName = False
    for word in list_words:
        if word == cmds.FROM:
            getTableName = True
            continue
        if getTableName:
            table_name = word
            break

    if list_words[1] == "*" or list_words[1] == "(*)":
        for i in range(len(list_tables)):
            if list_tables[i] == table_name:
                print(np.matrix(data_select[i])) # melhorar o print
                return True

    # if list_words[1].find(")") != -1:
    #     if list_words[1].find("(") == -1:
    #         print("ERROR: incorrect setence")
    #         return True

    # if list_words[1].find("(") != -1:
    #     if list_words[1].find(")") == -1:
    #         print("ERROR: incorrect setence")
    #         return True

    #     else:
    #         columns = list_words[1].split(",")
    #         columns[0] = columns[0].replace("(", "")
    #         columns[len(columns) - 1] = columns[len(columns) - 1].replace(")", "")

    #         for j in columns:
    #             print(j)
    return True