my_list = []

while True:
    element = input('Введи элемент списка или нажми q: ')
    if element == 'q':
        break
    else:
        my_list.append(element)

print(f'Исходный список: {my_list}')

i = 0
while True:
    try:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
    except IndexError:
        break
print(f'Измененный список: {list(my_list)}')



