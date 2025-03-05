# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\20\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\16")
        buf.write("\n\3\3\3\2\2\4\2\4\2\2\2\16\2\6\3\2\2\2\4\r\3\2\2\2\6")
        buf.write("\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\7\7\2\2\n\13\7")
        buf.write("\3\2\2\13\16\5\4\3\2\f\16\7\7\2\2\r\t\3\2\2\2\r\f\3\2")
        buf.write("\2\2\16\5\3\2\2\2\3\r")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




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





