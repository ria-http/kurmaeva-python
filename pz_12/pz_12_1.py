# В последовательности на n целых чисел умножить все элементы на первый элемент
listt = list(map(int, input('введите числа через пробел ').split()))

first = listt[0]
new = [i * first for i in listt]

print('начальный список:', listt)
print('новый список:', new)