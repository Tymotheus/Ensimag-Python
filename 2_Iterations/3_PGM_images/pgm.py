#to finish - getting dimensions from a user

#!/usr/bin/env python3
"""
Images PGM - circles
"""

#importing used modules
import math
import random

class Circle:

    #circle full of grey dots
    def __init__(self):
        self.center = [0,0]

    def create_in_window(self, width, height):
        #picking coordinates for the center of circle inside the window
        self.center = [random.randint(0.3*width,0.7*width), random.randint(0.3*height,0.7*height)]

        while True:
            self.radius = random.randint(min(width/5, height/5) ,min(width/2, height/2))
            #checking if whole circle stays inside the window
            if (self.center[0] > self.radius) and (self.center[1] > self.radius) and (self.center[0] + self.radius) < width and (self.center[1] + self.radius) < height :
                break

    def is_within_circle( self , x, y ):
        #if ( math.sqrt( (x-self.center[0])**2 + (y-self.center[1]**2)) < self.radius ):

        if math.sqrt( ( x-(self.center[0]) )**2 + ( y-(self.center[1]) )**2 )< self.radius:
            return True
        else:
            return False

    def svg(self):
        # qqch....
        print("I'm to be done...")

    #cos do procedury losowania kolorkoz itd

def main():

    #possible delvelopment:
    #size_of_square = 75
    #height = int(input("Please enter height of desired picture:"))
    #width = int(input("Now enter width of desired picture:"))


    width = 1000
    height = 1000

    C1 = Circle()
    C2 = Circle()

    C1.create_in_window(width, height)
    C2.create_in_window(width, height)

    ppm_file = open("image_1.ppm", "wt")
    ppm_file.write("P2 \n")
    ppm_file.write(str(width) + " " + str(height) + "\n")
    ppm_file.write("255 \n")

    for y in range(0,height):
        linestr = ""
        for x in range(0,width):
            if C1.is_within_circle( x,y ) or C2.is_within_circle(x,y):
                linestr += str(random.randint(0,255)) + " "
            else:
                linestr += "255 "
        ppm_file.write(linestr + "\n")

    ppm_file.close()

#executing
main()
