''' Cредствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Положительные числа:
Количество положительных чисел:
Отрицательные числа:
Количество отрицательных чисел: '''

with open('numbers.txt', 'w', encoding='utf-8') as file:
  file.write('-99 6 12 -36 20 45 100 -15')  # создаю список, содержащий 1 строку
with open('numbers.txt', 'r', encoding='utf-8') as file:
  nums = list(map(int, file.read().split()))

pol = [num for num in nums if num > 0]
otr = [num for num in nums if num < 0]
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write("Исходные данные: " + ' '.join(map(str, nums)) + '\n')
    file.write("Количество элементов: " + str(len(nums)) + '\n')
    file.write("Положительные числа: " + ' '.join(map(str, pol)) + '\n')
    file.write("Количество положительных чисел: " + str(len(pol)) + '\n')
    file.write("Отрицательные числа: " + ' '.join(map(str, otr)) + '\n')
    file.write("Количество отрицательных чисел: " + str(len(otr)) + '\n')
print('файлы созданы')