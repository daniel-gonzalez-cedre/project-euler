# 高明俊 daniel-simon-gonzalez

from math import sqrt
from math import floor
import numpy as np

def prime_factors(x):
    primes = [p for p in range(2, x + 1) if x % p == 0 and all(p % i != 0 for i in range(2, floor(sqrt(p)) + 1))]
    mult = []
    for p in primes:
        num = 1
        y = x
        while y % p == 0:
            num = num + 1
            y = y // p
        mult.append((p, num))
    tuples = {tuple([p for i in range(1, n)]) for (p, n) in mult}
    return tuples

def prime_factors_list(L):
    primes = {t for num in L for t in prime_factors(num)}
    return primes

def lcm(L):
    primes = prime_factors_list(L)
    prod = 1
    for t in primes:
        prod = prod*t[0]
    return prod

L = range(2, 21)
print(lcm(L))
