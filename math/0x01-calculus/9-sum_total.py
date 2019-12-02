#!/usr/bin/env python3
"""Calculate sum of squares"""


def summation_i_squared(n):
    """Calculate sum of squares up to n"""
    if n < 1 or n != int(n):
        return None
    if n == 1:
        return 1
    n2 = summation_i_squared(n-1)
    if n2 is None:
        return None
    return n*n + n2
