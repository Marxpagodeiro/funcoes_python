#Atividade 5 da lista de funções 
import random
def lista(n):
    lista=[]
    lista_ordem=[]
    for i in range(n):
        num=random.randint(0,100)
        while num in lista:
            num=random.randint(0,100)
        lista.append(num)
    lista_orginal=lista.copy()
    for j in range(n):
        menor_valor=min(lista)
        lista_ordem.append(menor_valor)
        lista.remove(menor_valor)
    return lista_orginal,lista_ordem

n=int(input("Informe a quantidade de valores que você deseja dentro da lista: "))
lista_original,lista_ordem=lista(n)
print("lista original: ",lista_original,"\nlista em ordem crescente: ",lista_ordem)