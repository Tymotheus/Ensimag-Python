#!/usr/bin/env python3
"""
pointy
"""

class Point:

    def __init__(self, x,y):
        self.coordonnees = [int(x), int(y)]

    def svg(self):
        print("<circle cx=\"{}\" cy=\"{}\" r=\"3\" fill=\"red\"/>".format(
            self.coordonnees[0],
            self.coordonnees[1]
        ))
    def __str__(self):
        return "x = " + str(self.coordonnees[0]) + ", y = " + str(self.coordonnees[1])

def main():

    array = []
    print("<svg width=\"640\" height=\"480\">")
    for x in range(0,1000):
        x = input()
        y = input()
        P = Point(x,y)
        array.append(P)

    for x in range(0,1000):
        array[x].svg()

    print("</svg>")

main()
