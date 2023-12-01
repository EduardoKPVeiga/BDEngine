import xml.etree.ElementTree as ET
import csv
import commands as cmds

def insert():
   
    tabela = input("(" + cmds.TABLE + ") " + ">> ")
    
    #[[00000,'AAAAAAA','BBBBBBB',0000.00]] tipo esperado
    
    dados = input("(" + cmds.DATA + ") " + ">> ") 
    
    print(dados, tabela)
    
    with open(tabela, 'a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for linha in dados:
            escritor_csv.writerow(linha)