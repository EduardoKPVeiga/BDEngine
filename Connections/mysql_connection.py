import mysql.connector
from mysql.connector import Error

connection = 0
cursor = 0

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