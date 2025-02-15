// 2252038

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {

lastTokenType = 0

def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        self.lastTokenType = result.type
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        self.lastTokenType = result.type
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        self.lastTokenType = result.type
        raise ErrorToken(result.text); 
    else:
        result = super().emit();
        self.lastTokenType = result.type
        return result;
}

options{
	language = Python3;
}

// ! ---------------- PASER ----------------------- */
program: list_declaration EOF;

//----------------------------------Declaration----------------------------------
list_declaration: declaration list_declaration | declaration;
declaration: var_declaration | const_declaration | func_declaration | struct_declaration | interface_declaration;


//----------------------------------Type----------------------------------
array_type: list_array_specific array_declare_type;
all_types: array_type | BOOLEAN | INT | FLOAT | STRING | ID;

//----------------------------------Const and Var---------------------------
var_declaration: VAR ID (all_types | (all_types | ) (ASSIGN expression)) SEMICOLON;
const_declaration: CONST ID ASSIGN expression SEMICOLON;

//method
method_declaration: LEFT_PAREN list_method_element RIGHT_PAREN;
list_method_element: method_element COMMA list_method_element | method_element;
method_element: ID ID;

//function
func_declaration: FUNC (method_declaration | ) ID LEFT_PAREN list_func_arguments_prime RIGHT_PAREN (all_types | ) LEFT_CURLY list_statement_prime RIGHT_CURLY SEMICOLON;
list_func_arguments_prime: list_func_arguments | ;
list_func_arguments: func_arguments COMMA list_func_arguments | func_arguments;
func_arguments: list_ID all_types;

//struct
struct_declaration: TYPE ID STRUCT LEFT_CURLY list_struct_argument RIGHT_CURLY SEMICOLON;
// list_struct_argument_prime: list_struct_argument | ;
list_struct_argument: struct_argument list_struct_argument | struct_argument; 
struct_argument: ID all_types SEMICOLON;

//interface
interface_declaration: TYPE ID INTERFACE LEFT_CURLY list_interface_method_declaration RIGHT_CURLY SEMICOLON;

// list_interface_method_declaration_prime: list_interface_method_declaration | ;
list_interface_method_declaration: interface_method_declaration list_interface_method_declaration | interface_method_declaration;
interface_method_declaration: ID LEFT_PAREN list_interface_method_element_prime RIGHT_PAREN (all_types | ) SEMICOLON;

list_interface_method_element_prime: list_interface_method_element | ;
list_interface_method_element: interface_method_element COMMA list_interface_method_element | interface_method_element;
interface_method_element: list_ID all_types;
list_ID: ID COMMA list_ID | ID;

//----------------------------------Statement----------------------------------

list_statement_prime: list_statement | ;
list_statement: statement list_statement | statement;
statement: const_declaration | var_declaration | assignment_statement | if_statement | for_statement | break_statement | continue_statement | call_statement | return_statement;

//assignment
assignment_statement: assignment_lhs (ASSIGN_COLON | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression SEMICOLON;

assignment_lhs: assignment_lhs (LEFT_SQUARE expression RIGHT_SQUARE | DOT ID) | ID;

//if
if_statement: IF LEFT_PAREN expression RIGHT_PAREN LEFT_CURLY list_statement_prime RIGHT_CURLY  list_elseif_prime  else_statement_prime SEMICOLON;

list_elseif_prime: list_elseif | ;
list_elseif: elseif list_elseif | elseif;
elseif: ELSE IF LEFT_PAREN expression RIGHT_PAREN LEFT_CURLY list_statement_prime RIGHT_CURLY;

else_statement_prime: else_statement | ;
else_statement: ELSE LEFT_CURLY list_statement_prime RIGHT_CURLY;

//for
for_statement: (basic_for | init_for | range_for) LEFT_CURLY list_statement_prime RIGHT_CURLY SEMICOLON;
basic_for: FOR expression ;
init_for: FOR (assignment_stmt_for | var_declaration_for) SEMICOLON expression SEMICOLON assignment_stmt_for;
range_for: FOR ID COMMA ID ASSIGN_COLON RANGE expression;

assignment_stmt_for: ID (ASSIGN_COLON | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression;
var_declaration_for: VAR ID (all_types | ) ASSIGN expression;

//break
break_statement: BREAK SEMICOLON;

//continue
continue_statement: CONTINUE SEMICOLON;

//call
call_statement: ((assignment_lhs DOT) | )ID LEFT_PAREN list_expression_prime RIGHT_PAREN SEMICOLON;

//return
return_statement: RETURN (expression | ) SEMICOLON;

//----------------------------------Literal----------------------------------

//literal
literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
    | BOOL_LIT
    | NIL_LIT
    | struct_literal
    | array_literal;
list_literal_prime: list_literal | ;
list_literal: literal COMMA list_literal | literal;

literal_primitive: ID | INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | NIL_LIT | struct_literal;

//array_literal
array_literal: array_type LEFT_CURLY list_array_element RIGHT_CURLY;

list_array_element: array_element COMMA list_array_element | array_element;
array_element: literal_primitive | (LEFT_CURLY list_array_element RIGHT_CURLY);

list_array_specific: array_specific list_array_specific | array_specific;
array_specific: LEFT_SQUARE (INT_LIT | ID) RIGHT_SQUARE; 

array_declare_type: BOOLEAN | INT | FLOAT | STRING | ID;

//struct_literal:
struct_literal: ID LEFT_CURLY list_struct_element_prime RIGHT_CURLY;
list_struct_element_prime: list_struct_element | ;
list_struct_element: struct_element COMMA list_struct_element | struct_element;
struct_element: ID COLON expression;

//function
function_call: ID LEFT_PAREN list_expression_prime RIGHT_PAREN;

//----------------------------------Expression----------------------------------
list_expression_prime: list_expression | ;
list_expression: expression COMMA list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (IS_EQUAL | IS_DIFF | LT | LT_EQUAL | GT | GT_EQUAL) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT|SUB) expression5 | expression6;
expression6: expression6 (LEFT_SQUARE expression RIGHT_SQUARE | DOT (ID | function_call)) | expression7;
expression7: LEFT_PAREN expression RIGHT_PAREN | literal | ID | function_call;

//! ---------------- PASER ----------------------- */


// ! ---------------- LEXER ----------------------- */
BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
IS_EQUAL: '==';
IS_DIFF: '!=';
LT: '<';
LT_EQUAL: '<=';
GT: '>';
GT_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ASSIGN_COLON: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DOT: '.';

LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_CURLY: '{';
RIGHT_CURLY: '}';
LEFT_SQUARE: '[';
RIGHT_SQUARE: ']';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';

ID: [a-zA-Z_][a-zA-Z0-9_]*;


BIN_INT_LIT: ('0b'|'0B') [0-1]+ -> type(INT_LIT);
OCT_INT_LIT: ('0o'|'0O') [0-7]+ -> type(INT_LIT);
HEX_INT_LIT: ('0x'|'0X') [0-9A-Fa-f]+ -> type(INT_LIT);

fragment DIGIT: [0-9];
fragment DIGITS: ('0' | [1-9] DIGIT*);
fragment OPT_FRAC: (DIGIT*)?;
fragment OPT_EXP: ([eE]('-'|'+')?DIGIT+)?;

INT_LIT: ('0' | [1-9] DIGIT*);
FLOAT_LIT: DIGIT+ DOT OPT_FRAC OPT_EXP;

fragment ESC_SEQ: '\\' [ntr"\\];
fragment ILLEGAL_ESC_SEQ: '\\' ~[ntr"\\];
fragment STRING_CHAR: (~[\r\n\\"] | ESC_SEQ);

STRING_LIT: '"' STRING_CHAR* '"';

WS: [ \t\f\r]+ -> skip; // skip spaces, tabs
NEWLINE: ('\r'? '\n') {
    if self.lastTokenType == self.RIGHT_SQUARE or self.lastTokenType == self.RIGHT_PAREN or self.lastTokenType == self.RIGHT_CURLY or self.lastTokenType == self.ID or self.lastTokenType == self.INT_LIT or self.lastTokenType == self.FLOAT_LIT or self.lastTokenType == self.BOOL_LIT or self.lastTokenType == self.STRING_LIT or self.lastTokenType == self.INT or self.lastTokenType == self.FLOAT or self.lastTokenType == self.BOOLEAN or self.lastTokenType == self.STRING or self.lastTokenType == self.RETURN or self.lastTokenType == self.CONTINUE or self.lastTokenType == self.BREAK or self.lastTokenType == self.NIL_LIT:
        self.text = ";"
        self.type = self.SEMICOLON
    else:
        self.skip()
};
COMMENT_BLOCK: '/*' (COMMENT_BLOCK | .)*? '*/' -> skip;
COMMENT_LINE:  '//' ~[\r\n]*  -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STRING_CHAR* ('\r\n'|'\n'|EOF) {
    if self.text[-1] == '\n':
        if self.text[-2] == '\r':
            self.text = self.text[:-2]
        else:
            self.text = self.text[:-1]
    elif self.text[-1] == '\r':
        self.text = self.text[: -1]
    else:
        self.text = self.text[:]
    raise UncloseString(self.text)
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_ESC_SEQ  {
    raise IllegalEscape(self.text[:])
};

//! ---------------- LEXER ----------------------- */