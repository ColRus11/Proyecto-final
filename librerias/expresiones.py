from librerias.matrices import matrix_add, matrix_sub, matrix_mul, scalar_mul

def evaluar_asignacion(ctx, visitor):
    if ctx.getChildCount() == 3:
        nombre = ctx.getChild(0).getText()
        valor = visitor.visit(ctx.getChild(2))
        visitor.contexto[-1][nombre] = valor
        return valor
    return visitor.visit(ctx.getChild(0))


def evaluar_igualdad(ctx, visitor):
    if len(ctx.relacionalExpr()) == 2:
        izq = visitor.visit(ctx.relacionalExpr(0))
        der = visitor.visit(ctx.relacionalExpr(1))
        op = ctx.getChild(1).getText()
        return izq == der if op == '==' else izq != der
    return visitor.visit(ctx.relacionalExpr(0))


def evaluar_relacional(ctx, visitor):
    if len(ctx.aditivoExpr()) == 2:
        izq = visitor.visit(ctx.aditivoExpr(0))
        der = visitor.visit(ctx.aditivoExpr(1))
        if izq is None or der is None:
            visitor.reportar_error("Comparación con variable indefinida", ctx)
            return False
        op = ctx.getChild(1).getText()
        return {
            '>':  izq > der,
            '<':  izq < der,
            '>=': izq >= der,
            '<=': izq <= der
        }.get(op, False)
    return visitor.visit(ctx.aditivoExpr(0))


def evaluar_aditivo(ctx, visitor):
    if len(ctx.multiplicativoExpr()) == 2:
        izq = visitor.visit(ctx.multiplicativoExpr(0))
        der = visitor.visit(ctx.multiplicativoExpr(1))
        op = ctx.getChild(1).getText()

        # Matrices (listas de listas)
        if isinstance(izq, list) and isinstance(der, list):
            if all(isinstance(f, list) for f in izq) and all(isinstance(f, list) for f in der):
                return matrix_add(izq, der) if op == '+' else matrix_sub(izq, der)

            # Listas 1D
            elif all(not isinstance(f, list) for f in izq) and all(not isinstance(f, list) for f in der):
                if op == '+':
                    return izq + der
                elif op == '-':
                    visitor.reportar_error("No se permite la resta de listas 1D", ctx)
                    return None

        # Escalares (int o float)
        if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
            return izq + der if op == '+' else izq - der

        # Combinación no válida
        visitor.reportar_error("Operación aditiva no válida entre tipos incompatibles", ctx)
        return None

    return visitor.visit(ctx.multiplicativoExpr(0))




def evaluar_multiplicativo(ctx, visitor):
    if len(ctx.potenciaExpr()) == 2:
        a = visitor.visit(ctx.potenciaExpr(0))
        b = visitor.visit(ctx.potenciaExpr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            if isinstance(a, list) and isinstance(b, list):
                return matrix_mul(a, b)
            if isinstance(a, (int, float)) and isinstance(b, list):
                return scalar_mul(a, b)
            if isinstance(a, list) and isinstance(b, (int, float)):
                return scalar_mul(b, a)
            return a * b
        if op == '/':
            return a / b
        if op == '%':
            return a % b
    return visitor.visit(ctx.potenciaExpr(0))


def evaluar_potencia(ctx, visitor):
    if len(ctx.unaryExpr()) == 2:
        base = visitor.visit(ctx.unaryExpr(0))
        exp = visitor.visit(ctx.unaryExpr(1))
        return base ** exp
    return visitor.visit(ctx.unaryExpr(0))


def evaluar_unario(ctx, visitor):
    if ctx.PLUS():
        return +visitor.visit(ctx.primary())
    if ctx.MINUS():
        return -visitor.visit(ctx.primary())
    return visitor.visit(ctx.primary())
