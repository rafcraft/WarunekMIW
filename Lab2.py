import numpy as np


def swap(a, rzad1, rzad2, col):
    for i in range(col):
        temp = a[rzad1][i]
        a[rzad1][i] = a[rzad2][i]
        a[rzad2][i] = temp


def rzad_macierzy(a):
    rzad = len(a)

    for row in range(rzad):
        if a[row][row] != 0:
            for col in range(len(a)):
                if col != row:
                    mnoznik = a[col][row] / a[row][row]
                    for i in range(rzad):
                        a[col][i] -= (mnoznik * a[row][i])
        else:
            redukcja = True
            for i in range(row + 1, len(a)):
                if a[i][row] != 0:
                    swap(a, row, i, rzad)
                    redukcja = False
                    break
            if redukcja:
                rzad -= 1
                for i in range(0, rzad, 1):
                    a[i][row] = a[i][rzad]
            row -= 1
    return rzad


A = ([[1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]])
B = ([[2, 1, -4], [3, 5, -7], [4, -5, -6]])
print(rzad_macierzy(A))
print(rzad_macierzy(B))
