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
                 | data_input
                 | set
                 | for
                 | constructor
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


#Inicio aporte Tomas Bolaños
#Entrada de Datos
#Ejemplo String? input= stdin.readLineSync();
def  p_data_input(p):
    '''
    data_input : STRING QUESTION ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON
    '''

#Estructura de Datos: Set
#Ejemplos var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};
#var names = <String>{};
#final constantSet = const {'fluorine','chlorine','bromine','iodine','astatine'};
def p_set(p):
    '''
    set : VAR ID ASSIGN LBRACKET value_list RBRACKET SEMICOLON
        | VAR ID ASSIGN LESS STRING GREATER LBRACKET RBRACKET SEMICOLON
        | FINAL ID ASSIGN CONST LBRACKET value_list RBRACKET SEMICOLON
    '''

#Estructura de Control for
#Ejemplos for (int i = 0; i < value; i++) { something }
#for (final candidate in candidates) { something }
#for (final Candidate(:atributo, :atributo) in candidates) { something}

def p_for_inicio(p):
    '''
    for_inicio : INT ID ASSIGN NUMBER
    | DOUBLE ID ASSIGN NDOUBLE
    '''

def p_for_conditions(p):
    '''
    for_conditions : conditions
    '''

def p_for_changes(p):
    '''
    for_changes : ID comparator value
        | ID INCREMENT
        | ID DECREMENT
        | ID comparator value COMMA for_changes
    '''

def p_foreach_id_parenthesis_content(p):
    '''
    foreach_id_parenthesis_content : COLON ID
    | COLON ID COMMA foreach_id_parenthesis_content
    '''

def p_for_parenthesis_content(p):
    '''
    for_parenthesis_content : for_inicio SEMICOLON for_conditions SEMICOLON for_changes
    | FINAL ID IN ID
    | FINAL ID LPAREN foreach_id_parenthesis_content RPAREN IN ID
    '''

def p_for(p):
    '''
    for : FOR LPAREN for_parenthesis_content RPAREN LBRACKET statement_list RBRACKET
    '''

#Funcion Constructor(muy difícil validar)
#  Point(this.x, this.y);

def p_constructor_parenthesis_content(p):
    '''
    constructor_parenthesis_content : THIS DOT ID
    | THIS DOT ID COMMA constructor_parenthesis_content
    '''

def p_constructor(p):
    '''
    constructor : ID LPAREN constructor_parenthesis_content RPAREN SEMICOLON
    '''


#Fin aporte de Tomas

# Manejo de errores
#def p_error(p):
#    print("Syntax error in line '%d'" % (p.lineno if p else "unknown"))

#Manejo de errores mas detallados
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' (value: '{p.value}') on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Inicializar el parser
parser = yacc.yacc()


# Función para ejecutar las pruebas
def test_parser(input_code):
    print("Parsing input:\n", input_code)
    result = parser.parse(input_code)
    print("Parsing result:", result)

# Pruebas
test_parser('String input = stdin.readLineSync();')
test_parser("var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};")
test_parser("var names = <String>{};")
test_parser("final constantSet = const {'fluorine','chlorine','bromine','iodine','astatine'};")
test_parser("for (int i = 0; i < 10; i++) { print(i); }")
test_parser("for (final candidate in candidates) { print(candidate); }")
test_parser("for (final Candidate(:atributo, :atributo) in candidates) { print('attributes'); }")
test_parser("Point(this.x, this.y);")

