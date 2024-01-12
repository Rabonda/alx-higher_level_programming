#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix_2 = []
        for indx in matrix:
            matrix_2.append(list(map(lambda x: x * x, indx)))
        return matrix_2
