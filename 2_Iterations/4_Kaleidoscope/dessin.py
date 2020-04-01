"""
File making a drawing? Generation of SVG file?
"""
import random
import triangle

def entete(width, height):
    """
    Generates header of svg File
    """
    print("<svg height=\""+str(height)+"\" width=\"" + str(width)+ "\">" )

def couleur_aleatoire():
    """
    Returns SVG colour code (?)
    """
    return((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

def affiche_triangle(tri, colour):
    """
    Prints svg-like triangle - returning code on output
    """
    print("<polygon points=\"",end="")
    for v in tri.vertices:
        print(str(v.x) + "," + str(v.y), end=" ")
    print("\" fill=\"rgb"+str(colour)+"\" fill-opacity=\"0.5\"/>")

def pied():
    """
    Returns ending of a file
    """
    print("</svg>")
