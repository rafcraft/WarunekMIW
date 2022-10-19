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


M1 = [[-2, 2, -3], [-1, 5, 3], [2, 0, -1]]
print(wyznacznik_rekurencja(M1))


def wyznacznik1(x):
    det = np.linalg.det(x)
    return det


def wyznacznik2(x):
    temp = len(x)
    if temp == 2:
        return "Wyznacznik macierzy 2x2: ", (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])
    if temp == 3:
        return "Wyznacznik macierzy 3x3: ", ((x[0][0] * x[1][1] * x[2][2] + x[1][0] * x[2][1] * x[0][2] + x[2][0] * x[0][1] * x[1][2]) -
                                             (x[0][2] * x[1][1] * x[2][0] + x[1][2] * x[2][1] * x[0][0] + x[2][2] * x[0][1] * x[1][0]))
    else:
        print("Macierz musi być kwadratowa!")


A = np.array([[10, 5], [6, 7]])
A3 = np.array([[10, 2, 2], [2, 5, 8], [1, 1, 1]])

print("Macierz 2x2", int(wyznacznik1(A)))
print("Macierz 3x3", int(wyznacznik1(A3)))

print(wyznacznik2(A))
print(wyznacznik2(A3))
