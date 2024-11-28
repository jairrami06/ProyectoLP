import ply.yacc as yacc
from analizador_lexico import tokens

resultados_semantico = []

# Inicio aporte Jair Ramírez
variables = {}
functions = {}

# Estructura principal
def p_program(p):
    '''program : statement_list'''

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''

def p_statement(p):
    '''statement : commonstatement
                 | constructor
                 | function
                 '''

def p_funcstatement_list(p):
    '''funcstatement_list : funcstatement
                      | funcstatement_list funcstatement'''

def p_funcstatement(p):
    '''
    funcstatement : commonstatement
                 | return
                 | data_input
                 | variable_usage
                 | SEMICOLON
                 | control_structures
                 | print
                 | call_function

    '''

def p_commonstatement(p):
     '''
    commonstatement : COMMENT_MULTI
                 | COMMENT_SINGLE
                 | list_definition
                 | variable_definition
                 | set
                 | map

    '''
     
def p_return(p):
    '''return : RETURN expression SEMICOLON'''

    
def p_control_structures(p):
    '''control_structures : control_structures_if_else
                          | control_structures_for
                          | control_structures_while'''

def p_variable_usage(p):
    '''variable_usage : ID SEMICOLON
                    | ID ASSIGN expression SEMICOLON
    '''
    if p[1] in variables:
        pass
    else:
        errormssg = f"Semantic error: variable {p[1]} not initialized"
        resultados_semantico.append(errormssg)

def p_call_function(p):
    '''call_function : ID LPAREN argument_list RPAREN
                     | ID LPAREN RPAREN'''
    function_name = p[1]
    if p[1] in functions:
        expected_params = len(functions[function_name])
        actual_params = len(p[3]) if len(p) == 5 else 0
        if expected_params != actual_params:
            errormssg = f"Semantic error: Function '{function_name}' expects {expected_params} parameters but {actual_params} were given."
            resultados_semantico.append(errormssg)
    else:
        errormssg = f"Semantic error: function {p[1]} not intialized"
        resultados_semantico.append(errormssg)

def  p_data_input(p):
    '''data_input : STRING ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON
               | STRING QUESTION ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON'''

def p_length(p):
    '''
    length : call_list DOT LENGTH
           | TEXT DOT LENGTH
           | ID DOT LENGTH
    '''
    if p.slice[1].type == "ID":  
        if p[1] in variables:  
            if isinstance(variables[p[1]], list): 
                pass
            else:
                errormssg = f"Semantic error: variable {p[1]} is not a list"
                resultados_semantico.append(errormssg)
        else:
            errormssg = f"Semantic error: list {p[1]} not initialized"
            resultados_semantico.append(errormssg)


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
    function : type ID LPAREN parameter_list RPAREN LBRACKET funcstatement_list RBRACKET
             | VOID ID LPAREN parameter_list RPAREN LBRACKET funcstatement_list RBRACKET
             | type ID LPAREN RPAREN LBRACKET funcstatement_list RBRACKET
             | VOID ID LPAREN RPAREN LBRACKET funcstatement_list RBRACKET
             | VOID ID LPAREN RPAREN LBRACKET RBRACKET
             | VOID ID LPAREN parameter_list RPAREN LBRACKET RBRACKET
    '''
    function_name = p[2]
    parameters = p[4] if len(p) == 9 else []
    functions[function_name] = parameters

def p_variable_definition(p):
    '''variable_definition : type ID ASSIGN expression SEMICOLON
                        | DYNAMIC ID ASSIGN expression SEMICOLON
                        | VAR ID ASSIGN expression SEMICOLON
                        '''
    variables[p[2]] = p[4]

def p_print(p):
    '''print : PRINT LPAREN RPAREN SEMICOLON
             | PRINT LPAREN expression RPAREN SEMICOLON
    '''

# Expresiones
def p_expression(p):
    '''expression : operations
                  | value
                  | conditions
                  | length
                  | call_function'''

def p_operations(p):
    '''
        operations : operand 
                  | operand operator operations    
    ''' 

def p_operand(p):
    '''
        operand : NUMBER
                  | NDOUBLE
                  | ID
    ''' 
    
def p_operator(p):
    '''
        operator : PLUS
                  | MINUS
                  | TIMES
                  | DIVIDE
                  | INT_DIVIDE
    '''    


def p_control_structures_if_else(p):
    '''control_structures_if_else : if_block
                          | if_block else_if_blocks
                          | if_block else_if_blocks else_block
                          | if_block else_block'''

def p_if_block(p):
    '''if_block : IF LPAREN conditions RPAREN LBRACKET funcstatement_list RBRACKET'''

def p_else_if_blocks(p):
    '''else_if_blocks : ELSE IF LPAREN conditions RPAREN LBRACKET funcstatement_list RBRACKET
                      | else_if_blocks ELSE IF LPAREN conditions RPAREN LBRACKET funcstatement_list RBRACKET'''

def p_else_block(p):
    '''else_block : ELSE LBRACKET funcstatement_list RBRACKET'''

def p_conditions(p):
    '''conditions : condition
                  | condition AND conditions
                  | condition OR conditions'''

def p_condition(p):
    '''condition : value comparator value
                 | NOT value'''

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


def p_call_list(p):
    '''
    call_list : LSBRACKET value_list RSBRACKET
    '''

# Listas
def p_list_definition(p):
    '''
    list_definition : LIST LESS type GREATER ID ASSIGN LSBRACKET value_list RSBRACKET SEMICOLON
    '''
    variables[p[5]] = list(p[7])
    p[0] = list(p[7])

def p_value_list(p):
    '''value_list : value
                  | value COMMA value_list'''

def p_type(p):
    '''type : INT
            | DOUBLE
            | STRING
            | BOOL
    '''
    
def p_value(p):
    '''value : operand
             | TEXT
    '''

def p_value_bool(p):
    '''value : TRUE
             | FALSE'''


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
    '''for_classic : FOR LPAREN for_classic_parenthesis_content RPAREN LBRACKET funcstatement_list RBRACKET'''

def p_for_in_parenthesis_content(p):
    '''for_in_parenthesis_content : FINAL ID IN ID'''

def p_for_in(p):
    '''for_in : FOR LPAREN for_in_parenthesis_content RPAREN LBRACKET funcstatement_list RBRACKET'''

def p_for_each_parenthesis_parenthesis_content(p):
    '''for_each_parenthesis_parenthesis_content : COLON ID
                                                | COLON ID COMMA for_each_parenthesis_parenthesis_content'''

def p_for_each_parenthesis_content(p):
    '''for_each_parenthesis_content : FINAL ID LPAREN for_each_parenthesis_parenthesis_content RPAREN IN ID'''

def p_for_each(p):
    '''for_each : FOR LPAREN for_each_parenthesis_content RPAREN LBRACKET funcstatement_list RBRACKET'''

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

# Aporte Víctor Valverde
### Tipo de funcion
def p_arrow_function(p):
    """
    function : type ID LPAREN parameter_list RPAREN ASSIGN GREATER expression
    """

### Estructura de control
def p_control_structures_while(p):
    """
    control_structures_while : WHILE LPAREN conditions RPAREN LBRACKET funcstatement_list RBRACKET
    """


### Estructura de datos
def p_map(p):
    """
    map : map_declaration map_assignment
    """


def p_map_declaration(p):
    """
    map_declaration : MAP LESS key_type COMMA type GREATER ID ASSIGN
    """


def p_map_assignment(p):
    """
    map_assignment : LBRACKET map_contents RBRACKET
    """


def p_map_contents(p):
    """
    map_contents : map_content
                 | map_content COMMA map_contents
    """


def p_map_content(p):
    """
    map_content : key_value COLON value
    """


def p_key_value(p):
    """
    key_value : TEXT
    """


def p_key_type(p):
    """
    key_type : STRING
    """
# Fin aporte Víctor Valverde



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
    message = f"Parsing result : {result}"
    resultados_sintactico.append(message)
    print(message)

# Pruebas


test_parser('''
    int binarySearch(int target) {
  // Lista ordenada definida dentro del método.
  List<int> sortedList = [1, 3, 5, 7, 9, 11, 13, 15, 17];

  int left = 0;
  int right = sortedList.length;

  while (left <= right) {
    int middle = left + right - left; 
    middle = middle ~/ 2;

    if (middle == target) {
      return middle; // Se encontró el elemento.
    } else if (middle < target) {
      left = middle + 1; // Buscar en el lado derecho.
    } else {
      right = middle - 1; // Buscar en el lado izquierdo.
    }
  }

  return -1; // El elemento no está presente en la lista.
}

void main() {
  int target = 7;

  int result = binarySearch(target);

  if (result != -1) {
    print('El número $target se encuentra en el índice $result.');
  } else {
    print('El número $target no está en la lista.');
  }
}            
''')


#Pruebas Tomas Bolaños
