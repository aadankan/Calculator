import math


class Algebra:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Add(self):
        return float(self.x) + float(self.y)

    def Substract(self):
        return float(self.x) - float(self.y)

    def Multiply(self):
        return float(self.x) * float(self.y)

    def Division(self):
        if self.y == '0':
            return "Nie mozna dzielic przez zero!"
        else:
            return float(self.x) / float(self.y)

    def Power(self):
        return round(math.pow(float(self.x), float(self.y)), 5)

    def nRoot(self):
        return round(math.pow(float(self.x), 1/float(self.y)), 5)

