#!/usr/bin/env python3
"""Custom padding size convolution"""
import numpy as np



def convolve_grayscale_padding(images, kernel, padding):
    """Compute convolution of images with kernel using custom padding"""
    ph, pw = padding
    m, h, w = images.shape[-3:]
    kh, kw = kernel.shape[-2:]
    out = np.zeros((m, h + 2*ph - kh + 1, w + 2*pw - kw + 1))

    images = np.pad(
        images,
        (
            (0, 0),  # no padding img axis
            (ph, ph),
            (pw, pw),
        ),
        mode='constant'
    )
    
    for row in range(out.shape[-2] - kh + 1):
        for col in range(out.shape[-1] - kw + 1):
            img = images[:, row:row+kh, col:col+kw]
            conv = (img * kernel).sum(axis=(-1, -2))
            out[:, row, col] = conv
    return out
