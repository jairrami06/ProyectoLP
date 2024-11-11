import ply.lex as lex

# reserved words - Jair Ramírez

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
  "yield": "YIELD"
}

# List of token names - Jair Ramírez

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MODULE',
    'VARIABLE',
    'NUMERAL',
    'FLOAT',
    'STRING',
    'EQUALS',
    'NOT_EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'AND',
    'OR',
    'NOT',
    'ASSIGN',
    'INCREMENT',
    'DECREMENT',
    'DOT',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'QUESTION',
    'DOUBLE_COLON',
) + tuple(reserved.values())

# Regular expression rules for simple tokens -
#Aporte de Tomás Steven Bolaños Fajardo
# number, variable, numeral, float, string no están incluidos porque irían mejor en la seccion de abajo
t_PLUS           = r'\+'
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_MODULE         = r'%'
t_EQUALS         = r'=='
t_NOT_EQUALS     = r'!='
t_GREATER        = r'>'
t_LESS           = r'<'
t_GREATER_EQUAL  = r'>='
t_LESS_EQUAL     = r'<='
t_AND            = r'&&'
t_OR             = r'\|\|'
t_NOT            = r'!'
t_ASSIGN         = r'='
t_INCREMENT      = r'\+\+'
t_DECREMENT      = r'--'
t_DOT            = r'\.'
t_COMMA          = r','
t_COLON          = r':'
t_SEMICOLON      = r';'
t_QUESTION       = r'\?'
t_DOUBLE_COLON   = r'::'
# Fin Aporte Tomas Steven Bolaños Fajardo

# A regular expression rule with some action code - 

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
pegar el algoritmo .dart
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)