from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
        # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecls.
    def visitVardecls(self, ctx:BKOOLParser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecltail.
    def visitVardecltail(self, ctx:BKOOLParser.VardecltailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mptype.
    def visitMptype(self, ctx:BKOOLParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ids.
    def visitIds(self, ctx:BKOOLParser.IdsContext):
        return self.visitChildren(ctx)
