from librerias.excepciones import ReturnValue
from librerias.core import crear_nuevo_contexto, obtener_funcion
from librerias.errores import reportar_error

def declarar_funcion(ctx, visitor):
    nombre = ctx.ID().getText()

    if ctx.parametros():
        ids = ctx.parametros().ID()
        parametros = [p.getText() for p in ids if hasattr(p, 'getText')]
    else:
        parametros = []

    bloque = ctx.bloque()
    visitor.contexto[0][nombre] = {
        'params': parametros,
        'bloque': bloque
    }
    return None



def llamar_funcion(ctx, visitor):
    """
    Llama a una función definida por el usuario.
    """
    nombre = ctx.ID().getText()
    argumentos = [visitor.visit(arg) for arg in ctx.argumentos().expresion()] if ctx.argumentos() else []

    funcion = obtener_funcion(nombre, visitor)
    if not funcion:
        return None

    parametros = funcion['params']
    if len(argumentos) != len(parametros):
        reportar_error(visitor,
            f"La función '{nombre}' esperaba {len(parametros)} argumentos, pero recibió {len(argumentos)}.",
            ctx
        )
        return None

    nuevo_ambito = crear_nuevo_contexto(parametros, argumentos)
    visitor.contexto.append(nuevo_ambito)
    try:
        visitor.visit(funcion['bloque'])
    except ReturnValue as retorno:
        visitor.contexto.pop()
        return retorno.valor
    visitor.contexto.pop()
    return None


def retornar_valor(ctx, visitor):
    """
    Evalúa la expresión de retorno y lanza ReturnValue para salir de la función.
    """
    valor = visitor.visit(ctx.expresion())
    raise ReturnValue(valor)
