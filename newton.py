#!/usr/bin/python3

import math

def find_root(f, ff, x0, eps):
    x = x0
    while abs(f(x)) > eps:
        x = x - f(x) / ff(x)

    return x

def minimize(f, ff, fff, x0, eps):
    x = find_root(ff, fff, x0, eps)
    if fff(x) < 0:
        return "Минимум не найден"
    return (x, f(x))

if __name__ == "__main__":
    f = lambda x: x**5/5 - 10*x**3/3 + 9 * x
    ff = lambda x: x**4 - 10 * x**2 + 9
    fff = lambda x: 4 * x**3 - 20 * x
    print(minimize(f, ff, fff, -1.5, 1e-5))
