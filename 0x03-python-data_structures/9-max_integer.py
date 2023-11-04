#!/usr/bin/python3
def max_integer(my_list=[]):
    max1 = my_list[0]
    for x in my_list:
        if max1 < x:
            max1 = x
    return max1
