#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    x = new.index(search)
    new.remove(search)
    new.insert(x, replace)
    return new
