"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        dims = self.visit(ctx.list_array_specific())
        declare_type = self.visit(ctx.array_declare_type())
        return [dims, declare_type]


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT(): return IntLiteral(int(ctx.INT_LIT().getText(), 0))
        elif ctx.FLOAT_LIT(): return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.BOOL_LIT(): return BooleanLiteral(ctx.BOOL_LIT().getText() == 'true')
        elif ctx.NIL_LIT(): return NilLiteral()
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#list_literal_prime.
    def visitList_literal_prime(self, ctx:MiniGoParser.List_literal_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal.
    def visitList_literal(self, ctx:MiniGoParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_primitive.
    def visitLiteral_primitive(self, ctx:MiniGoParser.Literal_primitiveContext):
        if ctx.INT_LIT(): return IntLiteral(int(ctx.INT_LIT().getText(), 0))
        elif ctx.FLOAT_LIT(): return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.BOOL_LIT(): return BooleanLiteral(ctx.BOOL_LIT().getText() == 'true')
        elif ctx.NIL_LIT(): return NilLiteral()
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        array_type = self.visit(ctx.array_type())
        dims = array_type[0]
        declare_type = array_type[1]
        return ArrayLiteral(dims, declare_type, self.visit(ctx.list_array_element()))


    # Visit a parse tree produced by MiniGoParser#list_array_element.
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        if ctx.list_array_element():
            return [self.visit(ctx.array_element())] + self.visit(ctx.list_array_element())
        return [self.visit(ctx.array_element())]


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visit(ctx.literal_primitive()) if ctx.literal_primitive() else self.visit(ctx.list_array_element())


    # Visit a parse tree produced by MiniGoParser#list_array_specific.
    def visitList_array_specific(self, ctx:MiniGoParser.List_array_specificContext):
        if (ctx.list_array_specific()):
            return [self.visit(ctx.array_specific())] + self.visit(ctx.list_array_specific())
        return [self.visit(ctx.array_specific())]


    # Visit a parse tree produced by MiniGoParser#array_specific.
    def visitArray_specific(self, ctx:MiniGoParser.Array_specificContext):
        return IntLiteral(int(ctx.INT_LIT().getText())) if ctx.INT_LIT() else Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#array_declare_type.
    def visitArray_declare_type(self, ctx:MiniGoParser.Array_declare_typeContext):
        if ctx.BOOLEAN(): return BoolType()
        elif ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.list_struct_element_prime()))


    # Visit a parse tree produced by MiniGoParser#list_struct_element_prime.
    def visitList_struct_element_prime(self, ctx:MiniGoParser.List_struct_element_primeContext):
        return self.visit(ctx.list_struct_element()) if ctx.list_struct_element() else []


    # Visit a parse tree produced by MiniGoParser#list_struct_element.
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        if ctx.list_struct_element():
            return [self.visit(ctx.struct_element())] + self.visit(ctx.list_struct_element())
        return [self.visit(ctx.struct_element())]

    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return (ctx.ID().getText(), self.visit(ctx.expression()))

    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return [ctx.ID().getText(), self.visit(ctx.list_expression_prime())]


    # Visit a parse tree produced by MiniGoParser#list_expression_prime.
    def visitList_expression_prime(self, ctx:MiniGoParser.List_expression_primeContext):
        return self.visit(ctx.list_expression()) if ctx.list_expression() else []


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visit(ctx.expression1()) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visit(ctx.expression2()) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visit(ctx.expression3()) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visit(ctx.expression4()) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))

    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visit(ctx.expression5()) if ctx.getChildCount() == 1 else BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visit(ctx.expression6()) if ctx.getChildCount() == 1 else  UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expression7())
        elif ctx.expression(): return ArrayCell(self.visit(ctx.expression6()), [self.visit(ctx.expression())])
        elif ctx.function_call():
            function_call = self.visit(ctx.function_call())
            func_name = function_call[0]
            func_arg = function_call[1]
            return MethCall(self.visit(ctx.expression6()), func_name, func_arg)
        return FieldAccess(self.visit(ctx.expression6()), ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.literal(): return self.visit(ctx.literal())
        elif ctx.function_call():
            function_call = self.visit(ctx.function_call())
            func_name = function_call[0]
            func_arg = function_call[1]
            return FuncCall(func_name, func_arg)
        return self.visit(ctx.expression())
