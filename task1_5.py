give = float(input('Введите выручку фирмы: '))
take = float(input('Введите издержки фирмы: '))

if give > take:
    print('Фирма работает с прибылью')
    print('Рентабельность выручки', give / take)
    employes = int(input('Введите численность сотрудников в фирме: '))
    print('Прибыль фирмы в расчете на одного сотрудника', (give - take) / employes)
else:
    print('Фирма работает в убыток')
