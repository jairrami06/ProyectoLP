import ply.yacc as yacc
from analizador_lexico import tokens

resultados_semantico = []

# Inicio aporte Jair Ramírez
symbol_table = {
    "variables": {},
    "functions": {},
}
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
                 | constructor
                 | control_structures
                 | function
                 | list_definition
                 | variable_definition
                 | variable_usage
                 | call_function
                 | SEMICOLON'''

def p_control_structures(p):
    '''control_structures : control_structures_if_else
                          | control_structures_for'''

def p_variable_usage(p):
    '''variable_usage : ID'''
    variable_name = p[1]
    if variable_name not in symbol_table["variables"]:
        errormssg=f"Semantic error: Variable '{variable_name}' not declared before usage."
        resultados_semantico.append(errormssg)
        print(errormssg)
    else:
        p[0] = symbol_table["variables"][variable_name]

def p_call_function(p):
    '''call_function : ID LPAREN argument_list RPAREN
                     | ID LPAREN RPAREN'''
    function_name = p[1]
    if function_name not in symbol_table["functions"]:
        errormssg=f"Semantic error: Function '{function_name}' not declared before usage."
        resultados_semantico.append(errormssg)
        print(errormssg)
    else:
        expected_params = len(symbol_table["functions"][function_name])
        actual_params = len(p[3]) if len(p) == 5 else 0
        if expected_params != actual_params:
            errormssg = f"Semantic error: Function '{function_name}' expects {expected_params} parameters but {actual_params} were given."
            resultados_semantico.append(errormssg)
            print(errormssg)



def  p_data_input(p):
    '''data_input : STRING ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON
               | STRING QUESTION ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON'''

def  p_length(p):
    '''length : call_list DOT LENGTH
              | TEXT DOT LENGTH'''

def p_argument_list(p):
    '''
    argument_list : expression
                  | argument_list COMMA expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_function(p):
    '''
    function : type ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET
             | VOID ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET
             | type ID LPAREN RPAREN LBRACKET statement_list RBRACKET
             | VOID ID LPAREN RPAREN LBRACKET statement_list RBRACKET
             | VOID ID LPAREN RPAREN LBRACKET RBRACKET
             | VOID ID LPAREN parameter_list RPAREN LBRACKET RBRACKET
    '''
    function_name = p[2]
    parameters = p[4] if len(p) == 9 else []
    if function_name in symbol_table["functions"]:
        errormssg = f"Semantic error: Function '{function_name}' already declared."
        resultados_semantico.append(errormssg)
        print(errormssg)
    else:
        symbol_table["functions"][function_name] = parameters

def p_variable_definition(p):
    '''variable_definition : type ID ASSIGN expression SEMICOLON
                        | DYNAMIC ID ASSIGN expression SEMICOLON
                        | VAR ID ASSIGN expression SEMICOLON
                        | INT ID ASSIGN length SEMICOLON'''
    variable_name = p[2]
    if variable_name in symbol_table["variables"]:
        errormssg = f"Semantic error: Variable '{variable_name}' already declared."
        resultados_semantico.append(errormssg)
        print(errormssg)
    else:
        symbol_table["variables"][variable_name] = p[4]

def p_print(p):
    '''print : PRINT LPAREN RPAREN SEMICOLON
             | PRINT LPAREN value RPAREN SEMICOLON
             | PRINT LPAREN expression RPAREN SEMICOLON
             | PRINT LPAREN length RPAREN SEMICOLON'''

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

def p_control_structures_if_else(p):
    '''control_structures_if_else : if_block
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

def p_parameter_list(p):
    '''parameter_list : parameter
                   | parameter_list COMMA parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_parameter(p):
    '''parameter : type ID
              | REQUIRED type ID'''
    p[0] = p[2] if len(p) == 3 else p[3]

# Tipos de datos
def p_type(p):
    '''type : INT
            | DOUBLE
            | STRING
            | BOOL
            | LIST'''

def p_call_list(p):
    '''
    call_list : LSBRACKET value_list RSBRACKET
    '''

# Listas
def p_list_definition(p):
    '''
    list_definition : LIST LESS type GREATER ID ASSIGN LSBRACKET value_list RSBRACKET SEMICOLON
    '''

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

def p_for_classic_initialization(p):
    '''for_classic_initialization : INT ID ASSIGN NUMBER
                          | DOUBLE ID ASSIGN NDOUBLE'''

def p_for_classic_conditions(p):
    '''for_classic_conditions : conditions'''

def p_for_classic_changes(p):
    '''for_classic_changes : ID comparator value
                           | ID INCREMENT
                           | ID DECREMENT
                           | ID comparator value COMMA for_classic_changes'''

def p_for_classic_parenthesis_content(p):
    '''for_classic_parenthesis_content : for_classic_initialization SEMICOLON for_classic_conditions SEMICOLON for_classic_changes'''

def p_for_classic(p):
    '''for_classic : FOR LPAREN for_classic_parenthesis_content RPAREN LBRACKET statement_list RBRACKET'''

def p_for_in_parenthesis_content(p):
    '''for_in_parenthesis_content : FINAL ID IN ID'''

def p_for_in(p):
    '''for_in : FOR LPAREN for_in_parenthesis_content RPAREN LBRACKET statement_list RBRACKET'''

def p_for_each_parenthesis_parenthesis_content(p):
    '''for_each_parenthesis_parenthesis_content : COLON ID
                                                | COLON ID COMMA for_each_parenthesis_parenthesis_content'''

def p_for_each_parenthesis_content(p):
    '''for_each_parenthesis_content : FINAL ID LPAREN for_each_parenthesis_parenthesis_content RPAREN IN ID'''

def p_for_each(p):
    '''for_each : FOR LPAREN for_each_parenthesis_content RPAREN LBRACKET statement_list RBRACKET'''

def p_control_structures_for(p):
    '''control_structures_for : for_classic
                              | for_in
                              | for_each'''

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

resultados_sintactico = []
# Manejo de errores más detallado
def p_error(p):
    if p:
        error_message = f"Syntax error at token '{p.type}' (value: '{p.value}') on line {p.lineno}"
    else:
        error_message = "Syntax error at EOF"
    resultados_sintactico.append(error_message)
    print(error_message)


# Inicializar el parser
parser = yacc.yacc()

# Función para ejecutar las pruebas
def test_parser(input_code):
    result = parser.parse(input_code)
    message = f"Parsing input : {input_code} \n Parsing result : {result}"
    resultados_sintactico.append(message)
    print(message)

# Pruebas
test_parser('int x = 10;')
test_parser('x;')
test_parser('y;')
test_parser('void myFunction(int a, int b) {;}')
test_parser('myFunction(10, 20);')
test_parser('myFunction(10);')
test_parser('otherFunction(10);')
test_parser('String? input = stdin.readLineSync();')
test_parser('int x = 10;')
test_parser('int var1 = "hola".length;')
test_parser('x;')
test_parser('y;')
test_parser('void myFunction(int a, int b) {;}')
test_parser('myFunction(10, 20);')
test_parser('myFunction(10);')
test_parser('otherFunction(10);')

#Pruebas Tomas Bolaños
'''
for (int i = 0; i < value; i++) { 
                   for (final candidate in candidates) { 
                        for (final Candidate(:atributo, :atributo) in candidates) {
                             print('Hola mundo');
                        }
                   }
               }
'''

# Pruebas
'''
int x = 10;
x;
y;
void myFunction(int a, int b) {;}
myFunction(10, 20);
myFunction(10);
otherFunction(10);
String? input = stdin.readLineSync();
int x = 10;
int var1 = "hola".length;
x;
y;
void myFunction(int a, int b) {;}
myFunction(10, 20);
myFunction(10);
otherFunction(10);
'''

#Pruebas Tomas Bolaños
test_parser("for (int i = 0; i < value; i++) { for (final candidate in candidates) { for (final Candidate(:atributo, :atributo) in candidates) { print('Hola mundo');}}}")
