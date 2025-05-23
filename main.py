from antlr4 import FileStream, CommonTokenStream
from ColRusLexer import ColRusLexer
from ColRusParser import ColRusParser
from  visitor import MiVisitor


def ejecutar_archivo(nombre_archivo):
    try:
        input_stream = FileStream(nombre_archivo, encoding='utf-8')
        lexer = ColRusLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = ColRusParser(tokens)

        # Crea el árbol de análisis (AST)
        tree = parser.programa()

        # Aplica el visitor
        visitor = MiVisitor()
        visitor.visit(tree)

        # Mostrar errores si existen
        visitor.ejecutar()

    except Exception as e:
        print(f"Error durante la ejecución: {e}")


if __name__ == "__main__":
    # Cambia aquí si tu archivo tiene otro nombre
    ejecutar_archivo("prueba.coru")
