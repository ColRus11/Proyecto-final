from ColRusVisitor import ColRusVisitor
from librerias.excepciones import ReturnValue
from librerias.errores import reportar_error, mostrar_errores
from librerias.funcion import declarar_funcion, llamar_funcion, retornar_valor
from librerias.condicionales import ejecutar_condicional, ejecutar_mientras, ejecutar_para
from librerias.valores import (
    obtener_literal,
    obtener_variable,
    construir_matriz,
    construir_fila,
    construir_lista_valores,
)
from librerias.expresiones import (
    evaluar_asignacion,
    evaluar_igualdad,
    evaluar_relacional,
    evaluar_aditivo,
    evaluar_multiplicativo,
    evaluar_potencia,
    evaluar_unario,
)
from librerias.funciones import evaluar_funcion_matematica
from librerias.archivos import ejecutar_funcion_archivo
from librerias.matrices import transpuesta, inversa, scalar_mul, matrix_add, matrix_mul, matrix_sub
from librerias.graficos import graficar
from librerias.modelos import cargar_modelo, guardar_modelo
from librerias.modelos import predecir




class MiVisitor(ColRusVisitor):
    def __init__(self):
        self.contexto = [{}]
        self.errores = []

    def reportar_error(self, mensaje, ctx=None):
        reportar_error(self, mensaje, ctx)

    def visitPrograma(self, ctx):
        print("Ejecutando programa...")
        for instr in ctx.instruccion():
            self.visit(instr)
        return self

    # Asignaciones
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.contexto[-1][nombre] = valor
        return valor

    # Control de flujo
    def visitCondicional(self, ctx):
        return ejecutar_condicional(ctx, self)

    def visitCicloMientras(self, ctx):
        return ejecutar_mientras(ctx, self)

    def visitCicloPara(self, ctx):
        return ejecutar_para(ctx, self)

    # Funciones definidas por el usuario
    def visitDeclaracionFuncion(self, ctx):
        return declarar_funcion(ctx, self)

    def visitLlamadaFuncion(self, ctx):
        return llamar_funcion(ctx, self)

    def visitRetorno(self, ctx):
        return retornar_valor(ctx, self)

    # Literales y primarios
    def visitLiteral(self, ctx):
        return obtener_literal(ctx)

    def visitPrimary(self, ctx):
        if ctx.ID():
            return obtener_variable(ctx, self)
        return self.visit(ctx.getChild(0))

    def visitMatrizLiteral(self, ctx):
        return construir_matriz(ctx, self)

    def visitFila(self, ctx):
        return construir_fila(ctx, self)

    def visitListaValores(self, ctx):
        return construir_lista_valores(ctx, self)

    # Expresiones con precedencia
    def visitAsignacionExpr(self, ctx):
        return evaluar_asignacion(ctx, self)

    def visitIgualdadExpr(self, ctx):
        return evaluar_igualdad(ctx, self)

    def visitRelacionalExpr(self, ctx):
        return evaluar_relacional(ctx, self)

    def visitAditivoExpr(self, ctx):
        return evaluar_aditivo(ctx, self)

    def visitMultiplicativoExpr(self, ctx):
        return evaluar_multiplicativo(ctx, self)

    def visitPotenciaExpr(self, ctx):
        return evaluar_potencia(ctx, self)

    def visitUnaryExpr(self, ctx):
        return evaluar_unario(ctx, self)

    def visitFuncionArchivo(self, ctx):
        nombre = ctx.getChild(0).getText()

        if nombre == "escribir" or nombre == "leer":
            from librerias.archivos import ejecutar_funcion_archivo
            return ejecutar_funcion_archivo(ctx, self)

        elif nombre == "cargar_modelo":
            return cargar_modelo(ctx, self)

        elif nombre == "guardar_modelo":
            return guardar_modelo(ctx, self)

        elif nombre == "predecir":
            return predecir(ctx, self)

        else:
            self.reportar_error(f"Función '{nombre}' no definida", ctx)
            return None

    def visitFuncionMatriz(self, ctx):
        nombre = ctx.getChild(0).getText()
        identificador = ctx.ID().getText()
        matriz = self.contexto[-1].get(identificador)

        if matriz is None:
            self.reportar_error(f"Matriz '{identificador}' no definida", ctx)
            return None

        try:
            if nombre == 'transpuesta':
                return transpuesta(matriz)
            elif nombre == 'inversa':
                return inversa(matriz)
            else:
                self.reportar_error(f"Función de matriz desconocida: {nombre}", ctx)
        except Exception as e:
            self.reportar_error(f"Error en operación de matriz: {str(e)}", ctx)
            return None

    def visitFuncionGrafica(self, ctx):
        args = ctx.argumentos().expresion() if ctx.argumentos() else []

        if len(args) != 2:
            self.reportar_error("La función 'graficar' requiere dos listas: x, y", ctx)
            return None

        x = self.visit(args[0])
        y = self.visit(args[1])

        # Adaptar si son matrices
        if isinstance(x, list) and isinstance(x[0], list):
            x = x[0]
        if isinstance(y, list) and isinstance(y[0], list):
            y = y[0]

        if not isinstance(x, list) or not isinstance(y, list):
            self.reportar_error("Los argumentos de 'graficar' deben ser listas", ctx)
            return None

        graficar(x, y)
        return None

    def visitUsoModulo(self, ctx):
        nombre = ctx.ID().getText()
        print(f"[Módulo] utilizando: {nombre}")
        return None

    # Errores
    def visitErrorNode(self, node):
        self.reportar_error(f"Error de sintaxis: {node.getText()}")

    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            result = self.visit(node.getChild(i))
        return result

    def visitListaLiteral(self, ctx):
        return self.visit(ctx.listaValores()) if ctx.listaValores() else []

    def visitAccesoIndice(self, ctx):
        nombre = ctx.ID().getText()
        indice = self.visit(ctx.expresion())
        from librerias.valores import acceso_indice
        return acceso_indice(nombre, indice, self)
    
    def visitFuncionIA(self, ctx):
        nombre = ctx.getChild(0).getText()

        if nombre == 'regresion':
            from librerias.regresion import regresion_lineal
            x = self.visit(ctx.expresion(0))
            y = self.visit(ctx.expresion(1))
            return regresion_lineal(x, y)

        elif nombre == 'mlp':
            from librerias.mlp import mlp
            entrada = self.visit(ctx.expresion(0))
            pesos = self.visit(ctx.expresion(1))
            sesgos = self.visit(ctx.expresion(2))
            return mlp(entrada, pesos, sesgos)

        elif nombre == 'red_neuronal':
            from librerias.red_neuronal import red_neuronal
            entrada = self.visit(ctx.expresion(0))
            capas = self.visit(ctx.expresion(1))
            pesos = self.visit(ctx.expresion(2))
            sesgos = self.visit(ctx.expresion(3))
            return red_neuronal(entrada, capas, pesos, sesgos)

        else:
            self.reportar_error(f"Función IA desconocida: {nombre}", ctx)
            return None

    # Finalización
    def ejecutar(self):
        return mostrar_errores(self)
