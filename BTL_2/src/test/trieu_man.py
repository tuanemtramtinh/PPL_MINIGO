import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_const_1(self):
        input = """const TrieuMan = foo( 1 ); """
        expect = str(Program([ConstDecl("TrieuMan",None,FuncCall("foo",[IntLiteral(1)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    
    def test_const_2(self):
        input = """const TrieuMan = TrieuMan(a(b(c(d(e(f(g(t()))))))));"""
        expect = str(Program([ConstDecl("TrieuMan",None,FuncCall("TrieuMan",[FuncCall("a",[FuncCall("b",[FuncCall("c",[FuncCall("d",[FuncCall("e",[FuncCall("f",[FuncCall("g",[FuncCall("t",[])])])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_const_3(self):
        input = """const TrieuMan = 1 + 2 * 3 / 4;"""
        expect = str(Program([ConstDecl("TrieuMan",None,BinaryOp("+", IntLiteral(1), BinaryOp("/", BinaryOp("*", IntLiteral(2), IntLiteral(3)), IntLiteral(4))))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_const_4(self):
        input = """const TrieuMan = foo( 1+2-3&&5--1 );"""
        expect = str(Program([ConstDecl("TrieuMan",None,FuncCall("foo",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_const_5(self):
        input = """const TrieuMan = foo( a[2][3][4][3] );"""
        expect = str(Program([ConstDecl("TrieuMan",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(3)])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_const_6(self):
        input = """const TrieuMan = a.b.c.d.e.f.g.h;"""
        expect = str(Program([ConstDecl("TrieuMan",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_const_7(self):
        input = """const TrieuMan = a.b().c(1, 2).d[3][4][5].e;"""
        expect = str(Program([ConstDecl("TrieuMan",None,FieldAccess(ArrayCell(FieldAccess(MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]),"d"),[IntLiteral(3),IntLiteral(4),IntLiteral(5)]),"e"))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_const_8(self):
        input = """const TrieuMan = a[b[c[d[e[f[g[h]]]]]]];"""
        expect = str(Program([ConstDecl("TrieuMan",None,ArrayCell(Id("a"),[ArrayCell(Id("b"),[ArrayCell(Id("c"),[ArrayCell(Id("d"),[ArrayCell(Id("e"),[ArrayCell(Id("f"),[ArrayCell(Id("g"),[Id("h")])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_const_9(self):
        input = """const TrieuMan = a{};"""
        expect = str(Program([ConstDecl("TrieuMan",None,StructLiteral("a",[]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_const_10(self):
        input = """const TrieuMan = a{b:1, c:2};"""
        expect = str(Program([ConstDecl("TrieuMan",None,StructLiteral("a",[("b",IntLiteral(1)),("c",IntLiteral(2))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_const_11(self):
        input = """const TrieuMan = a[b{c:1, d:2}];"""
        expect = str(Program([ConstDecl("TrieuMan",None,ArrayCell(Id("a"),[StructLiteral("b",[("c",IntLiteral(1)),("d",IntLiteral(2))])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_const_12(self):
        input = """const TrieuMan = ID(a,b,d, a,b,d, a,b,d, a,b,d, a,b,d, a,b,d);"""
        expect = str(Program([ConstDecl("TrieuMan",None,FuncCall("ID",[Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d")]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_const_13(self):
        input = """const TrieuMan = a[b[c[d[e[f[g[h]]]]]]][ID(a,b,d, a,b,d, a,b,d, a,b,d, a,b,d, a,b,d)];"""
        expect = str(Program([ConstDecl("TrieuMan",None,ArrayCell(Id("a"),[ArrayCell(Id("b"),[ArrayCell(Id("c"),[ArrayCell(Id("d"),[ArrayCell(Id("e"),[ArrayCell(Id("f"),[ArrayCell(Id("g"),[Id("h")])])])])])]),FuncCall("ID",[Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d"),Id("a"),Id("b"),Id("d")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_const_14(self):
        input = """const TrieuMan = [2][4][a][BDH]TrieuMan{0x123, nil, true, 3438593, 3.44};"""
        expect = str(Program([ConstDecl("TrieuMan",None,ArrayLiteral([IntLiteral(2),IntLiteral(4),Id("a"),Id("BDH")],Id("TrieuMan"),[IntLiteral("0x123"),NilLiteral(),BooleanLiteral(True),IntLiteral(3438593),FloatLiteral("3.44")]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_const_15(self):
        input = """const TrieuMan = 1 + 2 - 7 / 6 + a.a.a.a;"""
        expect = str(Program([ConstDecl("TrieuMan",None,BinaryOp("+", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), BinaryOp("/", IntLiteral(7), IntLiteral(6))), FieldAccess(FieldAccess(FieldAccess(Id("a"),"a"),"a"),"a")))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
        
    def test_func_1(self):
        input = """
        func TrieuMan(){
            a[1][2][3].c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.d.d.d.d.d.d.d.a[2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4].e.e.e.e.e.e.e.e.e.e.e.e.e.e := a[1][2][3].c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.d.d.d.d.d.d.d.a[2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4].e.e.e.e.e.e.e.e.e.e.e.e.e.e
        }
        """
        expect = str(Program([FuncDecl("TrieuMan",[],VoidType(),Block([Assign(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"d"),"d"),"d"),"d"),"d"),"d"),"d"),"a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"d"),"d"),"d"),"d"),"d"),"d"),"d"),"a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"))]))
]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_func_2(self):
        input = """func main() {
            return ;
        };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_func_3(self):
        input = """    
            func TrieuMan() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                    
                const TrieuMan = a.b() + 2;
            }                                       
        """
        expect = str(Program([FuncDecl("TrieuMan",[],VoidType(),Block([VarDecl("x",IntType(),BinaryOp("+", FuncCall("foo",[]), BinaryOp("/", IntLiteral(3), IntLiteral(4)))),VarDecl("y", None,BinaryOp("/", StringLiteral("\"Hello\""), IntLiteral(4))),VarDecl("z",Id("str"), None),ConstDecl("TrieuMan",None,BinaryOp("+", MethCall(Id("a"),"b",[]), IntLiteral(2)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_4(self):
        input = """
            func abc() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([Assign(Id("x"),BinaryOp("+", FuncCall("foo",[]), BinaryOp("/", IntLiteral(3), IntLiteral(4)))),Assign(ArrayCell(FieldAccess(Id("x"),"c"),[IntLiteral(2),IntLiteral(4)]),BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_func_5(self):
        input = """
            func abc() {
                if (x > 10) {} 
                if (x > 10) {
                    
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([]), None),If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([]), If(BinaryOp("==", Id("x"), IntLiteral(10)), Block([VarDecl("z",Id("str"), None)]), Block([VarDecl("z",Id("ID"), None)])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_func_6(self):
        input = """
            func abc() {
                for i < 10 {}
                for i := 0; i < 10; i += 1 {}
                for index, value := range array {}
            }
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([])),ForEach(Id("index"),Id("value"),Id("array"),Block([]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_7(self):
        input = """
            func abc() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
            }
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Break()])),Break(),Continue(),Return(IntLiteral(1)),Return(None),FuncCall("foo",[BinaryOp("+", IntLiteral(2), Id("x")),BinaryOp("/", IntLiteral(4), Id("y"))]),MethCall(Id("m"),"goo",[])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_func_8(self):
        input = """
            func abc() {
                x := 1;
                y := 2;
                z := x + y;
            }
            func main() {
                abc();
                println(z);
            }
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([Assign(Id("x"),IntLiteral(1)),Assign(Id("y"),IntLiteral(2)),Assign(Id("z"),BinaryOp("+", Id("x"), Id("y")))])),
			FuncDecl("main",[],VoidType(),Block([FuncCall("abc",[]),FuncCall("println",[Id("z")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_func_9(self):
        input = """
            func Add() {
                for var i = 0; i < 10; i += 1 {
                    // loop body
                }
            }
        """
        expect = str(Program([FuncDecl("Add",[],VoidType(),Block([ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_func_10(self):
        input = """
            func Add() {
                for x > 0 {
                    TrieuMan();
                    x := x - 1;
                    if (x == 5) {
                        TrieuMan();
                    }
                    TrieuMan();
                }
            }
        """
        expect = str(Program([FuncDecl("Add",[],VoidType(),Block([ForBasic(BinaryOp(">", Id("x"), IntLiteral(0)),Block([FuncCall("TrieuMan",[]),Assign(Id("x"),BinaryOp("-", Id("x"), IntLiteral(1))),If(BinaryOp("==", Id("x"), IntLiteral(5)), Block([FuncCall("TrieuMan",[])]), None),FuncCall("TrieuMan",[])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_func_11(self):
        input ="""
            func Add() {
                for i := 0; i < 10; i += i + 1 {
                    print("ICU loop, iteration: " + i);
                    if (i % 2 == 0) {
                        print("Even number: " + i);
                    } else {
                        print("Odd number: " + i);
                    }
                    // Additional processing or updates can be added here
                    print("End of iteration " + i);
                }
            }
        """
        expect = str(Program([FuncDecl("Add",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))),Block([FuncCall("print",[BinaryOp("+", StringLiteral("\"ICU loop, iteration: \""), Id("i"))]),If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), Block([FuncCall("print",[BinaryOp("+", StringLiteral("\"Even number: \""), Id("i"))])]), Block([FuncCall("print",[BinaryOp("+", StringLiteral("\"Odd number: \""), Id("i"))])])),FuncCall("print",[BinaryOp("+", StringLiteral("\"End of iteration \""), Id("i"))])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_func_12(self):
        input = """
            func TrieuMan(a,b,c int, d,e,f int){
                for index, value := range array {
                    print("Range loop: index = ", item);
                    
                    for j := 0; j < 3; j += j + 1 {
                        print("Nested ICU loop inside range, j = ");
                        if (j == 1) {
                            print("Value of j is 1");
                        }
                    }
                    
                    print("End of one range iteration");
                }
            }
        """
        expect = str(Program([FuncDecl("TrieuMan",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",IntType()),ParamDecl("d",IntType()),ParamDecl("e",IntType()),ParamDecl("f",IntType())],VoidType(),Block([ForEach(Id("index"),Id("value"),Id("array"),Block([FuncCall("print",[StringLiteral("\"Range loop: index = \""),Id("item")]),ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<", Id("j"), IntLiteral(3)),Assign(Id("j"),BinaryOp("+", Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))),Block([FuncCall("print",[StringLiteral("\"Nested ICU loop inside range, j = \"")]),If(BinaryOp("==", Id("j"), IntLiteral(1)), Block([FuncCall("print",[StringLiteral("\"Value of j is 1\"")])]), None)])),FuncCall("print",[StringLiteral("\"End of one range iteration\"")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_func_13(self):
        input = """
            func processData() {
                if (x > 0) {
                    y := y + 1;
                } else if (x == 0) {
                    y := y - 1;
                } else if (x == 0) {
                    y := y - 1;
                } else if (x == 0) {
                    y := y - 1;
                } else if (x == 0) {
                    y := y - 1;
                } else {
                    y := 0;
                };
                return y;
            };

        """
        expect = str(Program([FuncDecl("processData",[],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([Assign(Id("y"),BinaryOp("+", Id("y"), IntLiteral(1)))]), If(BinaryOp("==", Id("x"), IntLiteral(0)), Block([Assign(Id("y"),BinaryOp("-", Id("y"), IntLiteral(1)))]), If(BinaryOp("==", Id("x"), IntLiteral(0)), Block([Assign(Id("y"),BinaryOp("-", Id("y"), IntLiteral(1)))]), If(BinaryOp("==", Id("x"), IntLiteral(0)), Block([Assign(Id("y"),BinaryOp("-", Id("y"), IntLiteral(1)))]), If(BinaryOp("==", Id("x"), IntLiteral(0)), Block([Assign(Id("y"),BinaryOp("-", Id("y"), IntLiteral(1)))]), Block([Assign(Id("y"),IntLiteral(0))])))))),Return(Id("y"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_func_14(self):
        input ="""
            func updateRecord(a,c,d int,e float) {
                record.field := 100;
                record["key"] += 50;
                return;
            };

        """
        expect = str(Program([FuncDecl("updateRecord",[ParamDecl("a",IntType()),ParamDecl("c",IntType()),ParamDecl("d",IntType()),ParamDecl("e",FloatType())],VoidType(),Block([Assign(FieldAccess(Id("record"),"field"),IntLiteral(100)),Assign(ArrayCell(Id("record"),[StringLiteral("\"key\"")]),BinaryOp("+", ArrayCell(Id("record"),[StringLiteral("\"key\"")]), IntLiteral(50))),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_func_15(self):
        input = """
            func abc() {
                if (x > 10) {} 
                if (x > 10) {
                    
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }

        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([]), None),If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([]), If(BinaryOp("==", Id("x"), IntLiteral(10)), Block([VarDecl("z",Id("str"), None)]), Block([VarDecl("z",Id("ID"), None)])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_func_16(self):
        input ="""
            func abc() {
                x  := foo() + 3 / 4;
                x.c[2][4].c[2][4].c[2][4].c[2][4] := 1 + 2;                       
                x.c[2][4].c[2][4].c[2][4].c[2][4][2][4][2][4][2][4][2][4] := 1 + 2;                       
            }                                       
        """
        expect = str(Program([FuncDecl("abc",[],VoidType(),Block([Assign(Id("x"),BinaryOp("+", FuncCall("foo",[]), BinaryOp("/", IntLiteral(3), IntLiteral(4)))),Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("x"),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4)]),BinaryOp("+", IntLiteral(1), IntLiteral(2))),Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("x"),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4)]),"c"),[IntLiteral(2),IntLiteral(4),IntLiteral(2),IntLiteral(4),IntLiteral(2),IntLiteral(4),IntLiteral(2),IntLiteral(4),IntLiteral(2),IntLiteral(4)]),BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_func_17(self):
        input = """
            func Add() {
                a[2].b := 2;       
            }
        """
        expect = str(Program([FuncDecl("Add",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),IntLiteral(2))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_struct_func_1(self):
        input = """
            type Student struct  {
                name string;
                age int;
                grade float64;
            };

            func (s Student) getName() string {
                return s.name;
            }

        """
        expect = str(Program([StructType("Student",[("name",StringType()),("age",IntType()),("grade",Id("float64"))],[]),
			MethodDecl("s",Id("Student"),FuncDecl("getName",[],StringType(),Block([Return(FieldAccess(Id("s"),"name"))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_struct_func_2(self):
        input = """
                func (p Person) Greet() string {
                    if (1) {return;
                    }else if (1) {}
                };  
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([If(IntLiteral(1), Block([Return(None)]), If(IntLiteral(1), Block([]), None))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_struct_func_3(self):
        input = """
                func (p Person) Greet() string {
                    for i := 0
                        i < 10
                        i += 1 {
                        return
                    }
                    for i := 0
                        i < 10
                        i += 1 {
                        return
                    }
                };  
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_struct_func_4(self):
        input = """
                func (p Person) Greet() string {
                    return true;
                    return false;
                    return;
                    return nil;
                    return Greet();
                };  
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BooleanLiteral(True)),Return(BooleanLiteral(False)),Return(None),Return(NilLiteral()),Return(FuncCall("Greet",[]))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_struct_func_5(self):
        input = """
                func (p Person) Greet() string {
                    var a TrieuMan = Person;
                    a[0] := 1;
                    a[1] += 2;
                    a[2] -= 3;
                    return a[0] + a[1] + a[2];
                };  
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([VarDecl("a",Id("TrieuMan"),Id("Person")),Assign(ArrayCell(Id("a"),[IntLiteral(0)]),IntLiteral(1)),Assign(ArrayCell(Id("a"),[IntLiteral(1)]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(1)]), IntLiteral(2))),Assign(ArrayCell(Id("a"),[IntLiteral(2)]),BinaryOp("-", ArrayCell(Id("a"),[IntLiteral(2)]), IntLiteral(3))),Return(BinaryOp("+", BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(0)]), ArrayCell(Id("a"),[IntLiteral(1)])), ArrayCell(Id("a"),[IntLiteral(2)])))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_struct_func_6(self):
        input = """
                func (p Person) Greet() string {
                    var a [2][3]int;
                    return a[0] + a[1] + a[2] + a[0] + a[1] + a[2];
                };  
        """
        expect =str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),Return(BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(0)]), ArrayCell(Id("a"),[IntLiteral(1)])), ArrayCell(Id("a"),[IntLiteral(2)])), ArrayCell(Id("a"),[IntLiteral(0)])), ArrayCell(Id("a"),[IntLiteral(1)])), ArrayCell(Id("a"),[IntLiteral(2)])))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_struct_func_7(self):
        input = """
                func (p Person) Greet() string {
                    var a [2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3][2][3]int;
                };  
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3),IntLiteral(2),IntLiteral(3)],IntType()), None)])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_interface_1(self):
        input = """
                type Calculator interface {
                                            
                    Add(x, y int) int;
                    Subtract(a, b float, c int) [3]ID;
                    Reset()
                                            
                    SayHello(name string);
                                            
                }                                                                      
        """
        expect = str(Program([InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType()),Prototype("Subtract",[FloatType(),FloatType(),IntType()],ArrayType([IntLiteral(3)],Id("ID"))),Prototype("Reset",[],VoidType()),Prototype("SayHello",[StringType()],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_interface_2(self):
        input = """
                type ID interface {
                                            
                    GetID() int;
                                            
                }                                                                      
        """
        expect = str(Program([InterfaceType("ID",[Prototype("GetID",[],IntType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_interface_3(self):
        input = """
                type Calculator interface {
                                            
                    Add(x, y int) int;
                    Subtract(a, b float, c int) [3]ID;
                    Reset()
                                            
                    SayHello(name string);
                                            
                };"""
        expect = str(Program([InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType()),Prototype("Subtract",[FloatType(),FloatType(),IntType()],ArrayType([IntLiteral(3)],Id("ID"))),Prototype("Reset",[],VoidType()),Prototype("SayHello",[StringType()],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_interface_4(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {foo();} 
            func foo(){return;}
            func  (Cat c) foo() [2]int {return;}
"""
        expect = str(
            Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("foo",[],VoidType())]),
			FuncDecl("foo",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_interface_5(self):
        input = """
            type trieuMan interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = str(Program([InterfaceType("trieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_interface_6(self):
        input = """
            type trieuMan interface {
                Add(a, c int, b int) [2]string;
                Subtract(a, b int) int;
            }
            """
        expect = str(Program([InterfaceType("trieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType())),Prototype("Subtract",[IntType(),IntType()],IntType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_interface_7(self):
        input = """
            type trieuMan interface {
                Add(a, c int, b int) [2][3][5][4][6][6][6]string;
                Subtract(a, b int, a, b int, a, b TrieuMan) float;
            }
            """
        expect = str(Program([InterfaceType("trieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(5),IntLiteral(4),IntLiteral(6),IntLiteral(6),IntLiteral(6)],StringType())),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),Id("TrieuMan"),Id("TrieuMan")],FloatType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_interface_8(self):
        input = """
            type trieuMan interface {
                Add(a, c int, b int) [2][3][5][4][6][6][6]string;
                Subtract(a, b int, a, b int, a, b TrieuMan) float;
            }
            type TrieuMan interface {
                Add(a, c int, b int) [2][3][5][4][6][6][6]string;
                Subtract(a, b int, a, b int, a, b TrieuMan) float;
            }
            type TrieuMan interface {
                Add(a, c int, b int) [2][3][5][4][6][6][6]string;
                Subtract(a, b int, a, b int, a, b TrieuMan) float;
            }
            type TrieuMan interface {
                Add(a, c int, b int) [2][3][5][4][6][6][6]string;
                Subtract(a, b int, a, b int, a, b TrieuMan) float;
            }
            """
        expect = str(Program([InterfaceType("trieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(5),IntLiteral(4),IntLiteral(6),IntLiteral(6),IntLiteral(6)],StringType())),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),Id("TrieuMan"),Id("TrieuMan")],FloatType())]),
			InterfaceType("TrieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(5),IntLiteral(4),IntLiteral(6),IntLiteral(6),IntLiteral(6)],StringType())),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),Id("TrieuMan"),Id("TrieuMan")],FloatType())]),
			InterfaceType("TrieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(5),IntLiteral(4),IntLiteral(6),IntLiteral(6),IntLiteral(6)],StringType())),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),Id("TrieuMan"),Id("TrieuMan")],FloatType())]),
			InterfaceType("TrieuMan",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(5),IntLiteral(4),IntLiteral(6),IntLiteral(6),IntLiteral(6)],StringType())),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),Id("TrieuMan"),Id("TrieuMan")],FloatType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_struct_type_1(self):
        input = """
            type Student struct {
                name string;
                age int;
            }
            """
        expect = str(Program([StructType("Student", [("name", StringType()), ("age", IntType())], [])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_struct_type_2(self):
        input = """
            type Student struct {
                name string;
                age int;
                marks [3][3][3]float64;
            }
            """
        expect = str(Program([StructType("Student",[("name",StringType()),("age",IntType()),("marks",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],Id("float64")))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_struct_type_3(self):
        input = """
            type Student struct {
                name string;
                age int;
                marks boolean;
                friends [tri]Student;
            }
"""
        expect = str(Program([StructType("Student",[("name",StringType()),("age",IntType()),("marks",BoolType()),("friends",ArrayType([Id("tri")],Id("Student")))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_struct_type_4(self):
        input = """
            type Student struct {
                name string;
                age int;
                marks [3][3][3]float64;
                friends [tri]Student;
            }
            type tri struct {
                man string;
            }
            """
        
        expect = str(Program([StructType("Student",[("name",StringType()),("age",IntType()),("marks",ArrayType([IntLiteral(3),IntLiteral(3),IntLiteral(3)],Id("float64"))),("friends",ArrayType([Id("tri")],Id("Student")))],[]),
			StructType("tri",[("man",StringType())],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_struct_type_5(self):
        input="""
            type ComplexStruct struct {
                id        int;
                name      string;
                scores    [3]float;         
                metadata  [2]string;        
                flags     [1]boolean;   
            };
"""
        expect = str(Program([StructType("ComplexStruct",[("id",IntType()),("name",StringType()),("scores",ArrayType([IntLiteral(3)],FloatType())),("metadata",ArrayType([IntLiteral(2)],StringType())),("flags",ArrayType([IntLiteral(1)],BoolType()))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_struct_type_6(self):
        input = """
                    type Person struct {
                        name   string;
                        age    int;
                        scores [3]float;
                    };
"""
        expect = str(Program([StructType("Person",[("name",StringType()),("age",IntType()),("scores",ArrayType([IntLiteral(3)],FloatType()))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_arraylit_1(self):
        input = """
            var messyArr = [3]int{100 ,200,300};
            """
        expect = str(Program([VarDecl("messyArr", None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(100),IntLiteral(200),IntLiteral(300)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_arraylit_2(self):
        input = """
            var messyArr = [3][2]int{{100 ,200},{300,400},{500,600}};
            """
        expect = str(Program([VarDecl("messyArr", None,ArrayLiteral([IntLiteral(3),IntLiteral(2)],IntType(),[[IntLiteral(100),IntLiteral(200)],[IntLiteral(300),IntLiteral(400)],[IntLiteral(500),IntLiteral(600)]]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_arraylit_3(self):
        input = """
            var holder DataHolder = DataHolder {
                values: [4]int { 10,20,30,40 },
                labels: [4]string { "one","two","three","four" }};
            """
        expect = str(Program([VarDecl("holder",Id("DataHolder"),StructLiteral("DataHolder",[("values",ArrayLiteral([IntLiteral(4)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30),IntLiteral(40)])),("labels",ArrayLiteral([IntLiteral(4)],StringType(),[StringLiteral("\"one\""),StringLiteral("\"two\""),StringLiteral("\"three\""),StringLiteral("\"four\"")]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_arraylit_4(self):
        input = """
            var nestedStrArr = [2][3]string {
                { "a", "b", "c" },
                { "d" , "e", "f" }};
            """
        expect = str(Program([VarDecl("nestedStrArr", None,ArrayLiteral([IntLiteral(2),IntLiteral(3)],StringType(),[[StringLiteral("\"a\""),StringLiteral("\"b\""),StringLiteral("\"c\"")],[StringLiteral("\"d\""),StringLiteral("\"e\""),StringLiteral("\"f\"")]]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_arraylit_5(self):
        input = """
            var holder DataHolder = DataHolder {
                values: [4]int { 10,20,30,40 },
                labels: [4]string { "one","two","three","four" }};
            """
        expect = str(Program([VarDecl("holder",Id("DataHolder"),StructLiteral("DataHolder",[("values",ArrayLiteral([IntLiteral(4)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30),IntLiteral(40)])),("labels",ArrayLiteral([IntLiteral(4)],StringType(),[StringLiteral("\"one\""),StringLiteral("\"two\""),StringLiteral("\"three\""),StringLiteral("\"four\"")]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_arraylit_6(self):
        input = """
            var mixedStructArr = [2]Person {  
                Person { name:"Charlie", age: 40, scores: [3]float { 95.0, 93.0, 97.0 } },
                Person { name:"Dana", age: 35, scores: [3]float { 88.0, 90.0, 85.0 } }};
            """
        expect = str(Program([VarDecl("mixedStructArr", None,ArrayLiteral([IntLiteral(2)],Id("Person"),[StructLiteral("Person",[("name",StringLiteral("\"Charlie\"")),("age",IntLiteral(40)),("scores",ArrayLiteral([IntLiteral(3)],FloatType(),[FloatLiteral(95.0),FloatLiteral(93.0),FloatLiteral(97.0)]))]),StructLiteral("Person",[("name",StringLiteral("\"Dana\"")),("age",IntLiteral(35)),("scores",ArrayLiteral([IntLiteral(3)],FloatType(),[FloatLiteral(88.0),FloatLiteral(90.0),FloatLiteral(85.0)]))])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_arraylit_7(self):
        input = """
            var deepNested = [2][1][2][2]string {
                {
                    {{ "w", "x" }, { "y", "z" }}},
                {
                    {{ "p", "q" }, { "r", "s" }}}};
            """
        expect = str(Program([VarDecl("deepNested", None,ArrayLiteral([IntLiteral(2),IntLiteral(1),IntLiteral(2),IntLiteral(2)],StringType(),[[[[StringLiteral("\"w\""),StringLiteral("\"x\"")],[StringLiteral("\"y\""),StringLiteral("\"z\"")]]],[[[StringLiteral("\"p\""),StringLiteral("\"q\"")],[StringLiteral("\"r\""),StringLiteral("\"s\"")]]]]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    
    def test_var_1(self):
        input = "var a = 10;"
        expect = str(Program([VarDecl("a", None, IntLiteral(10))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_var_2(self):
        input = "var b int = 20;"
        expect = str(Program([VarDecl("b", IntType(), IntLiteral(20))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_const_16(self):
        input = "const c = 30;"
        expect = str(Program([ConstDecl("c", None, IntLiteral(30))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_const_17(self):
        input = "const msg = \"Hello\";"
        expect = str(Program([ConstDecl("msg", None, StringLiteral("\"Hello\""))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_new_5(self):
        input = "func foo() { return; };"
        expect = str(Program([FuncDecl("foo", [], VoidType(), Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_new_6(self):
        input = "func bar(x int) int { return x; };"
        expect = str(Program([FuncDecl("bar",[ParamDecl("x",IntType())],IntType(),Block([Return(Id("x"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_new_7(self):
        input = "func add(a int, b int) int { return a + b; };"
        expect = str(Program([FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([Return(BinaryOp("+", Id("a"), Id("b")))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_new_8(self):
        input = """
            func createArray() [3]int {
                return [3]int { 1, 2, 3 };
            };
        """
        expect = str(Program([FuncDecl("createArray", [], ArrayType([IntLiteral(3)], IntType()), 
                            Block([Return(ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_new_9(self):
        input = """
            func caller() int {
                return add(5, 7);
            };
        """
        expect = str(Program([FuncDecl("caller", [], IntType(), 
                            Block([Return(FuncCall("add", [IntLiteral(5), IntLiteral(7)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_new_10(self):
        input = "var arr = [4]int { 10, 20, 30, 40 };"
        expect = str(Program([VarDecl("arr", None, ArrayLiteral([IntLiteral(4)], IntType(), 
                            [IntLiteral(10), IntLiteral(20), IntLiteral(30), IntLiteral(40)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_new_11(self):
        input = "var matrix = [2][2]int { {1,2}, {3,4} };"
        expect = str(Program([VarDecl("matrix", None, ArrayLiteral([IntLiteral(2), IntLiteral(2)], IntType(), 
                            [[IntLiteral(1), IntLiteral(2)], [IntLiteral(3), IntLiteral(4)]]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_new_12(self):
        input = """
            func check(x int) int {
                if (x > 0) {
                    return 1;
                } else {
                    return -1;
                }
            };
        """
        expect = str(Program([FuncDecl("check",[ParamDecl("x",IntType())],IntType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([Return(IntLiteral(1))]), Block([Return(UnaryOp("-",IntLiteral(1)))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_new_13(self):
        input = """
            func loopTest() int {
                for x < 10 {
                    x := x + 1;
                }
                return x;
            };
        """
        expect = str(Program([FuncDecl("loopTest",[],IntType(),Block([ForBasic(BinaryOp("<", Id("x"), IntLiteral(10)),Block([Assign(Id("x"),BinaryOp("+", Id("x"), IntLiteral(1)))])),Return(Id("x"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_new_14(self):
        input = """
            func icuLoop() int {
                for i := 0; i < 5; i := i + 1 {
                    print(i);
                }
                return 0;
            };
        """
        expect = str(Program([FuncDecl("icuLoop",[],IntType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(5)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([FuncCall("print",[Id("i")])])),Return(IntLiteral(0))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_new_15(self):
        input = """
            func rangeLoop() {
                for idx, val := range collection {
                    print(idx);
                    print(val);
                }
                return;
            };
        """
        expect = str(Program([FuncDecl("rangeLoop",[],VoidType(),Block([ForEach(Id("idx"),Id("val"),Id("collection"),Block([FuncCall("print",[Id("idx")]),FuncCall("print",[Id("val")])])),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_new_16(self):
        input = "var threeD = [2][2][2]int { {{1,2},{3,4}}, {{5,6},{7,8}} };"
        expect = str(Program([VarDecl("threeD", None, ArrayLiteral([IntLiteral(2), IntLiteral(2), IntLiteral(2)], IntType(), 
                            [[[IntLiteral(1), IntLiteral(2)], [IntLiteral(3), IntLiteral(4)]],
                             [[IntLiteral(5), IntLiteral(6)], [IntLiteral(7), IntLiteral(8)]]]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_new_17(self):
        input = "var result = 5 + 3 * 2 - 1;"
        expect = str(Program([VarDecl("result", None, 
                            BinaryOp("-", BinaryOp("+", IntLiteral(5), BinaryOp("*", IntLiteral(3), IntLiteral(2))), IntLiteral(1)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_new_18(self):
        input = """
            func compute(x int) int {
                var y = x * 2;
                var z int = y + 10;
                return z;
            };
        """
        expect = str(Program([FuncDecl("compute",[ParamDecl("x",IntType())],IntType(),Block([VarDecl("y", None,BinaryOp("*", Id("x"), IntLiteral(2))),VarDecl("z",IntType(),BinaryOp("+", Id("y"), IntLiteral(10))),Return(Id("z"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_new_19(self):
        input = """
            func process() int {
                return sumArray([3]int { 7,8,9 });
            };
        """
        expect = str(Program([FuncDecl("process", [], IntType(), Block([
                    Return(FuncCall("sumArray", [ArrayLiteral([IntLiteral(3)], IntType(), 
                                        [IntLiteral(7), IntLiteral(8), IntLiteral(9)])]))
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_new_20(self):
        input = "var initVal = getValue();"
        expect = str(Program([VarDecl("initVal", None, FuncCall("getValue", []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_new_21(self):
        input = """
            func constantTest() int {
                const pi = 314;
                return pi;
            };
        """
        expect = str(Program([FuncDecl("constantTest", [], IntType(), Block([
                    ConstDecl("pi", None, IntLiteral(314)),
                    Return(Id("pi"))
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_new_22(self):
        input = """
            func nestedIf() int {
                for i := 0; i < 3; i := i + 1 {
                    if (i == 1) {
                        return 100;
                    } else {
                        continue;
                    }
                }
                return 0;
            };
        """
        expect = str(Program([FuncDecl("nestedIf",[],IntType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(3)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([If(BinaryOp("==", Id("i"), IntLiteral(1)), Block([Return(IntLiteral(100))]), Block([Continue()]))])),Return(IntLiteral(0))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_new_23(self):
        input = """
            var names = [2][2]string { {"Alice", "Bob"}, {"Charlie", "Dana"} };
        """
        expect = str(Program([VarDecl("names", None, ArrayLiteral([IntLiteral(2), IntLiteral(2)], StringType(), 
                            [[StringLiteral("\"Alice\""), StringLiteral("\"Bob\"")],
                             [StringLiteral("\"Charlie\""), StringLiteral("\"Dana\"")]]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_new_24(self):
        input = """
            func update() {
                obj.field := 10;
                return;
            };
        """
        expect = str(Program([FuncDecl("update",[],VoidType(),Block([Assign(FieldAccess(Id("obj"),"field"),IntLiteral(10)),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_new_25(self):
        input = """
            var people = [2]Person {
                Person { name:"Eve", age:28, scores: [3]float {80.0,85.0,90.0} },
                Person { name:"Frank", age:33, scores: [3]float {75.0,80.0,82.0} }};
        """
        expect = str(Program([VarDecl("people", None,ArrayLiteral([IntLiteral(2)],Id("Person"),[StructLiteral("Person",[("name",StringLiteral("\"Eve\"")),("age",IntLiteral(28)),("scores",ArrayLiteral([IntLiteral(3)],FloatType(),[FloatLiteral(80.0),FloatLiteral(85.0),FloatLiteral(90.0)]))]),StructLiteral("Person",[("name",StringLiteral("\"Frank\"")),("age",IntLiteral(33)),("scores",ArrayLiteral([IntLiteral(3)],FloatType(),[FloatLiteral(75.0),FloatLiteral(80.0),FloatLiteral(82.0)]))])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_new_26(self):
        input = "func logMessage(msg string, level int) { print(msg); };"
        expect = str(Program([FuncDecl("logMessage",[ParamDecl("msg",StringType()),ParamDecl("level",IntType())],VoidType(),Block([FuncCall("print",[Id("msg")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_new_27(self):
        input = "var spaced = [3]int {  1 ,  2,3  };"
        expect = str(Program([VarDecl("spaced", None, ArrayLiteral([IntLiteral(3)], IntType(), 
                            [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_new_28(self):
        input = """
            func callMethod() {
                obj.print("Hello");
                return;
            };
        """
        expect = str(Program([FuncDecl("callMethod",[],VoidType(),Block([MethCall(Id("obj"),"print",[StringLiteral("\"Hello\"")]),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_new_29(self):
        input = """
            func computeLocal() int {
                var x = 5;
                var y = x * 10;
                return y;
            };
        """
        expect = str(Program([FuncDecl("computeLocal", [], IntType(), Block([
                    VarDecl("x", None, IntLiteral(5)),
                    VarDecl("y", None, BinaryOp("*", Id("x"), IntLiteral(10))),
                    Return(Id("y"))
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_new_30(self):
        input = "var arr = getArray();"
        expect = str(Program([VarDecl("arr", None, FuncCall("getArray", []))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_new_31(self):
        input = """
            func loopCall() {
                for i := 0; i < 2; i := i + 1 {
                    obj.obj.obj.obj.obj.obj.obj.process();
                }
                return;
            };
        """
        expect = str(Program([FuncDecl("loopCall",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(2)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([MethCall(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("obj"),"obj"),"obj"),"obj"),"obj"),"obj"),"obj"),"process",[])])),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_new_32(self):
        input = """
            var mixedArr = [2][3][2]int { 
                { {1,2}, {3,4}, {5,6} },
                { {7,8}, {9,10}, {11,12} }};
        """
        expect = str(Program([VarDecl("mixedArr", None, ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(2)], IntType(), [
                    [[IntLiteral(1), IntLiteral(2)], [IntLiteral(3), IntLiteral(4)], [IntLiteral(5), IntLiteral(6)]],
                    [[IntLiteral(7), IntLiteral(8)], [IntLiteral(9), IntLiteral(10)], [IntLiteral(11), IntLiteral(12)]]
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_new_33(self):
        input = "func processArr(arr [3]int) int { return arr[0]; };"
        expect = str(Program([FuncDecl("processArr",[ParamDecl("arr",ArrayType([IntLiteral(3)],IntType()))],IntType(),Block([Return(ArrayCell(Id("arr"),[IntLiteral(0)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_new_34(self):
        input = "var emptyArr = [0]int{abcabc};"
        expect = str(Program([VarDecl("emptyArr", None,ArrayLiteral([IntLiteral(0)],IntType(),[Id("abcabc")]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_new_35(self):
        input = "func factorial(n int) int { if (n == 0) { return 1; }; return n * factorial(n - 1); };"
        expect = str(Program([FuncDecl("factorial",[ParamDecl("n",IntType())],IntType(),Block([If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([Return(IntLiteral(1))]), None),Return(BinaryOp("*", Id("n"), FuncCall("factorial",[BinaryOp("-", Id("n"), IntLiteral(1))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_new_36(self):
        input = """
            var multiline = [4]string {
                "one",
                "two",
                "three",
                "four"};
        """
        expect = str(Program([VarDecl("multiline", None, ArrayLiteral([IntLiteral(4)], StringType(), 
                            [StringLiteral("\"one\""), StringLiteral("\"two\""), StringLiteral("\"three\""), StringLiteral("\"four\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_new_37(self):
        input = """
            func testCall() {
                const msg = "Hi";
                obj.log(msg);
                return;
            };
        """
        expect = str(Program([FuncDecl("testCall",[],VoidType(),Block([ConstDecl("msg",None,StringLiteral("\"Hi\"")),MethCall(Id("obj"),"log",[Id("msg")]),Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
