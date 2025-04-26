# В двумерном списке элементы первого столбца возвести в куб.  6
import random
n, m = 4, 4
matrix = [[random.randint(1, 10) for i in range(m)] for i in range(n)]

print("matrix:")
for i in matrix:
  print(i)

mod_matr = [[x**3 if j == 0 else x for j, x in enumerate(row)] for row in matrix]
print('\n mod_matrix:')
for i in mod_matr:
  print(i)