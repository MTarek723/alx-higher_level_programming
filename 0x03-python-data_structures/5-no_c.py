#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in my_string:
        if ord(x) != 67 and ord(x) != 99:
            new_string += x
    return new_string
