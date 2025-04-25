# В двумерном списке найти сумму элементов второй половины матрицы.
import random
strr = int(input('введите количество строк '))
col = int(input('введите количество столбцов '))

matr = [[random.randint(0,10) for el in range(col)] for el in range(strr)]
print('исходная матрица: ')
for s in matr:
    print(s)

polovina = len(matr) // 2
srez = matr[polovina:]
print(srez)

summ = sum(sum(el) for el in srez)
print('сумма элементов второй половины матрицы: ', summ)