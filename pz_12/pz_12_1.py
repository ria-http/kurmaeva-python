# В последовательности на n целых чисел умножить все элементы на первый элемент
import random

n = int(input('введите количество чисел '))
listt = ([random.randint(0,50) for el in range(n)])

first = listt[0]
new = [i * first for i in listt]

print('начальный список:', listt)
print('новый список:', new)