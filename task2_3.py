month = int(input('Введи число месяца от 1 до 12: '))

# list:
year = ['зима', 'весна', 'лето', 'осень']
if month <= 2 or month == 12:
    print(year[0])
elif 3 <= month <= 5:
    print(year[1])
elif 6 <= month <= 8:
    print(year[2])
else:
    print(year[3])

# dict:
year2 = {1: 'зима', 2: 'зима', 12: 'зима',
         3: 'весна',  4: 'весна',  5: 'весна',
         6: 'лето', 7: 'лето', 8: 'лето',
         9: 'осень', 10: 'осень', 11: 'осень'}
print(year2[month])
