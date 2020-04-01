#!/usr/bin/env python3
"""
echiquier
"""

class Rectangle:

    #cords mean how far our Rect is from the top left display corner
    def __init__(self, x,y,colour):
        self.coordonnees = [int(x), int(y)]
        self.is_white = colour

    def svg(self):
        colour = self.is_white*255
        print("<rect x=" + "\"" + str(self.coordonnees[0]) +"\""
        + " y=" + "\"" + str(self.coordonnees[1]) + "\""
        + " width=\"75\" height=\"75\" style=\"fill:rgb("
        +str(colour)+","+str(colour)+","+str(colour)+"); stroke-width:1;stroke:rgb(0,0,0)\"/>")

    def __str__(self):
        return "x = " + str(self.coordonnees[0]) + ", y = " + str(self.coordonnees[1])

def main():

    #possible delvelopment:
    #size_of_square = 75
    print("<svg width=\"640\" height=\"640\">")

    array = []
    for x in range (0,8):
        for y in range (0,8):
            R = Rectangle(x*75,y*75,(x+y+1)%2)
            array.append(R)
            R.svg()

    print("</svg>")

#executing
main()
