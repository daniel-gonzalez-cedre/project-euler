# 高明俊 daniel-simon-gonzalez

def fib_sum(f1, f2, total, maximum):
    f3 = f1 + f2
    if f3 >= maximum:
        return total
    else:
        if f3 % 2 == 0:
            return fib_sum(f2, f3, total + f3, maximum)
        else:
            return fib_sum(f2, f3, total, maximum)

S = fib_sum(0, 1, 0, 4*pow(10, 6))
print(S)
