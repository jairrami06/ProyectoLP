import ply.lex as lex

# Aporte de Jair Ramírez

reserved = {
    "abstract": "ABSTRACT",
    "as": "AS",
    "assert": "ASSERT",
    "async": "ASYNC",
    "await": "AWAIT",
    "break": "BREAK",
    "case": "CASE",
    "catch": "CATCH",
    "class": "CLASS",
    "const": "CONST",
    "continue": "CONTINUE",
    "covariant": "COVARIANT",
    "default": "DEFAULT",
    "deferred": "DEFERRED",
    "do": "DO",
    "dynamic": "DYNAMIC",
    "else": "ELSE",
    "enum": "ENUM",
    "export": "EXPORT",
    "extends": "EXTENDS",
    "extension": "EXTENSION",
    "external": "EXTERNAL",
    "factory": "FACTORY",
    "false": "FALSE",
    "final": "FINAL",
    "finally": "FINALLY",
    "for": "FOR",
    "function": "FUNCTION",
    "get": "GET",
    "hide": "HIDE",
    "if": "IF",
    "implements": "IMPLEMENTS",
    "import": "IMPORT",
    "in": "IN",
    "interface": "INTERFACE",
    "is": "IS",
    "late": "LATE",
    "library": "LIBRARY",
    "mixin": "MIXIN",
    "new": "NEW",
    "null": "NULL",
    "on": "ON",
    "operator": "OPERATOR",
    "part": "PART",
    "required": "REQUIRED",
    "rethrow": "RETHROW",
    "return": "RETURN",
    "set": "SET",
    "show": "SHOW",
    "static": "STATIC",
    "super": "SUPER",
    "switch": "SWITCH",
    "sync": "SYNC",
    "this": "THIS",
    "throw": "THROW",
    "true": "TRUE",
    "try": "TRY",
    "typedef": "TYPEDEF",
    "var": "VAR",
    "void": "VOID",
    "while": "WHILE",
    "with": "WITH",
    "yield": "YIELD",
    "int": "INT",
    "double": "DOUBLE",
    "bool": "BOOL",
    "String": "STRING",
    "List": "LIST",
    "Map": "MAP",
    "Object": "OBJECT",
    "num": "NUM",
    "print": "PRINT",
}

tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "LSBRACKET",
    "RSBRACKET",
    "RBRACKET",
    "MODULE",
    "ID",
    "NUMERAL",
    "NDOUBLE",
    "TEXT",
    "EQUALS",
    "NOT_EQUALS",
    "GREATER",
    "LESS",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    "AND",
    "OR",
    "NOT",
    "ASSIGN",
    "INCREMENT",
    "DECREMENT",
    "DOT",
    "COMMA",
    "COLON",
    "DOLLARSIGN",
    "SEMICOLON",
    "QUESTION",
    "DOUBLE_COLON",
) + tuple(reserved.values())

# Fin aporte de Jair Ramírez

# Aporte de Tomás Steven Bolaños Fajardo
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"{"
t_LSBRACKET = r"\["
t_RSBRACKET = r"\]"
t_DOLLARSIGN = r"\$"
t_RBRACKET = r"}"
t_MODULE = r"%"
t_EQUALS = r"=="
t_NOT_EQUALS = r"!="
t_GREATER = r">"
t_LESS = r"<"
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_AND = r"&&"
t_OR = r"\|\|"
t_NOT = r"!"
t_ASSIGN = r"="
t_INCREMENT = r"\+\+"
t_DECREMENT = r"--"
t_DOT = r"\."
t_COMMA = r","
t_COLON = r":"
t_SEMICOLON = r";"
t_QUESTION = r"\?"
t_DOUBLE_COLON = r"::"
# Fin Aporte Tomas Steven Bolaños Fajardo


# Aporte por Victor Valverde
def t_COMMENT_SINGLE(t):
    r"//.*"
    pass  # Ignorar comentarios de una sola línea


def t_COMMENT_MULTI(t):
    r"/\*([^*]|\*+[^*/])*\*+/"
    pass  # Ignorar comentarios de varias líneas


def t_TEXT(t):
    # r'(["\'])(?:(?=(\\?))\2.)*?\1' Strings más complejos (anidados y saltos de linea con \n)
    r'"[^"\n]*"|\'[^\n]*\' '
    return t


def t_NDOUBLE(t):
    # r"[1-9]*[0-9]+\.[0-9]+" Double genérico
    # r"(?<!\d)(?:(?:0?\.\d+)|(?:[1-9]\d*\.\d+))(?!\d)"  # Incluye .3
    r"(?<!\d)(?:0?\.\d+|[1-9]\d*\.\d+)(?:[eE][+-]?\d+)?(?!\d)"  # Incluye notación científica y .3
    return t


def t_NUMBER(t):
    r"\d+"
    return t


def t_ID(t):
    r"[a-zA-Z_]\w*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_NUMERAL(t):
    r"\#"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Fin aporte por Víctor Valverde

lexer = lex.lex()

# Aporte de Jair Ramírez


def analizar_tokens(data):
    lexer.input(data)
    tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
        print(tok)

    return tokens


algoritmoJair = """
import 'dart:io';

void main() {
  print('¡Bienvenido al Buscador de Números Primos!');
  print('Ingrese el rango donde buscar primos.');

  // Leer rango del usuario
  stdout.write('Inicio del rango: ');
  int? rangoInicio = int.tryParse(stdin.readLineSync() ?? '');
  stdout.write('Fin del rango: ');
  int? rangoFin = int.tryParse(stdin.readLineSync() ?? '');

  // Validar entrada
  if (rangoInicio == null || rangoFin == null || rangoInicio > rangoFin || rangoInicio < 2) {
    print('Por favor, ingrese un rango válido (mayor o igual a 2).');
    return;
  }

  // Encontrar números primos
  List<int> primos = encontrarPrimos(rangoInicio, rangoFin);

  if (primos.isEmpty) {
    print('No se encontraron números primos en el rango proporcionado.');
    return;
  }

  // Mostrar los resultados
  print('Números primos encontrados: $primos');
  mostrarEstadisticas(primos);

  // Guardar resultados en un archivo
  guardarEnArchivo(primos, 'primos.txt');
  print('Los resultados se han guardado en el archivo "primos.txt".');
}

List<int> encontrarPrimos(int inicio, int fin) {
  List<bool> esPrimo = List.filled(fin + 1, true);
  esPrimo[0] = esPrimo[1] = false;

  for (int i = 2; i * i <= fin; i++) {
    if (esPrimo[i]) {
      for (int j = i * i; j <= fin; j += i) {
        esPrimo[j] = false;
      }
    }
  }

  List<int> primos = [];
  for (int k = inicio; k <= fin; k++) {
    if (esPrimo[k]) {
      primos.add(k);
    }
  }
  return primos;
}

void mostrarEstadisticas(List<int> primos) {
  int suma = primos.reduce((a, b) => a + b);
  double promedio = suma / primos.length;
  int maximo = primos.last;
  int minimo = primos.first;

  print('Estadísticas de los números primos encontrados:');
  print('Cantidad de números primos: ${primos.length}');
  print('Suma de los números primos: $suma');
  print('Promedio de los números primos: ${promedio.toStringAsFixed(2)}');
  print('Primo más pequeño: $minimo');
  print('Primo más grande: $maximo');
}

void guardarEnArchivo(List<int> primos, String nombreArchivo) {
  File archivo = File(nombreArchivo);
  archivo.writeAsStringSync('Números primos: ${primos.join(', ')}', mode: FileMode.write);
}

"""

resultado = analizar_tokens(algoritmoJair)


# Fin aporte de Jair Ramírez
