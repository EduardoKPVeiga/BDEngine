# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# use bancoTeste
# pegue (campo1,campo2,campo3) de 'tabela' onde 'condicao'
# pegue * de 'tabela'
# ponha-88888,KKKKKKK,PPPPPPP,0000.98-em-TESTE.csv
# 
#

# remova-222,111,222,aaa-de-teste.csv

BDName = " "
BD_FILE_PATH = "Files/"
LIST_TABLES_FILE_NAME = "list_tables.csv"

# SQL
SELECT = "pegue"
INTO = "em"
DELETE = "remova"
DATABASE = "banco"
TABLE = "tabela"
DELETE_TABLE = "aTabela"
FROM = "de"
WHERE = "onde"
ORDER_BY = "ordene por"
USE = "use"
DATA = "dados"

# CMD
INSERT = "ponha"
IMPORT = "import"
QUERY = "query"
EXIT = "exit"
FROM_MYSQL = FROM + " mysql"
FROM_CSV = FROM + " csv"