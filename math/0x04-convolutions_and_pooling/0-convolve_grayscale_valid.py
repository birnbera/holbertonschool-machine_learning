#!/usr/bin/env python3
"""Module containing greyscale convolution function"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Function to compute the convolution of (greyscale) images with kernel"""
    out = np.zeros(
        (
            images.shape[0],
            images.shape[1] - kernel.shape[0] + 1,
            images.shape[2] - kernel.shape[1] + 1,
        )
    )
    for row in range(out.shape[-2]):
        for col in range(out.shape[-1]):
            img = images[:, row:row+kernel.shape[0], col:col+kernel.shape[1]]
            conv = (img * kernel).sum(axis=(-1, -2))
            out[:, row, col] = conv
    return out
