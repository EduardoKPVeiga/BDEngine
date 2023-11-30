import xml.etree.ElementTree as ET
import commands as cmds
import numpy as np

BDxml_tree = 0
BDxml_root = 0

data_select = []
columns = []

def query(command):
    global data_select
    global columns
    
    data_select = []

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
        for table_data in BDxml_root.findall('table_data'):
            if table_data.get('name') == table_name:
                for row in table_data.findall('row'):
                    fields = []
                    for field in row.findall('field'):
                        fields.append(field.text)
                    data_select.append(fields)

                print(np.matrix(data_select))
                return True

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
    return True