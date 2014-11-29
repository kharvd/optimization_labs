#!/usr/bin/python3

def minimize(f, a, b, eps):
    delta = eps / 10.0
    while (b - a) > eps:
        m = (a + b) / 2.0
        l, r = m - delta, m + delta
        if f(l) < f(r):
            b = l
        else:
            a = r
    return (a, f(a))

if __name__ == "__main__":
    print(minimize(lambda u: 4 * u**2, -0.5, 0.5, 1e-5))
