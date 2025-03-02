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
        return Program(self.visit(ctx.list_declaration()))

    
    # Visit a parse tree produced by MiniGoParser#list_declaration.
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        if ctx.list_declaration():
            return [self.visit(ctx.declaration())] + self.visit(ctx.list_declaration())
        return [self.visit(ctx.declaration())]


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        dims = self.visit(ctx.list_array_specific())
        declare_type = self.visit(ctx.array_declare_type())
        return dims, declare_type
    
    # Visit a parse tree produced by MiniGoParser#all_types.
    def visitAll_types(self, ctx:MiniGoParser.All_typesContext):
        if ctx.BOOLEAN(): return BoolType()
        elif ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
        elif ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.array_type():
            dims, declare_type = self.visit(ctx.array_type())
            return ArrayType(dims, declare_type)
        return VoidType()


    # Visit a parse tree produced by MiniGoParser#var_declaration.
    def visitVar_declaration(self, ctx:MiniGoParser.Var_declarationContext):
        var_type = self.visit(ctx.all_types()) if ctx.all_types() else None
        expr = self.visit(ctx.expression()) if ctx.expression() else None   
        return VarDecl(ctx.ID().getText(), var_type, expr)


    # Visit a parse tree produced by MiniGoParser#const_declaration.
    def visitConst_declaration(self, ctx:MiniGoParser.Const_declarationContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#method_declaration.
    def visitMethod_declaration(self, ctx:MiniGoParser.Method_declarationContext):
        return self.visit(ctx.list_method_element())


    # Visit a parse tree produced by MiniGoParser#list_method_element.
    def visitList_method_element(self, ctx:MiniGoParser.List_method_elementContext):
        if ctx.list_method_element():
            return [self.visit(ctx.method_element())] + self.visit(ctx.list_method_element())
        return [self.visit(ctx.method_element())]


    # Visit a parse tree produced by MiniGoParser#method_element.
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        return (ctx.ID(0).getText(), Id(ctx.ID(1).getText()))

    # Visit a parse tree produced by MiniGoParser#func_declaration.
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return_type = self.visit(ctx.all_types()) if ctx.all_types() else VoidType()
        func_decl = FuncDecl(ctx.ID().getText(), self.visit(ctx.list_func_arguments_prime()), return_type, Block(self.visit(ctx.list_statement_prime())))
        
        if ctx.method_declaration():
            receiver, recType = self.visit(ctx.method_declaration())[0]
            return MethodDecl(receiver, recType, func_decl)
        return func_decl
        

    # Visit a parse tree produced by MiniGoParser#list_func_arguments_prime.
    def visitList_func_arguments_prime(self, ctx:MiniGoParser.List_func_arguments_primeContext):
        if ctx.list_func_arguments():
            return self.visit(ctx.list_func_arguments())
        return []


    # Visit a parse tree produced by MiniGoParser#list_func_arguments.
    def visitList_func_arguments(self, ctx:MiniGoParser.List_func_argumentsContext):
        if ctx.list_func_arguments():
            return self.visit(ctx.func_arguments()) + self.visit(ctx.list_func_arguments())
        return self.visit(ctx.func_arguments())


    # Visit a parse tree produced by MiniGoParser#func_arguments.
    def visitFunc_arguments(self, ctx:MiniGoParser.Func_argumentsContext):
        list_ID = self.visit(ctx.list_ID())
        type = self.visit(ctx.all_types())
        return [ParamDecl(id, type) for id in list_ID]

    # Visit a parse tree produced by MiniGoParser#struct_declaration.
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.list_struct_argument()), [])


    # Visit a parse tree produced by MiniGoParser#list_struct_argument.
    def visitList_struct_argument(self, ctx:MiniGoParser.List_struct_argumentContext):
        if ctx.list_struct_argument():
            return [self.visit(ctx.struct_argument())] + self.visit(ctx.list_struct_argument())
        return [self.visit(ctx.struct_argument())]


    # Visit a parse tree produced by MiniGoParser#struct_argument.
    def visitStruct_argument(self, ctx:MiniGoParser.Struct_argumentContext):
        return (ctx.ID().getText(), self.visit(ctx.all_types()))


    # Visit a parse tree produced by MiniGoParser#interface_declaration.
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.list_interface_method_declaration()))


    # Visit a parse tree produced by MiniGoParser#list_interface_method_declaration.
    def visitList_interface_method_declaration(self, ctx:MiniGoParser.List_interface_method_declarationContext):
        if ctx.list_interface_method_declaration():
            return [self.visit(ctx.interface_method_declaration())] + self.visit(ctx.list_interface_method_declaration())
        return [self.visit(ctx.interface_method_declaration())]


    # Visit a parse tree produced by MiniGoParser#interface_method_declaration.
    def visitInterface_method_declaration(self, ctx:MiniGoParser.Interface_method_declarationContext):
        list_type = self.visit(ctx.list_interface_method_element_prime())
        return_type = self.visit(ctx.all_types()) if ctx.all_types() else VoidType()
        return Prototype(ctx.ID().getText(), list_type, return_type)


    # Visit a parse tree produced by MiniGoParser#list_interface_method_element_prime.
    def visitList_interface_method_element_prime(self, ctx:MiniGoParser.List_interface_method_element_primeContext):
        return self.visit(ctx.list_interface_method_element()) if ctx.list_interface_method_element() else []


    # Visit a parse tree produced by MiniGoParser#list_interface_method_element.
    def visitList_interface_method_element(self, ctx:MiniGoParser.List_interface_method_elementContext):
        if ctx.list_interface_method_element():
            return self.visit(ctx.interface_method_element()) + self.visit(ctx.list_interface_method_element())
        return self.visit(ctx.interface_method_element())


    # Visit a parse tree produced by MiniGoParser#interface_method_element.
    def visitInterface_method_element(self, ctx:MiniGoParser.Interface_method_elementContext):
        list_ID = self.visit(ctx.list_ID())
        type = self.visit(ctx.all_types())
        return [type for id in list_ID]


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        if ctx.list_ID():
            return [ctx.ID().getText()] + self.visit(ctx.list_ID())
        return [ctx.ID().getText()]


    # Visit a parse tree produced by MiniGoParser#list_statement_prime.
    def visitList_statement_prime(self, ctx:MiniGoParser.List_statement_primeContext):
        return self.visit(ctx.list_statement()) if ctx.list_statement() else []


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        return [self.visit(ctx.statement())]

    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        assignment_lhs = self.visit(ctx.assignment_lhs())
        rhs = self.visit(ctx.expression())
        
        if ctx.ADD_ASSIGN(): rhs = BinaryOp('+', assignment_lhs, self.visit(ctx.expression()))
        elif ctx.SUB_ASSIGN(): rhs = BinaryOp('-', assignment_lhs, self.visit(ctx.expression()))
        elif ctx.MUL_ASSIGN(): rhs = BinaryOp('*', assignment_lhs, self.visit(ctx.expression()))
        elif ctx.DIV_ASSIGN(): rhs = BinaryOp('/', assignment_lhs, self.visit(ctx.expression()))
        elif ctx.MOD_ASSIGN(): rhs = BinaryOp('%', assignment_lhs, self.visit(ctx.expression()))
        
        return Assign(assignment_lhs, rhs)
    
    
    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        if ctx.getChildCount() == 1: return Id(ctx.ID().getText())
        if ctx.expression():
            assigment_lhs = self.visit(ctx.assignment_lhs())
            return ArrayCell(assigment_lhs.arr, assigment_lhs.idx  + [self.visit(ctx.expression())]) if type(assigment_lhs) == ArrayCell else ArrayCell(assigment_lhs, [self.visit(ctx.expression())])
        return FieldAccess(self.visit(ctx.assignment_lhs()), ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        def process(list_else_if, else_stmt):
            if len(list_else_if) == 0: return else_stmt
            exp, block = list_else_if[0]
            return If(exp, block, process(list_else_if[1:], else_stmt))
        
        list_else_if = self.visit(ctx.list_elseif_prime())
        else_stmt = self.visit(ctx.else_statement_prime())
        return If(self.visit(ctx.expression()), Block(self.visit(ctx.list_statement_prime())), process(list_else_if, else_stmt))


    # Visit a parse tree produced by MiniGoParser#list_elseif_prime.
    def visitList_elseif_prime(self, ctx:MiniGoParser.List_elseif_primeContext):
        return self.visit(ctx.list_elseif()) if ctx.list_elseif() else []


    # Visit a parse tree produced by MiniGoParser#list_elseif.
    def visitList_elseif(self, ctx:MiniGoParser.List_elseifContext):
        if ctx.list_elseif():
            return [self.visit(ctx.elseif())] + self.visit(ctx.list_elseif())
        return [self.visit(ctx.elseif())]


    # Visit a parse tree produced by MiniGoParser#elseif.
    def visitElseif(self, ctx:MiniGoParser.ElseifContext):
        return (self.visit(ctx.expression()), Block(self.visit(ctx.list_statement_prime())))


    # Visit a parse tree produced by MiniGoParser#else_statement_prime.
    def visitElse_statement_prime(self, ctx:MiniGoParser.Else_statement_primeContext):
        return self.visit(ctx.else_statement()) if ctx.else_statement() else None


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return Block(self.visit(ctx.list_statement_prime()))


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        block = Block(self.visit(ctx.list_statement_prime()))
        if ctx.basic_for(): return ForBasic(self.visit(ctx.basic_for()), block)
        elif ctx.init_for():
            init, cond, update = self.visit(ctx.init_for())
            return ForStep(init, cond, update, block)
        idx, val, expr = self.visit(ctx.range_for())
        return ForEach(idx, val, expr, block)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        init = self.visit(ctx.getChild(1))
        cond = self.visit(ctx.expression())
        update = self.visit(ctx.getChild(5))
        return init, cond, update


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        idx = Id(ctx.ID(0).getText())
        val = Id(ctx.ID(1).getText())
        expr = self.visit(ctx.expression())
        return idx, val, expr


    # Visit a parse tree produced by MiniGoParser#assignment_stmt_for.
    def visitAssignment_stmt_for(self, ctx:MiniGoParser.Assignment_stmt_forContext):
        rhs = self.visit(ctx.expression())
        if ctx.ADD_ASSIGN(): rhs = BinaryOp('+', Id(ctx.ID().getText()), self.visit(ctx.expression()))
        elif ctx.SUB_ASSIGN(): rhs = BinaryOp('-', Id(ctx.ID().getText()), self.visit(ctx.expression()))
        elif ctx.MUL_ASSIGN(): rhs = BinaryOp('*', Id(ctx.ID().getText()), self.visit(ctx.expression()))
        elif ctx.DIV_ASSIGN(): rhs = BinaryOp('/', Id(ctx.ID().getText()), self.visit(ctx.expression()))
        elif ctx.MOD_ASSIGN(): rhs = BinaryOp('%', Id(ctx.ID().getText()), self.visit(ctx.expression()))
        return Assign(Id(ctx.ID().getText()), rhs)


    # Visit a parse tree produced by MiniGoParser#var_declaration_for.
    def visitVar_declaration_for(self, ctx:MiniGoParser.Var_declaration_forContext):
        type = self.visit(ctx.all_types()) if ctx.all_types() else None
        return VarDecl(ctx.ID().getText(), type, self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return MethCall(self.visit(ctx.assignment_lhs()), ctx.ID().getText(), self.visit(ctx.list_expression_prime())) if ctx.assignment_lhs() else FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression_prime()))


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)


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
        elif ctx.ID(): return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        dims, declare_type = self.visit(ctx.array_type())
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
        return ctx.ID().getText(), self.visit(ctx.list_expression_prime())


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
        elif ctx.expression(): 
            result = self.visit(ctx.expression6())
            return ArrayCell(result.arr, result.idx  + [self.visit(ctx.expression())]) if type(result) == ArrayCell else ArrayCell(result, [self.visit(ctx.expression())])
        elif ctx.function_call():
            func_name, func_arg = self.visit(ctx.function_call())
            return MethCall(self.visit(ctx.expression6()), func_name, func_arg)
        return FieldAccess(self.visit(ctx.expression6()), ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.literal(): return self.visit(ctx.literal())
        elif ctx.function_call():
            func_name, func_arg = self.visit(ctx.function_call())
            return FuncCall(func_name, func_arg)
        return self.visit(ctx.expression())
