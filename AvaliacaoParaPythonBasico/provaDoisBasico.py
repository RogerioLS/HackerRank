import math
import os
import random
import re
import sys

class Rectangle:
    def __init__ (self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return 2*(self.length + self.width)
    pass
    """length = float(input('enter length:'))
        width = float(input('enter width:'))
    rectangle = Rectangle(length, width)
        print( rectangle.perimeter())
            enter length:5
            enter width:10
            30.0"""

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return 2*3.14*self.radius
    pass

    """ radius = float(input("Enter radius of circle"))
     my_circle = circle (radius)
        print(my_circle.area())
    """

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
