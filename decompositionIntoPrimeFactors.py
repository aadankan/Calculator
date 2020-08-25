def Decomposition(x):
    a = []
    b = 2
    while x != 1:
        while x % b == 0:
            x //= b
            a.append(b)

        b += 1

    return a
