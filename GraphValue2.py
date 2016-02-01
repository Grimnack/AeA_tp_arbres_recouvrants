import random as r
import Graphs
from Sommet import Sommet
from Arete import Arete
from collections import deque

class GraphValue(object):
    """docstring for GraphValue"""
    def __init__(self, matrix):
        super(GraphValue, self).__init__()            
        lesSommets = []
        for i in range(len(matrix)) :
            sommet = Sommet([],i)
            lesSommets.append(sommet)
        for i in range(len(matrix)) :
            for j in range(i) :
                if matrix[i][j] != -1 :
                    lesSommets[i].ajouteVoisin(lesSommets[j],matrix[i][j])
        self.lesSommets = lesSommets    


    def algoPrim(self) :
        F = set([])
        visited = [self.lesSommets[0]]
        self.lesSommets[0].tag = True
        nonMarques = self.lesSommets[0].getVoisinsNonMarques()
        while nonMarques != []:
            (y,arete) = min(nonMarques, key = lambda couple : couple[1].poids)
            if not y.tag :
                y.tag = True
                visited.append(y)
                F.add(arete)
                nonMarques.extend(y.getVoisinsNonMarques())
            nonMarques.remove((y,arete))
        return (F,visited)

    def printAlgoPrim(self) :
        t = self.algoPrim()
        print("aretes")
        for a in t[0] :
            print(a)
        print("sommets")
        for s in t[1] :
            print(s)

    def algoKruskal(self) :
        pass

def graphAlea(nbSommets, poidsMax) :
    matrix = []
    for i in range(nbSommets) :
        matrix.append([-1] * nbSommets)
    for i in range(nbSommets) :
        for j in range(i) :
            if 0.5 >= r.random() :
                poidsAlea = r.randint(1,poidsMAx)
                matrix[i][j] = poidsAlea
                matrix[j][i] = poidsAlea
    return GraphValue(matrix)

graph = GraphValue(Graphs.matrix1)
graph.printAlgoPrim()