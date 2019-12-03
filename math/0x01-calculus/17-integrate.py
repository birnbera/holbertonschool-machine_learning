#!/usr/bin/env python3
"""Integrate polynomial vector"""


def poly_integral(poly, C=0):
    """Integrate poly with constant factor C"""
    return [C] + [coef/i for i, coef in enumerate(poly, 1)]
