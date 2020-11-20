# 1 способ
# def my_func(x, y):
#     return x ** y
# print(my_func(2, -1))

# или проще:
# print((lambda x, y: x ** y)(2, -1))

# 2 способ
def my_func(x, y):
    i = 0
    answer = 0
    non_x = x
    while i != abs(y)-1:
        i += 1
        non_x = non_x * x
        answer = 1 / non_x
    print(round(answer, 8))


my_func(5, -4)
