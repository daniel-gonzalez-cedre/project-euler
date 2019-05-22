# 高明俊 daniel-simon-gonzalez

from math import sqrt
from math import floor
import sys

sys.setrecursionlimit(100002)

def is_prime(x):
    return all(x % num != 0 for num in range(2, floor(sqrt(x) + 1)))

def prime(N):
    return prime_N(2, 1, N)

def prime_N(p, n, N):
    if n == N:
        return p
    if p == 2:
        return prime_N(p + 1, n + 1, N)
    p = p + 2
    while not is_prime(p):
        p = p + 2
    return prime_N(p, n + 1, N)

print(prime(10001))
