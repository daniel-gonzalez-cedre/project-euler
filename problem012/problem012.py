# 高明俊 daniel-simon-gonzalez

from math import sqrt
from math import floor
import numpy as np

def num_div(x):
    if x == 1:
        return 1
    div = [x % n == 0 for n in range(1, floor(sqrt(x) + 1))]
    return 2*np.sum(div)

def triangle(div):
    n = 1
    tri = 1
    d = num_div(tri)
    while d <= div:
        n = n + 1
        tri = tri + n
        d = num_div(tri)
    return tri

div = 500
print(triangle(div))
