from graficos import plotar_grafo_q1, plotar_grafo_q2

print("1° Trabalho - Algoritmos Probabilísticos")
print("Q1 - Maior Peso do subgrafo bipartido")
print("-- A função implementada recebe um valor k de vértices para criação do grafo Gnp")
print("--Calcula o maior peso do subgrafo bipartido")
print("--Esse processo é feito de k até k+70 com paço 10")

k = int(input("Entre a quantidade de vértices: "))

plotar_grafo_q1(k)

print("\n\n Q2 - Maior conjunto independente")
k = int(input("Entre a quantidade de vértices: "))

plotar_grafo_q2(k)
