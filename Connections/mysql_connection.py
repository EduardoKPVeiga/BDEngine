import mysql.connector
from mysql.connector import Error

connection = 0
cursor = 0

def connect(_host, _database, _user, _password):
    global connection
    try:
        connection = mysql.connector.connect(host = _host,
                                            database = _database,
                                            user = _user,
                                            password = _password)
    except Error as e:
        print("Error while connecting to MySQL", e)
    return

def disconnect():
    global cursor
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")