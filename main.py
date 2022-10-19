def wyznacznik(a):
    indices = list(range(len(a)))
    wynik = 0
    if len(a) == 2 and len(a[0]) == 2:
        macierz2x2 = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return macierz2x2
    for x in indices:
        macierz_pomocnicza = a.copy()
        y = macierz_pomocnicza[1:]
        height = len(y)
        for i in range(height):
            y[i] = y[i][0:x] + y[i][x + 1:]

        sign = (-1) ** (x % 2)
        sub_det = wyznacznik(y)
        wynik += sign * a[0][x] * sub_det

    return wynik


M1 = [[-2, 2, -3], [-1, 5, 3], [2, 0, -1]]
print(wyznacznik(M1))
