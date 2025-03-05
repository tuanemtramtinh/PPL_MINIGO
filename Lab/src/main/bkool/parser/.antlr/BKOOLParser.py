# Generated from c://Code//PPL//Lab//src//main//bkool//parser//BKOOL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,14,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,12,8,1,
        1,1,0,0,2,0,2,0,0,12,0,4,1,0,0,0,2,11,1,0,0,0,4,5,3,2,1,0,5,6,5,
        0,0,1,6,1,1,0,0,0,7,8,5,5,0,0,8,9,5,1,0,0,9,12,3,2,1,0,10,12,5,5,
        0,0,11,7,1,0,0,0,11,10,1,0,0,0,12,3,1,0,0,0,1,11
    ]

class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "FLOATTYPE", 
                      "ID", "SEP" ]

    RULE_program = 0
    RULE_ids = 1

    ruleNames =  [ "program", "ids" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    FLOATTYPE=3
    ID=4
    SEP=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.ids()
            self.state = 5
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(BKOOLParser.SEP, 0)

        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ids




    def ids(self):

        localctx = BKOOLParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ids)
        try:
            self.state = 11
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(BKOOLParser.SEP)
                self.state = 8
                self.match(BKOOLParser.T__0)
                self.state = 9
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.match(BKOOLParser.SEP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





