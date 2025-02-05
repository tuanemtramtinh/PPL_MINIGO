grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// ! ---------------- PASER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */
program: NEWLINE* declaration (declaration | NEWLINE)* EOF;

//----------------------------------Terminate----------------------------------
terminate: (SEMICOLON NEWLINE* | NEWLINE+);

//----------------------------------Type----------------------------------
array_type: list_array_specific array_declare_type;
all_types: array_type | BOOLEAN | INT | FLOAT | STRING | ID;


//----------------------------------Declaration----------------------------------
declaration: (var_declaration | const_declaration | func_declaration | struct_declaration | interface_declaration) terminate;
var_declaration: VAR ID all_types? (ASSIGN expression)?;
const_declaration: CONST ID ASSIGN expression;

//method
method_declaration: LEFT_PAREN list_method_element RIGHT_PAREN;
list_method_element: method_element COMMA list_method_element | method_element;
method_element: ID ID;

//function
func_declaration: FUNC method_declaration? ID LEFT_PAREN list_func_arguments RIGHT_PAREN (all_types | list_array_specific ID)? LEFT_CURLY (NEWLINE | list_statement)* RIGHT_CURLY;
list_func_arguments: (func_arguments (COMMA list_func_arguments)*)?;
func_arguments: ID all_types;

//struct
struct_declaration: TYPE ID STRUCT LEFT_CURLY (NEWLINE | list_struct_argument)* RIGHT_CURLY;
list_struct_argument: struct_argument (list_struct_argument)*; 
struct_argument: ID all_types terminate;

//interface
interface_declaration: TYPE ID INTERFACE LEFT_CURLY (NEWLINE | interface_method_declaration)* RIGHT_CURLY;
interface_method_declaration: ID LEFT_PAREN list_interface_method_element RIGHT_PAREN all_types? terminate;
list_interface_method_element: (interface_method_element (COMMA list_interface_method_element)*)?;
interface_method_element: ID all_types?;


//----------------------------------Statement----------------------------------

list_statement: statement (list_statement)*;
statement: declaration | assignment_statement | if_statement | for_statement | break_statement | continue_statement | call_statement | return_statement;


//assignment
assignment_statement: expression (ASSIGN_COLON | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression (SEMICOLON | NEWLINE*);

//if
if_statement: IF LEFT_PAREN expression RIGHT_PAREN LEFT_CURLY (NEWLINE |list_statement)* RIGHT_CURLY list_elseif (ELSE LEFT_CURLY (NEWLINE |list_statement)* RIGHT_CURLY)? terminate;
list_elseif: elseif list_elseif | ;
elseif: ELSE IF LEFT_PAREN expression RIGHT_PAREN LEFT_CURLY (NEWLINE | list_statement)* RIGHT_CURLY;

//for
for_statement: (basic_for | init_for | range_for) LEFT_CURLY (NEWLINE | list_statement)* RIGHT_CURLY terminate;
basic_for: FOR expression ;
init_for: FOR (assignment_statement) SEMICOLON expression SEMICOLON assignment_statement ;
range_for: FOR ID COMMA ID ASSIGN_COLON RANGE ID;

//break
break_statement: BREAK terminate;

//continue
continue_statement: CONTINUE terminate;

//call
call_statement: (ID'.')?ID LEFT_PAREN list_expression? RIGHT_PAREN terminate;

//return
return_statement: RETURN expression? terminate;

//----------------------------------Literal----------------------------------

//TODO Literal 6.6 pdf

//literal
literal:
	INT_LIT
    | BIN_INT_LIT
    | OCT_INT_LIT
    | HEX_INT_LIT
	| FLOAT_LIT
	| STRING_LIT
    | TRUE
    | FALSE
    | array_literal
    | struct_literal;
list_literal: literal COMMA list_literal | literal;

//array_literal
array_literal: array_type LEFT_CURLY list_array_element RIGHT_CURLY;

list_array_element: array_element COMMA list_array_element | array_element;
array_element: literal | LEFT_CURLY list_literal  RIGHT_CURLY;

list_array_specific: array_specific list_array_specific | array_specific;
array_specific: LEFT_SQUARE INT_LIT RIGHT_SQUARE; 

array_declare_type: BOOLEAN | INT | FLOAT | STRING | ID;

//struct_literal:
struct_literal: ID LEFT_CURLY list_struct_element RIGHT_CURLY;
list_struct_element: struct_element COMMA list_struct_element | struct_element;
struct_element: ID COLON literal;

//function
function_call: ID LEFT_PAREN list_literal? RIGHT_PAREN;

// TODO 5.2 Expressions 6 pdf
list_expression: expression COMMA list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (IS_EQUAL | IS_DIFF | LT | LT_EQUAL | GT | GT_EQUAL) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT|SUB) expression6 | expression6;
expression6: expression6 (LEFT_SQUARE expression RIGHT_SQUARE| DOT expression | COMMA expression) | LEFT_PAREN expression RIGHT_PAREN | literal | ID | function_call;

//! ---------------- PASER ----------------------- */


// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

//TODO Keywords 3.3.2 pdf
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

//TODO Operators 3.3.3 pdf
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

//TODO Separators 3.3.4 pdf
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_CURLY: '{';
RIGHT_CURLY: '}';
LEFT_SQUARE: '[';
RIGHT_SQUARE: ']';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf

BIN_INT_LIT: ('0b'|'0B') [0-1]+{
    self.text = str(int(self.text, 0))
};
OCT_INT_LIT: ('0o'|'0O') [0-7]+{
    self.text = str(int(self.text, 0))
};
HEX_INT_LIT: ('0x'|'0X') [0-9A-Fa-f]+{
    self.text = str(int(self.text, 0))
};

fragment DIGIT: [0-9];
fragment DIGITS: [0-9]+;
fragment OPT_FRAC: ('.'DIGIT*)?;
fragment OPT_EXP: ([eE]('-'|'+')?DIGITS)?;

INT_LIT: DIGITS;
FLOAT_LIT: DIGITS OPT_FRAC OPT_EXP;

fragment ESC_SEQ: '\\' [ntr"\\];
fragment ILLEGAL_ESC_SEQ: '\\' ~[ntr"\\];
fragment STRING_CHAR: (~[\r\n\\"] | ESC_SEQ);

STRING_LIT: '"' STRING_CHAR* '"'{
    self.text = self.text[1:-1]
};

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f]+ -> skip; // skip spaces, tabs
NEWLINE: [\r\n]+;
COMMENT_BLOCK: '/*' (COMMENT_BLOCK | .)*? '*/' -> skip;
COMMENT_LINE:  '//' ~[\r\n]* NEWLINE -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STRING_CHAR* ('\n'|'\r'|EOF) {
    if self.text[-1] == '\n':
        if self.text[-2] == '\r':
            self.text = self.text[1:-2]
        else:
            self.text = self.text[1:-1]
    elif self.text[-1] == '\r':
        self.text = self.text[1: -1]
    else:
        self.text = self.text[1:]
    raise UncloseString(self.text)
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_ESC_SEQ '"' {
    raise IllegalEscape(self.text[1:-1])
};

//! ---------------- LEXER ----------------------- */