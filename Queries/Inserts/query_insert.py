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
        dados = [listacomandos[1].split(',')]
     
        with open(tabela, 'a', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for linha in dados:
                escritor_csv.writerow(linha)
        
def update(command:str):
    
    listacomandos = command.split('-')
    #atualize-tabela-com-dados-onde-condicao
    
    listacomandos = command.split('-')      
    if listacomandos[2] != cmds.WITH or listacomandos[4] != cmds.WHERE : 
        print("erro: comando errado ou inválido")
        return
    else:
        tabela = os.path.join("Files", cmds.BDName, listacomandos[1])
        lista_condicao = [listacomandos[5]]
        lista_dados = [listacomandos[3]]
        
        with open(tabela, 'r') as f:
            linhas = csv.reader(f, delimiter=';')
            lst = list((linhas))    
              
        if lista_condicao in lst:
            for i, sublista in enumerate(lst):
                if sublista == lista_condicao:
                    lst[i] = lista_dados
                    
            nova_lista_de_listas = []
            for sublist in lst:
                nova_sublista = [part.replace("'", "").replace('"', '') for item in sublist for part in item.split(',')]
                nova_lista_de_listas.append(nova_sublista)
            
            with open(tabela, 'w', newline='') as f: 
                writer = csv.writer(f)
                writer.writerows(nova_lista_de_listas)
        else:
            print("Nenhuma linha correspondente")
            return
    