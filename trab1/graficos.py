from q1 import *
from q2 import *
import matplotlib.pyplot as plt

#O maior peso encontrado rodando o algoritmo k vezes
def maior_peso(g,k):
    maior = 0.0

    for i in range(k):
        x = peso_subgrafo_bipartido_grande(g)
        if x > maior:
            maior = x

    return maior



fig,axes = plt.subplots(ncols = 3, nrows = 2)
x = 0
y = 0

for j in range(10,70,10):
    axes[x,y].set_title("Para n = " +  str(j))
    axes[x,y].grid(True)

    a = []
    b = []
    for i in range(5):
        g = Gnp(j,1/2)
        b.append(g.peso_total())
        a.append(maior_peso(g,5))

        print("O peso total de G é: ", g.peso_total())
        print("O maior foi: ", maior_peso(g,5))
    
    axes[x,y].plot(a,b)
    axes[x,y].set_xlabel("Peso total")
    axes[x,y].set_ylabel("Maior Peso encontrado")
    axes[x,y].set_xlim(min(a), max(a))
    axes[x,y].set_ylim(min(b), max(b))
    
    if(y < 2):
        y = y + 1
    else:
        if(x < 1):
            y = 0
            x = x + 1

plt.subplots_adjust(wspace = 0.3, hspace = 0.5)
plt.show()
