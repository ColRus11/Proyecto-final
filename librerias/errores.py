def reportar_error(visitor, mensaje, ctx=None):
    """
    Registra un mensaje de error en el visitor con información opcional de línea y columna.
    """
    if ctx and hasattr(ctx, 'start'):
        linea = ctx.start.line
        columna = ctx.start.column
        visitor.errores.append(f"Línea {linea}:{columna} - {mensaje}")
    else:
        visitor.errores.append(mensaje)


def mostrar_errores(visitor):
    """
    Imprime todos los errores almacenados y retorna False si hay errores.
    """
    if visitor.errores:
        print("\nErrores encontrados:")
        for e in visitor.errores:
            print("•", e)
        return False
    return True
