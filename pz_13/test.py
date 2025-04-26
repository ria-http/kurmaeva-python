# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
import random

strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(1, 10) for el in range(col)] for ell in range(strr)]
print('исходник:')
for i in matr:
    print(i)

last = [sss[-2:] for sss in matr]
res = sum(sum(el) for el in last) / (2 * strr)
print(res)

