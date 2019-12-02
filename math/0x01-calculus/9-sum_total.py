#!/usr/bin/env python3
"""Calculate sum of squares"""


def summation_i_squared(n):
    """Calculate sum of squares up to n"""
    if n < 1 or n != int(n):
        return None
    if n == 1:
        return 1
    return n*n + summation_i_squared(n-1)
