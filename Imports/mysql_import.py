from Connections import mysql_connection as mysqlc
import commands as cmds
import xml.etree.ElementTree as ET
import os
import csv
import main

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


import mysql.connector
import os

database_glob = None
host_glob = None
user_glob = None
password_glob = None
port_glob = 3306

def mysqlconnect():
    conn_params = {
        'host':host_glob,
        'user':user_glob,
        'password':password_glob,
        'database': database_glob,
        'port': port_glob
    }

    try:
        db_connection=mysql.connector.connect(**conn_params)
    except:
        print("error : Schema not found")
        return False
    
    print('Connected to server!')
    return db_connection

def mysql_check_table(table:str,cursor):
    try:
        query = ('select * from {}').format(table)
        cursor.execute(query)
        return True
    except:
        return False

def show_tables(cursor):
    print("Tables in {}:".format(database_glob))
    cursor.execute("show tables;")
    for row in cursor:
        for key in row:
            print('* '+row[key].strip("'"))

def show_database():
    conn = mysql.connector.connect (user=user_glob, password=password_glob,
                               host=host_glob,buffered=True)
    cursor = conn.cursor()
    databases = ("show databases;")
    cursor.execute(databases)
    print("Schemas in MySQL server:")
    for (databases) in cursor:
        print ('* '+databases[0])

def mysqlimport():
    global database_glob
    global host_glob
    global user_glob
    global password_glob

    print("")
    host_glob = input('Host: ')
    database_glob = input('Database: ')
    user_glob = input('User: ')
    password_glob = input('Password: ')
    print("")
    
    show_database()
    conn = None
    while not conn :
        print("Select schema: ")
        database_glob = input('>> ')
        conn = mysqlconnect() 
   
    cursor = conn.cursor(dictionary=True,buffered=True)
    
    show_tables(cursor)
    print('Type the table to import : ')
    table = input('>> ')

    while True:
        if mysql_check_table(table,cursor) :
            break
        else :
            print("error : Table not exists in server")
            print('Type the table to import : ')
            table = input('>> ')
        
    headers = cursor.column_names
    main.write_csv(cursor=cursor, colum_names=headers, bdname=database_glob)
            
    cursor.close()
    conn.close()

    return True