import csv
import commands as cmds
import os

def delete(command:str):     
         
    listacomandos = command.split('-')      
    if listacomandos[2] != cmds.FROM: 
        print("erro: comando errado ou inválido")
        return
    else:
        tabela = os.path.join("Files", "bdtest", listacomandos[3])
        lista = [listacomandos[1]]
        
        with open(tabela, 'r') as f:
            linhas = csv.reader(f, delimiter=';')
            lst = list((linhas))        
               
        if lista in lst:
            lst.remove(lista)   
            #altera a lista para uma lista de inteiros por conflito com (')
            lista_int = [[int(num) for num in s[0].split(',')] for s in lst]
            
            with open(tabela, 'w', newline='') as f: 
                writer = csv.writer(f)
                writer.writerows(lista_int)
        else:
            print("Nenhuma linha correspondente")
            return