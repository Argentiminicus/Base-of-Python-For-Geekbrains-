my_lessons = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lesson, other = line.split(':')
        hours = sum(map(int, ''.join([el for el in other if el == ' ' or '0' <= el <= '9']).split()))
        my_lessons[lesson] = hours
print(my_lessons)
