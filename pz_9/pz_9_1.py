#Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
#удалить из него второй и третий элементы. Отобразить исходный и получившийся
#словарь. Использовать for, range.

slovarik = {}
for i in range(7):
  slovarik[i] = i ** 2
print('1 версия: ',slovarik)

del slovarik[1]
del slovarik[2]

print('словарь с удаленными эл-ми: ',slovarik)