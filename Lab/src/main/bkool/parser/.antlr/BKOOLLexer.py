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
        1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,4,4,27,8,4,11,
        4,12,4,28,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,1,1,0,97,122,30,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,
        3,13,1,0,0,0,5,15,1,0,0,0,7,19,1,0,0,0,9,26,1,0,0,0,11,12,5,59,0,
        0,12,2,1,0,0,0,13,14,5,44,0,0,14,4,1,0,0,0,15,16,5,105,0,0,16,17,
        5,110,0,0,17,18,5,116,0,0,18,6,1,0,0,0,19,20,5,102,0,0,20,21,5,108,
        0,0,21,22,5,111,0,0,22,23,5,97,0,0,23,24,5,116,0,0,24,8,1,0,0,0,
        25,27,7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,
        0,0,0,29,10,1,0,0,0,2,0,28,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "ID" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


