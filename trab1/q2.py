import numpy as np
from random import randint

class Gnm:

    def __init__(self,n,m):
        self.matriz_adjacencias = np.zeros((n,n))
        self.m = m
        self.n = n

        aux = m
        while aux > 0 :
            i = randint(0,n-1)
            j = randint(0,n-1)

            if i != j:
                self.matriz_adjacencias[i][j] = 1
                self.matriz_adjacencias[j][i] = 1
                aux = aux - 1

    def sao_vizinhos(self,v,u):
        return self.matriz_adjacencias[v][u] == 1

    def ordem(self):
        return self.n

    def imprimir_matriz(self):
        print(self.matriz_adjacencias)
    
#Retorna o vértice de maior grau do conjunto a
def maior_grau_conjunto(G,a):

    k = len(a)
    v = [0] * k

    maior_vertice = 0
    maior_grau = 0

    for i in range(k):
        for j in range(i+1,k):
           if g.sao_vizinhos(a[i],a[j]):
                v[i] = v[i] + 1
                v[j] = v[j] + 1

    for i in range(k):
        if v[i] > maior_grau:
            maior_grau = v[i]
            maior_vertice = i

    return maior_vertice

#retorna True se o conjunto a é um conjunto independente de G
def conjunto_eh_independente(G,a):

    k = len(a)

    for i in range(k):
        for j in range(i+1,k):
            if g.sao_vizinhos(a[i],a[j]):
                return False

    return True


#retorna o tamanho do maior conjunto independente de G
def conjunto_independente_grande(G,d):
    a = []
    
    for i in range(G.ordem()):
        if(randint(1,d) == 1):
            a.append(i)
    
    
    while conjunto_eh_independente(G,a) == False:
        v = maior_grau_conjunto(G,a)
        a.pop(v)

    print(len(a))

    


#------MAIN------#

d = 10
n = 100
m = n/2 * d

#Testando se m ultrapassa o limete maximo de arestas para n vertices
if m > (n*n - n)/2:
    print("m muito grande")

else:
    g = Gnm(n,m)

    g.imprimir_matriz()

    conjunto_independente_grande(g,d)
    
    print(n/(2*d))

