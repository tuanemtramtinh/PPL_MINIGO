# Generated from c://Code//PPL//Lab//src//main//bkool//parser//BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,5,30,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,4,3,25,8,3,11,3,12,3,26,
        1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,2,1,0,97,122,3,0,44,44,59,
        59,91,91,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,1,11,1,0,0,0,3,13,1,0,0,0,5,17,1,0,0,0,7,24,1,0,0,0,9,28,
        1,0,0,0,11,12,5,44,0,0,12,2,1,0,0,0,13,14,5,105,0,0,14,15,5,110,
        0,0,15,16,5,116,0,0,16,4,1,0,0,0,17,18,5,102,0,0,18,19,5,108,0,0,
        19,20,5,111,0,0,20,21,5,97,0,0,21,22,5,116,0,0,22,6,1,0,0,0,23,25,
        7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,
        27,8,1,0,0,0,28,29,7,1,0,0,29,10,1,0,0,0,2,0,26,0
    ]

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
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


