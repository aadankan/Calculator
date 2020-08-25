def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    a = int(n**0.5) + 1
    for d in range(3, a, 2):
        if n % d == 0:
            return False
    return True