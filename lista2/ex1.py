#Atividade 1 da lista de funções 
import random
def lista(n):
    lista=[]
    for i in range(n):
        num=round(random.uniform(0,100),2)
        lista.append(num) 
    return lista
def mediamedianac(lista,n):
    soma=sum(lista)
    media=soma/n
    lista.sort()
    if n%2 == 0:
        meio=n/2
        valor_centro1=lista[int(meio)]
        valor_centro2=lista[int(meio)-1]
        mediana=(valor_centro1+valor_centro2)/2
    else:
        valor_central=lista[int((n/2))]
        mediana=valor_central
    return lista,media,mediana

n=int(input("Informe a quantidade de valores que você deseja dentro da lista: "))
lista_ordem,media,mediana=mediamedianac(lista(n),n)
print("A media da lista de {} valores em ordem crescente {} é {:.2f} e a mediana é {:.2f}".format(n,lista_ordem,media,mediana))

