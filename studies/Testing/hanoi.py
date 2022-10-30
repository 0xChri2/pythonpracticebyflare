def hanoi(n, start, ziel, hilf):
    if n == 1:
        print("Bewege Scheibe 1 von Start", start, "nach Ziel", ziel)
    else:
        hanoi(n - 1, start, hilf, ziel)
        print("Bewege Scheibe", n, "von Start", start, "nach Ziel", ziel)
        hanoi(n - 1, hilf, ziel, start)


n = 3
hanoi(n, 'S', 'Z', 'H')