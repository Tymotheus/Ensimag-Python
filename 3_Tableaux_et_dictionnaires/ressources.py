#!/usr/bin/env python3
"""
EN: Task: creating a structure to stock sets of resources.
Every resource is within the range of "0" and "number of elements - 1"
So we stock only indexes not values or elements.
We could use python "set" but it could be inefficient.
Each interval is gonna be represented by an array of two elements: index of begining and index of ending.
plages contigues - adjacent ranges
"""
from tycat import data_tycat
from itertools import takewhile, accumulate
from more_itertools import collate #sorts two lists into one list

class Ressources:
    """
    On stocke une liste de ressources, compressee par plages contigues.
    EN: Intervalles - array of some 2-elements arrays.
    EN: nombre_ressources - capacity of the array.
    """
    def __init__(self, nombre_ressources, intervalles=None):
        # requiert : si intervalles is not None, alors :
        #            - les intervalles sont non vides
        #            - les intervalles sont non contigus
        #            - les intervalles sont tries par indices croissants
        #            - intervalles[-1][1] <= nombre_ressources
        self.nombre_ressources = nombre_ressources
        if intervalles is not None:
            self.intervalles = intervalles
        else:
            self.intervalles = [[0, nombre_ressources]]

    def disponible(self, indice):
        """
        renvoie si l'indice donne est disponible dans la ressource.
        EN: Returns bool, determining if particular indice exists in the resources.
        """
        return any(i[0] <= indice < i[1] for i in self.intervalles)

    def reserve(self, ressources_demandees):
        """
        enleve le nombre de ressources demandees (premieres disponibles).
        renvoie les ressources correspondant aux plages reservees.
        EN: Reserves number of elements from the array, starting with the first ones.
        EN: Returns a new "Ressources" object, with elements removed from considered "Ressources" object.
        """
        taille_donnee = 0
        intervalles_donnes = []
        #EN: Accumulate - returns iterable/array/output, of gradually added elemets of list/iterable - argument
        #EN: Zipping intervals together with total size of elements given
        #EN: Takewhile: pred,seq seq[0], seq[1] until pred fails
        for i, taille_donnee in zip(self.intervalles, takewhile(lambda s: s < ressources_demandees, accumulate(i[1]-i[0] for i in self.intervalles))):
            intervalles_donnes.append(i)
        # Note: Arrete sur intervale just avant avoir satisfe le condition (intervale desiree) - lambda handles ca
        # Note: Intervale qui reste sera coupe sour 2
        intervalle_a_couper = self.intervalles[len(intervalles_donnes)]
        debut, fin = intervalle_a_couper
        fin_donne = debut + ressources_demandees - taille_donnee
        a_donner = [debut, fin_donne]

        if fin_donne == fin: #EN: We are devouring whole segment without cut
            self.intervalles = self.intervalles[len(intervalles_donnes)+1:]
        else: #EN: We must cut the segment
            self.intervalles[len(intervalles_donnes)][0] = fin_donne
            self.intervalles = self.intervalles[len(intervalles_donnes):]

        intervalles_donnes.append(a_donner)
        return Ressources(self.nombre_ressources, intervalles_donnes)

    def retourne(self, ressources_rendues):
        """
        remet les plages de ressources donnees dans le systeme.
        EN: Returns back resources taken by function reserve, saved in the argument.
        """
        ressources = collate(self.intervalles, ressources_rendues.intervalles)
        #print(ressources)
        intervalles = []
        intervalles.append(next(ressources))
        #print(intervalles)
        for intervalle in ressources:
            if intervalles[-1][1] == intervalle[0]:
                intervalles[-1][1] = intervalle[1]
            else:
                intervalles.append(intervalle)
        self.intervalles = intervalles

    def __str__(self):
        """
        renvoie une chaine 'visuelle' des ressources contenues dans self.
        par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
        les ressources 0, 3-7 sont disponibles.
        """
        return "[" + "".join('x' if self.disponible(i) else '.' for i in range(self.nombre_ressources)) + "]"

def test():
    """
    on teste en gruyerisant une ressource.
    """
    ressources = Ressources(10)
    print("Disponibles :", ressources)
    reservees = [ressources.reserve(c) for c in (2, 2, 3, 2, 1)]
    print("Disponibles :", ressources)
    ressources.retourne(reservees[1])
    print("Disponibles :", ressources)
    ressources.retourne(reservees[3])
    print("Disponibles :", ressources)
    print("Reservees   :", ressources.reserve(3))
    print("Disponibles :", ressources)
    print("Les intervalles :", ressources.intervalles)

if __name__ == "__main__":
    test()
