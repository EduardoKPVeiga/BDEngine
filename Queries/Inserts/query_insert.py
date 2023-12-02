import csv
import commands as cmds
import os

def insert(command:str):
     
    listacomandos = command.split('-')
    
    tabela = listacomandos[3]
           
    dados = [listacomandos[1].split(',')]
    
    if listacomandos[2] != cmds.INTO:
        print("Comando errado")
        return True
    
    else:     
        with open(tabela, 'a', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for linha in dados:
                escritor_csv.writerow(linha)