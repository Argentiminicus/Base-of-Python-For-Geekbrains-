from sys import argv


def salary():
    try:
        hours, salary_per_hours, bonus = [float(el) for el in argv[1:]]
        print(hours * salary_per_hours + bonus)
    except ValueError:
        print('Нужно ввести 3 числа')


salary()
