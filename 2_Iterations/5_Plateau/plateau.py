#!/usr/bin/env python3
"""
Generating fields for a snake board game. Each field has 40x40 dimension
"""
import sys

def header(width, height):
    print("<svg height=\""+str(height)+"\" width=\"" + str(width)+ "\">")

def footer():
    print("</svg>")

class Field:
    """
    cords mean how far our Rect is from the top left display corner
    """
    def __init__(self, x, y, number):
        self.number = number
        self.cords = [int(x), int(y)]
    def draw(self):
        print("<rect x=\"" + str(self.cords[0]) + "\" y=\"" + str(self.cords[1])
        +"\" width=\"40\" height = \"40\" "
        +"style =\"fill:white;stroke-width:1;stroke:black\" />")
        print("<text x=\"" + str(self.cords[0]+5) + "\" y=\"" + str(self.cords[1]+35)
        +"\" fill=\"red\">" + str(self.number) + "</text>")

    def move_up(self):
        return Field(self.cords[0],self.cords[1]-40,self.number+1)
    def move_down(self):
        return Field(self.cords[0],self.cords[1]+40,self.number+1)
    def move_left(self):
        return Field(self.cords[0]-40,self.cords[1],self.number+1)
    def move_right(self):
        return Field(self.cords[0]+40,self.cords[1],self.number+1)

def Make_Board(width, height):
    Board = []
    fields_horizontal = int(width/40)
    fields_vertical = int(height/40)

    current_x = 0
    y = 0
    f = Field(0, height - 40, 1)
    Board.append(f)
    while y < fields_vertical:
        for x in range(0,fields_horizontal-2):
            f = f.move_right()
            Board.append(f)

        if y+1<=fields_vertical:
            y += 1
            f = f.move_up()
            Board.append(f)
        else:
            break

        if y+1<=fields_vertical:
            y += 1
            f = f.move_up()
            Board.append(f)
        else:
            break

        for x in range(0,fields_horizontal-2):
            f = f.move_left()
            Board.append(f)

        if y+1<=fields_vertical:
            y += 1
            f = f.move_up()
            Board.append(f)
        else:
            break

        if y+1<=fields_vertical:
            y += 1
            f = f.move_up()
            Board.append(f)
        else:
            break

    for field in Board:
        field.draw()
    print("Fields vertical: ", fields_vertical, "Fields Horizontal: ", fields_horizontal)


def main():
    if len(sys.argv) != 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], " height width")
        sys.exit(1)

    header(int(sys.argv[1]), int(sys.argv[2]))
    Make_Board(int(sys.argv[1]), int(sys.argv[2]))

    footer()

main()
