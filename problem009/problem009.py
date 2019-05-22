# 高明俊 daniel-simon-gonzalez

import numpy as np

def search():
    for a in range(1, 1001):
        for b in range(a, 1001):
            c = np.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                return (a, b)
    return (0, 0)

a, b = search()
c = np.sqrt(a**2 + b**2)
print(int(a*b*c))
