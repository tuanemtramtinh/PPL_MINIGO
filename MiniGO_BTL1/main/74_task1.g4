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

program: 'votien'+ EOF;

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