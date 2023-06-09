from q1 import *
from q2 import *
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from random import randint

#O maior peso encontrado rodando o algoritmo k vezes
def maior_peso(g,k):
    maior = 0.0

    for i in range(k):
        x = peso_subgrafo_bipartido_grande(g)
        if x > maior:
            maior = x

    return maior


def plotar_grafo_q1(k):
    fig,axes = plt.subplots(ncols = 3, nrows = 2)
    x = 0
    y = 0
    fig.suptitle("Maior peso do subgrafo bipartido")

    for j in range(k,k+60,10):
        axes[x,y].set_title("Para n = " +  str(j))
        axes[x,y].grid(True)

        a = []
        b = []
        for i in range(5):
            g = Gnp(j,1/2)
            b.append(g.peso_total())
            a.append(maior_peso(g,5))
        
        axes[x,y].plot(a,b, 'ro')
        axes[x,y].set_xlabel("Maior peso encontrado")
        axes[x,y].set_ylabel("Peso total")
        axes[x,y].set_xlim(min(a) - 3, max(a) + 3)
        axes[x,y].set_ylim(min(b) - 3, max(b) + 3)
        
        if(y < 2):
            y = y + 1
        else:
            if(x < 1):
                y = 0
                x = x + 1


    plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
    plt.show()


def maior_conjunto(g,k):
    maior = 0.0;

    for i in range(k):
        x = conjunto_independente_grande(g);
        if x > maior:
            maior = x;

    return (x)

def plotar_grafo_q2(k):
    fig,axes = plt.subplots(ncols = 3, nrows = 2)
    x = 0
    y = 0
    fig.suptitle("Maior conjunto independente")

    for j in range(k,k+60,10):
        axes[x,y].set_title("Para n = " +  str(j))
        axes[x,y].grid(True)

        a = []
        b = []
        for i in range(5):
            d =  randint(5, j-1)
            g = Gnm(j,d)

            b.append(j/(2*d))
            a.append(maior_conjunto(g,5))
        
        axes[x,y].plot(a,b, 'ro')
        axes[x,y].set_xlabel("Maior conjunto encontrado")
        axes[x,y].set_ylabel("n / 2 * d")
        axes[x,y].set_xlim(min(a) - 3, max(a) + 3)
        axes[x,y].set_ylim(min(b) - 3, max(b) + 3)
        
        if(y < 2):
            y = y + 1
        else:
            if(x < 1):
                y = 0
                x = x + 1


    plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
    plt.show()


