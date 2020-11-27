lines = 0
with open('text_2.txt', 'r', encoding='utf-8') as file:
    for line, word in enumerate(file.readlines(), 1):
        lines += 1
        print(f'В строке № {line} - {len(word.split())} слов')
    print(f'Всего {lines} строк')
