#2. Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер числа, отличного от остальных.
a = input("введите 1-е число ")
b = input("введите 2-е число ")
c = input("введите 3-е число ")

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

if a == b and a == c:
  print("все числа равны")
elif a == b:
  print("отличается 3 число")
elif a == c:
  print("отличается 2 число")
elif b == c:
  print("отличается 1 число")
elif a != b and a != c and b != c:
  print("все числа разные")