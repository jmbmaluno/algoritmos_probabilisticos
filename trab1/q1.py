import matplotlib.pyplot as plt
import numpy as np
from random import random, randint

#Criando Classe para gerar um G(n,p)
class Gnp:

    def __init__(self,n,p):
        #Cria a matriz de adjacencia n x n usando a biblioteca numpy
        self.matriz_adjacencia = np.zeros((n,n))
        self.n = n
        self.m = 0
        
        #Percorre a matriz e para par de vértice
        #Escolhe numa propabilidade p se esses dois vértices serão vizinhos
        for i in range(n):
            for j in range(i+1,n):

                if randint(1,p**-1) == 1:

                    #Como o grafo não é direcionado
                    #O valor da adjancencia de i para j deve ser igual
                    #ao valor de j para i
                    self.matriz_adjacencia[i][j] = 1
                    self.matriz_adjacencia[j][i] = 1
                    self.m = self.m + 1
                    
    def imprimir_matriz(self):
        print(self.matriz_adjacencia)


    def existe_aresta(self, i, j):
        return (self.matriz_adjacencia[i][j] == 1)
    
    def apagar_aresta(self, i, j):
        self.matriz_adjacencia[i][j] = 0
        self.matriz_adjacencia[j][i] = 0

    def criar_aresta(self, i, j):
        self.matriz_adjacencia[i][j] = 1
        self.matriz_adjacencia[j][i] = 1

    def qtde_arestas(self):
        return self.m

    def qtde_vertices(self):
        return self.n



#Encontrar o maior subconjunto bipartido de G
#Teorema é que existe um subgrafo bipartido de G que tenha m/2 arestas
def subgrafo_bipartido_grande(G):
    a = []
    b = []
    n = G.qtde_vertices()

    for i in range(n):
        if(randint(1,2) == 1):
            a.append(i)
        else:
            b.append(i)
    
    x = 0
    for i in range(n):
        for j in range(i+1, n):
            if G.existe_aresta(i,j) and ((a.count(i) == 1 and b.count(j) == 1) or (a.count(j) == 1 and b.count(i) == 1)):
                x = x + 1
    
    return x


def grafico_gnp(k, n, p):
    X = np.zeros(k)
    M = np.zeros(k)
    maior = 0 

    for i in range(k):
        g = Gnp(n,p)
        M[i] = g.qtde_arestas()

        for j in range(5):
            aux = subgrafo_bipartido_grande(g)
            if aux > maior:
                maior = aux

        X[i] = maior

    plt.plot(M,X)
    plt.grid(True)
    plt.ylabel("Qtde de arestas do subgrafo bipartido de G")
    plt.xlabel("Qtde de arestas de G")
    plt.show()


"""
# ------ MAIN ------- #
g = Gnp(10,1/2)
maior_subconjunto_bipartido(g)
"""


"""
TEMPLATE PARA PLOTAR OS GRAFICOS
plt.plot(t, t2)
plt.grid(True)
plt.ylabel("some numbers")
plt.show()
"""
