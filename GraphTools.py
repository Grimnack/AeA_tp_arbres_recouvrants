import GraphValue as gv
import Graphs
from Sommet import Sommet
from Arete import Arete

def textToGraph(inFile):
    #recuperation des infos a partir du fichier
    f = open(inFile, "r")
    vertexes = []
    for line in f:
        print(line)
        vertex = [int(i) for i in line.rstrip().split(' ')]
        vertexes.append(vertex)
    f.close()
    
    #construction de la matrice
    nbVert = getNbVertexFromBranchMatrix(vertexes)
    matrix = []
    for i in range(nbVert):
        matrix.append([-1]*nbVert)
        
    #ajout des aretes dans la matrice
    for vertex in vertexes:
        x = vertex[0] - 1 # - 1 car notre matrice commence à 0
        for i in range(1, len(vertex), 2):
            y = vertex[i] - 1 # idem
            w = vertex[i + 1]
            matrix[x][y] = w
            matrix[y][x] = w #symétrie de la matrice

    return gv.GraphValue(matrix)

def getNbVertexFromBranchMatrix(mat):
    nbVert = 0
    for l in mat:
        nbVert = max(nbVert, l[0])
        for i in range(1, len(l), 2):
            nbVert = max(nbVert, l[i])
    return nbVert

def graphToText(graph, outFile):
    f = open(outFile, "w")
    for i in range(len(graph.lesSommets)):
        branches = graph.getBranchFrom(i)
        if branches :
            f.write(str(i + 1))
            for branch in branches:
                f.write(' ' + str(branch.sommet2.num + 1) + ' ' + str(branch.poids))
            f.write('\n')
    f.close()
    
#graph = gv.GraphValue(Graphs.matrix1)
#graphToText(graph, "mdr.graph")

graph = textToGraph("init.gr")
graphToText(graph, "copie.gr")
graph2 = textToGraph("copie.gr")

#resultat identique
graph.printAlgoKruskal()
graph2.printAlgoKruskal()
