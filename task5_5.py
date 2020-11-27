from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as file:
    numbers = [randint(1, 10) for _ in range(1, 10)]
    file.write(' '.join(map(str, numbers)))

print(sum(numbers))
