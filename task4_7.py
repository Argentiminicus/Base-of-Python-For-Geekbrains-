def fact(fact_user):
    factorial = 1
    if fact_user == 0:
        yield f'{fact_user}! = 1'
    for i in range(1, fact_user + 1):
        factorial *= i
        yield f'{i}! = {factorial}'


fact_user = int(input('Введите факториал какого числа хотите вычислить: '))
for el in fact(fact_user):
    print(el)

