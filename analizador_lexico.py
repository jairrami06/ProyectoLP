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

# A regular expression rule with some action code - 

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()