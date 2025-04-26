# В двумерном списке найти максимальный положительный элемент, кратный 4.

import random

strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(1, 10) for el in range(col)] for ell in range(strr)]
print('исходник:')
for i in matr:
    print(i)

max_num = max(filter(lambda x: x > 0 and not x % 4,
                   (num for row in matrix for num in row)),
             default=None)

print(max_num if max_num is not None else "Нет подходящих")