from librerias.matematica import sigmoid

def predecir(ctx, visitor):
    """
    Ejecuta forward pass de una red neuronal multicapa:
    - entrada: lista
    - pesos: lista de capas (listas de listas)
    - sesgos: lista de capas (listas)
    Retorna la salida final (lista).
    """
    try:
        # Obtener los 3 argumentos
        if not ctx.argumentos() or len(ctx.argumentos().expresion()) != 3:
            visitor.reportar_error("predecir requiere 3 argumentos: entrada, pesos, sesgos", ctx)
            return None

        entrada = visitor.visit(ctx.argumentos().expresion(0))
        pesos   = visitor.visit(ctx.argumentos().expresion(1))
        sesgos  = visitor.visit(ctx.argumentos().expresion(2))

        # Validación
        if not isinstance(entrada, list) or not isinstance(pesos, list) or not isinstance(sesgos, list):
            visitor.reportar_error("Los argumentos de predecir deben ser listas", ctx)
            return None

        # Forward pass
        activacion = entrada
        for capa_idx in range(len(pesos)):
            capa_pesos = pesos[capa_idx]
            capa_sesgos = sesgos[capa_idx]
            nuev_act = []
            # cada neurona
            for n_idx in range(len(capa_pesos)):
                w = capa_pesos[n_idx]
                b = capa_sesgos[n_idx]
                # suma ponderada
                suma = 0
                for j in range(len(activacion)):
                    suma += activacion[j] * w[j]
                suma += b
                # activación sigmoide
                nuev_act.append(sigmoid(suma))
            activacion = nuev_act

        return activacion

    except Exception as e:
        visitor.reportar_error(f"Error en predecir: {e}", ctx)
        return None


def guardar_modelo(ctx, visitor):
    try:
        if not ctx.argumentos() or len(ctx.argumentos().expresion()) != 3:
            visitor.reportar_error("guardar_modelo requiere 3 argumentos: nombre, pesos, sesgos", ctx)
            return None

        args = [visitor.visit(expr) for expr in ctx.argumentos().expresion()]
        nombre, pesos, sesgos = args

        with open(nombre, 'w') as archivo:
            archivo.write("pesos:\n")
            for capa in pesos:
                for neurona in capa:
                    linea = ",".join(str(w) for w in neurona)
                    archivo.write(linea + "\n")
                archivo.write("\n")

            archivo.write("sesgos:\n")
            for capa in sesgos:
                linea = ",".join(str(b) for b in capa)
                archivo.write(linea + "\n")

        print(f"[Modelo] guardado en '{nombre}'")

    except Exception as e:
        visitor.reportar_error(f"Error al guardar modelo: {e}", ctx)
        return None


def cargar_modelo(ctx, visitor):
    try:
        if not ctx.argumentos() or len(ctx.argumentos().expresion()) != 1:
            visitor.reportar_error("cargar_modelo requiere 1 argumento: nombre del archivo", ctx)
            return None

        nombre = visitor.visit(ctx.argumentos().expresion(0))
        with open(nombre, 'r') as archivo:
            lineas = [line.strip() for line in archivo.readlines()]

        pesos = []
        sesgos = []
        leyendo_pesos = False
        leyendo_sesgos = False
        capa_actual = []

        for linea in lineas:
            if not linea:
                if leyendo_pesos and capa_actual:
                    pesos.append(capa_actual)
                    capa_actual = []
                continue

            if linea.startswith("pesos:"):
                leyendo_pesos = True
                leyendo_sesgos = False
                continue
            elif linea.startswith("sesgos:"):
                leyendo_sesgos = True
                leyendo_pesos = False
                if capa_actual:
                    pesos.append(capa_actual)
                    capa_actual = []
                continue

            if leyendo_pesos:
                capa_actual.append([float(w) for w in linea.split(",")])
            elif leyendo_sesgos:
                sesgos.append([float(b) for b in linea.split(",")])

        if capa_actual and leyendo_pesos:
            pesos.append(capa_actual)

        return [pesos, sesgos]

    except Exception as e:
        visitor.reportar_error(f"Error al cargar modelo: {e}", ctx)
        return None
