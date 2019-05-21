# 高明俊 daniel-simon-gonzalez

from math import floor
from math import sqrt

L = 600851475143

def is_prime(x):
    if x % 2 == 0 and x != 2:
        return False
    if x < 2:
        return False
    p = floor(sqrt(x))
    if p % 2 == 0:
        p = p + 1
    while p > 2:
        if x % p == 0:
            return False
        p = p - 2
    return True

def largest_prime_factor(x):
    if is_prime(x):
        return x
    p = floor(sqrt(x))
    if p % 2 == 0:
        p = p + 1
    while p > 2:
        if x % p == 0 and is_prime(p):
            return p
        p = p - 2
    if x % 2 == 0:
        return 2

print(largest_prime_factor(L))
