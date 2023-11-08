#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.keys()
    for y in x:
        a_dictionary.update({y: a_dictionary.get(y)*2})
    return a_dictionary
