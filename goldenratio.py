#!/usr/bin/python3

import math

phi = (1 + math.sqrt(5)) / 2

def minimize(f, a, b, eps):
    while (b - a) > eps:
        l, r = b - (b - a) / phi, a + (b - a) / phi
        if f(l) < f(r):
            b = r
        else:
            a = l
    x = (a + b) / 2
    return (x, f(x))

if __name__ == "__main__":
    print(minimize(lambda x: x**5/5 - 10 * x**3 / 3 + 9 * x, -2, 2, 1e-5))
