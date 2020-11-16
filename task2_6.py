goods = []
dict_us = {}
list_name = []
list_price = []
list_quantity = []
list_measuring = []
i = 0
j = 1

while True:
    i += 1
    if i > 3:
        break
    else:
        name = input(f'Введи название {i}-го товара: ')
        list_name.append(name)
        dict_us['название'] = name

        price = float(input(f'Введи цену {i}-го товара: '))
        list_price.append(price)
        dict_us['цена'] = price

        quantity = int(input(f'Введи количество {i}-го товара: '))
        list_quantity.append(quantity)
        dict_us['количество'] = quantity

        measuring = input(f'Введи ед. измерения {i}-го товара: ')
        list_measuring.append(measuring)
        dict_us['ед'] = measuring

        tuple_us = (j, dict_us)
        goods.append((j, dict_us))
        j += 1
        if j > 3:
            break
print(f'\nСтруктура данных на товары:\n {goods}')

analitic = {'название': list_name, 'цена': list_price,
            'количество': list_quantity, 'ед': list_measuring}

print(f'\nА вот и аналитика:\n {analitic}')
