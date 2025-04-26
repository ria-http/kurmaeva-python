# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.  13.1
import random

strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(1, 10) for el in range(col)] for ell in range(strr)]
print('исходник:')
for i in matr:
    print(i)


print('итог:', summ)
