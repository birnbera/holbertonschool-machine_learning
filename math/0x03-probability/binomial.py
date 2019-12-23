#!/usr/bin/env python3
"""Module to represent binomial distribution"""


class Binomial:
    """Class to store parameters and methods of the binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """Initialize binomial distribution from data or set parameters 
        using n and p."""
        if data is None:
            try:
                self.n = int(n)
                assert n > 0
            except (TypeError, AssertionError):
                raise ValueError('n must be a positive integer')
            try:
                self.p = float(p)
                assert 0 < self.p < 1
            except (TypeError, AssertionError):
                raise ValueError('p must be greater than 0 and less than 1')
        elif type(data) != list:
            raise TypeError('data must be a list')
        elif len(data) < 2:
            raise ValueError('data must contain multiple values')
        else:
            mean = sum(data)/len(data)
            var = sum((d - mean)**2 for d in data)/len(data)
            p = 1.0 - var/mean
            n = sum(d/p for d in data)/len(data)
            if n % 1 < 0.5:
                n = int(n)
            else:
                n = int(n + 1)
            p = sum(d/n for d in data)/len(data)
            self.n = n
            self.p = float(p)
