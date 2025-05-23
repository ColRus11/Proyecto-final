from librerias.core import obtener_variable as obtener_valor_variable

def obtener_literal(ctx):
    """
    Convierte un literal (number, string, booleano) en su valor correspondiente.
    """
    if ctx.NUMBER():
        return float(ctx.NUMBER().getText())
    if ctx.STRING():
        texto = ctx.STRING().getText()
        return texto[1:-1]  # Remueve comillas
    if ctx.BOOLEANO():
        return ctx.BOOLEANO().getText() == 'verdadero'
    return None


def obtener_variable(ctx, visitor):
    """
    Devuelve el valor de una variable a partir del nombre.
    """
    if hasattr(ctx, 'getText'):
        nombre = ctx.getText()
    else:
        nombre = str(ctx)
    return obtener_valor_variable(nombre, visitor)


def construir_matriz(ctx, visitor):
    """
    Construye una matriz literal como lista de listas.
    """
    return [visitor.visit(fila) for fila in ctx.listaFilas().fila()]


def construir_fila(ctx, visitor):
    """
    Construye una fila como lista de valores.
    """
    return visitor.visit(ctx.listaValores())


def construir_lista_valores(ctx, visitor):
    """
    Devuelve la lista de expresiones evaluadas (una fila).
    """
    return [visitor.visit(exp) for exp in ctx.expresion()]

def acceso_indice(nombre, indice, visitor):
    valor = obtener_variable(nombre, visitor)

    if not isinstance(valor, list):
        visitor.reportar_error(f"'{nombre}' no es indexable", None)
        return None

    try:
        return valor[int(indice)]
    except IndexError:
        visitor.reportar_error(f"Índice fuera de rango en '{nombre}[{indice}]'", None)
    except Exception as e:
        visitor.reportar_error(f"Error al acceder a '{nombre}[{indice}]': {e}", None)
    return None

