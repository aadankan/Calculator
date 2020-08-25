class Divisibility:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self):
        try:
            if self.x % self.y == 0:
                return "Liczba " + str(self.x), " JEST podzielna przez:", self.y
            else:
                return "Liczba", self.x, "NIE JEST podzielna przez:", self.y
        except:
            return "Spróbuj ponownie:"
