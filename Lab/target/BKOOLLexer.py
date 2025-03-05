# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\33\n")
        buf.write("\5\r\5\16\5\34\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2")
        buf.write("\4\3\2c|\5\2..==]]\2 \2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2")
        buf.write("\7\23\3\2\2\2\t\32\3\2\2\2\13\36\3\2\2\2\r\16\7.\2\2\16")
        buf.write("\4\3\2\2\2\17\20\7k\2\2\20\21\7p\2\2\21\22\7v\2\2\22\6")
        buf.write("\3\2\2\2\23\24\7h\2\2\24\25\7n\2\2\25\26\7q\2\2\26\27")
        buf.write("\7c\2\2\27\30\7v\2\2\30\b\3\2\2\2\31\33\t\2\2\2\32\31")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\n\3\2\2\2\36\37\t\3\2\2\37\f\3\2\2\2\4\2\34\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    FLOATTYPE = 3
    ID = 4
    SEP = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID", "SEP" ]

    ruleNames = [ "T__0", "INTTYPE", "FLOATTYPE", "ID", "SEP" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


