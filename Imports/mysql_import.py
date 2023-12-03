from Connections import mysql_connection as mysqlc
import main
import mysql.connector
import commands as cmds

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
    print("\nTables in {}:".format(database_glob))
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
    #database_glob = input('Database: ')
    user_glob = input('User: ')
    password_glob = input('Password: ')
    print("")
    
    show_database()
    conn = None
    while not conn :
        print("\nSelect database: ")
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
    list_tables_cursor = []
    if table == cmds.ALL:
        print()
        cursor.execute("show tables;")
        for row in cursor:
            for key in row:
                list_tables_cursor.append(row[key].strip("'"))

        for table_name in list_tables_cursor:
            for key in table_name:
                mysql_check_table(table_name,cursor)
                headers = cursor.column_names
                main.write_csv(cursor=cursor, colum_names=headers, bdname=database_glob, table_name=table_name)
                
    else:
        main.write_csv(cursor=cursor, colum_names=headers, bdname=database_glob, table_name=table)
            
    cursor.close()
    conn.close()

    return True