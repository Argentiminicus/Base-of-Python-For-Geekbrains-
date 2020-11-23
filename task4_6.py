from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

i = 0
for el in cycle(['Да', 'Нет']):
    if i > 9:
        break
    else:
        i += 1
        print(el)
