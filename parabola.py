#!/usr/bin/python3

import math


def parabola_min(f, x1, x2, x3):
    f1, f2, f3 = f(x1), f(x2), f(x3)
    return x2 - ((x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)) / (2 * ((x2 - x1)* (f2 - f3) - (x2 - x3) * (f2 - f1)))


def minimize(f, a, b, eps):
    m = (a + b) / 2.0
    delta = eps / 10.0
    while (b - a) > eps:
        u = parabola_min(f, a, m, b)

        if u < m:
            if f(u) < f(m):
                new_triple = (a, u, m)
            elif f(u) > f(m):
                new_triple = (u, m, b)
            else:
                if f(a) > f(m):
                    new_triple = (a, u, b)
                elif f(m) > f(b):
                    new_triple = (u, m, b)
        elif u > m:
            if f(u) < f(m):
                new_triple = m, u, b
            elif f(u) > f(m):
                new_triple = a, m, u
            else:
                if f(b) > f(m):
                    new_triple = (m, u, b)
                elif f(a) > f(m):
                    new_triple = (a, m, u)
        else:
            if f(m - delta) < f(m):
                new_triple = (a, m - delta, b)
            elif f(m + delta) < f(m):
                new_triple = (a, m + delta, b)

        (a, m, b) = new_triple
        

    return (u, f(u))

if __name__ == "__main__":
    print(minimize(lambda x: x**5/5.0 - 10.0 * x**3 / 3.0 + 9.0 * x, -2, 2, 1e-5))
