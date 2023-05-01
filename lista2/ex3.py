#Atividade 3 da lista de funções 
import random
def lista(n):
    lista=[]
    for i in range(n):
        num=random.randint(0,100)
        while num in lista:
            num=random.randint(0,100)
        lista.append(num) 
    return lista
def desvio(lista,n):
    lista.sort()
    media=sum(lista)/n
    soma_quadrados = 0
    for i in range(n):
        soma_quadrados = soma_quadrados + ((lista[i] - media) ** 2)
    variancia = soma_quadrados / (n-1)
    desvio_padrão=variancia**0.5
    return desvio_padrão,lista

n=int(input("Informe a quantidade de valores que você deseja dentro da lista: "))
dp,listaS=desvio(lista(n),n)
print(listaS)
print("O desvio padrão da lista é : {:.2f} ".format(dp))

