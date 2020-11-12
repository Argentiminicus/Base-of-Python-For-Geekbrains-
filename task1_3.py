while True:
    n = int(input('Введи целое положительное число: '))
    if n <= 0:
        continue
    else:
        n = str(n)
        print(int(n) + int(n + n) + int(n + n + n))
        break
