import csv
import commands as cmds
import os

def delete(command:str):     
         
    listacomandos = command.split('-')     
    tabela = listacomandos[3]  
    dados = [listacomandos[1]]
    
    with open(tabela, 'r') as f:
        linhas = csv.reader(f, delimiter=';')
        lst = list((linhas)) 
  
    lista = dados
            
    if lista in lst:
        lst.remove(lista)   
        
        lista_int = [[int(num) for num in s[0].split(',')] for s in lst]
        
        with open(tabela, 'w', newline='') as f: 
            writer = csv.writer(f)
            writer.writerows(lista_int)
    else:
        print("erro")
        return