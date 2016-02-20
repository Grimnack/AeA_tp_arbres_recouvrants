import GraphValue2 as gv
import matplotlib.pyplot as plt
import time
import numpy as np

def moyenne50Temps(n,p,algo) :
    if algo == 0:
        print("algoPrim", n, "sommets", p, "proba")
    elif algo == 1 :
        print("algoKruskal", n, "sommets", p, "proba")
    temps = []
    couleurs = []
    for i in range(50) :
        graph = gv.graphAlea(n,15,p)
        start_time = time.time()
        if algo == 0 :
            graph.algoPrim()
        elif algo == 1 :
            graph.algoKruskal()
        interval = time.time() - start_time
        temps.append(interval)
    sommeT = sum(temps)
    return float(sommeT)/50.

def moyenne50Couverture(n,p,algo) :
    if algo == 0:
        print("algoPrim", n, "sommets", p, "proba")
    elif algo == 1 :
        print("algoKruskal", n, "sommets", p, "proba")
    couvertures = []
    couleurs = []
    for i in range(50) :
        graph = gv.graphAlea(n,15,p)
        couv = 0
        if algo == 0 :
            for arete in graph.algoPrim()[0]:
                couv += arete.poids
        elif algo == 1 :
            for arete in graph.algoKruskal()[0]:
                couv += arete.poids
        couvertures.append(couv)
    sommeC = sum(couvertures)
    return float(sommeC)/50.


def plotCouvertureTaille() :
    plt.xlabel('taille')
    x = np.linspace(10,30,num=9)
    plt.ylabel('couverture')
    y = np.zeros((3,9))
    for i in range(2) :
        for j in range(9) :
            y[i,j] = moyenne50Couverture(int(x[j]),0.5,i)
    labels=["algoPrim","algoKruskal"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

def plotCouvertureProba() :
    plt.xlabel('probabilité')
    x = np.linspace(0.1,0.9,num=9)
    plt.ylabel('couverture')
    y = np.zeros((3,9))
    for i in range(2) :
        for j in range(9) :
            y[i,j] = moyenne50Couverture(20,x[j],i)
    labels=["algoPrim","algoKruskal"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

def plotTempsTaille() :
    plt.xlabel('taille')
    x = np.linspace(10,30,num=9)
    plt.ylabel('temps')
    y = np.zeros((3,9))
    for i in range(2) :
        for j in range(9) :
            y[i,j] = moyenne50Temps(int(x[j]),0.5,i)
    labels=["algoPrim","algoKruskal"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

def plotTempsProba() :
    plt.xlabel('probabilité')
    x = np.linspace(0.1,0.9,num=9)
    plt.ylabel('temps')
    y = np.zeros((3,9))
    for i in range(2) :
        for j in range(9) :
            y[i,j] = moyenne50Temps(20,x[j],i)
    labels=["algoPrim","algoKruskal"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

plotCouvertureTaille()
plotCouvertureProba()
plotTempsTaille()
plotTempsProba()
# print(moyenne50Temps(50,0.5,0))
# print(moyenne50Temps(50,0.5,1))
# print(moyenne50Temps(50,0.5,2))
