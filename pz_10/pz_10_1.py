sadovod1 = {"Анжелика", "Виктория", "Гагарин"}
sadovod2 = {"Катарина", "Юбилейная", "Анжелика"}
sadovod3 = {"Гагарин", "Анжелика", "Катарина"}
all = {"Анжелика", "Виктория", "Гагарин", "Катарина", "Юбилейная", "Южная"}

print('есть у каждого: ', sadovod1 & sadovod2 & sadovod3)
print('есть хотя бы у 1: ', sadovod1 | sadovod2 | sadovod3 )
print('нет ни у 1-го: ', all -(sadovod1 | sadovod2 | sadovod3))