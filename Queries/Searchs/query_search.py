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
                WhereCondition(matrix=data_select[i], command=list_words)
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
                        fields_select.append({})
                        for key in line:
                            for field in list_fields:
                                if key == field:
                                    fields_select[cont][field] = line[key]
                        cont += 1
                    WhereCondition(matrix=fields_select, command=list_words)
                    return True
    return True

def WhereCondition(matrix:[{}],command:[]):
    has_where = False
    where_position = -1
    for i in range(len(command)):
        if command[i] == cmds.WHERE:
            has_where = True
            where_position = i
            break

    if has_where:
        field = command[where_position + 1]
        operator = command[where_position + 2]
        value = command[where_position + 3]
        value_is_word = False

        if value.find('"') != -1:
            value_is_word = True
        value = value.replace('"','')

        matrix_aux = matrix.copy()

        for line in matrix:
            for item in line:
                if item == field:

                    item_for_comparison = 0
                    value_for_comparison = 0

                    if value_is_word == False:
                        item_for_comparison = float(line.get(item))
                        value_for_comparison = float(value)
                    else:
                        item_for_comparison = line.get(item)
                        value_for_comparison = value

                    if operator == "=":
                        if item_for_comparison != value_for_comparison:
                            matrix_aux.remove(line)

                    elif operator == "!=":
                        if item_for_comparison == value_for_comparison:
                            matrix_aux.remove(line)

                    elif operator == ">":
                        try:
                            if item_for_comparison <= value_for_comparison:
                                matrix_aux.remove(line)
                        except:
                            continue

                    elif operator == "<":
                        try:
                            if item_for_comparison >= value_for_comparison:
                                matrix_aux.remove(line)
                        except:
                            continue

                    elif operator == "<=":
                        try:
                            if item_for_comparison > value_for_comparison:
                                matrix_aux.remove(line)
                        except:
                            continue

                    elif operator == ">=":
                        try:
                            if item_for_comparison < value_for_comparison:
                                matrix_aux.remove(line)
                        except:
                            continue

    PrintTable(matrix_aux)

def PrintTable(matrix:[{}]):
    table_line_num = len(matrix)
    table_column_num = len(matrix[0])
    print(np.matrix(matrix))