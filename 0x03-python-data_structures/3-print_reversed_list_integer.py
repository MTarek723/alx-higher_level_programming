def print_reversed_list_integer(my_list=[]):
    x = -1
    while x >= -len(my_list):
        print("{:d}".format(my_list[x]))
        x = x - 1
