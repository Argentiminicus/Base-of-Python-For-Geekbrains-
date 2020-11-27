with open('text_1.txt', 'w', encoding='utf-8') as data:
    while True:
        text = input('Введи строку или оставь пусто: ')
        print(text, file=data)
        if text == '':
            break
