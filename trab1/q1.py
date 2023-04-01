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
                    x = random()
                    self.matriz_adjacencia[i][j] = x
                    self.matriz_adjacencia[j][i] = x
                    self.m = self.m + 1
                    
    def imprimir_matriz(self):
        print(self.matriz_adjacencia)


    def existe_aresta(self, i, j):
        return (self.matriz_adjacencia[i][j] > 0)

    def valor_aresta(self, i, j):
        return self.matriz_adjacencia[i][j]
    
    def qtde_arestas(self):
        return self.m

    def qtde_vertices(self):
        return self.n

    def peso_total(self):
        soma = 0
        for i in range (self.n):
            for j in range(i+1, self.n):
                soma = soma + self.valor_aresta(i,j)

        return soma



#Encontrar o maior subconjunto bipartido de G
#Teorema é que existe um subgrafo bipartido de G que tenha m/2 arestas
def peso_subgrafo_bipartido_grande(G):
    peso = 0
    n = G.qtde_vertices()
    a = []
    b = []

    for i in range(n):
        if(randint(0,1) == 0):
            a.append(i)
        else:
            b.append(i)
    
    print("lista a: ", a)
    print("lista b: ", b)

    for i in range(n):
        for j in range(i+1,n):
            if a.count(i) == 1 and b.count(j) == 1 or a.count(j) == 1 and b.count(i) == 1:
                peso = peso + G.valor_aresta(i,j)

    print("peso do subgrafo: ", peso)

    """
    plt.title("Subgrafo Bipartido Grande")
    plt.scatter(M,X, color = 'r')
    plt.grid(True)
    plt.ylabel("Peso total no subgrafo bipartido de G")
    plt.xlabel("Peso total de G")
    plt.show() """


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
