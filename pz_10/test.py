listt = input('Введите имена через запятую: ')  # переменная для ввода имен

def names(listt):
  if len(listt) == 0:
      a = 'У Вас нет гостей'
      return a   #возвращаем то, что гостей у мнас нет

  all_guests = listt.split(' ') # каждого гостя мы разделяем пробелом и добавляем в список

  if len(all_guests) == 3:  #если длина списка имен гостей 3
      return listt  # возвращаем строку с именами

  if len(all_guests) >= 3:   # если длина списка имен гостей больше 3
      kolvo = len(all_guests) - 2  # то тут по усл делаем что количество гостей это их длина - 2
      a = f'{all_guests[0]}, {all_guests[1]} и еще {kolvo} гостей'  #тоже по усл
      return a  # возвращаем предложение

result = names(listt)  # выводим функцию и передаем ей строку имен
print(f'Гости: {result}') # выводим