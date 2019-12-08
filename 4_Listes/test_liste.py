#!/usr/bin/env python3
"""
quelques tests automatiques pour verifier que tout est ok dans le module liste
"""
from listes import Liste


def vecteur(liste):
    """
    convertit une liste en vecteur
    """
    return [c.valeur for c in liste.cellules()]


def ajout_tete_vide():
    """
    verifie l'ajout en tete dans une liste vide.
    """
    liste = Liste()
    liste.ajouter_en_tete(3)
    assert vecteur(liste) == [3]
    assert liste.tete is liste.queue
    assert liste.tete.suivant is None
    assert liste.queue.suivant is None


def ajout_tete_1():
    """
    verifie l'ajout en tete dans une liste non vide.
    """
    liste = Liste()
    liste.ajouter_en_tete(3)
    liste.ajouter_en_tete(5)
    assert vecteur(liste) == [5, 3]
    assert liste.tete.suivant is liste.queue
    assert liste.queue.suivant is None


def ajout_queue_vide():
    """
    verifie l'ajout en queue dans une liste vide.
    """
    liste = Liste()
    liste.ajouter_en_queue(3)
    assert vecteur(liste) == [3]
    assert liste.tete is liste.queue
    assert liste.tete.suivant is None
    assert liste.queue.suivant is None


def ajout_queue_1():
    """
    verifie l'ajout en queue dans une liste non vide.
    """
    liste = Liste()
    liste.ajouter_en_queue(3)
    liste.ajouter_en_queue(5)
    assert vecteur(liste) == [3, 5]
    assert liste.tete.suivant is liste.queue
    assert liste.queue.suivant is None


def suppression_1():
    """
    verifie la suppression du 1er element.
    """
    liste = Liste()
    liste.ajouter_en_queue(1)
    liste.ajouter_en_queue(2)
    liste.ajouter_en_queue(1)
    liste.supprimer(1)
    assert vecteur(liste) == [2, 1]
    assert liste.tete.suivant is liste.queue
    assert liste.queue.suivant is None


def suppression_2():
    """
    verifie la suppression du dernier element.
    """
    liste = Liste()
    liste.ajouter_en_queue(1)
    liste.ajouter_en_queue(2)
    liste.ajouter_en_queue(3)
    liste.supprimer(3)
    assert vecteur(liste) == [1, 2]
    assert liste.tete.suivant is liste.queue
    assert liste.queue.suivant is None


def suppression_3():
    """
    verifie la suppression du seul element d'une liste.
    """
    liste = Liste()
    liste.ajouter_en_queue(1)
    liste.supprimer(1)
    assert vecteur(liste) == []
    assert liste.tete is None
    assert liste.queue is None


def suppression_4():
    """
    verifie la suppression d'un element en milieu de liste.
    """
    liste = Liste()
    liste.ajouter_en_queue(1)
    liste.ajouter_en_queue(2)
    liste.ajouter_en_queue(3)
    liste.supprimer(2)
    assert vecteur(liste) == [1, 3]
    assert liste.tete.suivant is liste.queue
    assert liste.queue.suivant is None


def taille():
    """
    verifie que la taille de la liste est correcte
    """
    liste = Liste()
    liste.ajouter_en_queue(1)
    liste.ajouter_en_queue(2)
    liste.ajouter_en_queue(3)
    liste.ajouter_en_tete(3)
    liste.ajouter_en_tete(5)
    liste.supprimer(5)
    liste.supprimer(2)
    assert liste.taille == 3



def test(message, fonction):
    """
    essaie la fonction donne ; si aucune exception n'est levee, renvoie 1
    sinon 0
    """
    # pylint: disable=bare-except
    try:
        fonction()
    except:
        print("test echoue:", message)
        return 0
    return 1


def tests():
    """
    lance tous les tests et leve une exception
    """
    tests_ok = sum([
        test("ajout en tete dans une liste vide", ajout_tete_vide),
        test("ajout en tete dans une liste", ajout_tete_1),
        test("ajout en queue dans une liste vide", ajout_queue_vide),
        test("ajout en queue dans une liste", ajout_queue_1),
        test("suppression du premier element", suppression_1),
        test("suppression du dernier element", suppression_2),
        test("suppression de l'element d'une liste de taille1", suppression_3),
        test("suppression d'un element au milieu", suppression_4),
        test("verification de la taille", taille)
    ])
    print(tests_ok, "/ 9 tests ont reussi")


if __name__ == ("__main__"):
    tests()
