#!/usr/bin/env python3
"""Integrate polynomial vector"""


def poly_integral(poly, C=0):
    """Integrate poly with constant factor C"""
    if not poly \
       or not all(type(coef) in (float, int) for coef in poly) \
       or not type(C) == int:
        return None
    integral = [coef/i for i, coef in enumerate(poly, 1)]
    return [C] + [int(coef) if coef == int(coef) else coef for coef in integral]
