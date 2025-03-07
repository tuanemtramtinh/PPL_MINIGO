import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const Thanh_Tu = x + b;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BinaryOp("+", Id("x"), Id("b")))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 301))
    def test_002(self):
        input = """const Thanh_Tu = 1;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 302))
    def test_003(self):
        input = """const Thanh_Tu = 0b11;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,IntLiteral("0b11"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))
    def test_004(self):
        input = """const Thanh_Tu = 0o70;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,IntLiteral("0o70"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))
    def test_005(self):
        input = """const Thanh_Tu = 0Xa1;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,IntLiteral("0Xa1"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))
    def test_006(self):
        input = """const Thanh_Tu = 01.e-1;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,FloatLiteral("01.e-1"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))
    def test_007(self):
        input = """const Thanh_Tu = true;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))
    def test_008(self):
        input = """const Thanh_Tu = false;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))
    def test_009(self):
        input = """const Thanh_Tu = "Thanh Tu dep trai";"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,StringLiteral("\"Thanh Tu dep trai\""))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))
    def test_010(self):
        input = """const Thanh_Tu = nil;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,NilLiteral())]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))
    def test_011(self):
        input = """const Thanh_Tu = STRUCT {
            a : 1,
            b : false};"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))
    def test_012(self):
        input = """const Thanh_Tu = [ID] int {1};"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))
    def test_013(self):
        input = """const Thanh_Tu = [1][2] int {1., STRUCT{}, nil};"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral("1."),StructLiteral("STRUCT",[]),NilLiteral()]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))
    def test_014(self):
        input = """const Thanh_Tu = [1][2] STRUCT {{1, {3}}, {2}};"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1),[IntLiteral(3)]],[IntLiteral(2)]]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 314))
    def test_015(self):
        input = """const Thanh_Tu = d || e || p || t || r || a || i;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BinaryOp("||", BinaryOp("||", BinaryOp("||", BinaryOp("||", BinaryOp("||", BinaryOp("||", Id("d"), Id("e")), Id("p")), Id("t")), Id("r")), Id("a")), Id("i")))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))
    def test_016(self):
        input = """const Thanh_Tu = h >= e <= h > e < h == e != h;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", Id("h"), Id("e")), Id("h")), Id("e")), Id("h")), Id("e")), Id("h")))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))
    def test_017(self):
        input = """const Thanh_Tu = 1 * 2 / 3 % 4;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))
    def test_018(self):
        input = """const Thanh_Tu = ! - 1;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,UnaryOp("!",UnaryOp("-",IntLiteral(1))))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))
    def test_019(self):
        input = """const Thanh_Tu = !gay + sieu_dep_trai;"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,BinaryOp("+", UnaryOp("!",Id("gay")), Id("sieu_dep_trai")))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))
    def test_020(self):
        input = """const Thanh_Tu = sieu(dep_trai);"""
        expect = str(Program([ConstDecl("Thanh_Tu",None,FuncCall("sieu",[Id("dep_trai")]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))
    def test_021(self):
        input = """var Thanh_Tu int = 0b1010;"""
        expect = str(Program([VarDecl("Thanh_Tu",IntType(),IntLiteral("0b1010"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))
    def test_022(self):
        input = """var Thanh_Tu string = [2][3] int{{1,0,4}, {1,3,4}};"""
        expect = str(Program([VarDecl("Thanh_Tu",StringType(),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(0),IntLiteral(4)],[IntLiteral(1),IntLiteral(3),IntLiteral(4)]]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))
    def test_023(self):
        input = """var Thanh_Tu = a.b.c.d(a.c.b[2].d(a,b,c));"""
        expect = str(Program([VarDecl("Thanh_Tu", None,MethCall(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d",[MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"c"),"b"),[IntLiteral(2)]),"d",[Id("a"),Id("b"),Id("c")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))
    def test_024(self):
        input = """var Thanh_Tu = foo(a.b(b,c), [num][num] int {{1,2,3}, {4,5,6}, {7,8,9}});"""
        expect = str(Program([VarDecl("Thanh_Tu", None,FuncCall("foo",[MethCall(Id("a"),"b",[Id("b"),Id("c")]),ArrayLiteral([Id("num"),Id("num")],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)],[IntLiteral(7),IntLiteral(8),IntLiteral(9)]])]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))
    def test_025(self):
        input = """var Thanh_Tu = call(sir, 3.14e18, "hehe");"""
        expect = str(Program([VarDecl("Thanh_Tu", None,FuncCall("call",[Id("sir"),FloatLiteral("3.14e18"),StringLiteral("\"hehe\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))
    def test_026(self):
        input = """var Thanh_Tu = call(call(call(call(call(call(call(call(call(call(call(call())))))))))));"""
        expect = str(Program([VarDecl("Thanh_Tu", None,FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[FuncCall("call",[])])])])])])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 326))
    def test_027(self):
        input = """var Thanh_Tu [he][he] ID;"""
        expect = str(Program([VarDecl("Thanh_Tu",ArrayType([Id("he"),Id("he")],Id("ID")), None)]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))
    def test_028(self):
        input = """var Thanh_Tu Thanh_Tu;"""
        expect = str(Program([VarDecl("Thanh_Tu",Id("Thanh_Tu"), None)]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))
    def test_029(self):
        input = """var Thanh_Tu = 1 + 2 + 3 + false + true * !ID / abc % 10;"""
        expect = str(Program([VarDecl("Thanh_Tu", None,BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BooleanLiteral(False)), BinaryOp("%", BinaryOp("/", BinaryOp("*", BooleanLiteral(True), UnaryOp("!",Id("ID"))), Id("abc")), IntLiteral(10))))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))
    def test_030(self):
        input = """var Thanh_Tu = call.hehe.haha.hihi;"""
        expect = str(Program([VarDecl("Thanh_Tu", None,FieldAccess(FieldAccess(FieldAccess(Id("call"),"hehe"),"haha"),"hihi"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))
    def test_031(self):
        input = """type abc struct 
                {
                    abc xyz;
                    he he;
                    x int;
                    y string;
                    z float;
                    t [1][2][3] int;
                };"""
        expect = str(Program([StructType("abc",[("abc",Id("xyz")),("he",Id("he")),("x",IntType()),("y",StringType()),("z",FloatType()),("t",ArrayType([IntLiteral(1),IntLiteral(2),IntLiteral(3)],IntType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))
    def test_032(self):
        input = """    type ID struct {
        a int;
        b ID;
        c [2]int;
    };"""
        expect = str(Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))
    def test_033(self):
        input = """func foo (a, b int , d , e float) int {const a = b; b := a + b + c / d;}
    func foo (e string) int {var a = 1;}
    func foo (g float) [2] ID {var a = 1;}
    """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("d",FloatType()),ParamDecl("e",FloatType())],IntType(),Block([ConstDecl("a",None,Id("b")),Assign(Id("b"),BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), BinaryOp("/", Id("c"), Id("d"))))])),
			FuncDecl("foo",[ParamDecl("e",StringType())],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("g",FloatType())],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))
    def test_034(self):
        input = """func foo(x int){
            var thanhtu string = a([2]int{a}).b([2]int{d});
        }
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("x",IntType())],VoidType(),Block([VarDecl("thanhtu",StringType(),MethCall(FuncCall("a",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"b",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("d")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))
    def test_035(self):
        input = """
        func thanhtu(){
            a[1][2][3].c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.d.d.d.d.d.d.d.a[2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4].e.e.e.e.e.e.e.e.e.e.e.e.e.e := a[1][2][3].c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.c.d.d.d.d.d.d.d.a[2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4][2][3][4].e.e.e.e.e.e.e.e.e.e.e.e.e.e
        }
        """
        expect = str(Program([FuncDecl("thanhtu",[],VoidType(),Block([Assign(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"d"),"d"),"d"),"d"),"d"),"d"),"d"),"a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"c"),"d"),"d"),"d"),"d"),"d"),"d"),"d"),"a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"),"e"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))
    def test_036(self):
        input = """func hehe(a,b int, c,d float){
        }
        """
        expect = str(Program([FuncDecl("hehe",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",FloatType()),ParamDecl("d",FloatType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336))
    def test_037(self):
        input = """func recursive(a int){
                if (a > 0){
                    return 1;
                }else{
                    return 1 + recursive(a - 1);
                }
        }
        """
        expect = str(Program([FuncDecl("recursive",[ParamDecl("a",IntType())],VoidType(),Block([If(BinaryOp(">", Id("a"), IntLiteral(0)), Block([Return(IntLiteral(1))]), Block([Return(BinaryOp("+", IntLiteral(1), FuncCall("recursive",[BinaryOp("-", Id("a"), IntLiteral(1))])))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))
    def test_038(self):
        input = """func sum(a, b int){
            return a + b;
        }
        """
        expect = str(Program([FuncDecl("sum",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(BinaryOp("+", Id("a"), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))
    def test_039(self):
        input = """func minus(a, b int){
            return a - b;
        }
        """
        expect = str(Program([FuncDecl("minus",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(BinaryOp("-", Id("a"), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))
    def test_040(self):
        input = """func mul(a,b int){
            return a * b;
        }
        """
        expect = str(Program([FuncDecl("mul",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(BinaryOp("*", Id("a"), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))
    def test_041(self):
        input = """func div(a,b int){
            return a / b;
        }
        """
        expect = str(Program([FuncDecl("div",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(BinaryOp("/", Id("a"), Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))
    def test_042(self):
        input = """func mod(a,b int){
            return a % b;
        }
        """
        expect = Program([FuncDecl("mod",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(BinaryOp("%", Id("a"), Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))
    def test_043(self):
        input = """func printFunction(a int){
            for var i int = 0; i <= a; i += 1 {
                print(i);
            }

        }
        """
        expect = str(Program([FuncDecl("printFunction",[ParamDecl("a",IntType())],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(0)),BinaryOp("<=", Id("i"), Id("a")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([FuncCall("print",[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))
    def test_044(self):
        input = """func changeTempature (a int) int {
            return a / 3.6e0;
        }
        """
        expect = str(Program([FuncDecl("changeTempature",[ParamDecl("a",IntType())],IntType(),Block([Return(BinaryOp("/", Id("a"), FloatLiteral("3.6e0")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))
    def test_045(self):
        input = """func BinarySearch (target int, array [count] int) int {
            if (target > array[count / 2]){
                return BinarySearch(target, array[count / 2]);
            } else if (target < array[count / 2]){
                return BinarySearch(target, array[0]);
            } else {
                return count;
            }
        }
        """
        expect = str(Program([FuncDecl("BinarySearch",[ParamDecl("target",IntType()),ParamDecl("array",ArrayType([Id("count")],IntType()))],IntType(),Block([If(BinaryOp(">", Id("target"), ArrayCell(Id("array"),[BinaryOp("/", Id("count"), IntLiteral(2))])), Block([Return(FuncCall("BinarySearch",[Id("target"),ArrayCell(Id("array"),[BinaryOp("/", Id("count"), IntLiteral(2))])]))]), If(BinaryOp("<", Id("target"), ArrayCell(Id("array"),[BinaryOp("/", Id("count"), IntLiteral(2))])), Block([Return(FuncCall("BinarySearch",[Id("target"),ArrayCell(Id("array"),[IntLiteral(0)])]))]), Block([Return(Id("count"))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))
    def test_046(self):
        input = """type Calc interface {
                Add(a, c int, b int) [2]string;
            }
            """
        expect = str(Program([InterfaceType("Calc",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))
    def test_047(self):
        input = """
            func foo(){
                a["s"][foo()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
            """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))
    def test_048(self):
        input = """func findPrime(number int) boolean{
            for var i int = 1; i <= sqrt(number); i += 1 {
                if(number % i == 0){
                    break;
                    return false;
                }
            }
            return true;
        }
        """
        expect = str(Program([FuncDecl("findPrime",[ParamDecl("number",IntType())],BoolType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<=", Id("i"), FuncCall("sqrt",[Id("number")])),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([If(BinaryOp("==", BinaryOp("%", Id("number"), Id("i")), IntLiteral(0)), Block([Break(),Return(BooleanLiteral(False))]), None)])),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    def test_049(self):
        input = """
            func foo(){
                break;
                continue;
            } 
            """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    def test_050(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 
            } 
            """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([Return(IntLiteral(1))]), If(IntLiteral(2), Block([Return(IntLiteral(2))]), If(IntLiteral(3), Block([Return(IntLiteral(3))]), If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
    def test_051(self):
        input = """const a = a * (nil - "a");"""
        expect = str(Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("\"a\""))))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))
    def test_052(self):
        input = """func test(talk string){
            print("Com nuoc gi chua nguoi dep");
        }
        """
        expect = str(Program([FuncDecl("test",[ParamDecl("talk",StringType())],VoidType(),Block([FuncCall("print",[StringLiteral("\"Com nuoc gi chua nguoi dep\"")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))
    def test_053(self):
        input = """func coding(){
            execute("make a millionaire code plan");
            execute("make a plan");
            execute("find suitable technology");
            execute("design architecture of the app");
            execute("design SQL database");
            execute("type SQL queries into SQL database");
            execute("set up project");
            execute("create a git repository");
            execute("start coding hello world");
            execute("has bug");
            execute("fix for 2 hour");
            execute("give up");
            coding();
        }
        """
        expect = str(Program([FuncDecl("coding",[],VoidType(),Block([
            FuncCall("execute",[StringLiteral("\"make a millionaire code plan\"")]),
            FuncCall("execute",[StringLiteral("\"make a plan\"")]),
            FuncCall("execute",[StringLiteral("\"find suitable technology\"")]),
            FuncCall("execute",[StringLiteral("\"design architecture of the app\"")]),
            FuncCall("execute",[StringLiteral("\"design SQL database\"")]),
            FuncCall("execute",[StringLiteral("\"type SQL queries into SQL database\"")]),
            FuncCall("execute",[StringLiteral("\"set up project\"")]),
            FuncCall("execute",[StringLiteral("\"create a git repository\"")]),
            FuncCall("execute",[StringLiteral("\"start coding hello world\"")]),
            FuncCall("execute",[StringLiteral("\"has bug\"")]),
            FuncCall("execute",[StringLiteral("\"fix for 2 hour\"")]),
            FuncCall("execute",[StringLiteral("\"give up\"")]),
            FuncCall("coding",[])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))
    def test_054(self):
        input = """func foo(a [2]ID) {return;}
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))
    
    def test_055(self):
        input = """func life_of_gacha_player() {
            execute("download gacha game");
            execute("see waifu");
            execute("hold for waifu");
            execute("waifu's banner release");
            execute("75 roll but still nothing");
            execute("high hope about back to back");
            execute("80th roll, miss rate");
            execute("delete game");
            life_of_gacha_player();
        }
        """
        expect = str(Program([FuncDecl("life_of_gacha_player",[],VoidType(),Block([
            FuncCall("execute",[StringLiteral("\"download gacha game\"")]),
            FuncCall("execute",[StringLiteral("\"see waifu\"")]),
            FuncCall("execute",[StringLiteral("\"hold for waifu\"")]),
            FuncCall("execute",[StringLiteral("\"waifu's banner release\"")]),
            FuncCall("execute",[StringLiteral("\"75 roll but still nothing\"")]),
            FuncCall("execute",[StringLiteral("\"high hope about back to back\"")]),
            FuncCall("execute",[StringLiteral("\"80th roll, miss rate\"")]),
            FuncCall("execute",[StringLiteral("\"delete game\"")]),
            FuncCall("life_of_gacha_player",[])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))
    
    def test_056(self):
        input = """type person struct {
            name string;
            dob string;
            age int;
            yoe int;
            job string;
            address string;
        }
        """
        expect = str(Program([StructType("person",[("name",StringType()),("dob",StringType()),("age",IntType()),("yoe",IntType()),("job",StringType()),("address",StringType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    
    def test_057(self):
        input = """const a = a.b.c.d.e(hehe);"""
        expect = str(Program([ConstDecl("a",None,MethCall(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e",[Id("hehe")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    
    def test_058(self):
        input = """const a = ID {}.a[2].e(huhu);"""
        expect = str(Program([ConstDecl("a",None,MethCall(ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]),"e",[Id("huhu")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    
    def test_059(self):
        input = """const a = f() + f(1 + 2, 3.e-6);"""
        expect = str(Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral("3.e-6")])))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    
    def test_060(self):
        input = """var i boolean = true;"""
        expect = str(Program([VarDecl("i",BoolType(),BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    def test_061(self):
        input = """var i boolean = false;"""
        expect = str(Program([VarDecl("i",BoolType(),BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "361"))
    
    def test_062(self):
        input = """const thanh = "thanhtu";"""
        expect = str(Program([ConstDecl("thanh",None,StringLiteral("\"thanhtu\""))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "362"))
    
    def test_063(self):
        input = """
            type ID struct {
                a int;
                b ID;
                c [2]int;
            }
        """
        expect = str(Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "363"))
    
    def test_064(self):
        input = """
            func foo () {var a = 1;}
            func foo () int {var a = 1;}
            func foo () [2] ID {var a = 1;}
        """
        expect = str(Program([
            FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
            FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
            FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "364"))
    
    def test_065(self):
        input = """
            func foo (a int) {var a = 1;}
            func foo (a int, b ID) {var a = 1;}
            func foo (a, b int) {var a = 1;}
        """
        expect = str(Program([
            FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
            FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
            FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "365"))
    def test_066(self):
        input = """
            func (ID ID) foo (a int) {var a = 1;}
            func (ID ID) foo (a int, b ID) {var a = 1;}
            func (ID ID) foo (a, b int) {var a = 1;}
        """
        expect = str(Program([
            MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
            MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
            MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "366"))
    
    def test_067(self):
        input = """
            type INTERFACE interface {
                foo();
                foo() int;
                foo() [2]ID;
                foo(a int);
                foo(a int, b int);
                foo(a, b int);
            }
        """
        expect = str(Program([
            InterfaceType("INTERFACE",[
                Prototype("foo",[],VoidType()),
                Prototype("foo",[],IntType()),
                Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
                Prototype("foo",[IntType()],VoidType()),
                Prototype("foo",[IntType(),IntType()],VoidType()),
                Prototype("foo",[IntType(),IntType()],VoidType())]
            )]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "367"))
    
    def test_068(self):
        input = """
            const a = true + false - true;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "368"))
    
    def test_069(self):
        input = """
            const a = 1 - 2 % 3;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "369"))
    
    def test_070(self):
        input = """
            const a = 1 + -2 - 1;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "370"))
    def test_071(self):
        input = """
            const a = [1]ID{ThanhTu{}};
        """
        expect = str(Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("ThanhTu",[])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "371"))
    
    def test_072(self):
        input = """
            const a = [1][3]float{1.};
        """
        expect = str(Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral("1.")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "372"))
    
    def test_073(self):
        input = """
            const a = ID{a: 1, b: true};
        """
        expect = str(Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "373"))
    
    def test_074(self):
        input = """
            const a = ID{a: [1]int{1}};
        """
        expect = str(Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "374"))
    
    def test_075(self):
        input = """
            const a = ID{b: true};
        """
        expect = str(Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "375"))
    
    def test_076(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "376"))
    
    def test_077(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "377"))
    
    def test_078(self):
        input = """
            const a = 1 >= 2 + 3;
        """
        expect = str(Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "378"))
    
    def test_079(self):
        input = """
            const a = a[1][2][3][4];
        """
        expect = str(Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "379"))
    
    def test_080(self):
        input = """
            const a = a[1 + 2];
        """
        expect = str(Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "380"))
    def test_081(self):
        input = """const a = a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a(a()))))))))))))))))))))));"""
        expect = str(Program([ConstDecl("a",None,FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[FuncCall("a",[])])])])])])])])])])])])])])])])])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "381"))
    
    def test_082(self):
        input = """const a = a.a.a.a.a.a.a.aa.a.a.a.aa.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a;"""
        expect = str(Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"a"),"a"),"a"),"a"),"a"),"a"),"aa"),"a"),"a"),"a"),"aa"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "382"))
    
    def test_083(self):
        input = """
            func thanhtu() {
                for index, value := range array[2] {return;}
            }
        """
        expect = str(Program([FuncDecl("thanhtu",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "383"))
    def test_084(self):
        input = """
            func thanhtu() {
                foo(1, 2 + 3 + 9);
                a[2].foo(1,3);
            }
        """
        expect = str(Program([FuncDecl("thanhtu",[],VoidType(),Block([
            FuncCall("foo",[IntLiteral(1),BinaryOp("+", BinaryOp("+", IntLiteral(2), IntLiteral(3)), IntLiteral(9))]),
            MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "384"))
    
    def test_085(self):
        input = """
            func thanhtu() {
                a += 1 + 8 - 10 / !true + 1.e-18;
            }
        """
        expect = str(Program([FuncDecl("thanhtu",[],VoidType(),Block([
            Assign(Id("a"),BinaryOp("+", Id("a"), BinaryOp("+", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(8)), BinaryOp("/", IntLiteral(10), UnaryOp("!",BooleanLiteral(True)))), FloatLiteral("1.e-18"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "385"))
    
    def test_086(self):
        input = """
            type calculate interface {
                Add(x, y int) int;
                Sub(x, y int) int;
                Mul(x, y int) int;
                Div(x, y int) int;
                Mod(x, y int) int;
            }
        """
        expect = str(Program([InterfaceType("calculate",[
            Prototype("Add",[IntType(),IntType()],IntType()),
            Prototype("Sub",[IntType(),IntType()],IntType()),
            Prototype("Mul",[IntType(),IntType()],IntType()),
            Prototype("Div",[IntType(),IntType()],IntType()),
            Prototype("Mod",[IntType(),IntType()],IntType())
        ])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "386"))
    
    def test_087(self):
        input = """
            type thanhtu struct {
                a int;
                b float;
                c string;
                d [2][3] int;
                e boolean;
            }
        """
        expect = str(Program([StructType("thanhtu",[
            ("a",IntType()),
            ("b",FloatType()),
            ("c",StringType()),
            ("d",ArrayType([IntLiteral(2),IntLiteral(3)],IntType())),
            ("e",BoolType())
        ],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "387"))
    def test_088(self):
        input = """
            type thanhtu struct {
                a ID;
            }
        """
        expect = str(Program([StructType("thanhtu",[("a",Id("ID"))],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "388"))
    
    def test_089(self):
        input = """
            type INTERFACE interface {
                foo();
                foo() int;
                foo() [2]ID;
                foo(a int);
                foo(a int, b int);
                foo(a, b int);
            }
        """
        expect = str(Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),
            Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())
        ])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "389"))
    
    def test_090(self):
        input = """
            func foo () {
                continue;
                break;
                return;
                return 1;
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Continue(),
            Break(),
            Return(None),
            Return(IntLiteral(1))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "390"))
    
    def test_091(self):
        input = """
            func foo () {
                a[1] := 2;
                a[2][1+1] += 3;
                a.b -= 5;
                b.b[a + b].b.c[2] := 4;
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "391"))
    
    def test_092(self):
        input = """
            func foo () {
                a();
                a(1, 2);
                a(1);
                b.a.a();
                b.a.a(1, 2);
                b.a.a(1);
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "392"))
    
    def test_093(self):
        input = """
            func foo () {
                if (a) {return;}
                if (b) {return;} else {return;}
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "393"))
    
    def test_094(self):
        input = """
            func foo () {
                return a[2][3][4];
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "394"))
    
    def test_095(self):
        input = """
            func foo () {
                a.b[2][3][4] := 1;
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "395"))
    def test_096(self):
        input = """
            func foo () {
                a[1*2][1+2] := a[1*2][1+2];
                a[1+2] := a[1+2];
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "396"))
    
    def test_097(self):
        input = """const thanhtu = foo( a * (1+2) ); """
        expect = str(Program([ConstDecl("thanhtu",None,FuncCall("foo",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "397"))
    
    def test_098(self):
        input = """const thanhtu = foo( a(),b.a(2, 3) ); """
        expect = str(Program([ConstDecl("thanhtu",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "398"))
    
    def test_099(self):
        input = """const thanhtu = foo( [1]int{1}, [1][1]int{2} ); """
        expect = str(Program([ConstDecl("thanhtu",None,FuncCall("foo",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "399"))
    
    def test_100(self):
        input = """
            func (thanhtu v) foo(thanhtu int) {return;}
        """
        expect = str(Program([MethodDecl("thanhtu",Id("v"),FuncDecl("foo",[ParamDecl("thanhtu",IntType())],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, "400"))