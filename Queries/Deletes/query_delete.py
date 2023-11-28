from Connections import mysql_connection
condition = 0
table_name = 0
stringdelete = "DELETE FROM "

def delete():
    
    table_name = input('table_name: ')
    condition = input('condition: ')



    mysql_connection.cursor.execute("DELETE FROM table_name WHERE condition")
    
    
    return