from q1 import *
from q2 import *


n = 100
d = 10

g = Gnm(n,d)

g.imprimir_matriz()

conjunto_independente_grande(g)

print(n/(2*d))

"""
g = Gnp(5,1/2)

g.imprimir_matriz()

print("peso total de g: ", g.peso_total())

peso_subgrafo_bipartido_grande(g)"""
