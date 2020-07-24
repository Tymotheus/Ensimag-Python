#!/usr/bin/env python3
"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour generer des phrases aleatoires.
"""
import sys
from re import finditer
from random import choice
from random import choices #weighted random choice
from os import system


def mots(nom_fichier):
    """
    renvoie un iterateur sur tous les mots du fichier.
    elimine au passage tout ce qui n'est pas une lettre.
    """
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                yield mot.group(0)


def couples(iterateur):
    """
    renvoie un iterateur sur tous les couples d'elements successifs
    de l'iterateur donne.
    """
    valeur_precedente = next(iterateur)
    for valeur in iterateur:
        yield valeur_precedente, valeur
        valeur_precedente = valeur


def compte_mots_suivants(nom_fichier):
    """
    renvoie un dict associant a chaque mot m1 du fichier
    un dict associant a chaque mot m2 suivant m1 dans le fichier
    le nombre de fois ou m2 apparait apres m1.
    """
    dict = {}
    for couple in couples(mots("texte.txt")):
        #checking if the pair is already in the dictionary
        if couple[0] in dict:
            if couple[1] in dict[couple[0]]: #pair already in dict
                dict[couple[0]][couple[1]] += 1 #nombre associe a mot m2
            else: #first word already in dict, second not yet
                dict[couple[0]][couple[1]] = 1
        else: #word not existing in dict yet
            dict[couple[0]] = {couple[1] : 1}

    return dict


def affiche_graphe(suivants):
    """
    affiche le graphe dans le terminal.
    attention : petits textes seulement.
    """
    #saves the dictionary as a graph structure in the file
    with open("test.dot", "w") as fichier_dot:
        fichier_dot.write("digraph g { \n")
        for word in suivants:
            for successor in suivants[word]:
                fichier_dot.write("{} -> {} [label= {}];\n".format(word, successor, suivants[word][successor]))

        fichier_dot.write("\n}")

    system("dot -Tpng test.dot -o test.png")
    system("tycat test.png")


def analyse_texte():
    """
    analyse le fichier donne en argument et dessine le graphe
    des mots suivants.
    """
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    affiche_graphe(suivants)
    # une petite phrase aleatoire.
    mot_depart = choice(list(suivants.keys()))
    phrase = [mot_depart]
    for _ in range(10):
        phrase.append(suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def suivant_aleatoire(mot, suivants):
    """
    tire aleatoirement (uniformement en fonction des frequences)
    un suivant du mot donne.
    si le mot donne n'a pas de suivant, retourne un mot aleatoire.
    """
    #on tire aleatoirement
    #list index at the end necessary because choices returns a list not an item
    mot_choisi = choices( list(suivants[mot].keys()), weights=list(suivants[mot].values()) )[0]

    if mot_choisi == None:
        mot_choisi = choice(list(suivants.keys()))
    return mot_choisi

if __name__ == "__main__":
    analyse_texte()
