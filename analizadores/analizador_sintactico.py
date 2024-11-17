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
                           | VAR ID ASSIGN expression SEMICOLON'''

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

def p_expression_logic(p):
    '''expression : expression AND expression
                  | expression OR expression'''

def p_expression_comparison(p):
    '''expression : value comparator value'''

def p_expression_concat(p):
    '''expression : value PLUS value'''

def p_expression_value(p):
    '''expression : value'''

# Condicionales
def p_control_structures(p):
    '''control_structures : if_block
                          | if_block else_if_blocks
                          | if_block else_if_blocks else_block
                          | if_block else_block'''

def p_if_block(p):
    '''if_block : IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET'''

def p_else_if_blocks(p):
    '''else_if_blocks : ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET
                      | else_if_blocks ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET'''

def p_else_block(p):
    '''else_block : ELSE LBRACKET statement_list RBRACKET'''

def p_conditions(p):
    '''conditions : condition
                  | conditions AND conditions
                  | conditions OR conditions'''

def p_condition(p):
    '''condition : value comparator value
                 | NOT condition
                 | LPAREN conditions RPAREN'''

def p_comparator(p):
    '''comparator : GREATER
                  | LESS
                  | EQUALS
                  | GREATER_EQUAL
                  | LESS_EQUAL
                  | NOT_EQUALS'''

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
             | ID
             | interpolated_string'''

def p_value_bool(p):
    '''value : TRUE
             | FALSE'''

def p_interpolated_string(p):
    '''interpolated_string : TEXT PLUS ID
                           | TEXT PLUS expression'''

#Fin aporte Jair Ramírez

# Manejo de errores
def p_error(p):
    print("Syntax error in line '%d'" % (p.lineno if p else "unknown"))

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
int a = 5;
int b = 3;
int suma = a + b;
int resta = a - b;
int multiplicacion = a * b;
double division = a / b;
print("Suma: \$suma");
print("Resta: \$resta");
print("Multiplicación: \$multiplicacion");
print("División: \$division");
""")

test_parser("""
int edad = 20;
String pais = "México";
if (edad > 18 && pais == "México") {
    print("Eres mayor de edad en México.");
} else if (edad > 18 || pais != "México") {
    print("Eres mayor de edad, pero no en México.");
} else {
    print("Eres menor de edad.");
}
""")

test_parser("""
int entero = 42;
double decimal = 3.14;
String texto = "Hola Dart";
bool esVerdadero = true;
int suma = entero + 10;
bool condicion = entero > 10 && esVerdadero;
print("Entero: \$entero");
print("Decimal: \$decimal");
print("Texto: \$texto");
print("Condición: \$condicion");
""")

test_parser("""
List<int> numeros = [1, 2, 3, 4, 5];
""")
