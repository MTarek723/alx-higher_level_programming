#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    z = 0
    while (y < x):
        try:
            print("{:d}".format(my_list[y]), end="")
            y += 1
            z += 1
        except (TypeError, ValueError):
            y += 1
            continue
    print()
    return z
