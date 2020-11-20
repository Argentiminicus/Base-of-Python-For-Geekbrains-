def my_func(x, y, z):
    list_func = [x, y, z]
    minimum = min(list_func)

    position = list_func.index(minimum)
    list_func.pop(position)
    max_num = sum(list_func)

    return max_num


print(f'Сумма 2-х наибольших чисел: {my_func(10, 16, 45)}')
