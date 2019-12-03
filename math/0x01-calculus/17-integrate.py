#!/usr/bin/env python3
"""Integrate polynomial vector"""


def poly_integral(poly, C=0):
    """Integrate poly with constant factor C"""
    if not poly \
       or not all(isinstance(coef, (float, int)) for coef in poly) \
       or not isinstance(C, (float, int)):
        return None
    integral = [C] + [coef/i for i, coef in enumerate(poly, 1)]
    return [int(coef) if coef == int(coef) else coef for coef in integral]
