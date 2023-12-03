import csv
import commands as cmds
import os

def delete(command:str):     
         
    listacomandos = command.split('-')      
    if listacomandos[2] != cmds.FROM: 
        print("erro: comando errado ou inválido")
        return
    else:
        tabela = os.path.join("Files", cmds.BDName, listacomandos[3])
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

def deletedatabase(command:str): 
    
    listacomandos = command.split('-')
    
    decisao = input("(are you sure? Y/N ) " + ">> ")
    
    if decisao == 'Y':
        #deleta
        print("deletando  " + cmds.BDName)
        try:
            os.removedirs(os.path.join("Files", cmds.BDName))
        except:
            print("path not found (DATABASE)!")
    elif decisao == 'N':
        return 
    else:
        print("Erro")
        return 
          

def deletetable(command:str): 
    
    listacomandos = command.split('-')
        
    decisao = input("(are you sure? Y/N ) " + ">> ")
    
    if decisao == 'Y':
        #deleta
        print("deletando" + listacomandos[2])
        try:
            os.remove(os.path.join("Files", cmds.BDName, listacomandos[2]))
        except:
            print("path not found (TABLE)!")
            return True
    elif decisao == 'N':
        return True
    else:
        print("Erro")
        return True
        
