#!/usr/bin/env python3
"""
Generalne Description:
In the following task, I have implemented a class for a List with shared suffixes.
I have proposed several metohds for operating on it allocating and optimising memory.
The most important "suffixe" allows to concatenate one list to another, saving memory for shared suffixes.
Comments are both in French (by the teacher) and in English (by me).
"""
from tycat import data_tycat

class Cellule:
    """
    une cellule d'une liste. contient une valeur, un pointeur
    vers la cellule suivante, un compteur comptabilisant
    combien de listes ou de cellules pointent dessus.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        self.utilisation = 1

class Liste:
    """
    liste de cellules.
    des listes differentes peuvent partager des cellules communes.
    EN: But they don't have to share cells - the lists can be totally separate.
    EN: That can be a bit confusing cause in the picture in desription of the task they all share suffixe
    """
    def __init__(self, mot):
        """
        transforme un mot en liste non-partagee.
        EN: List is being built starting with the tail, finishing with the head
        """
        premiere_cellule = None
        self.taille = 0
        for lettre in reversed(mot):
            premiere_cellule = Cellule(lettre, premiere_cellule)
            self.taille += 1
        self.tete = premiere_cellule

    def cellules(self):
        """
        iterateur sur toute les cellules de la liste.
        """
        cellule_courante = self.tete
        while cellule_courante is not None:
            yield cellule_courante
            cellule_courante = cellule_courante.suivant

    def get_word(self):
        if self.taille == 0:
            print("Mot vide")
            return None
        else:
            cell = self.tete
            output = ""
            while cell is not None:
                output += cell.valeur
                cell = cell.suivant
            return output

    def get_this_cell(self,number): #number is position of a desired cell
        if number < 1:
            print("Error, number must be a positive number.")
        if number > self.taille:
            print("Error, number exceeds list size.")
            return None
        cell = self.tete
        for i in range(1,number):
            cell = cell.suivant
        return cell

    def copy_list(self,cell):
        """
        EN: 'cell' argument here is a cell 'just before' a cell with utilisation >1 (or head with util >1)
        EN: Here we go again to split lists which number of utilisation is greater than 1
        """
        if cell == None:
            print ("Error, invalid cell")
            return None

        if cell.utilisation > 1 and cell == self.tete:
            self.tete.utilisation -= 1
            new_head = Cellule(cell.valeur)
            self.tete = new_head
            current_new = new_head
            current_old = cell
        else:
            current_new = cell
            current_old = cell

        while current_old.suivant is not None:
            #if current_old.suivant.utilisation > 1: #this part is wrong but needs further verification
                #current_old.suivant.utilisation -= 1
            new_cellule = Cellule(current_old.suivant.valeur)
            help_cellule = current_old #this one is to prevent problems when new = old
            current_new.suivant = new_cellule
            current_old = help_cellule.suivant
            current_new = new_cellule

    def suffixe(self, autre):
        """
        ajoute la liste autre a la fin de la liste self
        (en partageant les cellules communes).
        si la fin de self etait deja partagee avec quelqu'un, alors
        on dedouble toute la partie partagee avant l'ajout.
        EN: This command adds 'autre' at the end of 'self'
        EN: If some cells is 'self' are already shared, we need to create a new list (new 'self') leaving old as a suffix
        """
        #EN: First - we need to check if some cells are shared.
        #EN: So we need to check if any cell has "utilisation" greater than 1
        if autre.taille == 0:
            print("Autre est une liste vide")
            return None
        if self == autre:
            print("Concatenating a list with itself")
            #EN: I think we could use here some reccurence
            new_liste = Liste(self.get_word())
            new_liste.get_this_cell(new_liste.taille).suivant = self.tete
            self.tete.utilisation += 1
            new_liste.taille = self.taille
            self.tete = new_liste.tete
            return None

        cell = self.tete
        #EN: Case when sufix of list starting with head is used more than once
        if cell.utilisation > 1:
            self.copy_list(cell)

        #EN: Case when sufix of list non starting with head is used more than once
        else:
            while cell.suivant is not None:
                if cell.suivant.utilisation > 1:
                    self.copy_list(cell)
                    break
                else:
                    cell = cell.suivant
        self.get_this_cell(self.taille).suivant = autre.tete
        self.taille += autre.taille
        autre.tete.utilisation += 1

    def __del__(self):
        """
        FR: destructeur.
        """
        print("Calling destructor")
        cell = self.tete
        while cell is not None:
            if cell.utilisation > 1:
                print("Decreasing utilisation of Cell: '" + cell.valeur + "' from: " + str(cell.utilisation) + " to: " + str(cell.utilisation-1) )
                cell.utilisation -= 1
                return None
            cell = cell.suivant

def test_listes():
    """
    FR: on teste toutes les operations de base, dans differentes configurations.
    """
    #EN: Important remark - we have an array of lists
    listes = [Liste(mot) for mot in ("SE", "PAS", "DE", "DEVIS")]
    data_tycat(listes)
    _ = input()
    print("on ajoute listes[0] apres liste[1], puis un mot vide")
    listes[1].suffixe(listes[0])
    listes[1].suffixe(Liste(""))
    data_tycat(listes)
    _ = input()
    print("on ajoute listes[1] apres listes[2] et listes[0] apres listes[3]")
    listes[2].suffixe(listes[1])
    listes[3].suffixe(listes[0])
    data_tycat(listes)
    _ = input()
    print("on efface 'DEVIS'")
    del listes[3]
    data_tycat(listes)
    _  = input()
    print("on ajoute 'NT' apres 'PASSE'")
    listes[1].suffixe(Liste("NT"))
    data_tycat(listes)
    _ = input()
    print("on ajoute 'SE' apres elle-meme")
    listes[0].suffixe(listes[0])
    data_tycat(listes)

if __name__ == "__main__":
    test_listes()
