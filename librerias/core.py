def obtener_variable(nombre, visitor):
    """
    Busca una variable en el stack de contexto del visitor.
    Si no existe, reporta un error.
    """
    for scope in reversed(visitor.contexto):
        if nombre in scope:
            return scope[nombre]
    visitor.reportar_error(f"Variable '{nombre}' no definida")
    return None


def asignar_variable(nombre, valor, visitor):
    """
    Asigna un valor a una variable en el contexto actual.
    """
    visitor.contexto[-1][nombre] = valor
    return valor


def actualizar_variable_existente(nombre, valor, visitor):
    """
    Busca en el stack de contextos y actualiza la variable si existe.
    Si no existe, se asigna en el contexto actual.
    """
    for scope in reversed(visitor.contexto):
        if nombre in scope:
            scope[nombre] = valor
            return valor
    # Si no se encontró, asignar en el contexto actual
    visitor.contexto[-1][nombre] = valor
    return valor


def obtener_funcion(nombre, visitor):
    """
    Busca una función declarada por el usuario en el contexto global.
    """
    for scope in reversed(visitor.contexto):
        if nombre in scope and isinstance(scope[nombre], dict):
            return scope[nombre]
    visitor.reportar_error(f"Función '{nombre}' no definida")
    return None


def crear_nuevo_contexto(parametros, argumentos):
    """
    Crea un nuevo diccionario de contexto a partir de una lista de parámetros y argumentos.
    """
    return dict(zip(parametros, argumentos))
