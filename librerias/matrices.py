def matrix_add(A, B):
    """
    Suma de dos matrices A + B
    """
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Dimensiones incompatibles para suma de matrices")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_sub(A, B):
    """
    Resta de dos matrices A - B
    """
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Dimensiones incompatibles para resta de matrices")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_mul(A, B):
    """
    Multiplicación de matrices A * B
    """
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    if n != n2:
        raise ValueError("Dimensiones incompatibles para multiplicación de matrices")
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def scalar_mul(esc, M):
    """
    Multiplicación escalar: esc * M
    """
    return [[esc * M[i][j] for j in range(len(M[0]))] for i in range(len(M))]

def transpuesta(matriz):
    """
    Devuelve la transpuesta de una matriz (intercambia filas por columnas).
    """
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


def inversa(matriz):
    """
    Calcula la inversa de una matriz 2x2. Solo implementado para matrices 2x2 por simplicidad.
    """
    if len(matriz) != 2 or len(matriz[0]) != 2:
        raise ValueError("La inversa solo está implementada para matrices 2x2")

    a, b = matriz[0]
    c, d = matriz[1]
    det = a * d - b * c

    if det == 0:
        raise ValueError("La matriz no tiene inversa (determinante cero)")

    factor = 1 / det
    return [[d * factor, -b * factor], [-c * factor, a * factor]]
