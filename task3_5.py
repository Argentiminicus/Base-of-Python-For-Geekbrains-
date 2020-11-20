def summa_numbers():
    """функция."""
    summa = 0
    while True:
        numbers = input('Введи строку из чисел, разделенных пробелом или для выхода нажми q: ').split()
        for element in numbers:
            if element != 'q':
                summa += int(element)
            else:
                return summa
        print(summa)


# print(summa_numbers())
print(input.__doc__)
