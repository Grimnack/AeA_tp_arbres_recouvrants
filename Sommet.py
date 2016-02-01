from Arete import Arete

class Sommet(object):
    """docstring for Sommet"""
    def __init__(self, listeArete, num):
        super(Sommet, self).__init__()
        self.aretes = listeArete[:]
        self.num = num
        self.tag = False 

    def __str__(self) :
        return str(self.num)
        
    def getVoisins(self) :
        voisins = []
        for arete in self.arete :
            voisins.append(arete.renvoieVoisin(self))
        return voisins

    def getVoisinsNonMarques(self) :
        '''
        fonction utile pour l algo de prim
        renvoie une liste de couples (sommet,arete)

        '''
        voisins = []
        for arete in self.aretes :
            voisin = arete.renvoieVoisin(self)
            if not voisin.tag :
                voisins.append((voisin,arete))
        return voisins

    def ajouteVoisin(self,sommet2,poids) :
        lien = Arete(self,sommet2,poids)
        self.aretes.append(lien)
        sommet2.aretes.append(lien)

    def renvoiePoidsMin(self) :
        '''
        a tester
        '''
        return min(self.aretes, key=lambda arete: arete.poids)    

