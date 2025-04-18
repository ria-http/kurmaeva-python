import random

# print([i ** 3 for i in range(0,15) if i % 2 == 0])

names = input("hdjdj ")
spl = list(names.split(' '))
print([el.title() for el in spl])