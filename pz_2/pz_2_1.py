#Вариант 16. Дано трехзначное число. Найти сумму и произведение его цифр.
num = input('введите 3-значное число ')
while type(num) != int:   #обработка исключений
  try:
    num = int(num)
    if 99 < num < 1000:   #проверка на 3-х значное число
      sot = num // 100
      des = (num // 10) % 10
      ed = num % 10
      print(sot, des, ed)
      summ = sot + des + ed
      pr = sot * des * ed
      print(' сумма чисел', summ, '\n', 'произведение чисел', pr)
    else:
      print('число не 3-значное')
      num = input('введите 3-значное число ')
  except ValueError:
    print('вы ввели не число')
    num = input('введите 3-значное число ')