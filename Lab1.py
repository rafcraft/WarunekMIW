import numpy as np


def wyznacznik_rekurencja(a):
    indices = list(range(len(a)))
    wynik = 0
    if len(a) == 2 and len(a[0]) == 2:
        macierz2x2 = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return macierz2x2
    for x in indices:
        macierz_pomocnicza = a.copy()
        y = macierz_pomocnicza[1:]
        wysokosc = len(y)
        for i in range(wysokosc):
            y[i] = y[i][0:x] + y[i][x + 1:]

        det = (-1) ** (x % 2)
        podmacierz = wyznacznik_rekurencja(y)
        wynik += det * a[0][x] * podmacierz

    return wynik


def wyznacznik1(x):
    det = np.linalg.det(x)
    return det


M1 = [[-2, 2, -3], [-1, 5, 3], [2, 0, -1]]
M2 = [[1, 3], [6, 5]]
M3 = [[1, 3, 5], [3, 5, 7], [3, 5, 6]]
print("M2 rekurencja: ", wyznacznik_rekurencja(M2))
print("M3 rekurencja: ", wyznacznik_rekurencja(M3))
print("M1 rekurencja: ", wyznacznik_rekurencja(M1))
print("")
print("##########################################")
print("")
print("Macierz z numpy M1: ", wyznacznik1(M1))
print("Macierz z numpy M1 (zaokraglenie): ", int(wyznacznik1(M1)))
print("Macierz z numpy M2: ", int(wyznacznik1(M2)))
print("Macierz z numpy M3: ", int(wyznacznik1(M3)))
