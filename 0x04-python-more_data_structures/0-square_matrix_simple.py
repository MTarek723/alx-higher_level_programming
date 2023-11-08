#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for x in matrix:
        result1 = []
        for y in x:
            result1.append(y**2)
        result.append(result1)
    return result
