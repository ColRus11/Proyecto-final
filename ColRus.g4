grammar ColRus;

// ----- Parser rules -----
programa
    : instruccion+ EOF
    ;

instruccion
    : asignacion PUNTOCOMA
    | usoModulo PUNTOCOMA
    | condicional
    | declaracionFuncion
    | llamadaFuncion PUNTOCOMA
    | funcionArchivo PUNTOCOMA
    | funcionGrafica PUNTOCOMA
    | retorno PUNTOCOMA
    | ciclo
    ;

usoModulo
    : UTILICE ID
    ;

asignacion
    : ID IGUAL expresion
    ;

condicional
    : SI PARENIZQ expresion PARENDER bloque (SINO bloque)?
    ;

ciclo
    : cicloMientras
    | cicloPara
    ;

cicloMientras
    : MIENTRAS PARENIZQ expresion PARENDER bloque
    ;

cicloPara
    : PARA ID EN RANGO PARENIZQ expresion COMA expresion PARENDER bloque
    ;

bloque
    : LLAVEIZQ instruccion* LLAVEDER
    ;

declaracionFuncion
    : FUNCION ID PARENIZQ parametros? PARENDER bloque
    ;

parametros
    : ID (COMA ID)*
    ;

llamadaFuncion
    : ID PARENIZQ argumentos? PARENDER
    ;

// Expresiones con precedencia
expresion
    : asignacionExpr
    ;

asignacionExpr
    : igualdadExpr (IGUAL asignacionExpr)?
    ;

igualdadExpr
    : relacionalExpr ((EQ | NE) relacionalExpr)*
    ;

relacionalExpr
    : aditivoExpr ((GT | GE | LT | LE) aditivoExpr)*
    ;

aditivoExpr
    : multiplicativoExpr ((PLUS | MINUS) multiplicativoExpr)*
    ;

multiplicativoExpr
    : potenciaExpr ((MUL | DIV | MOD) potenciaExpr)*
    ;

potenciaExpr
    : unaryExpr (POW unaryExpr)*
    ;

unaryExpr
    : (PLUS | MINUS)? primary
    ;

primary
    : literal
    | ID
    | accesoIndice
    | llamadaFuncion
    | funcionMatematica
    | funcionMatriz
    | funcionArchivo
    | funcionGrafica
    | matrizLiteral
    | listaLiteral
    | funcionIA
    | PARENIZQ expresion PARENDER
    ;

funcionMatematica
    : (RAIZ | SENO | COSENO | TANGENTE) PARENIZQ expresion PARENDER
    ;

funcionMatriz
    : (TRANSPUESTA | INVERSA) PARENIZQ ID PARENDER
    ;

funcionArchivo
    : (LEER | ESCRIBIR | CARGAR_MODELO | GUARDAR_MODELO | PREDECIR) 
      PARENIZQ argumentos? PARENDER
    ;


argumentos
    : expresion (COMA expresion)*
    ;

funcionGrafica
    : GRAFICAR PARENIZQ argumentos? PARENDER
    ;

matrizLiteral
    : MATRIZ PARENIZQ CORCHETEIZQ listaFilas CORCHETEDER PARENDER
    ;

listaFilas
    : fila (COMA fila)*
    ;

fila
    : CORCHETEIZQ listaValores CORCHETEDER
    ;

listaValores
    : expresion (COMA expresion)*
    ;

literal
    : NUMBER
    | STRING
    | BOOLEANO
    ;

// ----- Lexer rules -----
// Palabras clave
SI          : 'si';
SINO        : 'sino';
UTILICE     : 'utilice';
FUNCION     : 'funcion';
MIENTRAS    : 'mientras';
PARA        : 'para';
EN          : 'en';
RANGO       : 'rango';
LEER        : 'leer';
ESCRIBIR    : 'escribir';
GRAFICAR    : 'graficar';
RAIZ        : 'raiz';
SENO        : 'seno';
COSENO      : 'coseno';
TANGENTE    : 'tangente';
TRANSPUESTA : 'transpuesta';
INVERSA     : 'inversa';
MATRIZ      : 'matriz';
RETORNAR    : 'retornar';
REGRESION   : 'regresion';
MLP           : 'mlp';
RED           : 'red_neuronal';
CARGAR_MODELO : 'cargar_modelo';
GUARDAR_MODELO : 'guardar_modelo';
PREDECIR       : 'predecir';


// Operadores y símbolos
IGUAL       : '=';
EQ          : '==';
NE          : '!=';
GE          : '>=';
LE          : '<=';
GT          : '>';
LT          : '<';
PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
POW         : '^';
PARENIZQ    : '(';
PARENDER    : ')';
CORCHETEIZQ : '[';
CORCHETEDER : ']';
LLAVEIZQ    : '{';
LLAVEDER    : '}';
COMA        : ',';
PUNTOCOMA   : ';';



// Literales
NUMBER      : [0-9]+ ('.' [0-9]+)?;
STRING      : '"' ( ~["\\\r\n] | '\\' . )* '"';
BOOLEANO    : 'verdadero' | 'falso';

// Identificadores
ID          : [a-zA-Z_\p{L}][a-zA-Z_0-9\p{L}]*;

// Espacios y comentarios
WS          : [ \t\n\r]+ -> skip;
COMENTARIO  : ('//' ~[\n\r]* | '#' ~[\n\r]*) -> skip;

// Retornar
retorno
    : RETORNAR expresion
    ;

listaLiteral
    : CORCHETEIZQ listaValores? CORCHETEDER
    ;

accesoIndice
    : ID CORCHETEIZQ expresion CORCHETEDER
    ;

funcionIA
    : REGRESION PARENIZQ expresion COMA expresion PARENDER
    | MLP PARENIZQ expresion COMA expresion COMA expresion PARENDER
    | RED PARENIZQ expresion COMA expresion COMA expresion COMA expresion PARENDER
    ;


