def DzielnikiWlasciwe(a):
    wynik = []

    if a < 1:
        return "Liczba musi być większa od 1"

    for i in range(1, a // 2 + 1):
        if a % i == 0:
            wynik.append(i)
    wynik.append(a)

    if len(wynik) == 1 or len(wynik) == 2:
        return "Jest to LICZBA PIERWSZA"

    return wynik