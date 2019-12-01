#!/usr/bin/env python3
"""Demonstrate the use of numpy matrix multiplication operator"""
import numpy as np


def np_matmul(mat1, mat2):
    """Perform matrix multiplication between mat1 and mat2 in that order"""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return mat1@mat2
