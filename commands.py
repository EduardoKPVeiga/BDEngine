import os

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# use bancoTeste
# pegue (campo1,campo2,campo3) de 'tabela' onde 'condicao'
# pegue * de 'tabela'
#
#
#

BDName = " "
BD_FILE_PATH = "Files/"
ABS_FILE_PATH = os.path.join(os.path.dirname("__main__"), BD_FILE_PATH)
LIST_TABLES_FILE_NAME = "list_tables.csv"

# SQL
SELECT = "pegue"
INSERT = "ponha"
DELETE = "remova"
DATABASE = "banco"
TABLE = "tabela"
DELETE_TABLE = DELETE + " " + TABLE
FROM = "de"
WHERE = "onde"
ORDER_BY = "ordene por"
USE = "use"

# CMD
IMPORT = "importar"
QUERY = "query"
EXIT = "exit"
FROM_MYSQL = FROM + " mysql"
FROM_CSV = FROM + " csv"