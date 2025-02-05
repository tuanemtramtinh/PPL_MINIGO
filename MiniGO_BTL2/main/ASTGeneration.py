"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
    # pass
    # #copy function target/main/MiniGoVisitor.py

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.list_declaration()))

    # Visit a parse tree produced by MiniGoParser#terminate.
    def visitTerminate(self, ctx:MiniGoParser.TerminateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        list_array_specific = self.visit(ctx.list_array_specific())
        array_declare_type = self.visit(ctx.array_declare_type())
        return [list_array_specific, array_declare_type]

    # Visit a parse tree produced by MiniGoParser#all_types.
    def visitAll_types(self, ctx:MiniGoParser.All_typesContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.array_type():
            result = self.visit(ctx.array_type())
            return ArrayType(result[1], result[0])
        else:
            return StructType()

    # Visit a parse tree produced by MiniGoParser#var_declaration.
    def visitVar_declaration(self, ctx:MiniGoParser.Var_declarationContext):
        var_name = Id(ctx.getChild(1).getText())
        var_type = ''
        var_expr = ''
        if ctx.all_types():
            var_type = self.visit(ctx.getChild(2))
            if ctx.expression():
                var_expr = self.visit(ctx.getChild(4))
        else:
            var_expr = self.visit(ctx.getChild(3))
        return VariablesDecl(var_name, var_type, var_expr)

    # Visit a parse tree produced by MiniGoParser#const_declaration.
    def visitConst_declaration(self, ctx:MiniGoParser.Const_declarationContext):
        const_name = Id(ctx.getChild(1).getText())
        const_expr = self.visit(ctx.getChild(3))
        return ConstDecl(const_name, const_expr)

    # Visit a parse tree produced by MiniGoParser#list_declaration.
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        declaration_list = ctx.declaration()
        resultList = []
        
        for declaration in declaration_list:
            resultList.append(self.visit(declaration))
            
        return resultList

    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#var_declaration_global.
    def visitVar_declaration_global(self, ctx:MiniGoParser.Var_declaration_globalContext):
        return self.visit(ctx.var_declaration())

    # Visit a parse tree produced by MiniGoParser#const_declaration_global.
    def visitConst_declaration_global(self, ctx:MiniGoParser.Const_declaration_globalContext):
        return self.visit(ctx.const_declaration())

    # Visit a parse tree produced by MiniGoParser#method_declaration.
    def visitMethod_declaration(self, ctx:MiniGoParser.Method_declarationContext):
        return self.visit(ctx.list_method_element())

    # Visit a parse tree produced by MiniGoParser#list_method_element.
    def visitList_method_element(self, ctx:MiniGoParser.List_method_elementContext):
        result = None
        if (ctx.list_method_element()):
            result = [self.visit(ctx.method_element())] + self.visit(ctx.list_method_element())
        else:
            result =  [self.visit(ctx.method_element())] 
        
        return result[0]

    # Visit a parse tree produced by MiniGoParser#method_element.
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        method_type = self.visit(ctx.getChild(1))
        method_name = Id(ctx.getChild(0).getText())
        return VariablesDecl (method_name, method_type)

    # Visit a parse tree produced by MiniGoParser#func_declaration.
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        func_name = Id(ctx.getChild(1).getText())
        func_return_type = VoidType()
        func_body = []
        func_arguments = self.visit(ctx.list_func_arguments_prime())
        method_declaration = None
        
        if (ctx.method_declaration()):
            method_declaration = self.visit(ctx.method_declaration())
            func_name = Id(ctx.getChild(2).getText())
            
        if (ctx.all_types()):
            func_return_type = self.visit(ctx.all_types())

        if (ctx.list_statement_prime()):
            func_body = self.visit(ctx.list_statement_prime())
            
        return FunctionDecl(func_name, func_return_type, method_declaration, func_arguments, func_body)

    # Visit a parse tree produced by MiniGoParser#list_func_arguments_prime.
    def visitList_func_arguments_prime(self, ctx:MiniGoParser.List_func_arguments_primeContext):
        if (ctx.list_func_arguments()):
            return self.visit(ctx.list_func_arguments())
        return []

    # Visit a parse tree produced by MiniGoParser#list_func_arguments.
    def visitList_func_arguments(self, ctx:MiniGoParser.List_func_argumentsContext):
        if (ctx.list_func_arguments()):
            return [self.visit(ctx.func_arguments())] + self.visit(ctx.list_func_arguments())
        
        return [self.visit(ctx.func_arguments())]

    # Visit a parse tree produced by MiniGoParser#func_arguments.
    def visitFunc_arguments(self, ctx:MiniGoParser.Func_argumentsContext):
        argument_name = Id(ctx.ID().getText())
        argument_type = self.visit(ctx.all_types())
        
        return VariablesDecl(argument_name, argument_type)

    # Visit a parse tree produced by MiniGoParser#struct_declaration.
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        struct_name = Id(ctx.ID().getText())
        struct_body = []
        if ctx.list_struct_argument():
            struct_body = self.visit(ctx.list_struct_argument())
        return StructDecl(struct_name, struct_body)

    # Visit a parse tree produced by MiniGoParser#list_struct_argument.
    def visitList_struct_argument(self, ctx:MiniGoParser.List_struct_argumentContext):
        if (ctx.list_struct_argument()):
            return [self.visit(ctx.struct_argument())] + self.visit(ctx.list_struct_argument())
        
        return [self.visit(ctx.struct_argument())]

    # Visit a parse tree produced by MiniGoParser#struct_argument.
    def visitStruct_argument(self, ctx:MiniGoParser.Struct_argumentContext):
        struct_name = Id(ctx.getChild(0).getText())
        struct_type = self.visit(ctx.getChild(1))
        
        return VariablesDecl(struct_name, struct_type)

    # Visit a parse tree produced by MiniGoParser#interface_declaration.
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        interface_name = Id(ctx.getChild(1).getText())
        interface_body = []
        if (ctx.list_interface_method_declaration()):
            interface_body = self.visit(ctx.list_interface_method_declaration())
        return InterfaceDecl(interface_name, interface_body)
    
    # Visit a parse tree produced by MiniGoParser#list_interface_method_declaration.
    def visitList_interface_method_declaration(self, ctx:MiniGoParser.List_interface_method_declarationContext):
        if (ctx.list_interface_method_declaration()):
            return [self.visit(ctx.interface_method_declaration())] + self.visit(ctx.list_interface_method_declaration())
        
        return [self.visit(ctx.interface_method_declaration())]

    # Visit a parse tree produced by MiniGoParser#interface_method_declaration.
    def visitInterface_method_declaration(self, ctx:MiniGoParser.Interface_method_declarationContext):
        method_name = Id(ctx.ID().getText())
        method_body = self.visit(ctx.list_interface_method_element_prime())
        method_type = VoidType()
        
        if ctx.all_types():
            method_type = self.visit(ctx.all_types())
        
        return FunctionDecl(method_name, method_type, None, method_body, [])

    # Visit a parse tree produced by MiniGoParser#list_interface_method_element_prime.
    def visitList_interface_method_element_prime(self, ctx:MiniGoParser.List_interface_method_element_primeContext):
        if ctx.list_interface_method_element():
            return self.visit(ctx.list_interface_method_element())
        return []

    # Visit a parse tree produced by MiniGoParser#list_interface_method_element.
    def visitList_interface_method_element(self, ctx:MiniGoParser.List_interface_method_elementContext):
        result = []
        if ctx.list_interface_method_element():
            result = [self.visit(ctx.interface_method_element())] + self.visit(ctx.list_interface_method_element())
        else: 
            result = [self.visit(ctx.interface_method_element())]

        final = []
        for element in result:
            if type(element) == list:
                for i in element: final.append(i)
            else: final.append(element)
        
        return final

    # Visit a parse tree produced by MiniGoParser#interface_method_element.
    def visitInterface_method_element(self, ctx:MiniGoParser.Interface_method_elementContext):
        list_ID = self.visit(ctx.list_ID())
        element_type = self.visit(ctx.all_types())
        
        result = []
        
        if len(list_ID) >= 1:
            for element in list_ID:
                result.append(VariablesDecl(element, element_type))
        else:
            result = VariablesDecl(list_ID[0], element_type)
        
        return result

    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        if ctx.list_ID():
            return [Id(ctx.ID().getText())] + self.visit(ctx.list_ID())
        return [Id(ctx.ID().getText())]
    
    # Visit a parse tree produced by MiniGoParser#list_statement_prime.
    def visitList_statement_prime(self, ctx:MiniGoParser.List_statement_primeContext):
        if (ctx.list_statement()):
            return self.visit(ctx.list_statement())
        return []
    
    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if (ctx.list_statement()):
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        return [self.visit(ctx.statement())]

    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#var_declaration_stmt.
    def visitVar_declaration_stmt(self, ctx:MiniGoParser.Var_declaration_stmtContext):
        return self.visit(ctx.var_declaration())

    # Visit a parse tree produced by MiniGoParser#const_declaration_stmt.
    def visitConst_declaration_stmt(self, ctx:MiniGoParser.Const_declaration_stmtContext):
        return self.visit(ctx.const_declaration())

    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        assignment_lhs = self.visit(ctx.assignment_lhs())
        operator = ctx.getChild(1).getText()
        expression = self.visit(ctx.expression())
        
        return AssignStmt(assignment_lhs, operator, expression)

    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        if (ctx.getChildCount() == 1):
            return self.visitChildren(ctx)
        
        lhs = self.visit(ctx.getChild(0))
        rhs = None
        
        if ctx.LEFT_SQUARE() and ctx.RIGHT_SQUARE():
            rhs = self.visit(ctx.getChild(2))
            return ArrayCell(lhs, rhs)
        else:
            rhs = Id(ctx.getChild(2).getText())
            return FieldAccess(lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#assignment_lhs_element.
    def visitAssignment_lhs_element(self, ctx:MiniGoParser.Assignment_lhs_elementContext):
        return Id(ctx.ID().getText())

    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        if_condition = self.visit(ctx.expression())
        if_stmt = self.visit(ctx.list_statement_prime())
        elif_stmt = self.visit(ctx.list_elseif_prime())
        else_stmt = self.visit(ctx.else_statement_prime())
        
        return If(if_condition, if_stmt, elif_stmt, else_stmt)

    # Visit a parse tree produced by MiniGoParser#list_elseif_prime.
    def visitList_elseif_prime(self, ctx:MiniGoParser.List_elseif_primeContext):
        if (ctx.list_elseif()):
            return self.visit(ctx.list_elseif())
        return []

    # Visit a parse tree produced by MiniGoParser#list_elseif.
    def visitList_elseif(self, ctx:MiniGoParser.List_elseifContext):
        if (ctx.list_elseif()):
            return [self.visit(ctx.elseif())] + self.visit(ctx.list_elseif())
        return [self.visit(ctx.elseif())]

    # Visit a parse tree produced by MiniGoParser#elseif.
    def visitElseif(self, ctx:MiniGoParser.ElseifContext):
        return (self.visit(ctx.expression()), self.visit(ctx.list_statement_prime()))
    
    # Visit a parse tree produced by MiniGoParser#else_statement_prime.
    def visitElse_statement_prime(self, ctx:MiniGoParser.Else_statement_primeContext):
        if ctx.else_statement():
            return self.visit(ctx.else_statement())
        return []

    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visit(ctx.list_statement_prime())

    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        for_type = self.visit(ctx.getChild(0))
        for_body = self.visit(ctx.list_statement_prime())
        
        if ctx.basic_for():
            return For(None, for_type, None, for_body)
        if ctx.init_for():
            return For(for_type[0], for_type[1], for_type[2], for_body)
            
        return For(for_type[0], for_type[1], for_type[2], for_body)

    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visit(ctx.expression())

    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        init = self.visit(ctx.getChild(1))
        condition = self.visit(ctx.getChild(3))
        update = self.visit(ctx.getChild(5))
        return [init, condition, update]

    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        index = Id(ctx.getChild(1).getText())
        value = Id(ctx.getChild(3).getText())
        expression = self.visit(ctx.expression())
        return [index, value, expression]

    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()

    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()

    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):        
        call_obj = None
        call_name = Id(ctx.ID().getText())
        call_param = self.visit(ctx.list_expression_prime())

        if (ctx.assignment_lhs()):
            call_obj = self.visit(ctx.assignment_lhs())
            
        return CallStmt(call_obj, call_name, call_param)

    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return_body = None
        
        if (ctx.expression()):
            return_body = self.visit(ctx.expression())
            
        return Return(return_body)

    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText(), 0))
        
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
    
        if ctx.NIL():
            return NilLiteral()
        
        if ctx.TRUE() or ctx.FALSE():
            if ctx.TRUE():
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
            
        if ctx.struct_literal():
            return self.visit(ctx.struct_literal())

        if ctx.array_literal():
            return self.visit(ctx.array_literal())

    # Visit a parse tree produced by MiniGoParser#list_literal_prime.
    def visitList_literal_prime(self, ctx:MiniGoParser.List_literal_primeContext):
        if (ctx.list_literal()):
            return self.visit(ctx.list_literal())
        return []

    # Visit a parse tree produced by MiniGoParser#list_literal.
    def visitList_literal(self, ctx:MiniGoParser.List_literalContext):
        if ctx.list_literal():
            return [self.visit(ctx.literal())] + self.visit(ctx.list_literal())
        return [self.visit(ctx.literal())]

    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        array_type = self.visit(ctx.array_type())
        list_array_specific = array_type[0]
        array_declare_type = array_type[1]
        list_array_element = self.visit(ctx.list_array_element())
        
        return ArrayLiteral(array_declare_type, list_array_specific, list_array_element)

    # Visit a parse tree produced by MiniGoParser#list_array_element.
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        if (ctx.list_array_element()):
            return [self.visit(ctx.array_element())] + self.visit(ctx.list_array_element())
        return [self.visit(ctx.array_element())]

    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniGoParser#list_array_specific.
    def visitList_array_specific(self, ctx:MiniGoParser.List_array_specificContext):
        if (ctx.list_array_specific()):
            return [self.visit(ctx.array_specific())] + self.visit(ctx.list_array_specific())
        return [self.visit(ctx.array_specific())]

    # Visit a parse tree produced by MiniGoParser#array_specific.
    def visitArray_specific(self, ctx:MiniGoParser.Array_specificContext):
        return int(ctx.INT_LIT().getText())


    # Visit a parse tree produced by MiniGoParser#array_declare_type.
    def visitArray_declare_type(self, ctx:MiniGoParser.Array_declare_typeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return ClassType(Id(ctx.ID().getText()))

    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        struct_name = Id(ctx.getChild(0).getText())
        struct_body = self.visit(ctx.getChild(2))
        
        return StructLiteral(struct_name, struct_body)

    # Visit a parse tree produced by MiniGoParser#list_struct_element_prime.
    def visitList_struct_element_prime(self, ctx:MiniGoParser.List_struct_element_primeContext):
        if (ctx.list_struct_element()):
            return self.visit(ctx.list_struct_element())
        else:
            return []

    # Visit a parse tree produced by MiniGoParser#list_struct_element.
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        if (ctx.list_struct_element()):
            return [self.visit(ctx.struct_element())] + self.visit(ctx.list_struct_element())
        else:
            return [self.visit(ctx.struct_element())]

    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        struct_element_name = Id(ctx.getChild(0).getText())
        
        struct_element_value = self.visit(ctx.getChild(2))
        
        return (struct_element_name, struct_element_value)

    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        func_name = Id(ctx.ID().getText())
        func_param = self.visit(ctx.getChild(2))
        return [func_name, func_param]

    # Visit a parse tree produced by MiniGoParser#list_expression_prime.
    def visitList_expression_prime(self, ctx:MiniGoParser.List_expression_primeContext):
        if ctx.list_expression():
            return self.visit(ctx.list_expression())
        return []

    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]

    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        
        operator = ctx.getChild(1).getText()
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        
        return BinaryOp(operator, lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        
        operator = ctx.getChild(1).getText()
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        
        return BinaryOp(operator, lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        
        operator = ctx.getChild(1).getText()
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        
        return BinaryOp(operator, lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        
        operator = ctx.getChild(1).getText()
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        
        return BinaryOp(operator, lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        
        operator = ctx.getChild(1).getText()
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        
        return BinaryOp(operator, lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        
        operator = ctx.getChild(0).getText()
        rhs = self.visit(ctx.getChild(1))

        return UnaryOp(operator, rhs)

    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        if ctx.LEFT_SQUARE() and ctx.RIGHT_SQUARE:
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return ArrayCell(lhs, rhs)
        elif ctx.function_call():
            field_name = self.visit(ctx.getChild(0))
            func = self.visit(ctx.getChild(2))
            func_name = func[0]
            func_param = func[1]
            return CallExpr(field_name, func_name, func_param)
        else:
            lhs = self.visit(ctx.getChild(0))
            rhs = Id(ctx.ID().getText())
            return FieldAccess(lhs, rhs)
        
    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.function_call():
                func = self.visit(ctx.function_call())
                func_name = func[0]
                func_param = func[1]
                return CallExpr('', func_name, func_param)
            else:
                return self.visitChildren(ctx)
    

        return self.visit(ctx.expression())

