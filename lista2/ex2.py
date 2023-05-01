#Atividade 2 da lista de funções 
import random
def verifica(i,j,n):
    if (i>0 and j>0 and n>0):
        if (i < n and j < n and i < j and n<=100):
            return True
def lista(k):
    lista=[]
    for i in range(k):
        num=random.randrange(0,100)
        lista.append(num) 
    return lista
def troca(x,y,lista):
    aux = lista[x-1]
    lista[x-1] = lista[y-1]
    lista[y-1] = aux
    return lista
#programa inicial
i=int(input("informe o numero i:"))
j=int(input("informe o numero j:"))
n=int(input("informe o numero n:"))
verd=verifica(i,j,n)
if verd == True:
    lista1=lista(n)
    print(lista1)
    print(troca(i,j,lista1))
else:
    print("Valores inválidos na entrada de dados")

