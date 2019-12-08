#!/usr/bin/env python3
"""
listes simplements chainees + quelques operations
"""
from tycat import data_tycat, trace


class Cellule:
    """
    une cellule d'une liste. contient une valeur et un pointeur
    vers la cellule suivante.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant


#possible problems - liste vide et liste avec un single element
class Liste:
    """
    une liste simplement chainee.
    contient un pointeur sur la cellule en tete de liste et un autre sur
    la queue de liste.
    un compteur permet de savoir rapidement la taille de la liste.
    """
    def __init__(self): #tete is head, queue is tail, taille is size
        self.tete = None
        self.queue = None
        self.taille = 0

    #@trace
    def ajouter_en_tete(self, valeur):
        """
        ajoute une cellule en tete. cout : O(1).
        """
        if self.tete is None:
            C1 = Cellule(valeur)
            self.tete = C1
            self.queue = C1
            self.taille += 1
        else:
            C1 = Cellule(valeur, self.tete)
            self.tete = C1
            self.taille += 1


    #@trace
    def ajouter_en_queue(self, valeur):
        """
        ajoute une cellule en queue. cout : O(1).
        on peut le faire rapidement grace au pointeur de queue.
        """
        if self.tete is None:
            C1 = Cellule(valeur)
            self.tete = C1
            self.queue = C1
            self.taille += 1
        else:
            C1 = Cellule(valeur)
            self.queue.suivant = C1
            self.queue = C1
            self.taille += 1

    def cellules(self):
        """
        iterateur sur chaque cellule.
        Edit - to jak ten generator do zwracania kolejnych wartości żeby można było po tym iterować w pętli
        """
        cell = self.tete
        while cell is not None:
            yield cell
            cell = cell.suivant

    def recherche(self, valeur):
        """
        renvoie la premiere cellule contenant la valeur donnee.
        """
        if self.tete is None:
            print("Liste vide")
            return None
        else:
            cell = self.tete
            while True:
                if cell.valeur is valeur:
                    return cell
                else:
                    cell = cell.suivant
                    if cell is None:
                        print("There is no cell with this value")
                        return None


    #possible problems - liste vide, liste avec un single element
    #@trace
    def supprimer(self, valeur):
        """
        enleve la premiere cellule contenant la valeur donnee.
        """
        if self.tete is None: #liste vide
            print("Liste vide")
            return None

        elif self.taille == 1: #one element liste
            if self.tete.valeur == valeur:
                self.tete = None
                self.queue = None
                self.taille = 0
                return None
            else:
                print("There is no element with this value")
                return None

        else: #liste has at least 2 elements
            prec = None
            cour = self.tete

            while True: #the main loop
                if cour.valeur == valeur:
                    if cour == self.tete: #element being deleted is the head
                        self.tete = self.tete.suivant
                        self.taille -= 1
                        return None
                    elif cour == self.queue: #element being deleted is the tail
                        prec.suivant = None
                        self.queue = prec
                        self.taille -= 1
                        return None
                    else: #element being deleted is neither the head nor the tail
                        prec.suivant = cour.suivant
                        self.taille -= 1
                        return None
                else:
                    prec = cour
                    cour = cour.suivant
                    if cour is None:
                        print("There is no element with this value")
                        return None

    def __str__(self):
        """
        affiche (val1, val2, val3....)
        """
        if self.taille == 0:
            print("Liste vide")
            return ""
        else:
            list_string = "("
            cell = self.tete
            while True:
                list_string = list_string + str(cell.valeur)
                if cell.suivant is not None: #there are still cells
                    list_string = list_string + ", "
                    cell = cell.suivant
                else: #that was the last cell
                    list_string = list_string + ")"
                    return list_string


def test_listes():
    """
    on teste toutes les operations de base, dans differentes configurations.
    """
    exemple = Liste()
    a = 42 #variable to show data_tycat working
    #data_tycat(exemple, a)
    #return
    exemple.ajouter_en_tete(3)
    exemple.ajouter_en_tete(5)
    exemple.ajouter_en_queue(2)
    exemple.ajouter_en_queue(4)
    data_tycat(exemple, a)
    #return
    print("exemple : ", exemple)
    print("recherche : ", exemple.recherche(3).valeur)
    print("adresses des cellules : ",
          ",".join([hex(id(c))for c in exemple.cellules()]))
    exemple.supprimer(3)
    print("apres suppression de 5 : ", exemple)
    exemple.supprimer(5)
    print("apres suppression de 5 : ", exemple)
    data_tycat(exemple, a)

if __name__ == "__main__":
    test_listes()
