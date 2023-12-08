from Connections import mysql_connection as mysqlc
import main
import mysql.connector
import commands as cmds
from Connections import mysql_connection as connect 

def mysql_check_table(table:str,cursor):
    if table == cmds.ALL:
        return True
    else:
        try:
            query = ('select * from {}').format(table)
            cursor.execute(query)
            return True
        except:
            return False

def show_tables(cursor):
    print("\nTables in {}:".format(connect.database_glob))
    cursor.execute("show tables;")
    for row in cursor:
        for key in row:
            print('* '+row[key].strip("'"))

def show_database():
    conn = mysql.connector.connect (user=connect.user_glob, password=connect.password_glob,
                               host=connect.host_glob,buffered=True)
    cursor = conn.cursor()
    databases = ("show databases;")
    cursor.execute(databases)
    print("Schemas in MySQL server:")
    for (databases) in cursor:
        print ('* '+databases[0])

def mysqlimport():
    print("")
    connect.host_glob = input('Host: ')
    #connect.database_glob = input('Database: ')
    connect.user_glob = input('User: ')
    connect.password_glob = input('Password: ')
    print("")
    
    show_database()
    conn = None
    while not conn :
        print("\nSelect database: ")
        connect.database_glob = input('>> ')
        conn = connect.mysqlconnect() 
   
    cursor = conn.cursor(dictionary=True,buffered=True)
    
    #show_tables(cursor)
    #print('Type the table to import : ')
    #table = input('>> ')
    table = cmds.ALL

    while True:
        if mysql_check_table(table,cursor) :
            break
        else :
            print("error : Table not exists in server")
            print('Type the table to import : ')
            table = input('>> ')
        
    headers = cursor.column_names
    list_tables_cursor = []
    list_tables_dict = []
    list_tables_dict_header = ["name", "filename"]
    if table == cmds.ALL:
        print()
        cursor.execute("show tables;")
        for row in cursor:
            for key in row:
                list_tables_cursor.append(row[key].strip("'"))

        for table_name in list_tables_cursor:

            list_tables_dict_item = {list_tables_dict_header[0] : table_name, list_tables_dict_header[1] : table_name + ".csv"}
            list_tables_dict.append({})
            list_tables_dict[len(list_tables_dict) - 1] = list_tables_dict_item.copy()

            for key in table_name:
                mysql_check_table(table_name,cursor)
                headers = cursor.column_names
                main.write_csv(cursor=cursor, colum_names=headers, bdname=connect.database_glob, filename=table_name)
        
        main.write_csv(cursor=list_tables_dict, colum_names=list_tables_dict_header, bdname=connect.database_glob, filename=cmds.LIST_TABLES_FILE_NAME)    
    else:
        main.write_csv(cursor=cursor, colum_names=headers, bdname=connect.database_glob, filename=table)
            
    cursor.close()
    conn.close()

    return True