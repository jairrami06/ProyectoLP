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
    "Function": "FUNCTION",
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
    "main": "MAIN",
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
    "RBRACKET",
    "MODULE",
    "VARIABLE",
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

# A regular expression rule with some action code - Victor Valverde


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


def t_VARIABLE(t):
    r"[a-zA-Z_]\w*"
    t.type = reserved.get(t.value, "VARIABLE")
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
int factorial(int n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

void main() {
  int number = 5;
  print("El factorial de $number es: ${factorial(number)}");
}
"""

resultado = analizar_tokens(algoritmoJair)


# Fin aporte de Jair Ramírez

algoritmotbolanos="""
int fibonacci(int n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

void main() {
  print(fibonacci(8)); // 21
}


"""

resultado = analizar_tokens(algoritmotbolanos)
