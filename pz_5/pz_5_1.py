#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами.
#Значения n и m программа должна запрашивать
def prak(n, m):
  summ = 0
  while n <= m:
    summ += n
    n += 1
  print(summ)

n1 = input('введите 1-е число ')   #обьявляем переменные, которые типо привязаны к нашей функции
m1 = input('введите 2-е число ')

while type(n1) != int:
  try:
    n1 = int(n1)
  except ValueError:
    print('неправильно ввели 1 число')
    n1 = input('введите 1-e число ')

while type(m1) != int:
  try:
    m1 = int(m1)
  except ValueError:
    print('неправильно ввели 2 число')
    m1 = input('введите 2-e число ')

prak(n1, m1)