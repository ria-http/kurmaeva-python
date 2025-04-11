# Составить генератор (yield), который переведет символы строки из нижнего регистра в верхний.
sss = input('введите строку ')
def up(sss):
  yield from [i.upper() for i in sss]

upp = "".join(up(sss))
print(upp)