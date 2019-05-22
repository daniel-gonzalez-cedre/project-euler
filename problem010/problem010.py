# 高明俊 daniel-simon-gonzalez

from math import sqrt
from math import floor
import numpy as np

def primes(n):
    primes = [p for p in range(2, N) if all(p % i != 0 for i in range(2, floor(sqrt(p)) + 1))]
    return primes

N = 2*pow(10, 6)
S = np.sum(primes(N))
print(S)
