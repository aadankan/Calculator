import turtle
from math import *
import numpy as np



class DrawingFigures:
    def __init__(self, x=1, y=1, h=1, r=1, a=1, b=1, wtime=0.2, sleep=3):
        self.x = int(x) * 10
        self.y = int(y) * 10
        self.h = int(h) * 10
        self.r = int(r) * 10
        self.a = int(a) * 10
        self.b = int(b) * 10


    def Square(self):
        t = turtle.Turtle()
        for i in range(4):
            t.forward(self.x)
            t.right(90)
        turtle.done()

    def Rectangle(self):
        t = turtle.Turtle()
        for i in range(2):
            t.forward(self.x)
            t.right(90)
            t.forward(self.y)
            t.right(90)

        turtle.done()

    def Triangle(self):
        t = turtle.Turtle()
        t.forward(self.x)
        t.left(90+degrees(np.arcsin(self.x/2/sqrt(pow(self.x/2, 2) + pow(self.h, 2)))))
        t.forward(sqrt(pow(self.x/2, 2) + pow(self.h, 2)))
        t.left((90-degrees(np.arcsin(self.x/2/sqrt(pow(self.x/2, 2) + pow(self.h, 2)))))*2)
        t.forward(sqrt(pow(self.x/2, 2) + pow(self.h, 2)))
        turtle.done()

    def Circle(self):
        t = turtle.Turtle()
        t.circle(self.r)
        turtle.done()

    def TallOval(self):
        t = turtle.Turtle()
        t.left(45)
        for loop in range(2):
            t.circle(self.r, 90)
            t.circle(self.r / 2, 90)

        turtle.done()

    def FlatOval(self):
        t = turtle.Turtle()
        t.right(45)
        for loop in range(2):
            t.circle(self.r, 90)
            t.circle(self.r / 2, 90)

        turtle.done()

    def Trapeze(self):
        t = turtle.Turtle()
        t.forward(self.b)
        t.left(90+degrees(np.arcsin((self.b - self.a) / 2 / sqrt(pow((self.b - self.a) / 2, 2) + pow(self.h, 2)))))
        t.forward(sqrt(pow((self.b - self.a) / 2, 2) + pow(self.h, 2)))
        t.left(90-degrees(np.arcsin((self.b - self.a) / 2 / sqrt(pow((self.b - self.a) / 2, 2) + pow(self.h, 2)))))
        t.forward(self.a)
        t.left(90-degrees(np.arcsin((self.b - self.a) / 2 / sqrt(pow((self.b - self.a) / 2, 2) + pow(self.h, 2)))))
        t.forward(sqrt(pow((self.b - self.a) / 2, 2) + pow(self.h, 2)))
        turtle.done()

    def Rhombus(self):
        t = turtle.Turtle()
        for i in range(2):
            t.forward(self.a)
            t.left(45)
            t.forward(self.a)
            t.left(135)

        turtle.done()

    def Parallelogram(self):
        t = turtle.Turtle()
        for i in range(2):
            for i in range(2):
                t.forward(self.a)
                t.left(45)
                t.forward(self.a)
                t.left(135)




