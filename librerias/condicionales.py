def ejecutar_condicional(ctx, visitor):
    """
    Ejecuta una estructura condicional `si (...) { ... } sino { ... }`.
    """
    condicion = visitor.visit(ctx.expresion())
    if condicion:
        return visitor.visit(ctx.bloque(0))
    elif ctx.SINO():
        return visitor.visit(ctx.bloque(1))
    return None


def ejecutar_mientras(ctx, visitor):
    """
    Ejecuta un ciclo `mientras (...) { ... }`.
    """
    resultados = []
    while visitor.visit(ctx.expresion()):
        resultados.append(visitor.visit(ctx.bloque()))
    return resultados


def ejecutar_para(ctx, visitor):
    """
    Ejecuta un ciclo `para i en rango (inicio, fin) { ... }`.
    """
    var_name = ctx.ID().getText()
    inicio = visitor.visit(ctx.expresion(0))
    fin    = visitor.visit(ctx.expresion(1))
    resultados = []

    visitor.contexto.append({})
    for i in range(int(inicio), int(fin) + 1):
        visitor.contexto[-1][var_name] = i
        resultados.append(visitor.visit(ctx.bloque()))
    visitor.contexto.pop()

    return resultados
