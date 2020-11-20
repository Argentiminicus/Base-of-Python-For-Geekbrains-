def func(x, y):
    try:
        x = int(x)
        y = int(y)
        print(round((x / y), 2))
    except ZeroDivisionError:
        print('Вторым числом вы ввели ноль.')
    except ValueError:
        print('Нужно вводить числа')


number1 = input('Введи первое число: ')
number2 = input('Введи второе число: ')

func(number1, number2)
