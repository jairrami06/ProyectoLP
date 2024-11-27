
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AS ASSERT ASSIGN ASYNC AWAIT BOOL BREAK CASE CATCH CLASS COLON COMMA CONST CONTINUE COVARIANT DECREMENT DEFAULT DEFERRED DIVIDE DO DOLLARSIGN DOT DOUBLE DOUBLE_COLON DYNAMIC ELSE ENUM EQUALS EXPORT EXTENDS EXTENSION EXTERNAL FACTORY FALSE FINAL FINALLY FOR FUNCTION GET GREATER GREATER_EQUAL HIDE ID IF IMPLEMENTS IMPORT IN INCREMENT INT INTERFACE IS LATE LBRACKET LENGTH LESS LESS_EQUAL LIBRARY LIST LPAREN LSBRACKET MAP MINUS MIXIN MODULE NDOUBLE NEW NOT NOT_EQUALS NULL NUM NUMBER NUMERAL OBJECT ON OPERATOR OR PART PLUS PRINT QUESTION RBRACKET READLINESYNC REQUIRED RETHROW RETURN RPAREN RSBRACKET SEMICOLON SET SHOW STATIC STDIN STRING SUPER SWITCH SYNC TEXT THIS THROW TIMES TRUE TRY TYPEDEF VAR VOID WHILE WITH YIELDprogram : statement_liststatement_list : statement\n| statement_list statementstatement : print\n| data_input\n| set\n| constructor\n| control_structures\n| function\n| list_definition\n| variable_definition\n| variable_usage\n| call_function\n| SEMICOLONcontrol_structures : control_structures_if_else\n| control_structures_forvariable_usage : IDcall_function : ID LPAREN argument_list RPAREN\n| ID LPAREN RPARENdata_input : STRING ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON\n| STRING QUESTION ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLONlength : call_list DOT LENGTH\n| TEXT DOT LENGTH\nargument_list : expression\n              | argument_list COMMA expression\n\nfunction : type ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET\n         | VOID ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET\n         | type ID LPAREN RPAREN LBRACKET statement_list RBRACKET\n         | VOID ID LPAREN RPAREN LBRACKET statement_list RBRACKET\n         | VOID ID LPAREN RPAREN LBRACKET RBRACKET\n         | VOID ID LPAREN parameter_list RPAREN LBRACKET RBRACKET\nvariable_definition : type ID ASSIGN expression SEMICOLON\n| DYNAMIC ID ASSIGN expression SEMICOLON\n| VAR ID ASSIGN expression SEMICOLON\n| INT ID ASSIGN length SEMICOLONprint : PRINT LPAREN RPAREN SEMICOLON\n| PRINT LPAREN value RPAREN SEMICOLON\n| PRINT LPAREN expression RPAREN SEMICOLON\n| PRINT LPAREN length RPAREN SEMICOLONexpression : expression PLUS expression\n| expression MINUS expression\n| expression TIMES expression\n| expression DIVIDE expressionexpression : expression AND expression\n| expression OR expressionexpression : value comparator valueexpression : value PLUS valueexpression : valuecontrol_structures_if_else : if_block\n| if_block else_if_blocks\n| if_block else_if_blocks else_block\n| if_block else_blockif_block : IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKETelse_if_blocks : ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET\n| else_if_blocks ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKETelse_block : ELSE LBRACKET statement_list RBRACKETconditions : condition\n| conditions AND conditions\n| conditions OR conditionscondition : value comparator value\n| NOT condition\n| LPAREN conditions RPARENcomparator : GREATER\n| LESS\n| EQUALS\n| GREATER_EQUAL\n| LESS_EQUAL\n| NOT_EQUALSparameter_list : parameter\n| parameter_list COMMA parameterparameter : type ID\n| REQUIRED type IDtype : INT\n| DOUBLE\n| STRING\n| BOOL\n| LIST\ncall_list : LSBRACKET value_list RSBRACKET\n\nlist_definition : LIST LESS type GREATER ID ASSIGN LSBRACKET value_list RSBRACKET SEMICOLON\nvalue_list : value\n| value_list COMMA valuevalue : NUMBER\n| NDOUBLE\n| TEXT\n| ID\n| interpolated_stringvalue : TRUE\n| FALSEinterpolated_string : TEXT PLUS ID\n| TEXT PLUS expression\nset : VAR ID ASSIGN LBRACKET value_list RBRACKET SEMICOLON\n    | VAR ID ASSIGN LESS STRING GREATER LBRACKET RBRACKET SEMICOLON\n    | FINAL ID ASSIGN CONST LBRACKET value_list RBRACKET SEMICOLON\nfor_classic_initialization : INT ID ASSIGN NUMBER\n| DOUBLE ID ASSIGN NDOUBLEfor_classic_conditions : conditionsfor_classic_changes : ID comparator value\n| ID INCREMENT\n| ID DECREMENT\n| ID comparator value COMMA for_classic_changesfor_classic_parenthesis_content : for_classic_initialization SEMICOLON for_classic_conditions SEMICOLON for_classic_changesfor_classic : FOR LPAREN for_classic_parenthesis_content RPAREN LBRACKET statement_list RBRACKETfor_in_parenthesis_content : FINAL ID IN IDfor_in : FOR LPAREN for_in_parenthesis_content RPAREN LBRACKET statement_list RBRACKETfor_each_parenthesis_parenthesis_content : COLON ID\n| COLON ID COMMA for_each_parenthesis_parenthesis_contentfor_each_parenthesis_content : FINAL ID LPAREN for_each_parenthesis_parenthesis_content RPAREN IN IDfor_each : FOR LPAREN for_each_parenthesis_content RPAREN LBRACKET statement_list RBRACKETcontrol_structures_for : for_classic\n| for_in\n| for_each\nconstructor_parenthesis_content : THIS DOT ID\n| THIS DOT ID COMMA constructor_parenthesis_content\n\nconstructor : ID LPAREN constructor_parenthesis_content RPAREN SEMICOLON\n'
    
_lr_action_items = {'SEMICOLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,52,56,57,59,60,61,62,68,72,73,85,88,91,97,101,102,111,118,126,127,132,139,143,144,148,154,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,181,186,191,193,195,197,198,201,202,203,204,205,206,207,208,209,210,211,220,223,225,227,228,229,233,234,235,236,241,242,246,248,249,250,251,252,253,256,257,258,259,260,265,267,268,269,270,272,273,279,280,281,282,283,284,288,289,290,],[14,14,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,101,-82,-83,-85,-86,-87,-88,-19,-48,-84,-51,14,-57,158,-36,162,165,172,181,-18,186,193,197,198,14,-61,-37,-46,-47,-38,-40,-41,-42,-43,-44,-45,-39,-23,-85,-90,-22,-114,-34,14,-32,14,-33,-35,-56,-62,14,-58,-59,-60,14,14,14,237,-96,246,14,14,14,14,-30,14,14,14,14,-94,-95,-91,268,14,-28,14,-31,-29,14,-53,-102,-104,-108,279,281,-93,-26,-27,14,14,-20,288,-92,289,14,-54,-21,-79,-55,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[15,15,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,15,-36,-18,15,-37,-38,-39,-114,-34,15,-32,15,-33,-35,-56,15,15,15,15,15,15,15,15,-30,15,15,15,15,-91,15,-28,15,-31,-29,15,-53,-102,-104,-108,-93,-26,-27,15,15,-20,-92,15,-54,-21,-79,-55,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,44,47,48,68,76,78,85,88,101,127,131,138,148,162,165,172,181,186,190,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[16,16,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,82,-50,-52,-19,82,82,-51,16,-36,-18,185,82,16,-37,-38,-39,-114,-34,82,16,-32,16,-33,-35,-56,16,16,16,16,16,16,16,16,-30,16,16,16,16,-91,16,-28,16,-31,-29,16,-53,-102,-104,-108,-93,-26,-27,16,16,-20,-92,16,-54,-21,-79,-55,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[18,18,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,18,-36,-18,18,-37,-38,-39,-114,-34,18,-32,18,-33,-35,-56,18,18,18,18,18,18,18,18,-30,18,18,18,18,-91,18,-28,18,-31,-29,18,-53,-102,-104,-108,-93,-26,-27,18,18,-20,-92,18,-54,-21,-79,-55,]),'FINAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,51,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[19,19,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,98,-19,-51,19,-36,-18,19,-37,-38,-39,-114,-34,19,-32,19,-33,-35,-56,19,19,19,19,19,19,19,19,-30,19,19,19,19,-91,19,-28,19,-31,-29,19,-53,-102,-104,-108,-93,-26,-27,19,19,-20,-92,19,-54,-21,-79,-55,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,38,39,47,48,50,64,68,74,77,79,81,82,83,85,88,89,93,98,99,100,101,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,127,128,129,130,134,142,147,148,151,152,153,158,162,165,172,178,181,186,187,191,192,193,195,197,198,199,201,203,207,208,209,212,223,225,227,228,229,233,234,235,236,237,240,246,249,250,251,252,253,254,256,257,258,259,260,268,269,270,272,273,274,277,279,281,283,284,288,289,290,291,],[17,17,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,37,-17,40,41,-15,-16,42,43,-77,45,46,-49,-109,-110,-111,-74,-76,-3,59,66,59,-50,-52,59,59,-19,59,59,-77,-73,-75,59,-51,17,59,59,159,160,161,-36,59,59,-63,-64,-65,-66,-67,-68,59,59,59,59,59,59,174,-18,59,183,59,188,196,59,17,59,59,59,59,-37,-38,-39,59,-114,-34,59,17,226,-32,17,-33,-35,59,-56,17,17,17,17,238,17,17,17,17,-30,17,17,17,17,262,264,-91,17,-28,17,-31,-29,59,17,-53,-102,-104,-108,-93,-26,-27,17,17,59,286,-20,-92,17,-54,-21,-79,-55,262,]),'VOID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[23,23,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,23,-36,-18,23,-37,-38,-39,-114,-34,23,-32,23,-33,-35,-56,23,23,23,23,23,23,23,23,-30,23,23,23,23,-91,23,-28,23,-31,-29,23,-53,-102,-104,-108,-93,-26,-27,23,23,-20,-92,23,-54,-21,-79,-55,]),'LIST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,44,47,48,68,76,78,85,88,101,127,138,148,162,165,172,181,186,190,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[24,24,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,79,-50,-52,-19,79,79,-51,24,-36,-18,79,24,-37,-38,-39,-114,-34,79,24,-32,24,-33,-35,-56,24,24,24,24,24,24,24,24,-30,24,24,24,24,-91,24,-28,24,-31,-29,24,-53,-102,-104,-108,-93,-26,-27,24,24,-20,-92,24,-54,-21,-79,-55,]),'DYNAMIC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[25,25,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,25,-36,-18,25,-37,-38,-39,-114,-34,25,-32,25,-33,-35,-56,25,25,25,25,25,25,25,25,-30,25,25,25,25,-91,25,-28,25,-31,-29,25,-53,-102,-104,-108,-93,-26,-27,25,25,-20,-92,25,-54,-21,-79,-55,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,44,47,48,51,68,76,78,85,88,101,127,138,148,162,165,172,181,186,190,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[26,26,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,81,-50,-52,99,-19,81,81,-51,26,-36,-18,81,26,-37,-38,-39,-114,-34,81,26,-32,26,-33,-35,-56,26,26,26,26,26,26,26,26,-30,26,26,26,26,-91,26,-28,26,-31,-29,26,-53,-102,-104,-108,-93,-26,-27,26,26,-20,-92,26,-54,-21,-79,-55,]),'DOUBLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,44,47,48,51,68,76,78,85,88,101,127,138,148,162,165,172,181,186,190,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[31,31,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,31,-50,-52,100,-19,31,31,-51,31,-36,-18,31,31,-37,-38,-39,-114,-34,31,31,-32,31,-33,-35,-56,31,31,31,31,31,31,31,31,-30,31,31,31,31,-91,31,-28,31,-31,-29,31,-53,-102,-104,-108,-93,-26,-27,31,31,-20,-92,31,-54,-21,-79,-55,]),'BOOL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,44,47,48,68,76,78,85,88,101,127,138,148,162,165,172,181,186,190,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[32,32,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,32,-50,-52,-19,32,32,-51,32,-36,-18,32,32,-37,-38,-39,-114,-34,32,32,-32,32,-33,-35,-56,32,32,32,32,32,32,32,32,-30,32,32,32,32,-91,32,-28,32,-31,-29,32,-53,-102,-104,-108,-93,-26,-27,32,32,-20,-92,32,-54,-21,-79,-55,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,49,68,85,86,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[33,33,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,87,-19,-51,146,33,-36,-18,33,-37,-38,-39,-114,-34,33,-32,33,-33,-35,-56,33,33,33,33,33,33,33,33,-30,33,33,33,33,-91,33,-28,33,-31,-29,33,-53,-102,-104,-108,-93,-26,-27,33,33,-20,-92,33,-54,-21,-79,-55,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,88,101,127,148,162,165,172,181,186,191,193,195,197,198,201,203,207,208,209,223,225,227,228,229,233,234,235,236,246,249,250,251,252,253,256,257,258,259,260,268,269,270,272,273,279,281,283,284,288,289,290,],[34,34,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,34,-36,-18,34,-37,-38,-39,-114,-34,34,-32,34,-33,-35,-56,34,34,34,34,34,34,34,34,-30,34,34,34,34,-91,34,-28,34,-31,-29,34,-53,-102,-104,-108,-93,-26,-27,34,34,-20,-92,34,-54,-21,-79,-55,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,68,85,101,127,162,165,172,181,186,193,197,198,201,229,246,250,252,253,257,258,259,260,268,269,270,279,281,284,288,289,290,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-19,-51,-36,-18,-37,-38,-39,-114,-34,-32,-33,-35,-56,-30,-91,-28,-31,-29,-53,-102,-104,-108,-93,-26,-27,-20,-92,-54,-21,-79,-55,]),'RBRACKET':([3,4,5,6,7,8,9,10,11,12,13,14,17,20,21,27,28,29,30,35,47,48,56,57,59,60,61,62,68,72,73,85,101,123,127,148,162,163,164,165,166,167,168,169,170,171,172,174,175,181,184,186,193,195,197,198,201,216,222,225,227,228,229,233,234,235,236,246,247,249,250,251,252,253,257,258,259,260,268,269,270,273,279,281,283,284,288,289,290,],[-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,-15,-16,-49,-109,-110,-111,-3,-50,-52,-82,-83,-85,-86,-87,-88,-19,-48,-84,-51,-36,-80,-18,201,-37,-46,-47,-38,-40,-41,-42,-43,-44,-45,-39,-85,-90,-114,220,-34,-32,229,-33,-35,-56,-81,248,250,252,253,-30,257,258,259,260,-91,267,269,-28,270,-31,-29,-53,-102,-104,-108,-93,-26,-27,284,-20,-92,290,-54,-21,-79,-55,]),'LPAREN':([15,17,33,34,42,43,50,87,89,93,146,147,151,152,158,159,199,217,244,],[36,39,50,51,76,78,89,147,89,89,199,89,89,89,89,213,89,243,266,]),'QUESTION':([16,],[38,]),'LESS':([24,53,56,57,58,59,60,61,62,72,73,74,92,163,164,166,167,168,169,170,171,174,175,262,],[44,106,-82,-83,-84,-85,-86,-87,-88,106,-84,131,106,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,106,]),'ELSE':([27,47,257,284,290,],[49,86,-53,-54,-55,]),'GREATER':([31,32,53,56,57,58,59,60,61,62,72,73,79,80,81,82,92,163,164,166,167,168,169,170,171,174,175,185,262,],[-74,-76,105,-82,-83,-84,-85,-86,-87,-88,105,-84,-77,142,-73,-75,105,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,221,105,]),'RPAREN':([36,39,53,54,55,56,57,58,59,60,61,62,67,69,71,72,73,76,78,90,91,94,95,96,135,137,140,149,154,163,164,166,167,168,169,170,171,173,174,175,176,182,183,188,200,202,204,205,206,224,226,231,238,239,243,245,261,264,266,275,276,285,286,287,292,],[52,68,102,111,118,-82,-83,-84,-85,-86,-87,-88,126,127,-24,-48,-84,136,141,150,-57,155,156,157,189,-69,194,202,-61,-46,-47,-40,-41,-42,-43,-44,-45,-23,-85,-90,-22,-25,-112,-71,232,-62,-58,-59,-60,-70,-72,255,-103,263,265,-113,-101,-105,280,-98,-99,-97,-107,-106,-100,]),'NUMBER':([36,39,50,64,74,77,83,89,93,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,214,254,274,],[56,56,56,56,56,56,56,56,56,56,56,-63,-64,-65,-66,-67,-68,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,241,56,56,]),'NDOUBLE':([36,39,50,64,74,77,83,89,93,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,215,254,274,],[57,57,57,57,57,57,57,57,57,57,57,-63,-64,-65,-66,-67,-68,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,242,57,57,]),'TEXT':([36,39,50,64,74,77,83,84,89,93,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,254,274,],[58,73,73,73,73,73,73,145,73,73,73,73,-63,-64,-65,-66,-67,-68,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'TRUE':([36,39,50,64,74,77,83,89,93,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,254,274,],[61,61,61,61,61,61,61,61,61,61,61,-63,-64,-65,-66,-67,-68,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'FALSE':([36,39,50,64,74,77,83,89,93,103,104,105,106,107,108,109,110,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,254,274,],[62,62,62,62,62,62,62,62,62,62,62,-63,-64,-65,-66,-67,-68,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'LSBRACKET':([36,84,230,],[64,64,254,]),'ASSIGN':([37,40,41,42,45,46,66,160,161,196,],[65,74,75,77,83,84,125,214,215,230,]),'THIS':([39,219,],[70,70,]),'LBRACKET':([49,74,86,133,136,141,150,155,156,157,189,194,221,232,255,],[88,130,88,187,191,195,203,207,208,209,223,227,247,256,272,]),'NOT':([50,89,93,147,151,152,158,199,],[93,93,93,93,93,93,93,93,]),'PLUS':([53,54,56,57,58,59,60,61,62,71,72,73,132,139,143,163,164,166,167,168,169,170,171,174,175,182,],[104,112,-82,-83,120,-85,-86,-87,-88,112,104,120,112,112,112,-46,-47,112,112,112,112,112,112,-85,112,112,]),'MINUS':([53,54,56,57,58,59,60,61,62,71,72,73,132,139,143,163,164,166,167,168,169,170,171,174,175,182,],[-48,113,-82,-83,-84,-85,-86,-87,-88,113,-48,-84,113,113,113,-46,-47,113,113,113,113,113,113,-85,113,113,]),'TIMES':([53,54,56,57,58,59,60,61,62,71,72,73,132,139,143,163,164,166,167,168,169,170,171,174,175,182,],[-48,114,-82,-83,-84,-85,-86,-87,-88,114,-48,-84,114,114,114,-46,-47,114,114,114,114,114,114,-85,114,114,]),'DIVIDE':([53,54,56,57,58,59,60,61,62,71,72,73,132,139,143,163,164,166,167,168,169,170,171,174,175,182,],[-48,115,-82,-83,-84,-85,-86,-87,-88,115,-48,-84,115,115,115,-46,-47,115,115,115,115,115,115,-85,115,115,]),'AND':([53,54,56,57,58,59,60,61,62,71,72,73,90,91,132,139,143,149,154,163,164,166,167,168,169,170,171,174,175,182,200,202,204,205,206,211,231,],[-48,116,-82,-83,-84,-85,-86,-87,-88,116,-48,-84,151,-57,116,116,116,151,-61,-46,-47,116,116,116,116,116,116,-85,116,116,151,-62,151,151,-60,151,151,]),'OR':([53,54,56,57,58,59,60,61,62,71,72,73,90,91,132,139,143,149,154,163,164,166,167,168,169,170,171,174,175,182,200,202,204,205,206,211,231,],[-48,117,-82,-83,-84,-85,-86,-87,-88,117,-48,-84,152,-57,117,117,117,152,-61,-46,-47,117,117,117,117,117,117,-85,117,117,152,-62,152,152,-60,152,152,]),'EQUALS':([53,56,57,58,59,60,61,62,72,73,92,163,164,166,167,168,169,170,171,174,175,262,],[107,-82,-83,-84,-85,-86,-87,-88,107,-84,107,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,107,]),'GREATER_EQUAL':([53,56,57,58,59,60,61,62,72,73,92,163,164,166,167,168,169,170,171,174,175,262,],[108,-82,-83,-84,-85,-86,-87,-88,108,-84,108,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,108,]),'LESS_EQUAL':([53,56,57,58,59,60,61,62,72,73,92,163,164,166,167,168,169,170,171,174,175,262,],[109,-82,-83,-84,-85,-86,-87,-88,109,-84,109,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,109,]),'NOT_EQUALS':([53,56,57,58,59,60,61,62,72,73,92,163,164,166,167,168,169,170,171,174,175,262,],[110,-82,-83,-84,-85,-86,-87,-88,110,-84,110,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,110,]),'COMMA':([56,57,59,60,61,62,69,71,72,73,122,123,135,137,140,163,164,166,167,168,169,170,171,174,175,182,183,184,188,216,222,224,226,264,271,285,],[-82,-83,-85,-86,-87,-88,128,-24,-48,-84,178,-80,190,-69,190,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,-25,219,178,-71,-81,178,-70,-72,278,178,291,]),'RSBRACKET':([56,57,59,60,61,62,72,73,122,123,163,164,166,167,168,169,170,171,174,175,216,271,],[-82,-83,-85,-86,-87,-88,-48,-84,177,-80,-46,-47,-40,-41,-42,-43,-44,-45,-85,-90,-81,282,]),'DOT':([58,63,70,124,145,177,180,],[119,121,129,179,119,-78,218,]),'STDIN':([65,125,],[124,180,]),'CONST':([75,],[133,]),'REQUIRED':([76,78,190,],[138,138,138,]),'LENGTH':([119,121,],[173,176,]),'IN':([159,263,],[212,277,]),'READLINESYNC':([179,218,],[217,244,]),'COLON':([213,278,],[240,240,]),'INCREMENT':([262,],[275,]),'DECREMENT':([262,],[276,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,88,191,195,203,207,208,209,223,227,256,272,],[2,148,225,228,233,234,235,236,249,251,273,283,]),'statement':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[3,35,3,35,3,3,3,3,3,3,3,35,3,35,35,35,35,35,35,35,3,3,35,35,]),'print':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'data_input':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'set':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'constructor':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'control_structures':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'function':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'list_definition':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'variable_definition':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'variable_usage':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'call_function':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'control_structures_if_else':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'control_structures_for':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'type':([0,2,44,76,78,88,138,148,190,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[22,22,80,134,134,22,192,22,134,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'if_block':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'for_classic':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'for_in':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'for_each':([0,2,88,148,191,195,203,207,208,209,223,225,227,228,233,234,235,236,249,251,256,272,273,283,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'else_if_blocks':([27,],[47,]),'else_block':([27,47,],[48,85,]),'value':([36,39,50,64,74,77,83,89,93,103,104,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,254,274,],[53,72,92,123,72,72,72,92,92,163,164,72,72,72,72,72,72,72,72,123,92,92,92,206,92,216,123,92,123,285,]),'expression':([36,39,74,77,83,112,113,114,115,116,117,120,128,],[54,71,132,139,143,166,167,168,169,170,171,175,182,]),'length':([36,84,],[55,144,]),'interpolated_string':([36,39,50,64,74,77,83,89,93,103,104,112,113,114,115,116,117,120,128,130,147,151,152,153,158,178,187,199,254,274,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'call_list':([36,84,],[63,63,]),'constructor_parenthesis_content':([39,219,],[67,245,]),'argument_list':([39,],[69,]),'conditions':([50,89,147,151,152,158,199,],[90,149,200,204,205,211,231,]),'condition':([50,89,93,147,151,152,158,199,],[91,91,154,91,91,91,91,91,]),'for_classic_parenthesis_content':([51,],[94,]),'for_in_parenthesis_content':([51,],[95,]),'for_each_parenthesis_content':([51,],[96,]),'for_classic_initialization':([51,],[97,]),'comparator':([53,72,92,262,],[103,103,153,274,]),'value_list':([64,130,187,254,],[122,184,222,271,]),'parameter_list':([76,78,],[135,140,]),'parameter':([76,78,190,],[137,137,224,]),'for_classic_conditions':([158,],[210,]),'for_each_parenthesis_parenthesis_content':([213,278,],[239,287,]),'for_classic_changes':([237,291,],[261,292,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','analizador_sintactico.py',11),
  ('statement_list -> statement','statement_list',1,'p_statement_list','analizador_sintactico.py',14),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','analizador_sintactico.py',15),
  ('statement -> print','statement',1,'p_statement','analizador_sintactico.py',18),
  ('statement -> data_input','statement',1,'p_statement','analizador_sintactico.py',19),
  ('statement -> set','statement',1,'p_statement','analizador_sintactico.py',20),
  ('statement -> constructor','statement',1,'p_statement','analizador_sintactico.py',21),
  ('statement -> control_structures','statement',1,'p_statement','analizador_sintactico.py',22),
  ('statement -> function','statement',1,'p_statement','analizador_sintactico.py',23),
  ('statement -> list_definition','statement',1,'p_statement','analizador_sintactico.py',24),
  ('statement -> variable_definition','statement',1,'p_statement','analizador_sintactico.py',25),
  ('statement -> variable_usage','statement',1,'p_statement','analizador_sintactico.py',26),
  ('statement -> call_function','statement',1,'p_statement','analizador_sintactico.py',27),
  ('statement -> SEMICOLON','statement',1,'p_statement','analizador_sintactico.py',28),
  ('control_structures -> control_structures_if_else','control_structures',1,'p_control_structures','analizador_sintactico.py',31),
  ('control_structures -> control_structures_for','control_structures',1,'p_control_structures','analizador_sintactico.py',32),
  ('variable_usage -> ID','variable_usage',1,'p_variable_usage','analizador_sintactico.py',35),
  ('call_function -> ID LPAREN argument_list RPAREN','call_function',4,'p_call_function','analizador_sintactico.py',43),
  ('call_function -> ID LPAREN RPAREN','call_function',3,'p_call_function','analizador_sintactico.py',44),
  ('data_input -> STRING ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON','data_input',9,'p_data_input','analizador_sintactico.py',56),
  ('data_input -> STRING QUESTION ID ASSIGN STDIN DOT READLINESYNC LPAREN RPAREN SEMICOLON','data_input',10,'p_data_input','analizador_sintactico.py',57),
  ('length -> call_list DOT LENGTH','length',3,'p_length','analizador_sintactico.py',60),
  ('length -> TEXT DOT LENGTH','length',3,'p_length','analizador_sintactico.py',61),
  ('argument_list -> expression','argument_list',1,'p_argument_list','analizador_sintactico.py',65),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','analizador_sintactico.py',66),
  ('function -> type ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET','function',8,'p_function','analizador_sintactico.py',75),
  ('function -> VOID ID LPAREN parameter_list RPAREN LBRACKET statement_list RBRACKET','function',8,'p_function','analizador_sintactico.py',76),
  ('function -> type ID LPAREN RPAREN LBRACKET statement_list RBRACKET','function',7,'p_function','analizador_sintactico.py',77),
  ('function -> VOID ID LPAREN RPAREN LBRACKET statement_list RBRACKET','function',7,'p_function','analizador_sintactico.py',78),
  ('function -> VOID ID LPAREN RPAREN LBRACKET RBRACKET','function',6,'p_function','analizador_sintactico.py',79),
  ('function -> VOID ID LPAREN parameter_list RPAREN LBRACKET RBRACKET','function',7,'p_function','analizador_sintactico.py',80),
  ('variable_definition -> type ID ASSIGN expression SEMICOLON','variable_definition',5,'p_variable_definition','analizador_sintactico.py',90),
  ('variable_definition -> DYNAMIC ID ASSIGN expression SEMICOLON','variable_definition',5,'p_variable_definition','analizador_sintactico.py',91),
  ('variable_definition -> VAR ID ASSIGN expression SEMICOLON','variable_definition',5,'p_variable_definition','analizador_sintactico.py',92),
  ('variable_definition -> INT ID ASSIGN length SEMICOLON','variable_definition',5,'p_variable_definition','analizador_sintactico.py',93),
  ('print -> PRINT LPAREN RPAREN SEMICOLON','print',4,'p_print','analizador_sintactico.py',101),
  ('print -> PRINT LPAREN value RPAREN SEMICOLON','print',5,'p_print','analizador_sintactico.py',102),
  ('print -> PRINT LPAREN expression RPAREN SEMICOLON','print',5,'p_print','analizador_sintactico.py',103),
  ('print -> PRINT LPAREN length RPAREN SEMICOLON','print',5,'p_print','analizador_sintactico.py',104),
  ('expression -> expression PLUS expression','expression',3,'p_expression_arithmetic','analizador_sintactico.py',108),
  ('expression -> expression MINUS expression','expression',3,'p_expression_arithmetic','analizador_sintactico.py',109),
  ('expression -> expression TIMES expression','expression',3,'p_expression_arithmetic','analizador_sintactico.py',110),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_arithmetic','analizador_sintactico.py',111),
  ('expression -> expression AND expression','expression',3,'p_expression_logic','analizador_sintactico.py',114),
  ('expression -> expression OR expression','expression',3,'p_expression_logic','analizador_sintactico.py',115),
  ('expression -> value comparator value','expression',3,'p_expression_comparison','analizador_sintactico.py',118),
  ('expression -> value PLUS value','expression',3,'p_expression_concat','analizador_sintactico.py',121),
  ('expression -> value','expression',1,'p_expression_value','analizador_sintactico.py',124),
  ('control_structures_if_else -> if_block','control_structures_if_else',1,'p_control_structures_if_else','analizador_sintactico.py',127),
  ('control_structures_if_else -> if_block else_if_blocks','control_structures_if_else',2,'p_control_structures_if_else','analizador_sintactico.py',128),
  ('control_structures_if_else -> if_block else_if_blocks else_block','control_structures_if_else',3,'p_control_structures_if_else','analizador_sintactico.py',129),
  ('control_structures_if_else -> if_block else_block','control_structures_if_else',2,'p_control_structures_if_else','analizador_sintactico.py',130),
  ('if_block -> IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET','if_block',7,'p_if_block','analizador_sintactico.py',133),
  ('else_if_blocks -> ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET','else_if_blocks',8,'p_else_if_blocks','analizador_sintactico.py',136),
  ('else_if_blocks -> else_if_blocks ELSE IF LPAREN conditions RPAREN LBRACKET statement_list RBRACKET','else_if_blocks',9,'p_else_if_blocks','analizador_sintactico.py',137),
  ('else_block -> ELSE LBRACKET statement_list RBRACKET','else_block',4,'p_else_block','analizador_sintactico.py',140),
  ('conditions -> condition','conditions',1,'p_conditions','analizador_sintactico.py',143),
  ('conditions -> conditions AND conditions','conditions',3,'p_conditions','analizador_sintactico.py',144),
  ('conditions -> conditions OR conditions','conditions',3,'p_conditions','analizador_sintactico.py',145),
  ('condition -> value comparator value','condition',3,'p_condition','analizador_sintactico.py',148),
  ('condition -> NOT condition','condition',2,'p_condition','analizador_sintactico.py',149),
  ('condition -> LPAREN conditions RPAREN','condition',3,'p_condition','analizador_sintactico.py',150),
  ('comparator -> GREATER','comparator',1,'p_comparator','analizador_sintactico.py',153),
  ('comparator -> LESS','comparator',1,'p_comparator','analizador_sintactico.py',154),
  ('comparator -> EQUALS','comparator',1,'p_comparator','analizador_sintactico.py',155),
  ('comparator -> GREATER_EQUAL','comparator',1,'p_comparator','analizador_sintactico.py',156),
  ('comparator -> LESS_EQUAL','comparator',1,'p_comparator','analizador_sintactico.py',157),
  ('comparator -> NOT_EQUALS','comparator',1,'p_comparator','analizador_sintactico.py',158),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','analizador_sintactico.py',161),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','analizador_sintactico.py',162),
  ('parameter -> type ID','parameter',2,'p_parameter','analizador_sintactico.py',169),
  ('parameter -> REQUIRED type ID','parameter',3,'p_parameter','analizador_sintactico.py',170),
  ('type -> INT','type',1,'p_type','analizador_sintactico.py',175),
  ('type -> DOUBLE','type',1,'p_type','analizador_sintactico.py',176),
  ('type -> STRING','type',1,'p_type','analizador_sintactico.py',177),
  ('type -> BOOL','type',1,'p_type','analizador_sintactico.py',178),
  ('type -> LIST','type',1,'p_type','analizador_sintactico.py',179),
  ('call_list -> LSBRACKET value_list RSBRACKET','call_list',3,'p_call_list','analizador_sintactico.py',183),
  ('list_definition -> LIST LESS type GREATER ID ASSIGN LSBRACKET value_list RSBRACKET SEMICOLON','list_definition',10,'p_list_definition','analizador_sintactico.py',189),
  ('value_list -> value','value_list',1,'p_value_list','analizador_sintactico.py',193),
  ('value_list -> value_list COMMA value','value_list',3,'p_value_list','analizador_sintactico.py',194),
  ('value -> NUMBER','value',1,'p_value','analizador_sintactico.py',198),
  ('value -> NDOUBLE','value',1,'p_value','analizador_sintactico.py',199),
  ('value -> TEXT','value',1,'p_value','analizador_sintactico.py',200),
  ('value -> ID','value',1,'p_value','analizador_sintactico.py',201),
  ('value -> interpolated_string','value',1,'p_value','analizador_sintactico.py',202),
  ('value -> TRUE','value',1,'p_value_bool','analizador_sintactico.py',205),
  ('value -> FALSE','value',1,'p_value_bool','analizador_sintactico.py',206),
  ('interpolated_string -> TEXT PLUS ID','interpolated_string',3,'p_interpolated_string','analizador_sintactico.py',209),
  ('interpolated_string -> TEXT PLUS expression','interpolated_string',3,'p_interpolated_string','analizador_sintactico.py',210),
  ('set -> VAR ID ASSIGN LBRACKET value_list RBRACKET SEMICOLON','set',7,'p_set','analizador_sintactico.py',225),
  ('set -> VAR ID ASSIGN LESS STRING GREATER LBRACKET RBRACKET SEMICOLON','set',9,'p_set','analizador_sintactico.py',226),
  ('set -> FINAL ID ASSIGN CONST LBRACKET value_list RBRACKET SEMICOLON','set',8,'p_set','analizador_sintactico.py',227),
  ('for_classic_initialization -> INT ID ASSIGN NUMBER','for_classic_initialization',4,'p_for_classic_initialization','analizador_sintactico.py',236),
  ('for_classic_initialization -> DOUBLE ID ASSIGN NDOUBLE','for_classic_initialization',4,'p_for_classic_initialization','analizador_sintactico.py',237),
  ('for_classic_conditions -> conditions','for_classic_conditions',1,'p_for_classic_conditions','analizador_sintactico.py',240),
  ('for_classic_changes -> ID comparator value','for_classic_changes',3,'p_for_classic_changes','analizador_sintactico.py',243),
  ('for_classic_changes -> ID INCREMENT','for_classic_changes',2,'p_for_classic_changes','analizador_sintactico.py',244),
  ('for_classic_changes -> ID DECREMENT','for_classic_changes',2,'p_for_classic_changes','analizador_sintactico.py',245),
  ('for_classic_changes -> ID comparator value COMMA for_classic_changes','for_classic_changes',5,'p_for_classic_changes','analizador_sintactico.py',246),
  ('for_classic_parenthesis_content -> for_classic_initialization SEMICOLON for_classic_conditions SEMICOLON for_classic_changes','for_classic_parenthesis_content',5,'p_for_classic_parenthesis_content','analizador_sintactico.py',249),
  ('for_classic -> FOR LPAREN for_classic_parenthesis_content RPAREN LBRACKET statement_list RBRACKET','for_classic',7,'p_for_classic','analizador_sintactico.py',252),
  ('for_in_parenthesis_content -> FINAL ID IN ID','for_in_parenthesis_content',4,'p_for_in_parenthesis_content','analizador_sintactico.py',255),
  ('for_in -> FOR LPAREN for_in_parenthesis_content RPAREN LBRACKET statement_list RBRACKET','for_in',7,'p_for_in','analizador_sintactico.py',258),
  ('for_each_parenthesis_parenthesis_content -> COLON ID','for_each_parenthesis_parenthesis_content',2,'p_for_each_parenthesis_parenthesis_content','analizador_sintactico.py',261),
  ('for_each_parenthesis_parenthesis_content -> COLON ID COMMA for_each_parenthesis_parenthesis_content','for_each_parenthesis_parenthesis_content',4,'p_for_each_parenthesis_parenthesis_content','analizador_sintactico.py',262),
  ('for_each_parenthesis_content -> FINAL ID LPAREN for_each_parenthesis_parenthesis_content RPAREN IN ID','for_each_parenthesis_content',7,'p_for_each_parenthesis_content','analizador_sintactico.py',265),
  ('for_each -> FOR LPAREN for_each_parenthesis_content RPAREN LBRACKET statement_list RBRACKET','for_each',7,'p_for_each','analizador_sintactico.py',268),
  ('control_structures_for -> for_classic','control_structures_for',1,'p_control_structures_for','analizador_sintactico.py',271),
  ('control_structures_for -> for_in','control_structures_for',1,'p_control_structures_for','analizador_sintactico.py',272),
  ('control_structures_for -> for_each','control_structures_for',1,'p_control_structures_for','analizador_sintactico.py',273),
  ('constructor_parenthesis_content -> THIS DOT ID','constructor_parenthesis_content',3,'p_constructor_parenthesis_content','analizador_sintactico.py',280),
  ('constructor_parenthesis_content -> THIS DOT ID COMMA constructor_parenthesis_content','constructor_parenthesis_content',5,'p_constructor_parenthesis_content','analizador_sintactico.py',281),
  ('constructor -> ID LPAREN constructor_parenthesis_content RPAREN SEMICOLON','constructor',5,'p_constructor','analizador_sintactico.py',286),
]
