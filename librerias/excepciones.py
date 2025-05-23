class ReturnValue(Exception):
    """
    Excepción para manejar 'retornar' en funciones del lenguaje.
    Al lanzar esta excepción, se detiene la ejecución del bloque de la función.
    """
    def __init__(self, valor):
        self.valor = valor
