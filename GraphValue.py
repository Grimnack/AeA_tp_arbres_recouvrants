import random as r
import collection import deque

class GraphValue(object):
    """docstring for GraphValue"""
    def __init__(self, matrix, poids):
        super(GraphValue, self).__init__()
        self.voisins = []
        for ligne in matrix :
            self.voisins.append(ligne[:])
        self.poids = []
        for ligne in poids :
            self.poids.append(ligne[:])

    def resteVoisinNonTag(self,tag,sommet) :
        lesVoisins = []
        for ligne in matrix[sommet] :
            for i in range(ligne) :  
                if matrix[sommet][i] :
                    lesVoisins.append(i)
        for voisin in lesVoisins :
            if tag[voisin] == False :
                return True
        return False


    def runPrim(self) :
        tag = [False] * n
        cpt = n # pour savoir si il existe toujours des sommet non marqués 
        # initialisation d'une file vide
        f = deque([])
        # on marque arbitrairement un sommet
        tag[0] = True
        while  :






    def runKruskal(self) :



def graphAlea(n,p) :
    matrix = []
    poids = []
    N = n**4 # puissance 4
    for i in range(n) :
        matrix.append([False]*n)
        poids.append([-1]*n)
    for i in range(n) :
        for j in range(i+1,n) :
            if p >= r.random() :
                matrix[i][j] = True
                matrix[j][i] = True
    for i in range(n) :
        for j in range(i+1,n) :
            if matrix[i][j] :
                poids[i][j] = r.randint(1,N)
                poids[j][i] = poids[i][j]

    return GraphValue(matrix,poids)

graph = graphAlea(4,0.5)
print(graph.poids)

    
