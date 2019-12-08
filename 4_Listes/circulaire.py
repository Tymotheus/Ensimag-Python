#!/usr/bin/env python3
"""
listes triees, circulaires avec sentinelle.
"""
from tycat import data_tycat, trace

class Cellule:
    """
    valeur + suivant
    """
    #pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
#question - should liste vide with sentinel, show next as a sentinel or as None?
class Liste:
    """
    liste circulaire triee, simplement chainee avec sentinelle.
    """
    def __init__(self, sentinelle, iterable=None):
        """
        remplit la liste avec les elements de l'iterable donne.
        'sentinelle' precise la valeur de la cellule sentinelle.
        pre-condition: l'iterable donne est trie.
        """

        self.tete = Cellule(sentinelle, None)
        cell = self.tete
        if iterable is not None:
            for i in iterable:
                cell.suivant = Cellule(i)
                cell = cell.suivant
        cell.suivant = self.tete



    def cellules(self, inclure_sentinelle=False):
        """
        renvoie un iterateur sur toutes les cellules de la liste.
        'inclure_sentinelle' est un booleen permettant de preciser
        si la sentinelle est incluse ou non dans les cellules iterees.
        """
        if inclure_sentinelle is True:
            cell = self.tete
        else:
            cell = self.tete.suivant
        while True:
            yield cell
            cell = cell.suivant
            if cell == self.tete:
                break


    def decoupe(self):
        """
        coupe la liste en 2 (une cellule sur 2).
        par exemple (1,4,2,3,5) produit (1,2,5) et (4,3).
        renvoie les deux nouvelles listes.
        aucune nouvelle cellule n'est creee (hormis les sentinelles
        des deux nouvelles listes),
        en sortie la liste est vide.
        """

        if self.tete.suivant is not None:
            newborn = Liste(float("inf"))
        else:
            print("Liste is vide")
            return None

        old_tail = self.tete
        new_tail = newborn.tete
        for_old_list = True
        cour = old_tail.suivant #current cell on which we decide what to do with
        while cour is not self.tete:
            if for_old_list is True:
                old_tail.suivant = cour
                old_tail = old_tail.suivant
                for_old_list = False
            elif for_old_list is False:
                new_tail.suivant = cour
                new_tail = new_tail.suivant
                for_old_list = True
            cour = cour.suivant
        old_tail.suivant = self.tete
        new_tail.suivant = newborn.tete
        return self, newborn




    def ajouter(self, valeur):
        """
        ajoute la valeur donnee a la bonne place dans la liste.
        pre-condition : valeur n'est pas la valeur de la sentinelle.
        """
        cell = Cellule(valeur)
        prec = self.tete
        if prec.suivant is None: #liste vide
            prec.suivant = cell
            cell.suivant = self.tete
            return None
        cour = prec.suivant
        while cour.valeur < cell.valeur:
            prec = cour
            cour = cour.suivant
        cell.suivant = cour
        prec.suivant = cell
        return None

    def supprimer(self, valeur):
        """
        supprime la premiere cellule contenant la valeur donnee.
        pre-condition : valeur n'est pas la valeur de la sentinelle.
        """
        prec = self.tete
        cour = prec.suivant
        if cour is None:
            print("Liste vide")
            return None
        while True:
            if cour.valeur == valeur:
                prec.suivant = cour.suivant
                return None
            else:
                prec = cour
                cour = cour.suivant
                if cour is self.tete:
                    print("There is no element with this value")
                    return None


    def __str__(self):
        cell = self.tete.suivant
        if cell is None:
            print("Liste vide")
            return ""
        else:
            list_string = "("
            while True:
                list_string = list_string + str(cell.valeur)
                if cell.suivant is not self.tete: #there are still cellules
                    list_string = list_string + ", "
                    cell = cell.suivant
                else:
                    list_string = list_string + ")"
                    return list_string


def test():
    """
    tests simples des differentes methodes (a completer).
    """
    entiers = Liste(float("inf"), range(8))
    data_tycat(entiers)
    pairs, impairs = entiers.decoupe()
    data_tycat(pairs,impairs)
    print(pairs, impairs)
    print(entiers)
    pairs.supprimer(4)
    pairs.supprimer(0)
    pairs.supprimer(2)
    pairs.supprimer(6)
    impairs.ajouter(6)
    impairs.ajouter(0)
    data_tycat(pairs,impairs)

if __name__ == "__main__":
    test()
