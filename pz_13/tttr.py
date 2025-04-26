# Для каждого столбца матрицы с четным номером найти сумму ее элементов. 14,1
import random

strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(1, 10) for el in range(col)] for ell in range(strr)]
print('исходник:')
for i in matr:
    print(i)

res = [sum(row) / len(row) for i, row in enumerate(matr, 1) if i % 2 != 0]


