from basicAlgebra import Algebra
from geometricFigures import Figures
from drawingFigures import DrawingFigures
from divisibilityOfNumbers import Divisibility
from primeNumber import czy_pierwsza
from dividers import DzielnikiWlasciwe
from decompositionIntoPrimeFactors import Decomposition


def main():
    run = True
    while run:
        print(" 0. Wyjscie")
        print(" 1. Podstawowa algebra: ")
        print(" 2. Figury geometryczne: ")
        print(" 3. Podzielność liczb")
        print(" 4. Liczba pierwsza")
        print(" 5. Dzielniki liczb")
        print(" 6. Rozkład na czynniki pierwsze")
        print(" 7. Największy wspólny dzielnik")
        print(" 8. Najmniejsza wspólna wielokrotność")
        option = input("Wybierz opcje: ")
        if option == '0':
            break
        if option == '1':
            print(" 1. Dodawanie")
            print(" 2. Odejmowanie")
            print(" 3. Mnożenie")
            print(" 4. Dzielenie")
            print(" 5. Potęgowanie")
            print(" 6. Pierwiastkowanie n-tego stopnia")
            option = input("Wybierz opcje: ")
            a = input("Podaj pierwsza liczbę:")
            b = input("Podaj drugą liczbę:")
            x = Algebra(a, b)
            try:
                if option == "1":
                    print("Wynik to:", x.Add())
                if option == "2":
                    print("Wynik to:", x.Substract())
                if option == "3":
                    print("Wynik to:", x.Multiply())
                if option == "4":
                    print("Wynik to:", x.Division())
                if option == "5":
                    print("Wynik to:", x.Power())
                if option == "6":
                    print("Wynik to:", x.nRoot())
            except:
                print("Bląd, spróbuj ponownie")
                continue
        if option == '2':
            print(" 1. Kwadrat")
            print(" 2. Prostokąt")
            print(" 3. Trójkąt")
            print(" 4. Koło")
            print(" 5. Owal")
            print(" 6. Trapez")
            print(" 7. Romb")
            print(" 8. Równoległobok")

            option = input("Wybierz opcję: ")
            if option == "1":
                a = input("Podaj bok kwadratu: ")
                x = Figures(a)
                print("Wynik to:", x.Square())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a)
                    x.Square()
                else:
                    continue

            if option == "2":
                a = input("Podaj pierwszy bok prostokąta: ")
                b = input("Podaj drugi bok prostokąta: ")
                x = Figures(a, b)
                print("Wynik to:", x.Rectangle())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a, b)
                    x.Rectangle()
                else:
                    continue

            if option == "3":
                a = input("Podaj podstawę trojkąta: ")
                h = input("Podaj wysokość trojkąta: ")
                x = Figures(a, h=h)
                print("Wynik to:", x.Triangle())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a, h=h)
                    x.Triangle()
                else:
                    continue

            if option == "4":
                r = input("Podaj promień koła: ")
                x = Figures(r=r)
                print("Wynik to:", x.Circle())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(r=r)
                    x.Circle()
                else:
                    continue

            if option == "5":
                r = input("Podaj pierwsza półoś owalu: ")
                h = input("Podaj druga półoś owalu: ")
                x = Figures(r=r, h=h)
                print("Wynik to:", x.Oval())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(r=r)
                    if h > r:
                        x.FlatOval()
                    elif h < r:
                        x.TallOval()
                    else:
                        x.Circle()
                else:
                    continue

            if option == "6":
                a = input("Podaj długość górnej podstawy: ")
                b = input("Podaj długość dolnej podstawy: ")
                h = input("Podaj wysokość trapezu: ")
                x = Figures(a=a, b=b, h=h)
                print("Wynik to:", x.Trapeze())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a=a, b=b, h=h)
                    x.Trapeze()
                else:
                    continue

            if option == "7":
                a = input("Podaj długość podstawy: ")
                h = input("Podaj wysokość rombu: ")
                x = Figures(a=a, h=h)
                print("Wynik to:", x.Rhombus())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a=a, h=h)
                    x.Rhombus()
                else:
                    continue

            if option == "8":
                a = input("Podaj długość podstawy: ")
                h = input("Podaj wysokość równoległoboku: ")
                x = Figures(a=a, h=h)
                print("Wynik to:", x.Parallelogram())
                print("Narysować?")
                option = input("(Tak/Nie): ").upper()
                if option == "TAK":
                    x = DrawingFigures(a=a, h=h)
                    x.Parallelogram()
                else:
                    continue
        if option == '3':
            a = input("Podaj liczbę do sprawdzenia: ")
            b = input("Podaj dzielnik: ")
            x = Divisibility(int(a), int(b))
            print(x.check())
        if option == '4':
            a = input("Podaj liczbę do sprawdzenia: ")
            if czy_pierwsza(int(a)) == True:
                print("\n" + a + " JEST liczbą pierwszą \n")
            elif czy_pierwsza(int(a)) == False:
                print("\n" + a + " NIE JEST liczbą pierwszą \n")
        if option == '5':
            a = input("Podaj liczbę do sprawdzenia: ")
            print("Dzielniki to: " + str(DzielnikiWlasciwe(int(a))))
        if option == '6':
            a = input("Podaj liczbę do rozkłądu: ")
            print("Dzielniki to: " + str(Decomposition(int(a))))
        if option == '7':




main()
