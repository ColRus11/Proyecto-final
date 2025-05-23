def escribir(*args):
    """
    Imprime cualquier cantidad de argumentos, incluyendo listas (matrices).
    """
    salida = []
    for arg in args:
        if isinstance(arg, list):
            # Se asume lista de listas (matriz)
            if all(isinstance(fila, list) for fila in arg):
                for fila in arg:
                    salida.append("[" + " ".join(map(str, fila)) + "]")
            else:
                salida.append("[" + " ".join(map(str, arg)) + "]")
        else:
            salida.append(str(arg))
    print(" ".join(salida))


def leer(ruta):
    """
    Intenta leer el contenido de un archivo de texto. Devuelve el contenido como string.
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta}' no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
    return None


def ejecutar_funcion_archivo(ctx, visitor):
    """
    Llama a las funciones nativas de archivos: leer(), escribir().
    """
    funcion = ctx.getChild(0).getText()
    args = [visitor.visit(exp) for exp in ctx.expresion()]

    if funcion == 'escribir':
        escribir(*args)
    elif funcion == 'leer':
        if args:
            return leer(args[0])
    else:
        visitor.reportar_error(f"Función de archivo desconocida: {funcion}", ctx)
    return None
