#!/usr/bin/env python3
"""Demonstrate array concatenation using numpy"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate mat1 and mat2 along the specified axis"""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return np.concatenate([mat1, mat2], axis=axis)
