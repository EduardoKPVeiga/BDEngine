import commands as cmds
import csv
import numpy as np

BDxml_tree = 0
BDxml_root = 0

data_select = []
list_tables = []

def query(command:str) -> bool:
    global data_select

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

    # pegue * de [table_name]
    if list_words[1] == "*" or list_words[1] == "(*)":
        for i in range(len(list_tables)):
            if list_tables[i] == table_name:
                print(np.matrix(data_select[i])) # melhorar o print
                return True

    # pegue (field1,field2,...) de [table_name]
    if list_words[1].find(")") != -1:
        if list_words[1].find("(") == -1:
            print("ERROR: incorrect setence")
            return True

    if list_words[1].find("(") != -1:
        if list_words[1].find(")") == -1:
            print("ERROR: incorrect setence")
            return True

        else:
            fields = list_words[1].replace('(','')
            fields = fields.replace(')','')
            list_fields = fields.split(',')

            fields_select = []

            for i in range(len(list_tables)):
                if list_tables[i] == table_name:
                    cont = 0
                    for line in data_select[i]:
                        fields_select.append([])
                        for key in line:
                            for field in list_fields:
                                if key == field:
                                    fields_select[cont].append(line[key])
                        cont += 1
                    print(np.matrix(fields_select))
                    return True
    return True