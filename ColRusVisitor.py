# Generated from ColRus.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ColRusParser import ColRusParser
else:
    from ColRusParser import ColRusParser

# This class defines a complete generic visitor for a parse tree produced by ColRusParser.

class ColRusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ColRusParser#programa.
    def visitPrograma(self, ctx:ColRusParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#instruccion.
    def visitInstruccion(self, ctx:ColRusParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#usoModulo.
    def visitUsoModulo(self, ctx:ColRusParser.UsoModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#asignacion.
    def visitAsignacion(self, ctx:ColRusParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#condicional.
    def visitCondicional(self, ctx:ColRusParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#ciclo.
    def visitCiclo(self, ctx:ColRusParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#cicloMientras.
    def visitCicloMientras(self, ctx:ColRusParser.CicloMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#cicloPara.
    def visitCicloPara(self, ctx:ColRusParser.CicloParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#bloque.
    def visitBloque(self, ctx:ColRusParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#declaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:ColRusParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#parametros.
    def visitParametros(self, ctx:ColRusParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:ColRusParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#expresion.
    def visitExpresion(self, ctx:ColRusParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#asignacionExpr.
    def visitAsignacionExpr(self, ctx:ColRusParser.AsignacionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#igualdadExpr.
    def visitIgualdadExpr(self, ctx:ColRusParser.IgualdadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#relacionalExpr.
    def visitRelacionalExpr(self, ctx:ColRusParser.RelacionalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#aditivoExpr.
    def visitAditivoExpr(self, ctx:ColRusParser.AditivoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#multiplicativoExpr.
    def visitMultiplicativoExpr(self, ctx:ColRusParser.MultiplicativoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#potenciaExpr.
    def visitPotenciaExpr(self, ctx:ColRusParser.PotenciaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#unaryExpr.
    def visitUnaryExpr(self, ctx:ColRusParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#primary.
    def visitPrimary(self, ctx:ColRusParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#funcionMatematica.
    def visitFuncionMatematica(self, ctx:ColRusParser.FuncionMatematicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#funcionMatriz.
    def visitFuncionMatriz(self, ctx:ColRusParser.FuncionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#funcionArchivo.
    def visitFuncionArchivo(self, ctx:ColRusParser.FuncionArchivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#argumentos.
    def visitArgumentos(self, ctx:ColRusParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#funcionGrafica.
    def visitFuncionGrafica(self, ctx:ColRusParser.FuncionGraficaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#matrizLiteral.
    def visitMatrizLiteral(self, ctx:ColRusParser.MatrizLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#listaFilas.
    def visitListaFilas(self, ctx:ColRusParser.ListaFilasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#fila.
    def visitFila(self, ctx:ColRusParser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#listaValores.
    def visitListaValores(self, ctx:ColRusParser.ListaValoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#literal.
    def visitLiteral(self, ctx:ColRusParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#retorno.
    def visitRetorno(self, ctx:ColRusParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#listaLiteral.
    def visitListaLiteral(self, ctx:ColRusParser.ListaLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#accesoIndice.
    def visitAccesoIndice(self, ctx:ColRusParser.AccesoIndiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#funcionIA.
    def visitFuncionIA(self, ctx:ColRusParser.FuncionIAContext):
        return self.visitChildren(ctx)



del ColRusParser