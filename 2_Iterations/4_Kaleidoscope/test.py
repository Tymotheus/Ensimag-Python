#!/usr/bin/env python3
from triangle import triangle_aleatoire
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class B:
    def __init__(self, cords):
        self.x = cords[0]
        self.y = cords[1]

def main():
    tupla = (2,3)
    a = A(1,5)
    b = B(tupla)
    print("x of a is: ", a.x, " y of a is: ", a.y)
    print("x of b is: ", b.x, " y of b is: ", b.y)

    t1 = triangle_aleatoire((0,10),(5,10))
    for _ in t1.vertices:
        print(_.x, _.y)
main()
