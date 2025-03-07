import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """
            const pear = "khanh_pear";
    """
        expect = str(Program([ConstDecl("pear",None,StringLiteral("\"khanh_pear\""))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_002(self):
        input = """
            const khanh_pear = true;
    """
        expect = str(Program([ConstDecl("khanh_pear",None,BooleanLiteral(True))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_003(self):
        input = """
            const pear = fruit(2, 3.5, \"mammam\", true, false)
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("fruit",[IntLiteral(2),FloatLiteral(3.5),StringLiteral("\"mammam\""),BooleanLiteral(True),BooleanLiteral(False)]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_004(self):
        input = """
            const pear = chickeN(1 + 2 * 3 % 4 || 1000 / 3.14);
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("chickeN",[BinaryOp("||", BinaryOp("+", IntLiteral(1), BinaryOp("%", BinaryOp("*", IntLiteral(2), IntLiteral(3)), IntLiteral(4))), BinaryOp("/", IntLiteral(1000), FloatLiteral(3.14)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_005(self):
        input = """
            const pear = chickeN(cock(123), arr[2][ID]);
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("chickeN",[FuncCall("cock",[IntLiteral(123)]),ArrayCell(Id("arr"),[IntLiteral(2),Id("ID")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_006(self):
        input = """
            const pear = Hihi[2][3].haha.huhu();
    """
        expect = str(Program([ConstDecl("pear",None,MethCall(FieldAccess(ArrayCell(Id("Hihi"),[IntLiteral(2),IntLiteral(3)]),"haha"),"huhu",[]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_007(self):
        input = """
            const pear = pear() + peach[2][a.b[2]] + 5*and(u || v);
    """
        expect = str(Program([ConstDecl("pear",None,BinaryOp("+", BinaryOp("+", FuncCall("pear",[]), ArrayCell(Id("peach"),[IntLiteral(2),ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)])])), BinaryOp("*", IntLiteral(5), FuncCall("and",[BinaryOp("||", Id("u"), Id("v"))]))))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_008(self):
        input = """
            const pear = PearLe(Fruit {a: 1, b: 2, c: \"hihi\"});
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("PearLe",[StructLiteral("Fruit",[("a",IntLiteral(1)),("b",IntLiteral(2)),("c",StringLiteral("\"hihi\""))])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_009(self):
        input = """
            const pear = fruit([1]int{byebye}, [2][4]float{24});
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("fruit",[ArrayLiteral([IntLiteral(1)],IntType(),[Id("byebye")]),ArrayLiteral([IntLiteral(2),IntLiteral(4)],FloatType(),[IntLiteral(24)])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_010(self):
        input = """
            const pear = fruit([2][5]string{2, {1, 3}, {{5, 5.11}, 1, 3.5}});
    """
        expect = str(Program([ConstDecl("pear",None,FuncCall("fruit",[ArrayLiteral([IntLiteral(2),IntLiteral(5)],StringType(),[IntLiteral(2),[IntLiteral(1),IntLiteral(3)],[[IntLiteral(5),FloatLiteral(5.11)],IntLiteral(1),FloatLiteral(3.5)]])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_011(self):
        input = """
            var apple = [ID][NAME]string{\"drogod\"};
            const pear = a.b.c.d.e.f[1].g(2);
            var banana = a.b.c.d.e.f[1].g(2) && apple;
    """
        expect = str(Program([VarDecl("apple", None,ArrayLiteral([Id("ID"),Id("NAME")],StringType(),[StringLiteral("\"drogod\"")])),
			ConstDecl("pear",None,MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),[IntLiteral(1)]),"g",[IntLiteral(2)])),
			VarDecl("banana", None,BinaryOp("&&", MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),[IntLiteral(1)]),"g",[IntLiteral(2)]), Id("apple")))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_012(self):
        input = """
            func pear() int {return;}
    """
        expect = str(Program([FuncDecl("pear",[],IntType(),Block([Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_013(self):
        input = """
            func pear(a int) {return;}
            func pear(a string, b boolean) {return;}
            func pear(a, b, c float, d , e string) {return;}
    """
        expect = str(Program([FuncDecl("pear",[ParamDecl("a",IntType())],VoidType(),Block([Return(None)])),
			FuncDecl("pear",[ParamDecl("a",StringType()),ParamDecl("b",BoolType())],VoidType(),Block([Return(None)])),
			FuncDecl("pear",[ParamDecl("a",FloatType()),ParamDecl("b",FloatType()),ParamDecl("c",FloatType()),ParamDecl("d",StringType()),ParamDecl("e",StringType())],VoidType(),Block([Return(None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_014(self):
        input = """
            func pear(a int) {var a = a + b;}
    """
        expect = str(Program([FuncDecl("pear",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,BinaryOp("+", Id("a"), Id("b")))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_015(self):
        input = """
            var khanhPear = a[pear1(1, 2) + a.b.c[2]][a.b.c.pear2(x,y,z)];
    """
        expect = str(Program([VarDecl("khanhPear", None,ArrayCell(Id("a"),[BinaryOp("+", FuncCall("pear1",[IntLiteral(1),IntLiteral(2)]), ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)])),MethCall(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"pear2",[Id("x"),Id("y"),Id("z")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_016(self):
        input = """
            type Fruit struct {
                a int;
                b float;
                c hihi;
            }
    """
        expect = str(Program([StructType("Fruit",[("a",IntType()),("b",FloatType()),("c",Id("hihi"))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_017(self):
        input = """
            type PearLe interface {
                Go(x, y int) float;
                Stop();
            }
    """
        expect = str(Program([InterfaceType("PearLe",[Prototype("Go",[IntType(),IntType()],FloatType()),Prototype("Stop",[],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_018(self):
        input = """
            const ambaturine = 0 <= 1 <= 2;
            var coconut = 1 > 2 < 3 >= 4 <=5 == 6;
            type PearLe interface {
                Go(x, y coconut) float;
                ambaturine();
            }
    """
        expect = str(Program([ConstDecl("ambaturine",None,BinaryOp("<=", BinaryOp("<=", IntLiteral(0), IntLiteral(1)), IntLiteral(2))),
			VarDecl("coconut", None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6))),
			InterfaceType("PearLe",[Prototype("Go",[Id("coconut"),Id("coconut")],FloatType()),Prototype("ambaturine",[],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_019(self):
        input = """
            func (seed s) mango(a , b int) {return seeds;};
    """
        expect = str(Program([MethodDecl("seed",Id("s"),FuncDecl("mango",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(Id("seeds"))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_020(self):
        input = """
            func (ripe p) banana(a , b int, c why) {return a.a.a.a.a.a.a.a[1][2][3][4][5][6];}
            func (seed s) mango(a , b int) {return a[1].b.c()[2].d.e();}
    """
        expect = str(Program([MethodDecl("ripe",Id("p"),FuncDecl("banana",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",Id("why"))],VoidType(),Block([Return(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"a"),"a"),"a"),"a"),"a"),"a"),"a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))),
			MethodDecl("seed",Id("s"),FuncDecl("mango",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    
    def test_021(self):
        input = """
            func fruit(a int, b string){
                var hello = [2][3]int{{2, 3},{{\"string\"}}};
            }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",StringType())],VoidType(),Block([VarDecl("hello", None,ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(2),IntLiteral(3)],[[StringLiteral("\"string\"")]]]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_022(self):
        input = """
            func votien() {
                a += 1;
                b -= banana;
                c *= hihi[2] || trump * 5;
                d := hsr[2][3][D[go][go]];
            }
    """
        expect = str(Program([FuncDecl("votien",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("b"),BinaryOp("-", Id("b"), Id("banana"))),Assign(Id("c"),BinaryOp("*", Id("c"), BinaryOp("||", ArrayCell(Id("hihi"),[IntLiteral(2)]), BinaryOp("*", Id("trump"), IntLiteral(5))))),Assign(Id("d"),ArrayCell(Id("hsr"),[IntLiteral(2),IntLiteral(3),ArrayCell(Id("D"),[Id("go"),Id("go")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_023(self):
        input = """
            func fruity() {
                a += 1;
                b -= banana;
                c *= hihi[2] || trump * 5;
                d := hsr[2][3][D[go][go]];
            }
    """
        expect = str(Program([FuncDecl("fruity",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("b"),BinaryOp("-", Id("b"), Id("banana"))),Assign(Id("c"),BinaryOp("*", Id("c"), BinaryOp("||", ArrayCell(Id("hihi"),[IntLiteral(2)]), BinaryOp("*", Id("trump"), IntLiteral(5))))),Assign(Id("d"),ArrayCell(Id("hsr"),[IntLiteral(2),IntLiteral(3),ArrayCell(Id("D"),[Id("go"),Id("go")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_024(self):
        input = """
        func lofiiiii() {
            fruit(1, 2);
            a[2].fruit(1, 3);
            a[2].fruit.hello(1);
        }
    """
        expect = str(Program([FuncDecl("lofiiiii",[],VoidType(),Block([FuncCall("fruit",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"fruit",[IntLiteral(1),IntLiteral(3)]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"fruit"),"hello",[IntLiteral(1)])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_025(self):
        input = """
        func lofiiiii(a int, b string) {
            a["s"][foo()] := a[2][2][3];
            a[2] := a[3][4];
            b.c.a[2] := b.c.a[2];
            b.c.a[2][3] := b.c.a[2][3];
        }
    """
        expect = str(Program([FuncDecl("lofiiiii",[ParamDecl("a",IntType()),ParamDecl("b",StringType())],VoidType(),Block([Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_026(self):
        input = """
            var a int = [2][2]int{{1, true}, {\"hello\", 3.14e21}};
            const b = a.b.c.d.e.g.f.g.h.i.j.k.l.m.n;
    """
        expect = str(Program([VarDecl("a",IntType(),ArrayLiteral([IntLiteral(2),IntLiteral(2)],IntType(),[[IntLiteral(1),BooleanLiteral(True)],[StringLiteral("\"hello\""),FloatLiteral("3.14e21")]])),
			ConstDecl("b",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"g"),"f"),"g"),"h"),"i"),"j"),"k"),"l"),"m"),"n"))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_027(self):
        input = """
            type gogogo interface {
                fruit();
                fruit(a int) int;
                fruit(b int, c float) [2]ID;
                fruit(a int);
                fruit(a int, b int);
                fruit(a, b int, c float);
            }
    """
        expect = str(Program([InterfaceType("gogogo",[Prototype("fruit",[],VoidType()),Prototype("fruit",[IntType()],IntType()),Prototype("fruit",[IntType(),FloatType()],ArrayType([IntLiteral(2)],Id("ID"))),Prototype("fruit",[IntType()],VoidType()),Prototype("fruit",[IntType(),IntType()],VoidType()),Prototype("fruit",[IntType(),IntType(),FloatType()],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_028(self):
        input = """
            func foo () {
                continue;
                break;
                return;
                return 1;
            }
    """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_029(self):
        input = """
            func fruit () {
                if (a) {return;}
            }
    """
        expect = str(Program([FuncDecl("fruit",[],VoidType(),Block([If(Id("a"), Block([Return(None)]), None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))


    def test_030(self):
        input = """
        
            func fruit () {
                if (a) {return;
                } else{
                    continue;
                    return fruit(2,3,\"true\",3.45e-11);
                }
            }
    """
        expect = str(Program([FuncDecl("fruit",[],VoidType(),Block([If(Id("a"), Block([Return(None)]), Block([Continue(),Return(FuncCall("fruit",[IntLiteral(2),IntLiteral(3),StringLiteral("\"true\""),FloatLiteral("3.45e-11")]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_031(self):
        input = """
        
        func fruit (a, b int) {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([If(Id("a"), Block([Return(None)]), None),If(Id("b"), Block([Return(None)]), Block([Return(None)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_032(self):
        input = """
        
        func fruit (a, b int) {
            if (a) {return;}
            if (b >= fruit) {return;}
            if (game <= heino) {return;}
            if (damedane == !MA) {return;}
            if (tuai) {return outgroup();} else {return nauxoi();}
        }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([If(Id("a"), Block([Return(None)]), None),If(BinaryOp(">=", Id("b"), Id("fruit")), Block([Return(None)]), None),If(BinaryOp("<=", Id("game"), Id("heino")), Block([Return(None)]), None),If(BinaryOp("==", Id("damedane"), UnaryOp("!",Id("MA"))), Block([Return(None)]), None),If(Id("tuai"), Block([Return(FuncCall("outgroup",[]))]), Block([Return(FuncCall("nauxoi",[]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_033(self):
        input = """
        func fruit (a, b in, k float) {
            if (1){return a;} else if (2){return b[2];} else if (3){return c - d;} else {break;}
            if (1){return true;} else if (2){return false;} else if (3){continue;}
        }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",Id("in")),ParamDecl("b",Id("in")),ParamDecl("k",FloatType())],VoidType(),Block([If(IntLiteral(1), Block([Return(Id("a"))]), If(IntLiteral(2), Block([Return(ArrayCell(Id("b"),[IntLiteral(2)]))]), If(IntLiteral(3), Block([Return(BinaryOp("-", Id("c"), Id("d")))]), Block([Break()])))),If(IntLiteral(1), Block([Return(BooleanLiteral(True))]), If(IntLiteral(2), Block([Return(BooleanLiteral(False))]), If(IntLiteral(3), Block([Continue()]), None)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_034(self):
        input = """
        
        func fruit () {
            a();
            a(1, 2);
            a.b(1);
            b.a[5][1].a();
            b.a.a[2] := a[1][3];
            a[1+1][5*6%8] := fruit(2, arr[2]);
        }

    """
        expect = str(Program([FuncDecl("fruit",[],VoidType(),Block([FuncCall("a",[]),FuncCall("a",[IntLiteral(1),IntLiteral(2)]),MethCall(Id("a"),"b",[IntLiteral(1)]),MethCall(ArrayCell(FieldAccess(Id("b"),"a"),[IntLiteral(5),IntLiteral(1)]),"a",[]),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"a"),"a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1)),BinaryOp("%", BinaryOp("*", IntLiteral(5), IntLiteral(6)), IntLiteral(8))]),FuncCall("fruit",[IntLiteral(2),ArrayCell(Id("arr"),[IntLiteral(2)])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_035(self):
        input = """
        
        func efruit(x int) {
            if (x > 0) { 
                if (x % 2 == 0) { return x * 2; } else { return x + 1; }
            } else { return 0; }
        }

    """
        expect = str(Program([FuncDecl("efruit",[ParamDecl("x",IntType())],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([If(BinaryOp("==", BinaryOp("%", Id("x"), IntLiteral(2)), IntLiteral(0)), Block([Return(BinaryOp("*", Id("x"), IntLiteral(2)))]), Block([Return(BinaryOp("+", Id("x"), IntLiteral(1)))]))]), Block([Return(IntLiteral(0))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    
    def test_036(self):
        input = """
        
        func fruit(x int) {
            if (x > 0) { return x; }else { return -x; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType())],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([Return(Id("x"))]), Block([Return(UnaryOp("-", Id("x")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_037(self):
        input = """
        
        func fruit(x int) {
            if (x > 0) { 
                if (x % 2 == 0) { return x * 2; }else { return x + 1; }
            }else { return 0; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType())],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([If(BinaryOp("==", BinaryOp("%", Id("x"), IntLiteral(2)), IntLiteral(0)), Block([Return(BinaryOp("*", Id("x"), IntLiteral(2)))]), Block([Return(BinaryOp("+", Id("x"), IntLiteral(1)))]))]), Block([Return(IntLiteral(0))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_038(self):
        input = """
        
        func fruit(x int) {
            if (x > 10) { return 100; }else if (x > 5) { return 50; }else { return 0; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType())],VoidType(),Block([If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([Return(IntLiteral(100))]), If(BinaryOp(">", Id("x"), IntLiteral(5)), Block([Return(IntLiteral(50))]), Block([Return(IntLiteral(0))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_039(self):
        input = """
        
        func fruit(a int, b int) {
            if (a > 0 && b > 0) { return a + b; }else if (a < 0 || b < 0) { return a * b; }else { return 0; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()), ParamDecl("b",IntType())],VoidType(),Block([If(BinaryOp("&&", BinaryOp(">", Id("a"), IntLiteral(0)), BinaryOp(">", Id("b"), IntLiteral(0))), Block([Return(BinaryOp("+", Id("a"), Id("b")))]), If(BinaryOp("||", BinaryOp("<", Id("a"), IntLiteral(0)), BinaryOp("<", Id("b"), IntLiteral(0))), Block([Return(BinaryOp("*", Id("a"), Id("b")))]), Block([Return(IntLiteral(0))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_040(self):
        input = """
        
        func fruit(flag boolean) {
            if (flag) { return "Yes"; }else { return "No"; }
        }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("flag",BoolType())],VoidType(),Block([If(Id("flag"), Block([Return(StringLiteral("\"Yes\""))]), Block([Return(StringLiteral("\"No\""))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_041(self):
        input = """
        
        func fruit(a int, b int) {
            if (a + b > 10) { return a * b; }else if (a - b < 5) { return a / b; }else { return a % b; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([If(BinaryOp(">", BinaryOp("+", Id("a"), Id("b")), IntLiteral(10)), Block([Return(BinaryOp("*", Id("a"), Id("b")))]), If(BinaryOp("<", BinaryOp("-", Id("a"), Id("b")), IntLiteral(5)), Block([Return(BinaryOp("/", Id("a"), Id("b")))]), Block([Return(BinaryOp("%", Id("a"), Id("b")))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_042(self):
        input = """
        
        func fruit(x int, y int) {
            if ((x * y) % 2 == 0) { return x - y; }else if ((x + y) / 2 > 5) { return x + y; 
            }else { return x * y; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],VoidType(),Block([If(BinaryOp("==", BinaryOp("%", BinaryOp("*", Id("x"), Id("y")), IntLiteral(2)), IntLiteral(0)), Block([Return(BinaryOp("-", Id("x"), Id("y")))]), If(BinaryOp(">", BinaryOp("/", BinaryOp("+", Id("x"), Id("y")), IntLiteral(2)), IntLiteral(5)), Block([Return(BinaryOp("+", Id("x"), Id("y")))]), Block([Return(BinaryOp("*", Id("x"), Id("y")))])))]))
		]))

        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_043(self):
        input = """
        func fruit(arr [10]int, idx int) {
            if (arr[idx] > 0) { return arr[idx] * 2; 
            }else if (arr[idx - 1] < 0) { return arr[idx - 1] + 5; 
            }else { return arr[idx] / 2;}
        }
    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(10)],IntType())),ParamDecl("idx",IntType())],VoidType(),Block([If(BinaryOp(">", ArrayCell(Id("arr"),[Id("idx")]), IntLiteral(0)), Block([Return(BinaryOp("*", ArrayCell(Id("arr"),[Id("idx")]), IntLiteral(2)))]), If(BinaryOp("<", ArrayCell(Id("arr"),[BinaryOp("-", Id("idx"), IntLiteral(1))]), IntLiteral(0)), Block([Return(BinaryOp("+", ArrayCell(Id("arr"),[BinaryOp("-", Id("idx"), IntLiteral(1))]), IntLiteral(5)))]), Block([Return(BinaryOp("/", ArrayCell(Id("arr"),[Id("idx")]), IntLiteral(2)))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_044(self):
        input = """
        
        func fruit(a int, b int, c int) {
            if (a * b - c > 10) { return a + c; 
            }else if (b / c < 3) { return b * c; 
            }else { return a - b; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",IntType())],VoidType(),Block([If(BinaryOp(">", BinaryOp("-", BinaryOp("*", Id("a"), Id("b")), Id("c")), IntLiteral(10)), Block([Return(BinaryOp("+", Id("a"), Id("c")))]), If(BinaryOp("<", BinaryOp("/", Id("b"), Id("c")), IntLiteral(3)), Block([Return(BinaryOp("*", Id("b"), Id("c")))]), Block([Return(BinaryOp("-", Id("a"), Id("b")))])))]))
    ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_045(self):
        input = """
        
        func fruit(a ID, b ID) {
            if (a.value > b.value) { return a; 
            }else if (b.value >= 10) { return haha(); 
            }else if (b.value == 10) { return huhu(); 
            }else if (b.value +  arr[2] != 10) { return tri(); 
            }else { return a.b.fruit(); }
        }

        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",Id("ID")),ParamDecl("b",Id("ID"))],VoidType(),Block([If(BinaryOp(">", FieldAccess(Id("a"),"value"), FieldAccess(Id("b"),"value")), Block([Return(Id("a"))]), If(BinaryOp(">=", FieldAccess(Id("b"),"value"), IntLiteral(10)), Block([Return(FuncCall("haha",[]))]), If(BinaryOp("==", FieldAccess(Id("b"),"value"), IntLiteral(10)), Block([Return(FuncCall("huhu",[]))]), If(BinaryOp("!=", BinaryOp("+", FieldAccess(Id("b"),"value"), ArrayCell(Id("arr"),[IntLiteral(2)])), IntLiteral(10)), Block([Return(FuncCall("tri",[]))]), Block([Return(MethCall(FieldAccess(Id("a"),"b"),"fruit",[]))])))))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_046(self):
        input = """
        
        func fruit(arr [5][2]ID, index int) {
            if (arr[index].value > 0) { return arr[index]; 
            }else if (arr[index - 1].value < 0) { return arr[index - 1]; 
            }else { return arr[0]; }
        }

        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(5),IntLiteral(2)],Id("ID"))),ParamDecl("index",IntType())],VoidType(),Block([If(BinaryOp(">", FieldAccess(ArrayCell(Id("arr"),[Id("index")]),"value"), IntLiteral(0)), Block([Return(ArrayCell(Id("arr"),[Id("index")]))]), If(BinaryOp("<", FieldAccess(ArrayCell(Id("arr"),[BinaryOp("-", Id("index"), IntLiteral(1))]),"value"), IntLiteral(0)), Block([Return(ArrayCell(Id("arr"),[BinaryOp("-", Id("index"), IntLiteral(1))]))]), Block([Return(ArrayCell(Id("arr"),[IntLiteral(0)]))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_047(self):
        input = """
        
        func fruit(a float, b float) {
            if (a / b > 2.5) { return a * b; 
            }else if (b - a < 1.5) { return a + b; 
            }else { return a - b; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",FloatType()),ParamDecl("b",FloatType())],VoidType(),Block([If(BinaryOp(">", BinaryOp("/", Id("a"), Id("b")), FloatLiteral(2.5)), Block([Return(BinaryOp("*", Id("a"), Id("b")))]), If(BinaryOp("<", BinaryOp("-", Id("b"), Id("a")), FloatLiteral(1.5)), Block([Return(BinaryOp("+", Id("a"), Id("b")))]), Block([Return(BinaryOp("-", Id("a"), Id("b")))])))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_048(self):
        input = """
        
        func fruit(a int, b int, c int) {
            if ((a + b) * c > 20) { 
                return a - b; 
            }else if ((b - c) / 2 < 5) {
              return c; 
            }else { return a * b * c; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",IntType())],VoidType(),Block([If(BinaryOp(">", BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), Id("c")), IntLiteral(20)), Block([Return(BinaryOp("-", Id("a"), Id("b")))]), If(BinaryOp("<", BinaryOp("/", BinaryOp("-", Id("b"), Id("c")), IntLiteral(2)), IntLiteral(5)), Block([Return(Id("c"))]), Block([Return(BinaryOp("*", BinaryOp("*", Id("a"), Id("b")), Id("c")))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_049(self):
        input = """
        
        func fruit(x int, y int, arr [10]int) {
            if (arr[x] + arr[y] > 100) { return arr[x] * 2; 
            }else if (arr[x - 1] < arr[y + 1]) { return arr[y] - arr[x]; 
            }else { return arr[0]; }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("arr",ArrayType([IntLiteral(10)],IntType()))],VoidType(),Block([If(BinaryOp(">", BinaryOp("+", ArrayCell(Id("arr"),[Id("x")]), ArrayCell(Id("arr"),[Id("y")])), IntLiteral(100)), Block([Return(BinaryOp("*", ArrayCell(Id("arr"),[Id("x")]), IntLiteral(2)))]), If(BinaryOp("<", ArrayCell(Id("arr"),[BinaryOp("-", Id("x"), IntLiteral(1))]), ArrayCell(Id("arr"),[BinaryOp("+", Id("y"), IntLiteral(1))])), Block([Return(BinaryOp("-", ArrayCell(Id("arr"),[Id("y")]), ArrayCell(Id("arr"),[Id("x")])))]), Block([Return(ArrayCell(Id("arr"),[IntLiteral(0)]))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_050(self):
        input = """
        
        func fruit(a ID, b ID, arr [5][kaka]ID) {
            if (a.value + b.value > 50) { return a; }else if (arr[2].value < 10) { return arr[2]; }else { return b.b.fruit(); }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",Id("ID")),ParamDecl("b",Id("ID")),ParamDecl("arr",ArrayType([IntLiteral(5),Id("kaka")],Id("ID")))],VoidType(),Block([If(BinaryOp(">", BinaryOp("+", FieldAccess(Id("a"),"value"), FieldAccess(Id("b"),"value")), IntLiteral(50)), Block([Return(Id("a"))]), If(BinaryOp("<", FieldAccess(ArrayCell(Id("arr"),[IntLiteral(2)]),"value"), IntLiteral(10)), Block([Return(ArrayCell(Id("arr"),[IntLiteral(2)]))]), Block([Return(MethCall(FieldAccess(Id("b"),"b"),"fruit",[]))])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_051(self):
        input = """
        
        func fruit(arr [10]ID) {
            for arr[i] < 10 {
                return;
                return 1;
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(10)],Id("ID")))],VoidType(),Block([ForBasic(BinaryOp("<", ArrayCell(Id("arr"),[Id("i")]), IntLiteral(10)),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_052(self):
            input = """
            
            func fruit(n int) {
                for i := 0; i < n; i += 2 {
                    return;
                    return 1;
                }
            }

        """
            expect = str(Program([FuncDecl("fruit",[ParamDecl("n",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), Id("n")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(2))),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
            self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_053(self):
            input = """
            
            func fruit(arr ID) {
                for i, value := range arr {
                    return;
                    return 1;
                }
            }

        """
            expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",Id("ID"))],VoidType(),Block([ForEach(Id("i"),Id("value"),Id("arr"),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
            self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_054(self):
            input = """
            
            func fruit(a int) {
                for i := a + 1; i[0] <= 20; i -= 3 {
                    return;
                    return 1;
                }
            }

        """
            expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<=", ArrayCell(Id("i"),[IntLiteral(0)]), IntLiteral(20)),Assign(Id("i"),BinaryOp("-", Id("i"), IntLiteral(3))),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
            self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_055(self):
            input = """
            
            func fruit(arr [3][MAGAMING]ID) {
                for arr[i + 1] {
                    return;
                    return 1;
                }
            }

        """
            expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(3),Id("MAGAMING")],Id("ID")))],VoidType(),Block([ForBasic(ArrayCell(Id("arr"),[BinaryOp("+", Id("i"), IntLiteral(1))]),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
            self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_056(self):
        input = """
        
        func fruit(arr [10]ID, x int) {
            for arr[x * 2 + 1] < (x + 5) * 3 {
                return;
                return arr[x - 1];
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(10)],Id("ID"))),ParamDecl("x",IntType())],VoidType(),Block([ForBasic(BinaryOp("<", ArrayCell(Id("arr"),[BinaryOp("+", BinaryOp("*", Id("x"), IntLiteral(2)), IntLiteral(1))]), BinaryOp("*", BinaryOp("+", Id("x"), IntLiteral(5)), IntLiteral(3))),Block([Return(None),Return(ArrayCell(Id("arr"),[BinaryOp("-", Id("x"), IntLiteral(1))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))


    def test_057(self):
        input = """
        
        func fruit(n int, step int) {
            for i := n / 2; i[step % 3] > n - 1; i += step * 2 - 1 {
                return;
                return n * step;
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("n",IntType()),ParamDecl("step",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),BinaryOp("/", Id("n"), IntLiteral(2))),BinaryOp(">", ArrayCell(Id("i"),[BinaryOp("%", Id("step"), IntLiteral(3))]), BinaryOp("-", Id("n"), IntLiteral(1))),Assign(Id("i"),BinaryOp("+", Id("i"), BinaryOp("-", BinaryOp("*", Id("step"), IntLiteral(2)), IntLiteral(1)))),Block([Return(None),Return(BinaryOp("*", Id("n"), Id("step")))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_058(self):
        input = """
        
        func fruit(a, b ID) {
            for index, value := range b[a.id % 2] {
                return;
                return value * index;
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",Id("ID")),ParamDecl("b",Id("ID"))],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("b"),[BinaryOp("%", FieldAccess(Id("a"),"id"), IntLiteral(2))]),Block([Return(None),Return(BinaryOp("*", Id("value"), Id("index")))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_059(self):
        input = """
        
        func fruit(a int, arr [ID]ID) {
            for i := a + 2; i[1] * 2 < arr[3] + a; i -= arr[a % 2] * 3 {
                return;
                return i[2] + arr[a];
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("arr",ArrayType([Id("ID")],Id("ID")))],VoidType(),Block([ForStep(Assign(Id("i"),BinaryOp("+", Id("a"), IntLiteral(2))),BinaryOp("<", BinaryOp("*", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(2)), BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(3)]), Id("a"))),Assign(Id("i"),BinaryOp("-", Id("i"), BinaryOp("*", ArrayCell(Id("arr"),[BinaryOp("%", Id("a"), IntLiteral(2))]), IntLiteral(3)))),Block([Return(None),Return(BinaryOp("+", ArrayCell(Id("i"),[IntLiteral(2)]), ArrayCell(Id("arr"),[Id("a")])))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_060(self):
        input = """
        
        func fruit(arr [6][n]ID, x int, y int) {
            for arr[x + y] {
                return;
                return arr[(x * 2) % y];
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([IntLiteral(6),Id("n")],Id("ID"))),ParamDecl("x",IntType()),ParamDecl("y",IntType())],VoidType(),Block([ForBasic(ArrayCell(Id("arr"),[BinaryOp("+", Id("x"), Id("y"))]),Block([Return(None),Return(ArrayCell(Id("arr"),[BinaryOp("%", BinaryOp("*", Id("x"), IntLiteral(2)), Id("y"))]))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_061(self):
        input = """
        
        func fruit(arr ID, x int) {
            for i := x * 2; i[1] < arr[5] + x; i += arr[x % 3] {
                if (arr[i % 2] > x) {
                    return arr[i / 2];
                } else if (x * 3 < arr[i % 4]) {
                    return arr[i] + x;
                } else {
                    return 0;
                }
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",Id("ID")),ParamDecl("x",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),BinaryOp("*", Id("x"), IntLiteral(2))),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(5)]), Id("x"))),Assign(Id("i"),BinaryOp("+", Id("i"), ArrayCell(Id("arr"),[BinaryOp("%", Id("x"), IntLiteral(3))]))),Block([If(BinaryOp(">", ArrayCell(Id("arr"),[BinaryOp("%", Id("i"), IntLiteral(2))]), Id("x")), Block([Return(ArrayCell(Id("arr"),[BinaryOp("/", Id("i"), IntLiteral(2))]))]), If(BinaryOp("<", BinaryOp("*", Id("x"), IntLiteral(3)), ArrayCell(Id("arr"),[BinaryOp("%", Id("i"), IntLiteral(4))])), Block([Return(BinaryOp("+", ArrayCell(Id("arr"),[Id("i")]), Id("x")))]), Block([Return(IntLiteral(0))])))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_062(self):
        input = """
        
        func fruit(n int, arr, eng ID) {
            for arr[n * 2 + 1] {
                if (arr[2] * n > 10) {
                    return arr[n];
                } else {
                    for i := 0; i[2] < 5; i += n / 2 {
                        return i * arr[n % 2];
                    }
                }
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("n",IntType()),ParamDecl("arr",Id("ID")),ParamDecl("eng",Id("ID"))],VoidType(),Block([ForBasic(ArrayCell(Id("arr"),[BinaryOp("+", BinaryOp("*", Id("n"), IntLiteral(2)), IntLiteral(1))]),Block([If(BinaryOp(">", BinaryOp("*", ArrayCell(Id("arr"),[IntLiteral(2)]), Id("n")), IntLiteral(10)), Block([Return(ArrayCell(Id("arr"),[Id("n")]))]), Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(2)]), IntLiteral(5)),Assign(Id("i"),BinaryOp("+", Id("i"), BinaryOp("/", Id("n"), IntLiteral(2)))),Block([Return(BinaryOp("*", Id("i"), ArrayCell(Id("arr"),[BinaryOp("%", Id("n"), IntLiteral(2))])))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_063(self):
        input = """
        
        func fruit(a int, b float, arr ID) {
            for i := a; i[1] > b; i -= arr[b % 2] {
                if (i % 2 == 0) {
                    return arr[i];
                } else {
                    if (b * 3 < arr[a % 3]) {
                        return arr[b / 2];
                    } else {
                        return arr[a - 1];
                    }
                }
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",FloatType()),ParamDecl("arr",Id("ID"))],VoidType(),Block([ForStep(Assign(Id("i"),Id("a")),BinaryOp(">", ArrayCell(Id("i"),[IntLiteral(1)]), Id("b")),Assign(Id("i"),BinaryOp("-", Id("i"), ArrayCell(Id("arr"),[BinaryOp("%", Id("b"), IntLiteral(2))]))),Block([If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), Block([Return(ArrayCell(Id("arr"),[Id("i")]))]), Block([If(BinaryOp("<", BinaryOp("*", Id("b"), IntLiteral(3)), ArrayCell(Id("arr"),[BinaryOp("%", Id("a"), IntLiteral(3))])), Block([Return(ArrayCell(Id("arr"),[BinaryOp("/", Id("b"), IntLiteral(2))]))]), Block([Return(ArrayCell(Id("arr"),[BinaryOp("-", Id("a"), IntLiteral(1))]))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_064(self):
        input = """
        
        func fruit(x int, y int) {
            for index, value := range [3]int{x, y, {x, arr}} {
                if (index % 2 == 0) {
                    return value * 2;
                } else if (value + index > 10) {
                    return value - 3;
                } else {
                    return 1;
                }
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(3)],IntType(),[Id("x"),Id("y"),[Id("x"),Id("arr")]]),Block([If(BinaryOp("==", BinaryOp("%", Id("index"), IntLiteral(2)), IntLiteral(0)), Block([Return(BinaryOp("*", Id("value"), IntLiteral(2)))]), If(BinaryOp(">", BinaryOp("+", Id("value"), Id("index")), IntLiteral(10)), Block([Return(BinaryOp("-", Id("value"), IntLiteral(3)))]), Block([Return(IntLiteral(1))])))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_065(self):
        input = """
        
        func fruit(arr ID, n int) {
            for i := 0; i[2] < arr[n % 3] * 2; i += n - 1 {
                if (arr[i] * n > 10) {
                    return arr[i];
                } else {
                    for j := 1; j[1] < n; j *= 2 {
                        if (j % 3 == 0) {
                            return arr[j];
                        } else {
                            return 0;
                        }
                    }
                }
            }
        }

    """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",Id("ID")),ParamDecl("n",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(2)]), BinaryOp("*", ArrayCell(Id("arr"),[BinaryOp("%", Id("n"), IntLiteral(3))]), IntLiteral(2))),Assign(Id("i"),BinaryOp("+", Id("i"), BinaryOp("-", Id("n"), IntLiteral(1)))),Block([If(BinaryOp(">", BinaryOp("*", ArrayCell(Id("arr"),[Id("i")]), Id("n")), IntLiteral(10)), Block([Return(ArrayCell(Id("arr"),[Id("i")]))]), Block([ForStep(Assign(Id("j"),IntLiteral(1)),BinaryOp("<", ArrayCell(Id("j"),[IntLiteral(1)]), Id("n")),Assign(Id("j"),BinaryOp("*", Id("j"), IntLiteral(2))),Block([If(BinaryOp("==", BinaryOp("%", Id("j"), IntLiteral(3)), IntLiteral(0)), Block([Return(ArrayCell(Id("arr"),[Id("j")]))]), Block([Return(IntLiteral(0))]))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_066(self):
        input = """
        const arr = [4]float{1.2, 3.4, 5.6, 7.8};
        """
        expect = str(Program([ConstDecl("arr",None,ArrayLiteral([IntLiteral(4)],FloatType(),[FloatLiteral(1.2),FloatLiteral(3.4),FloatLiteral(5.6),FloatLiteral(7.8)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_067(self):
        input = """
        const matrix = [2][3]int{{1, 2, 3}, {4, 5, 6}};
        """
        expect = str(Program([ConstDecl("matrix",None,ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_068(self):
        input = """
        var colors COLOR = [3]string{"red", "green", "blue"};
        """
        expect = str(Program([VarDecl("colors",Id("COLOR"),ArrayLiteral([IntLiteral(3)],StringType(),[StringLiteral("\"red\""),StringLiteral("\"green\""),StringLiteral("\"blue\"")]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_069(self):
        input = """
        var points = [2][2]float{{1.1, 2.2}, {3.3, 4.4}};
        """
        expect = str(Program([VarDecl("points", None,ArrayLiteral([IntLiteral(2),IntLiteral(2)],FloatType(),[[FloatLiteral(1.1),FloatLiteral(2.2)],[FloatLiteral(3.3),FloatLiteral(4.4)]]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_070(self):
        input = """
        const data = [5]boolean{true, false, true, false, true};
        """
        expect = str(Program([ConstDecl("data",None,ArrayLiteral([IntLiteral(5)],BoolType(),[BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_071(self):
        input = """
        const person = Person{name: \"Alice\", age: 25}
        """
        expect = str(Program([ConstDecl("person",None,StructLiteral("Person",[("name",StringLiteral("\"Alice\"")),("age",IntLiteral(25))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_072(self):
        input = """
        var emptyPerson hello = Person{}
        """
        expect = str(Program([VarDecl("emptyPerson",Id("hello"),StructLiteral("Person",[]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_073(self):
        input = """
        const rectangle = Shape{width: 10.5, height: 20.3}
        """
        expect = str(Program([ConstDecl("rectangle",None,StructLiteral("Shape",[("width",FloatLiteral(10.5)),("height",FloatLiteral(20.3))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_074(self):
        input = """
        const book = Book{title: \"Programming 101\", pages: 300, price: 29.99}
        """
        expect = str(Program([ConstDecl("book",None,StructLiteral("Book",[("title",StringLiteral("\"Programming 101\"")),("pages",IntLiteral(300)),("price",FloatLiteral(29.99))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_075(self):
        input = """
        var car = Car{brand: "Toyota", year: 2022, electric: false}
        """
        expect = str(Program([VarDecl("car", None,StructLiteral("Car",[("brand",StringLiteral("\"Toyota\"")),("year",IntLiteral(2022)),("electric",BooleanLiteral(False))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_076(self):
        input = """
        type khanhpear struct {
            name string;
            age int;
        }
        """
        expect = str(Program([StructType("khanhpear",[("name",StringType()),("age",IntType())],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_077(self):
        input = """
        type khanhpear struct {
            brand string;
            year int;
            electric boolean;
        }
        """
        expect = str(Program([StructType("khanhpear",[("brand",StringType()),("year",IntType()),("electric",BoolType())],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_078(self):
        input = """
        type khanhpear struct {
            x float;
            y float;
        }
        
        type khanhpear struct {
            topLeft khanhpear;
            bottomRight khanhpear;
        }
        """
        expect = str(Program([StructType("khanhpear",[("x",FloatType()),("y",FloatType())],[]),
			StructType("khanhpear",[("topLeft",Id("khanhpear")),("bottomRight",Id("khanhpear"))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_079(self):
        input = """
        type khanhpear struct {
            id string;
            name string;
            position string;
            salary float;
        }
        
        type khanhpear struct {
            name string;
            manager khanhpear;
            employees [10]khanhpear;
        }
        """
        expect = str(Program([StructType("khanhpear",[("id",StringType()),("name",StringType()),("position",StringType()),("salary",FloatType())],[]),
			StructType("khanhpear",[("name",StringType()),("manager",Id("khanhpear")),("employees",ArrayType([IntLiteral(10)],Id("khanhpear")))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_080(self):
        input = """
        type khanhpear struct {
            value int;
            next [1][xx][2]khanhpear;
        }
        """
        expect = str(Program([StructType("khanhpear",[("value",IntType()),("next",ArrayType([IntLiteral(1),Id("xx"),IntLiteral(2)],Id("khanhpear")))],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_081(self):
        input = """
        type khanhpear interface {
            Speak(name string);
        }
        """
        expect = str(Program([InterfaceType("khanhpear",[Prototype("Speak",[StringType()],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_082(self):
        input = """
        type khanhpear interface {
            GetID() int;
            SetID(id int);
        }
        """
        expect = str(Program([InterfaceType("khanhpear",[Prototype("GetID",[],IntType()),Prototype("SetID",[IntType()],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_083(self):
        input = """
        type khanhpear interface {
            Add(x, y int) int;
            Subtract(a, b, c float) float;
        }
        """
        expect = str(Program([InterfaceType("khanhpear",[Prototype("Add",[IntType(),IntType()],IntType()),Prototype("Subtract",[FloatType(),FloatType(),FloatType()],FloatType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_084(self):
        input = """
        type khanhpear interface {
            Compute(a int, b float) float;
            Display(msg string);
            Reset();
        }
        """
        expect = str(Program([InterfaceType("khanhpear",[Prototype("Compute",[IntType(),FloatType()],FloatType()),Prototype("Display",[StringType()],VoidType()),Prototype("Reset",[],VoidType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_085(self):
        input = """
        type khanhpear interface {
            Process(data , file [10]int) int;
            Transform(input string) string;
        }
        """
        expect = str(Program([InterfaceType("khanhpear",[Prototype("Process",[ArrayType([IntLiteral(10)],IntType()),ArrayType([IntLiteral(10)],IntType())],IntType()),Prototype("Transform",[StringType()],StringType())])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_086(self):
        input = """
        func fruit(x int, y int) int {
            return x + y;
        }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([Return(BinaryOp("+", Id("x"), Id("y")))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_087(self):
        input = """
        func fruit(name string) string {
            continue;
            return name;
            break;
            return banana();
        }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("name",StringType())],StringType(),Block([Continue(),Return(Id("name")),Break(),Return(FuncCall("banana",[]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_088(self):
        input = """
        func fruit(x float, y float) float {
            return x * y;
        }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("x",FloatType()),ParamDecl("y",FloatType())],FloatType(),Block([Return(BinaryOp("*", Id("x"), Id("y")))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_089(self):
        input = """
        type khanhpear struct {
            value int;
        }
        """
        expect = str(Program([StructType("khanhpear",[("value",IntType())],[])
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_090(self):
        input = """
        type khanhpear struct {
            price float;
        }
        func (p khanhpear) fruit() float {
            return p.price * 2;
        }
        """
        expect = str(Program([StructType("khanhpear",[("price",FloatType())],[]),
			MethodDecl("p",Id("khanhpear"),FuncDecl("fruit",[],FloatType(),Block([Return(BinaryOp("*", FieldAccess(Id("p"),"price"), IntLiteral(2)))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_091(self):
        input = """
        type khanhpear struct {
            amount int;
        }
        func (a khanhpear) fruit(x int) int {
            return a.amount + x;
        }
        """
        expect = str(Program([StructType("khanhpear",[("amount",IntType())],[]),
			MethodDecl("a",Id("khanhpear"),FuncDecl("fruit",[ParamDecl("x",IntType())],IntType(),Block([Return(BinaryOp("+", FieldAccess(Id("a"),"amount"), Id("x")))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_092(self):
        input = """
        type khanhpear struct {
            weight float;
        }
        func (w khanhpear) fruit(y float) float {
            return w.weight - y;
        }
        """
        expect = str(Program([StructType("khanhpear",[("weight",FloatType())],[]),
			MethodDecl("w",Id("khanhpear"),FuncDecl("fruit",[ParamDecl("y",FloatType())],FloatType(),Block([Return(BinaryOp("-", FieldAccess(Id("w"),"weight"), Id("y")))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_093(self):
        input = """
        type khanhpear struct {
            count int;
        }
        func (c khanhpear) fruit() int {
            return c.count * 10;
        }
        """
        expect = str(Program([StructType("khanhpear",[("count",IntType())],[]),
			MethodDecl("c",Id("khanhpear"),FuncDecl("fruit",[],IntType(),Block([Return(BinaryOp("*", FieldAccess(Id("c"),"count"), IntLiteral(10)))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_094(self):
        input = """
        type khanhpear struct {
            status boolean;
        }
        func (s khanhpear) fruit() boolean {
            return s.status;
        }
        """
        expect = str(Program([StructType("khanhpear",[("status",BoolType())],[]),
			MethodDecl("s",Id("khanhpear"),FuncDecl("fruit",[],BoolType(),Block([Return(FieldAccess(Id("s"),"status"))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_095(self):
        input = """
        type khanhpear struct {
            message string;
        }
        func (m khanhpear) fruit() string {
            return m.message.hello[2][3].fruit();
        }
        """
        expect = str(Program([StructType("khanhpear",[("message",StringType())],[]),
			MethodDecl("m",Id("khanhpear"),FuncDecl("fruit",[],StringType(),Block([Return(MethCall(ArrayCell(FieldAccess(FieldAccess(Id("m"),"message"),"hello"),[IntLiteral(2),IntLiteral(3)]),"fruit",[]))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_096(self):
        input = """
        type khanhpear struct {
            status boolean;
        }
        func (s khanhpear) fruit() boolean {
            if (s.status) {
                return 0;
            } else {
                return 1;
            }
        }
        """
        expect = str(Program([StructType("khanhpear",[("status",BoolType())],[]),
			MethodDecl("s",Id("khanhpear"),FuncDecl("fruit",[],BoolType(),Block([If(FieldAccess(Id("s"),"status"), Block([Return(IntLiteral(0))]), Block([Return(IntLiteral(1))]))])))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))


    def test_097(self):
        input = """
            func fruit(a int, b int) int {
                arr[a + b][2] := arr[3][1];
                if (arr[a][1] > b) {
                    arr[a][0] := arr[2][1] + 5;
                } else if(arr[k][l] <= u >= !henna){
                    arr[a][1] := arr[2][8] + 5;
                }else {
                    arr[a][0] := arr[1][1] - 3;
                }
                return arr[a][0];
            }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([Assign(ArrayCell(Id("arr"),[BinaryOp("+", Id("a"), Id("b")),IntLiteral(2)]),ArrayCell(Id("arr"),[IntLiteral(3),IntLiteral(1)])),If(BinaryOp(">", ArrayCell(Id("arr"),[Id("a"),IntLiteral(1)]), Id("b")), Block([Assign(ArrayCell(Id("arr"),[Id("a"),IntLiteral(0)]),BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(1)]), IntLiteral(5)))]), If(BinaryOp(">=", BinaryOp("<=", ArrayCell(Id("arr"),[Id("k"),Id("l")]), Id("u")), UnaryOp("!",Id("henna"))), Block([Assign(ArrayCell(Id("arr"),[Id("a"),IntLiteral(1)]),BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(8)]), IntLiteral(5)))]), Block([Assign(ArrayCell(Id("arr"),[Id("a"),IntLiteral(0)]),BinaryOp("-", ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(1)]), IntLiteral(3)))]))),Return(ArrayCell(Id("arr"),[Id("a"),IntLiteral(0)]))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_098(self):
        input = """
        func fruit(arr [ohmy]int) int {
            sum := 0;
            for i := 0; i < 10; i := i + 1 {
                if (arr[i] > 5) {
                    for hehe >= arr[1][2][3]{
                        sum := sum + arr[i];
                    }
                }
            }
            return sum;
        }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("arr",ArrayType([Id("ohmy")],IntType()))],IntType(),Block([Assign(Id("sum"),IntLiteral(0)),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([If(BinaryOp(">", ArrayCell(Id("arr"),[Id("i")]), IntLiteral(5)), Block([ForBasic(BinaryOp(">=", Id("hehe"), ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Block([Assign(Id("sum"),BinaryOp("+", Id("sum"), ArrayCell(Id("arr"),[Id("i")])))]))]), None)])),Return(Id("sum"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_099(self):
        input = """
        type khanhpear struct {
            count int;
        }
        func (p khanhpear) fruit(n int) int {
            for i := 1; i <= n; i := i * 2 {
                p.count := p.count + i;
            }
            return p.count;
        }
        """
        expect = str(Program([StructType("khanhpear",[("count",IntType())],[]),
                MethodDecl("p",Id("khanhpear"),FuncDecl("fruit",[ParamDecl("n",IntType())],IntType(),Block([ForStep(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=", Id("i"), Id("n")),Assign(Id("i"),BinaryOp("*", Id("i"), IntLiteral(2))),Block([Assign(FieldAccess(Id("p"),"count"),BinaryOp("+", FieldAccess(Id("p"),"count"), Id("i")))])),Return(FieldAccess(Id("p"),"count"))])))
            ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_100(self):
        input = """
        func fruit(n int) int {
            sum := 0;
            for i, arr := range [x][y][z]int{2, {arr}}{
                if (i % 2 == 0 ){
                    sum := sum + i;
                } else {
                    sum := sum - i;
                }
            }
            return sum;
        }
        """
        expect = str(Program([FuncDecl("fruit",[ParamDecl("n",IntType())],IntType(),Block([Assign(Id("sum"),IntLiteral(0)),ForEach(Id("i"),Id("arr"),ArrayLiteral([Id("x"),Id("y"),Id("z")],IntType(),[IntLiteral(2),[Id("arr")]]),Block([If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), Block([Assign(Id("sum"),BinaryOp("+", Id("sum"), Id("i")))]), Block([Assign(Id("sum"),BinaryOp("-", Id("sum"), Id("i")))]))])),Return(Id("sum"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    