#!/usr/bin/env python3
"""
EN: Implementation of pivot algorithm. Input is an array of n elements and a pointer for a pivot.
Our task is to split input and return two separated arrays:
one with elements smaller or equal to pivot, the other with elements greater than pivot

FR: On se propose implémenter un algorithme de pivot de différentes façons.
On a en entrée /input/ un tableau de n éléments comparables ainsi que l’indice d’une case du tableau contenant le pivot. On souhaite déplacer les éléments du tableau en les comparant au pivot.
Dans un premier temps, implémentez une fonction pivote(tableau, indice_pivot) renvoyant deux tableaux  : le premier contient tous les éléments inférieurs ou égaux au pivot, le second tous les éléments supérieurs au pivot. Le pivot lui même n’appartient à aucun des tableaux renvoyés. Il y a en général de nombreuses possibilités de solutions, l’ordre entre les "petits" (resp. les "grands") n’étant pas contraint.

Dans un second temps, on se propose de travailler en place. Au lieu de renvoyer deux tableaux, on déplace directement les éléments du tableau d’entrée (en procédant par échanges). On vous demande de ne pas utiliser de tableaux additionnels. Attention cette implémentation est difficile et nécessite sans doute d’essayer un peu sur papier avant de commencer.
"""
def pivote(tableau, indice_pivot):
    """
    input is an array and an integer - position of pivot in our array
    """
    size = len(tableau)
    smaller_array, greater_array = [],[]
    for i in range(0,size-1):
        if i == indice_pivot:
            pass
        elif tableau[i] > tableau[indice_pivot]:
            greater_array.append(tableau[i])
        elif tableau[i] <= tableau[indice_pivot]:
            smaller_array.append(tableau[i])
        else:
            print("Error")
            return None

    return smaller_array, greater_array

def main():

    array = [3,0,10,1,6,9,5,3,9,0,5,8,9,8,4,2,0,9,6,2]
    print("Starting array: ", array)
    a,b = pivote(array,0)
    print("Smaller arrray: ", a)
    print("Greater arrray: ", b)
main()
