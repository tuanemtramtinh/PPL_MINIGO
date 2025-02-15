# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declaration.
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_types.
    def visitAll_types(self, ctx:MiniGoParser.All_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declaration.
    def visitVar_declaration(self, ctx:MiniGoParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declaration.
    def visitConst_declaration(self, ctx:MiniGoParser.Const_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declaration.
    def visitMethod_declaration(self, ctx:MiniGoParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_element.
    def visitList_method_element(self, ctx:MiniGoParser.List_method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_element.
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_declaration.
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_func_arguments_prime.
    def visitList_func_arguments_prime(self, ctx:MiniGoParser.List_func_arguments_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_func_arguments.
    def visitList_func_arguments(self, ctx:MiniGoParser.List_func_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_arguments.
    def visitFunc_arguments(self, ctx:MiniGoParser.Func_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declaration.
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_argument.
    def visitList_struct_argument(self, ctx:MiniGoParser.List_struct_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_argument.
    def visitStruct_argument(self, ctx:MiniGoParser.Struct_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declaration.
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_method_declaration.
    def visitList_interface_method_declaration(self, ctx:MiniGoParser.List_interface_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_declaration.
    def visitInterface_method_declaration(self, ctx:MiniGoParser.Interface_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_method_element_prime.
    def visitList_interface_method_element_prime(self, ctx:MiniGoParser.List_interface_method_element_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_method_element.
    def visitList_interface_method_element(self, ctx:MiniGoParser.List_interface_method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_element.
    def visitInterface_method_element(self, ctx:MiniGoParser.Interface_method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_prime.
    def visitList_statement_prime(self, ctx:MiniGoParser.List_statement_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elseif_prime.
    def visitList_elseif_prime(self, ctx:MiniGoParser.List_elseif_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elseif.
    def visitList_elseif(self, ctx:MiniGoParser.List_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif.
    def visitElseif(self, ctx:MiniGoParser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement_prime.
    def visitElse_statement_prime(self, ctx:MiniGoParser.Else_statement_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_stmt_for.
    def visitAssignment_stmt_for(self, ctx:MiniGoParser.Assignment_stmt_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declaration_for.
    def visitVar_declaration_for(self, ctx:MiniGoParser.Var_declaration_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal_prime.
    def visitList_literal_prime(self, ctx:MiniGoParser.List_literal_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal.
    def visitList_literal(self, ctx:MiniGoParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_primitive.
    def visitLiteral_primitive(self, ctx:MiniGoParser.Literal_primitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_element.
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_specific.
    def visitList_array_specific(self, ctx:MiniGoParser.List_array_specificContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_specific.
    def visitArray_specific(self, ctx:MiniGoParser.Array_specificContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_declare_type.
    def visitArray_declare_type(self, ctx:MiniGoParser.Array_declare_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_element_prime.
    def visitList_struct_element_prime(self, ctx:MiniGoParser.List_struct_element_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_element.
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression_prime.
    def visitList_expression_prime(self, ctx:MiniGoParser.List_expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)



del MiniGoParser