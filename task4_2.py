my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

more_prev = [num for num in my_list if my_list[my_list.index(num)] > my_list[my_list.index(num)-1]
             and num != my_list[0]]

print(more_prev)
