#!/usr/bin/env python3
"""Calculate sum of squares"""


def summation_i_squared(n):
    """Calculate sum of squares up to n"""
    if n < 1 or n != int(n):
        return None
    return sum(i**2 for i in range(int(n)+1))
