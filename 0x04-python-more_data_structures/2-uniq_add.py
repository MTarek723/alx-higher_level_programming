#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set()
    sum1 = 0
    for x in my_list:
        new.add(x)
    for y in new:
        sum1 = sum1 + y
    return sum1
