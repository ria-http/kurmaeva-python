# В двумерном списке найти сумму элементов второй половины матрицы.
matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
polovina = len(matr) // 2
srez = matr[polovina:]
print(srez)

summ = sum(sum(el) for el in srez)
print(summ)