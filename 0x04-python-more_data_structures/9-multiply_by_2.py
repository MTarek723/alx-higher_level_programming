#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = a_dictionary.copy()
    x = a_dictionary.keys()
    for y in x:
        d.update({y: a_dictionary.get(y)*2})
    return d
