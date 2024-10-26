#Дано вещественное число A и целое число N (>0). Используя один цикл, найти значение выражения 1 - A + A2 - A3 + ... +(-1)N AN. Условный оператор не использовать.
# 1 - a + a2 - a3
a = input("введите вещественное число ")
n = input("введите целое число ")
while type(a) != float:   #обработка исключений
  try:
    a = float(a)
  except ValueError:
    print('неправильно ввели 1 число')
    a = input('введите 1-e число ')

while type(n) != int:
  try:
    n = int(n)
  except ValueError:
    print('неправильно ввели 2 число')
    n = input('введите 2-e число ')

summ = 0.0
result = 1.0
count = 0

if n > 0:   #проверка на положительное число
  while count <= n:
    summ += result
    result *= -a
    count += 1
  print ('итоговое значение ', summ)
else:
  print('введите число больше 0')