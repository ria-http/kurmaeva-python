# Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
n = input('введите количество элементов списка ')
while type(n) != int:  # обработка исключений
  try:
    n = int(n)
  except ValueError:
    print('неправильно ввели число')
    n = input('введите количество элементов списка ')

print('введите', n, 'чисел через пробел')
a = list(map(int, input().split()))

ind1 = -1  # хранение индексов одинаковых элементов
ind2 = -1

for i in range(n):
  for j in range(i + 1, n):  # проверка элемента после i
    if a[i] == a[j]:
      ind1 = i
      ind2 = j
      break

print('индексы одинаковых элементов :', ind1, ind2)