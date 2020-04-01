from point import Point
import random
import math

class triangle_aleatoire:
    """
    Triangle class
    """
    def __init__(self, x_range=(0,0), y_range=(0,0) ):
        self.vertices = []
        for i in range(3):
            self.vertices.append(Point(
            [random.randint(x_range[0],x_range[1]), random.randint(y_range[0], y_range[1])])
            )

    def rotation_autour(self, centre, angle):
        t_new = triangle_aleatoire()
        new_ver = []
        for v in self.vertices:
            x_new = int((v.x - centre.x)*math.cos(angle)-(v.y - centre.y)*math.sin(angle) + centre.x)
            y_new = int((v.x - centre.x)*math.sin(angle)+(v.y - centre.y)*math.cos(angle) + centre.y)
            new_ver.append(Point([x_new, y_new]))
        t_new.vertices = new_ver
        return t_new
