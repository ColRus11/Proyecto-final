def sqrt(x, tol=1e-10):
    """
    Calcula la raíz cuadrada de un número usando el método de Newton-Raphson.
    """
    if x < 0:
        return float('nan')
    r = x
    while abs(r * r - x) > tol:
        r = (r + x / r) / 2
    return r


def factorial(n):
    """
    Calcula el factorial de un número entero.
    """
    res = 1
    for i in range(2, int(n) + 1):
        res *= i
    return res


def seno(x, n=10):
    """
    Aproxima el seno usando la serie de Taylor.
    """
    res = 0
    for i in range(n):
        res += ((-1) ** i * x ** (2 * i + 1)) / factorial(2 * i + 1)
    return res


def coseno(x, n=10):
    """
    Aproxima el coseno usando la serie de Taylor.
    """
    res = 0
    for i in range(n):
        res += ((-1) ** i * x ** (2 * i)) / factorial(2 * i)
    return res


def tangente(x):
    """
    Calcula la tangente como seno / coseno.
    """
    c = coseno(x)
    if abs(c) < 1e-10:
        return float('inf')  # Evitar división por cero
    return seno(x) / c


def evaluar_funcion_matematica(ctx, visitor):
    """
    Llama a la función matemática correspondiente según el identificador.
    """
    nombre = ctx.getChild(0).getText()
    valor = visitor.visit(ctx.expresion())

    if nombre == 'raiz':
        return sqrt(valor)
    elif nombre == 'seno':
        return seno(valor)
    elif nombre == 'coseno':
        return coseno(valor)
    elif nombre == 'tangente':
        return tangente(valor)

    visitor.reportar_error(f"Función matemática desconocida: {nombre}", ctx)
    return 0
