# 高明俊 daniel-simon-gonzalez

import numpy as np

def is_pal(x):
    s = str(x)
    return s == s[::-1]

def pal_prod(digits):
    vect = np.asarray(range(pow(10, digits - 1), pow(10, digits)))[:, None]
    grid = (vect @ vect.T).flatten()
    palindromes = [g for g in grid if is_pal(g)]
    return max(palindromes)

digits = 3
print(pal_prod(digits))
