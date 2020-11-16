my_list = [7, 5, 3, 3, 2]

while True:
    n_user = int(input('Введи новый элемент рейтинга - натуральное положительное число: '))
    i = 0
    for n in my_list:
        if n_user <= n:
            i += 1
    my_list.insert(i, n_user)
    print(my_list)
