n_max = None
while True:
    n = int(input('Введи целое положительное число из нескольких цифр: '))
    if n <= 0 or n < 10:
        continue
    else:
        n_max = n % 10
        n = n // 10
        while True:
            b = n % 10
            if b == 0:
                break
            n = n // 10
            if n_max < b:
                n_max = b
        break

print(n_max)
