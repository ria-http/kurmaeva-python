#1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».
a = input('введите 1-е число ')
b = input('введите 2-е число ')
c = input('введите 3-е число ')
while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print('неправильно ввели 1 число')
    a = input('введите 1-e число ')

while type(b) != int:
  try:
    b = int(b)
  except ValueError:
    print('неправильно ввели 2 число')
    b = input('введите 2-e число ')

while type(c) != int:
  try:
    c = int(c)
  except ValueError:
    print('неправильно ввели 3 число')
    c = input('введите 3-e число ')

if a > 0 and b > 0 and c < 0:
  с
  print(t)
elif a > 0 and b < 0 and c > 0:
  t = True
  print(t)
elif a < 0 and b > 0 and c > 0:
  t = True
  print(t)
else:
  f = False
  print(f)