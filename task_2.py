# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


mass_1 = [1, 5, 7, 3, 178, 56, -1, 25, -17, 36]
n_min = 0
n_max = 78

new_mass = []
new_mass_1 = []

for i in range(len(mass_1)):
    if n_min < mass_1[i] < n_max:
        new_mass.append(i)
    else:
        new_mass_1.append(i)

print (new_mass)