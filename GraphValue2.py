import random as r
import Graphs
from Sommet import Sommet
from Arete import Arete
from collections import deque

class GraphValue(object):
    """docstring for GraphValue"""
    def __init__(self, matrix):
        super(GraphValue, self).__init__()
        self.lesAretes = []            
        lesSommets = []
        for i in range(len(matrix)) :
            sommet = Sommet([],i)
            lesSommets.append(sommet)
        for i in range(len(matrix)) :
            for j in range(i) :
                if matrix[i][j] != -1 :
                    lesSommets[i].ajouteVoisin(lesSommets[j],matrix[i][j],self)
        self.lesSommets = lesSommets    

    def resetSommets(self) :
        for sommet in self.lesSommets:
            sommet.tag = False

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
        self.resetSommets()
        return (F,visited)

    def printAlgoPrim(self) :
        t = self.algoPrim()
        print("Algorithme Prim")
        print("aretes")
        for a in t[0] :
            print(a)
        print("sommets")
        for s in t[1] :
            print(s)

    def algoKruskal(self) :
        A = []
        visited = set([])
        lesAretes = self.lesAretes[:]
        composantesConnexes = []
        for sommet in self.lesSommets :
            composantesConnexes.append([sommet])
        lesAretes.sort(key=lambda arete: arete.poids)
        for arete in lesAretes :
            ensemble1 = find(arete.sommet1,composantesConnexes)
            ensemble2 = find(arete.sommet2,composantesConnexes)
            if ensemble1 != ensemble2 :
                A.append(arete) 
                if len(ensemble1) < len(ensemble2) :
                    for sommet in ensemble1 :
                        ensemble2.append(sommet)
                    composantesConnexes.remove(ensemble1)
                else :
                    for sommet in ensemble2 :
                        ensemble1.append(sommet)
                    composantesConnexes.remove(ensemble2)
        for arete in A:
            visited.add(arete.sommet1.num)
            visited.add(arete.sommet2.num)
        return (A, visited)

    def printAlgoKruskal(self) :
        t = self.algoKruskal()
        print("Algorithme Kruskal")
        print("aretes")
        for a in t[0] :
            print(a)
        print("sommets")
        for s in t[1] :
            print(s)
    

def find(x,composantesConnexes) :
    for ensemble in composantesConnexes :
        if x in ensemble :
            return ensemble


def compAretes(a1,a2) :
    if a1.poids < a2.poids :
        return -1
    elif a1.poids > a2.poids :
        return 1
    else :
        return 0

def graphAlea(nbSommets, poidsMax, p) :
    matrix = []
    for i in range(nbSommets) :
        matrix.append([-1] * nbSommets)
    for i in range(nbSommets) :
        for j in range(i) :
            if p >= r.random() :
                poidsAlea = r.randint(1,poidsMax)
                matrix[i][j] = poidsAlea
                matrix[j][i] = poidsAlea
    return GraphValue(matrix)

graph = GraphValue(Graphs.matrix1)
graph.printAlgoPrim()
graph.printAlgoKruskal()

graph.printAlgoPrim()
graph.printAlgoKruskal()
