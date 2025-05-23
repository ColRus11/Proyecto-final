def regresion_lineal(x, y):
    """
    Calcula la regresión lineal y = m*x + b
    Devuelve (pendiente, intercepto)
    """
    if len(x) != len(y):
        raise ValueError("Las listas x e y deben tener la misma longitud")

    n = len(x)
    suma_x = sum(x)
    suma_y = sum(y)
    suma_x2 = sum([xi * xi for xi in x])
    suma_xy = sum([x[i] * y[i] for i in range(n)])

    divisor = n * suma_x2 - suma_x ** 2
    if divisor == 0:
        raise ValueError("No se puede calcular la regresión: división por cero")

    m = (n * suma_xy - suma_x * suma_y) / divisor
    b = (suma_y - m * suma_x) / n

    return [m, b]
