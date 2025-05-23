from librerias.matematica import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def red_neuronal(entrada, capas, pesos, sesgos):
    """
    Ejecuta una red neuronal multicapa (solo forward).
    - entrada: lista de entrada
    - capas: lista con número de neuronas por capa
    - pesos: lista de matrices (pesos[capa][neurona][entrada])
    - sesgos: lista de listas (sesgos[capa][neurona])
    """
    if len(capas) != len(pesos) or len(capas) != len(sesgos):
        raise ValueError("Dimensión de capas, pesos o sesgos incorrecta")

    activacion = entrada
    for capa in range(len(capas)):
        activacion_nueva = []
        for i in range(int(capas[capa])):
            suma = 0
            for j in range(len(activacion)):
                suma += activacion[j] * pesos[capa][i][j]
            suma += sesgos[capa][i]
            activacion_nueva.append(sigmoid(suma))
        activacion = activacion_nueva

    return activacion
