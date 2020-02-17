#!/usr/bin/env python3
"""Matrix minor"""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Compute first minor matrix"""
    try:
        assert isinstance(matrix, list)
        assert len(matrix) > 0
        assert all(isinstance(row, list) for row in matrix)
    except AssertionError:
        raise TypeError('matrix must be a list of lists')

    try:
        assert all(len(row) == len(matrix) for row in matrix)
    except AssertionError:
        raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix) == 1:
        return [[1]]

    minors = []
    for i1, row in enumerate(matrix):
        minor_row = []
        for j1 in range(len(row)):
            sub_matrix = []
            for i2, row in enumerate(matrix):
                if i2 != i1:
                    sub_row = []
                    for j2 in range(len(row)):
                        if j2 != j1:
                            sub_row.append(matrix[i2][j2])
                    sub_matrix.append(sub_row)
            minor_row.append(determinant(sub_matrix))
        minors.append(minor_row)
    return minors
