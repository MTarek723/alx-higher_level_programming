#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    y = 0
    new_list = my_list[:]
    for x in my_list:
        if x % 2 == 0:
            new_list[y] = True
            y = y + 1
        else:
            new_list[y] = False
            y = y + 1
    return new_list
