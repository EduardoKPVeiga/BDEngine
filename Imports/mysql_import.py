from Connections import mysql_connection as mysqlc
import commands as cmds
import xml.etree.ElementTree as ET
import os
import csv

list_tables = []

def Import():
    print("")
    host = input('Host: ')
    database = input('Database: ')
    user = input('User: ')
    password = input('Password: ')
    print("")

    print("Connecting to database...\n")
    if mysqlc.connect(host, database, user, password):
        print("Connected.")
    else:
        print("\nReturning to main menu...\n")
        return True

    print("")
    os.system("mysqldump -u " + user + " --password=" + password + " -h " + host + " --xml " + database + " > Files/" + database + ".xml")

    script_dir = os.path.dirname("__main__")
    dir_path = os.path.join(script_dir, cmds.BD_FILE_PATH)
    if os.path.exists(dir_path) == False:
        os.mkdir(dir_path)
    ConvertXmlToCsv(database)
    CreateListTables()

    return True

def ConvertXmlToCsv(database : str):
    BDxml_tree = ET.parse(cmds.BD_FILE_PATH + database + '.xml')
    BDxml_root = BDxml_tree.find("database")

    # Save CSV Header of each table
    table_header_matrix = []
    table_header_line = []
    table_name_vector = []
    
    for table_structure in BDxml_root.findall('table_structure'):
        table_header_matrix.append([])
        list_tables.append(table_structure.get('name'))

    cont = 0
    for table_structure in BDxml_root.findall('table_structure'):
        table_name_vector.append(table_structure.get('name'))

        for field in table_structure.findall('field'):
            table_header_line.append(field.get('Field'))

        table_header_matrix[cont] = table_header_line.copy()
        cont += 1
        table_header_line.clear()

    # Save CSV with data
    table_data_matrix = []
    table_data_line = []
    cont_data = 0
    cont = 0
    for table_data in BDxml_root.findall('table_data'):
        for row in table_data.findall('row'):
            table_data_matrix.append([])

        for row in table_data.findall('row'):
            for field in row.findall('field'):
                table_data_line.append(field.text)

            table_data_matrix[cont_data] = table_data_line.copy()
            table_data_line.clear()
            cont_data += 1

        path = os.path.join(cmds.BD_FILE_PATH, database)
        ConvertMatrixIntoCsv(table_matrix=table_data_matrix, fields_name_vector=table_header_matrix[cont], filepath=path, filename=table_name_vector[cont])
        table_data_matrix.clear()
        cont_data = 0
        cont += 1

def ConvertMatrixIntoCsv(table_matrix, fields_name_vector: list, filepath: str, filename: str):
    script_dir = os.path.dirname("__main__")
    name = filename + ".csv"
    abs_file_path = os.path.join(script_dir, filepath)

    with open(abs_file_path + "/" + name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields_name_vector)
        dict_to_write = {}
        writer.writeheader()

        for row in table_matrix:
            for i in range(len(fields_name_vector)):
                dict_to_write[fields_name_vector[i]] = row[i]

            writer.writerow(dict_to_write)
            dict_to_write.clear()

def CreateListTables():
    script_dir = os.path.dirname("__main__")
    cmds.BDName = "bdtest"
    abs_file_path = os.path.join(script_dir, cmds.BD_FILE_PATH, cmds.BDName)

    field_names = ['name', 'filename']

    with open(abs_file_path + "/" + cmds.LIST_TABLES_FILE_NAME, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        for table in list_tables:
            writer.writerow({field_names[0]:table, field_names[1]:table + '.csv'})