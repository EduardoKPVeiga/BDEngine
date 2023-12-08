import os

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# use bancoTeste
# pegue (campo1,campo2,campo3) de 'tabela' onde 'campo' 'condicao' 'valor'
# pegue * de 'tabela'
# ponha-88888,KKKKKKK,PPPPPPP,0000.98-em-TESTE.csv
# pegue * de [tabela1],[tabela2] junte usando [campo]
#
# atualize-tabela-com-dados-onde-condicao
# remova-aTabela-teste.csv
# remova-banco (apaga o banco em uso)
# remova-222,111,222,aaa-de-teste.csv

BDName = " "
BD_FILE_PATH = "Files/"
ABS_FILE_PATH = os.path.join(os.path.dirname("__main__"), BD_FILE_PATH)
LIST_TABLES_FILE_NAME = "list_tables"

# DB Language
SELECT = "pegue"
INTO = "em"
DELETE = "remova"
DATABASE = "banco"
TABLE = "tabela"
DELETE_TABLE = "aTabela"
FROM = "de"
WHERE = "onde"
ORDER = "ordene"
BY = "com"
ASC = "asc"
DESC = "desc"
USE = "use"
DATA = "dados"
INSERT = "ponha"
JOIN = "junte"
USING = "usando"
UPDATE = "atualize"

# CMD
IMPORT = "import"
QUERY = "query"
EXIT = "exit"
FROM_MYSQL = FROM + " mysql"
FROM_CSV = FROM + " csv"
ALL = "todas"
