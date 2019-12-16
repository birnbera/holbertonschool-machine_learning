#!/usr/bin/env python3
"""Module to store exponential probability related class"""
e = 2.7182818285


class Exponential:
    """Class to represent the exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Initialize an exponential from data or lambtha if data is missing"""
        self.lambtha = float(lambtha)
        if data is None and self.lambtha <= 0:
            raise ValueError('lambtha must be a positive value')
        if data is not None:
            if type(data) != list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = (sum(data)/len(data))**-1
