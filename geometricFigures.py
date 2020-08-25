from math import *

class Figures:
    def __init__(self, x=1, y=1, h=1, r=1, a=1, b=1):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.h = h
        self.r = r

    def Square(self):
        return float(self.x) ** 2

    def Rectangle(self):
        return float(self.x) * float(self.y)

    def Triangle(self):
        return round(float(self.x) * float(self.h) / 2, 5)

    def Circle(self):
        return round(pow(float(self.r), 2) * pi, 5)

    def Oval(self):
        return round(float(self.r) * float(self.h) * pi, 5)

    def Trapeze(self):
        return round((float(self.a)+float(self.b)) * float(self.h) / 2, 5)

    def Rhombus(self):
        return round((float(self.a)*float(self.h)))

    def Parallelogram(self):
        return round((float(self.a)*float(self.h)))
