# В двумерном списке найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьей строки исходной матрицы на полученные суммы.
import random
strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(0,10) for el in range(col)] for el in range(strr)]

print('исходная матрица: ')
for s in matr:
    print(s)

sum_str = [sum(el) for el in matr]
print('сумма элементов строк:', sum_str)

matr[2] = sum_str
print('итоговая матрица: ')
for i in matr:
    print(i)