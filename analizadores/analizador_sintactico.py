import ply.yacc as yacc
from analizador_lexico import tokens

# Inicio aporte Jair Ramírez
# Estructura principal
def p_program(p):
    '''program : statement_list'''

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''

def p_statement(p):
    '''statement : print
                 | control_structures
                 | function
                 | list_definition
                 | variable_definition
                 | SEMICOLON'''

# Definición de variables
def p_variable_definition(p):
    '''variable_definition : type ID ASSIGN expression SEMICOLON
                           | DYNAMIC ID ASSIGN expression SEMICOLON
                           | VAR ID ASSIGN expression SEMICOLON
                           | STATIC type ID ASSIGN expression SEMICOLON
                           | STATIC VAR ID ASSIGN expression SEMICOLON
                           | STATIC DYNAMIC ID ASSIGN expression SEMICOLON'''

# Print
def p_print(p):
    '''print : PRINT LPAREN RPAREN SEMICOLON
             | PRINT LPAREN value RPAREN SEMICOLON
             | PRINT LPAREN expression RPAREN SEMICOLON'''

# Expresiones
def p_expression_arithmetic(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

def p_expression_concat(p):
    '''expression : value PLUS value'''

def p_expression_value(p):
    '''expression : value'''

# Condicionales
def p_control_structures(p):
    '''control_structures : if_block
                          | if_block else_block'''

def p_if_block(p):
    '''if_block : IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET'''

def p_else_block(p):
    '''else_block : ELSE LBRACKET statement_list RBRACKET'''

def p_conditions(p):
    '''conditions : condition
                  | conditions AND condition
                  | conditions OR condition'''

def p_condition(p):
    '''condition : value comparator value
                 | NOT value'''

def p_comparator(p):
    '''comparator : GREATER
                  | LESS
                  | EQUALS
                  | GREATER_EQUAL
                  | LESS_EQUAL'''

# Funciones
def p_function(p):
    '''function : type ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET
                | VOID ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET
                | type ID LPAREN RPAREN LBRACKET statement_list RBRACKET
                | VOID ID LPAREN RPAREN LBRACKET statement_list RBRACKET'''

def p_parameter_list(p):
    '''parameter_list : parameter
                      | parameter_list COMMA parameter'''

def p_parameter(p):
    '''parameter : type ID
                 | REQUIRED type ID'''

# Tipos de datos
def p_type(p):
    '''type : INT
            | DOUBLE
            | STRING
            | BOOL
            | LIST'''

# Listas
def p_list_definition(p):
    '''list_definition : LIST LSBRACKET value_list RSBRACKET SEMICOLON
                       | LIST LESS type GREATER ID ASSIGN LSBRACKET value_list RSBRACKET SEMICOLON'''

def p_value_list(p):
    '''value_list : value
                  | value_list COMMA value'''

# Valores
def p_value(p):
    '''value : NUMBER
             | NDOUBLE
             | TEXT
             | ID'''

def p_value_bool(p):
    '''value : TRUE
             | FALSE'''

# Manejo de errores
def p_error(p):
    print("Syntax error in line '%d'" % p.lineno)

# Fin aporte Jair Ramírez

# Inicializar el parser
parser = yacc.yacc()

# Función para ejecutar las pruebas
def test_parser(input_code):
    print("Parsing input:\n", input_code)
    result = parser.parse(input_code)
    print("Parsing result:", result)


# Pruebas

test_parser("print(42);")
test_parser("print('Hello, World!');")
test_parser("print(5 + 3);")

test_parser("""
if (x > 10) {
    print(42);
} else {
    print(0);
}
""")
test_parser("""
if (a == b) {
    print('Equal');
}
""")

test_parser("""
void myFunction(int x, int y) {
    print(x);
}
""")

test_parser("""
void greet(int name) {
    print('Hello ' + name);
}
""")

test_parser("""
List<int> numbers = [1, 2, 3, 4];
""")

test_parser("""
List<String> names = ['Alice', 'Bob', 'Charlie'];
""")

'''
while True:
    try:
        s = input('dart > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    '''

