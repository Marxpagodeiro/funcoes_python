#Atividade 4 da lista de funções 
import random
def lista(k):
    lista=[]
    for i in range(k):
        num=random.randrange(0,100)
        lista.append(num) 
    return lista
def acumolo(lista,n):
    soma=0
    lista_nova=[]
    for i in range(n):
        soma += lista[i]
        lista_nova.append(soma)
    return lista_nova

n=int(input("Informe a quantidade de valores que você deseja dentro da lista: "))
lista_entrada=lista(n)
lista_saida=acumolo(lista_entrada,n)
print("Entrada",lista_entrada)
print("Saida",lista_saida)