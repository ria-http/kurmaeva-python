#Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить циклический сдвиг
#элементов списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..., AN — в AK).
#Допускается использовать вспомогательный список из 4 элементов.

n = input('введите количество элементов списка ')
while type(n) != int:    #обработка исключений
  try:
    n = int(n)
  except ValueError:
    print('неправильно ввели число')
    n = input('введите количество элементов списка ')

print('введите', n, 'чисел через пробел')
a = list(map(int, input().split()))

k = input('введите сдвиг ')
while type(k) != int:    #обработка исключений
  try:
    k = int(k)
  except ValueError:
    print('неправильно ввели число')
    k = input('введите количество элементов списка ')

helpler = [0] * 4   #нью список

for i in range(k):
    helpler[i] = a[n - k + i]

for i in range(n - k - 1, -1, -1):     # cдвигаем оставшиеся элементы вправо
    a[i + k] = a[i]

for i in range(k):
    a[i] = helpler[i]

print('cписок после сдвига:', a)