#!/usr/bin/env python3
"""
geometrie
"""

from random import randint
class Point:
    """
    point du plan
    """
    #la classe Point est un peu jouet
    def __init__(self):
        """
        creqtion d`un point aleatoire
        """
        self.coordonnees = [randint(1, 800), randint(1, 600)]

    def svg(self):
        """
        affichage du point en svg
        """
        print("<circle cx=\"{}\" cy=\"{}\" r=\"3\" fill=\"red\"/>".format(
            self.coordonnees[0],
            self.coordonnees[1]
        ))

def main():
    """
    creation d`un triangle aleatoire + affichage en svg
    """
    triangle = [Point(), Point(), Point()]
    print("<svg width=\"800\" height=\"600\">")
    triangle[0].svg()
    triangle[1].svg()
    triangle[2].svg()
    print("</svg>")

main()
