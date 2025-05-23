def pi():
    return 3.14159265358979

def abs(x):
    return x if x >= 0 else -x

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def exp(x, n=20):
    resultado = 1
    termino = 1
    for i in range(1, n + 1):
        termino *= x / i
        resultado += termino
    return resultado

def sqrt(x, tol=1e-10):
    r = x
    while abs(r * r - x) > tol:
        r = (r + x / r) / 2
    return r

def seno(x, n=10):
    res = 0
    for i in range(n):
        num = (-1) ** i * x ** (2 * i + 1)
        den = factorial(2 * i + 1)
        res += num / den
    return res

def coseno(x, n=10):
    res = 0
    for i in range(n):
        num = (-1) ** i * x ** (2 * i)
        den = factorial(2 * i)
        res += num / den
    return res

def tangente(x):
    c = coseno(x)
    if abs(c) < 1e-10:
        return float('inf')
    return seno(x) / c

def sigmoid(x):
    return 1 / (1 + exp(-x))

