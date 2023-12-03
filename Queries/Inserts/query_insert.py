import csv
import commands as cmds
import os

def insert(command:str):
     
    listacomandos = command.split('-')
    if listacomandos[2] != cmds.INTO:
        print("erro: comando errado ou inválido")
        return
    else:
        tabela = os.path.join("Files", cmds.BDName, listacomandos[3])
        #testar se a linha existe?
        dados = [listacomandos[1].split(',')]
     
        with open(tabela, 'a', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for linha in dados:
                escritor_csv.writerow(linha)