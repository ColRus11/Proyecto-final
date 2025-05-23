def graficar(valores_x, valores_y, ancho=40, alto=10):
    """
    Imprime un gráfico simple en consola a partir de listas x, y.
    - ancho: número de caracteres horizontales (resolución X)
    - alto: número de líneas verticales (resolución Y)
    """
    if not valores_x or not valores_y or len(valores_x) != len(valores_y):
        print("[Error] Listas vacías o de diferente longitud.")
        return

    min_y, max_y = min(valores_y), max(valores_y)
    rango_y = max_y - min_y if max_y != min_y else 1

    # Normalizar y escalar
    puntos = []
    for x, y in zip(valores_x, valores_y):
        y_norm = int((y - min_y) / rango_y * (alto - 1))
        puntos.append((x, y_norm))

    # Generar la grilla
    canvas = [[' ' for _ in range(len(valores_x))] for _ in range(alto)]

    for i, (_, y) in enumerate(puntos):
        fila = alto - 1 - y
        if 0 <= fila < alto and 0 <= i < len(valores_x):
            canvas[fila][i] = '*'

    # Imprimir de arriba hacia abajo
    for fila in canvas:
        print(''.join(fila))
    print("─" * len(valores_x))
    print(" ".join(map(str, valores_x)))
