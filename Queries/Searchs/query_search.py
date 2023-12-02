import commands as cmds
import numpy as np
import string

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
                matrix_aux = WhereCondition(matrix=data_select[i], command=list_words)
                matrix_aux = OrderByCondition(matrix=matrix_aux, command=list_words)
                PrintTable(matrix_aux)

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

            # Verifica se a tabela existe
            for i in range(len(list_tables)):
                if list_tables[i] == table_name:
                    cont = 0

                    # Seleciona a matriz que corresponde a tabela
                    for line in data_select[i]:
                        fields_select.append({})
                        for key in line:
                            for field in list_fields:
                                if key == field:
                                    fields_select[cont][field] = line[key]
                        cont += 1

                    # Verifica e trata os comandos 'where' e 'order by'
                    matrix_aux = WhereCondition(matrix=fields_select, command=list_words)
                    matrix_aux = OrderByCondition(matrix=matrix_aux, command=list_words)

                    PrintTable(matrix_aux)
                    return True
    return True

def WhereCondition(matrix:[{}],command:[]) -> [{}]:

    # Verifica se o comando possui 'where'
    has_where = False
    where_position = -1
    for i in range(len(command)):
        if command[i] == cmds.WHERE:
            has_where = True
            where_position = i
            break

    matrix_aux = matrix.copy()

    if has_where:
        field = command[where_position + 1]
        operator = command[where_position + 2]
        value = command[where_position + 3]
        value_is_word = False

        # Verifica se o valor passado na condição é string
        if value.find('"') != -1:
            value_is_word = True
        value = value.replace('"','')

        for line in matrix:
            for item in line:

                # Procura o campo da condição ('where')
                if item == field:

                    item_for_comparison = 0
                    value_for_comparison = 0

                    # Se não é uma string, convert para float
                    if value_is_word == False:
                        item_for_comparison = float(line.get(item))
                        value_for_comparison = float(value)
                    else:
                        item_for_comparison = line.get(item)
                        value_for_comparison = value

                    # Operações aceitas pelo 'where'
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

    return matrix_aux

def OrderByCondition(matrix:[{}],command:[]) -> [{}]:

    # Verifica se o comando possui 'order by'
    has_order = False
    order_position = -1
    for i in range(len(command)):
        if command[i] == cmds.ORDER:
            has_order = True
            order_position = i
            break

    if has_order: 
        has_by = True
        for i in range(len(command)):
            if command[i] == cmds.BY:
                has_by = True
                break

        if has_by:
            field = command[order_position + 2]

            # Verifica se é ascendente ou descendente
            reverse = False
            if len(command) > order_position + 3:
                if command[order_position + 3] == cmds.DESC:
                    reverse = True

            value = matrix[0].get(field)
            is_string = False
            for letter in value:
                if letter in string.ascii_letters:
                    is_string = True

            if is_string == False:
                matrix = sorted(matrix, key=lambda d: float(d[field]), reverse=reverse)
            else:
                matrix = sorted(matrix, key=lambda d: d[field], reverse=reverse)
        
        else:
            print("ERROR: invalid command")
            return []

    return matrix

def PrintTable(matrix:[{}]):
    table_line_num = len(matrix)
    table_column_num = len(matrix[0])
    print(np.matrix(matrix))