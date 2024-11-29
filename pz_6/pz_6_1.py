# Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, … .
n = input('введите количество элементов списка ')
while type(n) != int:  # обработка исключений
  try:
    n = int(n)
  except ValueError:
    print('неправильно ввели число')
    n = input('введите количество элементов списка ')

left = 0  # начало списка
right = n - 1  # конец списка
a = list(range(n))
result = []

while left <= right:
  if left < right:  # добавляем 2 элемента в начало
    result.append(a[left])
    left += 1
  if left <= right:
    result.append(a[left])
    left += 1

  if left <= right:  # добавляем 2 элемента в конец
    result.append(a[right])
    right -= 1
  if left <= right:
    result.append(a[right])
    right -= 1

print(result)