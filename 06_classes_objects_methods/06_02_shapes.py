'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def sa(self):
        sa = pi * self.radius ** 2
        return sa

    def ouside(self):
        circ = 2 * self.radius * pi
        return circ


class Rectangle(object):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def sa(self):
        sa = self.height * self.width
        return sa

    def ouside(self):
        perim = 2 * self.height + 2 * self.width
        return perim

#tests
mycircle1 = Circle(3)
mycircle2 = Circle(9)
myrec1 = Rectangle(4, 6)
myrec2 = Rectangle(2, 19)

print(mycircle1.sa())
print(mycircle2.ouside())
print(myrec1.sa())
print(myrec2.ouside())
