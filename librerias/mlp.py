from librerias.matematica import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def mlp(entrada, pesos, sesgos):
    """
    Red neuronal feedforward de una capa (sin entrenamiento).
    - entrada: lista de valores
    - pesos: lista de listas (una por neurona)
    - sesgos: lista de valores
    """
    if len(pesos) != len(sesgos):
        raise ValueError("El número de neuronas no coincide entre pesos y sesgos")

    salida = []
    for i in range(len(pesos)):
        if len(pesos[i]) != len(entrada):
            raise ValueError(f"Dimensión de pesos[{i}] no coincide con la entrada")

        z = 0
        for j in range(len(entrada)):
            z += entrada[j] * pesos[i][j]
        z += sesgos[i]

        salida.append(sigmoid(z))

    return salida
