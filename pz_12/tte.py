import random

# print([i ** 3 for i in range(0,15) if i % 2 == 0])  # возвести в куб четные числа

# names = input("hdjdj ")  # писать имена с большой буквы  в списке
# spl = list(names.split(' '))
# print([el.title() for el in spl])

word = input('ВВЕДИТЕ СЛОВА ')  # добавить слова в список, если их длина больше 4
listt = list(word.split(' '))
print([el for el in listt if len(el) > 4])