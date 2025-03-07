import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        """test_001"""
        input = """func main () {
            a.b[1][2].c.d[3][4][5][6].e.f := a;
            x += y + 12;
            x -= z - 17;
            a *= k * 0o11;
            b /= n / \"Hello World!\";
            c %= 0x123456789 + 1;
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("a"), "b"), [IntLiteral(1), IntLiteral(2)]), "c"), "d"), [IntLiteral(3), IntLiteral(4), IntLiteral(5), IntLiteral(6)]), "e"), "f"), Id("a")),
                Assign(Id("x"), BinaryOp("+", Id("x"), BinaryOp("+", Id("y"), IntLiteral(12)))),
                Assign(Id("x"), BinaryOp("-", Id("x"), BinaryOp("-", Id("z"), IntLiteral(17)))),
                Assign(Id("a"), BinaryOp("*", Id("a"), BinaryOp("*", Id("k"), IntLiteral("0o11")))),
                Assign(Id("b"), BinaryOp("/", Id("b"), BinaryOp("/", Id("n"), StringLiteral("\"Hello World!\"")))),
                Assign(Id("c"), BinaryOp("%", Id("c"), BinaryOp("+", IntLiteral("0x123456789"), IntLiteral(1)))),
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_002(self):
        """test_002"""
        input = """var x int ;"""
        expect = str(Program([
            VarDecl("x",IntType(),None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_003(self):
        """test_003"""
        input = """func main (x, y int) {
            print(\"Hello World!\");
        }; var x int ;"""
        expect = str(Program([
            FuncDecl("main",[ParamDecl("x", IntType()), ParamDecl("y", IntType())],VoidType(),Block([FuncCall("print", [StringLiteral("\"Hello World!\"")])])),VarDecl("x",IntType(),None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
   
    def test_004(self):
        """test_004"""
        input = """func main() {
            a[1][2].b.c[3][4].d[5].e[6].f := 12;
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), "b"), "c"), [IntLiteral(3), IntLiteral(4)]), "d"), [IntLiteral(5)]), "e"), [IntLiteral(6)]), "f"), IntLiteral(12))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_005(self):
        """test_005"""
        input = """func main() {
            a := Person{name: \"Alice\", age: 30};
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), StructLiteral("Person", [["name", StringLiteral("\"Alice\"")], ["age", IntLiteral(30)]]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_006(self):
        """test_006"""
        input = """func main() {
            a[1][2].b[3][4] := 12;
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), "b"), [IntLiteral(3), IntLiteral(4)]), IntLiteral(12))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_007(self):
        """test_007"""
        input = """
            func main() {
                a[1][2].b[3][4].c[5][6] := Person{name: \"Alice\", age: 30, sex: \"Female\"}
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), "b"), [IntLiteral(3), IntLiteral(4)]), "c"), [IntLiteral(5), IntLiteral(6)]), StructLiteral("Person", [["name", StringLiteral("\"Alice\"")], ["age", IntLiteral(30)], ["sex", StringLiteral("\"Female\"")]]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_008(self):
        """test_008"""
        input = """func main() {
            a[1][2].b[3][4] := a[1][2].b[3][4].c[5][6]
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), "b"), [IntLiteral(3), IntLiteral(4)]), ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), "b"), [IntLiteral(3), IntLiteral(4)]), "c"), [IntLiteral(5), IntLiteral(6)]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_009(self):
        """test_009"""
        input = """func main() {
            a[1+1][2].b[3][4] := -!a - !1;
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(1)),IntLiteral(2)]),"b"),[IntLiteral(3),IntLiteral(4)]),BinaryOp("-",UnaryOp("-",UnaryOp("!", Id("a"))),UnaryOp("!",IntLiteral(1))))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_010(self):
        """test_010"""
        input = """func main() {Person.Name[1][2].Salary[4] := 1.0 + !true + !false + -0x123 * 1.0 / -2.0;}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(
                    ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), [IntLiteral(4)]), 
                    BinaryOp("+", BinaryOp("+", BinaryOp("+", FloatLiteral(1.0), UnaryOp("!", BooleanLiteral("True"))), UnaryOp("!", BooleanLiteral("False"))), BinaryOp("/", BinaryOp("*", UnaryOp("-", IntLiteral("0x123")), FloatLiteral(1.0)), UnaryOp("-", FloatLiteral(2.0))))
                )
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_011(self):
        """test_011"""
        input = """func main() {Person.Name[1][2].Salary := Person.Name[1][2].Salary[4];}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), [IntLiteral(4)]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_012(self):
        """test_012"""
        input = """func main() {Person.Name[1][2].Salary[4] := foo(1 + -a, b, moo(yoo()));}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), [IntLiteral(4)]), FuncCall("foo", [BinaryOp("+", IntLiteral(1), UnaryOp("-", Id("a"))), Id("b"), FuncCall("moo", [FuncCall("yoo", [])])]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_013(self):
        """test_013"""
        input = """func main() {Person.Name[1][2].Salary[4] := Something.foo(1 + -a, b, moo(yoo()));}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), [IntLiteral(4)]), MethCall(Id("Something"), "foo", [BinaryOp("+", IntLiteral(1), UnaryOp("-", Id("a"))), Id("b"), FuncCall("moo", [FuncCall("yoo", [])])]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_014(self):
        """test_014"""
        input = """func main() {Person.Name[1][2].Salary := foo(1 + -a, b, moo(too.yoo()[1][2].x[3].y[4]));}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(ArrayCell(FieldAccess(Id("Person"), "Name"), [IntLiteral(1), IntLiteral(2)]), "Salary"), FuncCall("foo", [BinaryOp("+", IntLiteral(1), UnaryOp("-", Id("a"))), Id("b"), FuncCall("moo", [ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(MethCall(Id("too"), "yoo", []), [IntLiteral(1), IntLiteral(2)]), "x"), [IntLiteral(3)]), "y"), [IntLiteral(4)])])]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_015(self):
        """test_015"""
        input = """func main() {Person.Salary := Calculate(salary)[1].a[2][3].b[4][5][6].c.d;}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(Id("Person"), "Salary"), FieldAccess(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FuncCall("Calculate", [Id("salary")]), [IntLiteral(1)]), "a"), [IntLiteral(2), IntLiteral(3)]), "b"), [IntLiteral(4), IntLiteral(5), IntLiteral(6)]), "c"), "d"))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_016(self):
        """test_016"""
        input = """func main() {Person.Salary := Bonus(percent)[1].isOkay(12, 24)[8].okay().getFunc[4].getMeth;}"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(Id("Person"), "Salary"), FieldAccess(ArrayCell(FieldAccess(MethCall(ArrayCell(MethCall(ArrayCell(FuncCall("Bonus", [Id("percent")]), [IntLiteral(1)]), "isOkay", [IntLiteral(12), IntLiteral(24)]), [IntLiteral(8)]), "okay", []), "getFunc"), [IntLiteral(4)]), "getMeth"))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_017(self):
        """test_017"""
        input = """const Pi = 3.14;"""
        expect = str(Program([ConstDecl("Pi", None, FloatLiteral(3.14))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_018(self):
        """test_018"""
        input = """
            const Pi = 3.14;
            const Greeting = "Hello, MiniGo!";
            const MaxSize = 100 + 50;
        """
        expect = str(Program([
            ConstDecl("Pi", None, FloatLiteral(3.14)), 
            ConstDecl("Greeting", None, StringLiteral("\"Hello, MiniGo!\"")), 
            ConstDecl("MaxSize", None, BinaryOp("+", IntLiteral(100), IntLiteral(50)))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_019(self):
        """test_019"""
        input = """
            var personA Person;
            var companyB Company;
        """
        expect = str(Program([
            VarDecl("personA", Id("Person"), None),
            VarDecl("companyB", Id("Company"), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_020(self):
        """test_020"""
        input = """
            var salaray int;
            var name string;
            var gender boolean;
            var percent float;
        """
        expect = str(Program([
            VarDecl("salaray", IntType(), None), 
            VarDecl("name", StringType(), None), 
            VarDecl("gender", BoolType(), None), 
            VarDecl("percent", FloatType(), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_021(self):
        """test_021"""
        input = """
            var grade [1][2]float
            var name [3][4]string
            var gender [5][6][7][8]boolean
            var books [9][MOD][MAX_INT]int
            var checking [10]float
        """
        expect = str(Program([
            VarDecl("grade", ArrayType([IntLiteral(1), IntLiteral(2)], FloatType()), None),
            VarDecl("name", ArrayType([IntLiteral(3), IntLiteral(4)], StringType()), None),
            VarDecl("gender", ArrayType([IntLiteral(5), IntLiteral(6), IntLiteral(7), IntLiteral(8)], BoolType()), None),
            VarDecl("books", ArrayType([IntLiteral(9), Id("MOD"), Id("MAX_INT")], IntType()), None),
            VarDecl("checking", ArrayType([IntLiteral(10)], FloatType()), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_022(self):
        """test_022"""
        input = """
            var grade [1][2]Grades
            var name [3][4]Names
            var gender [5][6][7][8]Genders
            var books [9][MOD][MAX_INT]Books
            var checking [10]Checkings
        """
        expect = str(Program([
            VarDecl("grade", ArrayType([IntLiteral(1), IntLiteral(2)], Id("Grades")), None),
            VarDecl("name", ArrayType([IntLiteral(3), IntLiteral(4)], Id("Names")), None),
            VarDecl("gender", ArrayType([IntLiteral(5), IntLiteral(6), IntLiteral(7), IntLiteral(8)], Id("Genders")), None),
            VarDecl("books", ArrayType([IntLiteral(9), Id("MOD"), Id("MAX_INT")], Id("Books")), None),
            VarDecl("checking", ArrayType([IntLiteral(10)], Id("Checkings")), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_023(self):
        """test_023"""
        input = """func main() {
            a := a * (1+2)
            b := 1+2-3&&5--1
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), BinaryOp("*",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),
                Assign(Id("b"), BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp("-",IntLiteral(5),UnaryOp("-",IntLiteral(1)))))
            ]))                
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_024(self):
        """test_024"""
        input = """func main() {
            a := ------1 + -!-!-!-!2 * -4 / -8;
            b := a > b <= c;
            c := -1 + -2 * -4 / -8;
            d := a || b || c || d;
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), BinaryOp("+", UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1))))))), BinaryOp("/", BinaryOp("*", UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2))))))))), UnaryOp("-", IntLiteral(4))), UnaryOp("-", IntLiteral(8))))),
                Assign(Id("b"), BinaryOp("<=",BinaryOp(">",Id("a"),Id("b")),Id("c"))),
                Assign(Id("c"), BinaryOp("+", UnaryOp("-", IntLiteral(1)), BinaryOp("/", BinaryOp("*", UnaryOp("-", IntLiteral(2)), UnaryOp("-", IntLiteral(4))), UnaryOp("-", IntLiteral(8))))),
                Assign(Id("d"), BinaryOp("||", BinaryOp("||", BinaryOp("||", Id("a"), Id("b")), Id("c")), Id("d")))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_025(self):
        """test_025"""
        input = """
            const test_025_a = foo(a > b <= c);
            const test_025_b = foo(a[2][3]); 
        """
        expect = str(Program([
            ConstDecl("test_025_a", None, FuncCall("foo", [BinaryOp("<=",BinaryOp(">",Id("a"),Id("b")),Id("c"))])),
            ConstDecl("test_025_b", None, FuncCall("foo", [ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_026(self):
        """test_026"""
        input = """
            const test_026_a = foo( a.b.c ); 
            const test_026_b = foo(a(),b.a(2, 3));
        """
        expect = str(Program([
            ConstDecl("test_026_a", None, FuncCall("foo", [FieldAccess(FieldAccess(Id("a"), "b"), "c")])),
            ConstDecl("test_026_b", None, FuncCall("foo", [FuncCall("a", []), MethCall(Id("b"), "a", [IntLiteral(2), IntLiteral(3)])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_027(self):
        """test_027"""
        input = """
            const test_027_a = foo(12); 
            const test_027_b = foo(1.0, true, false, nil, \"Hello World!\");
        """
        expect = str(Program([
            ConstDecl("test_027_a", None, FuncCall("foo", [IntLiteral(12)])),
            ConstDecl("test_027_b", None, FuncCall("foo", [FloatLiteral(1.0), BooleanLiteral("True"), BooleanLiteral("False"), NilLiteral(), StringLiteral("\"Hello World!\"")]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_028(self):
        """test_028"""
        input = """
            const test_028_a = foo(PersonA {}, PersonB {GPA: 4.0});
            const test_028_b = foo(idStr);
        """
        expect = str(Program([
            ConstDecl("test_028_a", None, FuncCall("foo", [StructLiteral("PersonA", []), StructLiteral("PersonB", [("GPA", FloatLiteral(4.0))])])),
            ConstDecl("test_028_b", None, FuncCall("foo", [Id("idStr")]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_029(self):
        """test_029"""
        input = """
            const test_029 = foo([1]int{1}, [1][2]int{4});
        """
        expect = str(Program([
            ConstDecl("test_029", None, FuncCall("foo", [ArrayLiteral([IntLiteral(1)], IntType(), [IntLiteral(1)]), ArrayLiteral([IntLiteral(1), IntLiteral(2)], IntType(), [IntLiteral(4)])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_030(self):
        """test_030"""
        input = """func main() {
            arr := [3]int{10, 20, 30}
            marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("arr"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)])),
                Assign(Id("marr"), ArrayLiteral([IntLiteral(2), IntLiteral(3)], IntType(), [[IntLiteral(1), IntLiteral(2), IntLiteral(3)], [IntLiteral(4), IntLiteral(5), IntLiteral(6)]]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_031(self):
        """test_031"""
        input = """
            var test_031_a = 1;
            var test_031_b float;
            var test_031_c string = \"abcd\";
        """
        expect = str(Program([
            VarDecl("test_031_a", None, IntLiteral(1)),
            VarDecl("test_031_b", FloatType(), None),
            VarDecl("test_031_c", StringType(), StringLiteral("\"abcd\""))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_032(self):
        """test_032"""
        input = """
            var test_032_a = Person{Name: \"Harry Potter\", age: 18};
            var test_032_b float = 10.0;
            var test_032_c string = \"abcd\";
            var test_032_d = \"Hello\";
            var test_032_e = MOD;
        """
        expect = str(Program([
            VarDecl("test_032_a", None, StructLiteral("Person", [("Name", StringLiteral("\"Harry Potter\"")), ("age", IntLiteral(18))])),
            VarDecl("test_032_b", FloatType(), FloatLiteral(10.0)),
            VarDecl("test_032_c", StringType(), StringLiteral("\"abcd\"")),
            VarDecl("test_032_d", None, StringLiteral("\"Hello\"")),
            VarDecl("test_032_e", None, Id("MOD"))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_033(self):
        """test_033"""
        input = """
            func main() {
                a := [1][2]Person{{personA, personB, 3}, {4, 5, 6}}
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), ArrayLiteral([IntLiteral(1), IntLiteral(2)], Id("Person"), [[Id("personA"), Id("personB"), IntLiteral(3)], [IntLiteral(4), IntLiteral(5), IntLiteral(6)]]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_034(self):
        """test_034"""
        input = """
            type Calculator interface {
                Add(x, y int) int;
                Subtract(a, b float, c int) float;
                Reset()
                SayHello(name string)
            }
        """
        expect = str(Program([
            InterfaceType("Calculator", [
                Prototype("Add", [IntType(), IntType()], IntType()),
                Prototype("Subtract", [FloatType(), FloatType(), IntType()], FloatType()),
                Prototype("Reset", [], VoidType()),
                Prototype("SayHello", [StringType()], VoidType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_035(self):
        """test_035"""
        input = """
            type Calculator interface {
                Add(x, y int) int;
                Subtract(a, b float, c int) float;
                Reset()
                SayHello(name string)
            }

            type Person interface {
                getName()
                setName(name string)
                get_salary() float
            }
        """
        expect = str(Program([
            InterfaceType("Calculator", [
                Prototype("Add", [IntType(), IntType()], IntType()),
                Prototype("Subtract", [FloatType(), FloatType(), IntType()], FloatType()),
                Prototype("Reset", [], VoidType()),
                Prototype("SayHello", [StringType()], VoidType())
            ]),
            InterfaceType("Person", [
                Prototype("getName", [], VoidType()), 
                Prototype("setName", [StringType()], VoidType()), 
                Prototype("get_salary", [], FloatType())
            ])
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_036(self):
        """test_036"""
        input = """
            type Person struct {
                name string ;
                age int ;
                lover Person;
            }
        """
        expect = str(Program([
            StructType("Person", [("name", StringType()), ("age", IntType()), ("lover", Id("Person"))], [])
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_037(self):
        """test_037"""
        input = """func main() {        
            for i < 10 {
                var x int = 10.0;
            }

            for 1 == 1 {
                var x int = 10.0;
            }
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)), Block([VarDecl("x", IntType(), FloatLiteral(10.0))])),
                ForBasic(BinaryOp("==", IntLiteral(1), IntLiteral(1)), Block([VarDecl("x", IntType(), FloatLiteral(10.0))]))
            ]))                
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_038(self):
        """test_038"""
        input = """
            func FunctionTemp(x boolean) Person {
                for i := 0; i < 10; i += 1 {
                    var x int = 10.0;
                }

                for var i = \"0\"; 10 > i; i += 1 {
                    var x int = 9.5;
                }
            }
        """
        expect = str(Program([
            FuncDecl("FunctionTemp", [ParamDecl("x", BoolType())], Id("Person"), Block([
                ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([VarDecl("x", IntType(), FloatLiteral(10.0))])),
                ForStep(VarDecl("i", None, StringLiteral("\"0\"")), BinaryOp(">", IntLiteral(10), Id("i")), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([VarDecl("x", IntType(), FloatLiteral(9.5))]))
            ]))            
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_039(self):
        """test_039"""
        input = """
            func main() {
                arr := [3]int{10, 20, 30}
                for _, value := range arr {
                    const MOD = 2004;
                }

                arr := [3]int{10, 20, 30}
                for index, value := range arr.a[1].b {
                    const MAXN = 100000;
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("arr"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)])), 
                ForEach(Id("_"), Id("value"), Id("arr"), Block([ConstDecl("MOD", None, IntLiteral(2004))])),
                Assign(Id("arr"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)])), 
                ForEach(Id("index"), Id("value"), FieldAccess(ArrayCell(FieldAccess(Id("arr"), "a"), [IntLiteral(1)]), "b"), Block([ConstDecl("MAXN", None, IntLiteral(100000))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_040(self):
        """test_040"""
        input = """
            func main() {
                for _, value := range [3]int{10, 20, 30} {
                    const MOD = 2004;
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)]), Block([ConstDecl("MOD", None, IntLiteral(2004))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_041(self):
        """test_041"""
        input = """
            func fib(n int) int {
                for idx, value := range arr[1][2][3][4].x.y[5] {
                    const MOD = 2004;
                }

                for idx, value := range arr.t[1][2][3][4].x.y[5] {
                    const MOD = 2004;
                }
            }
        """
        expect = str(Program([
            FuncDecl("fib", [ParamDecl("n", IntType())], IntType(), Block([
                ForEach(Id("idx"), Id("value"), ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("arr"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), "x"), "y"), [IntLiteral(5)]), Block([ConstDecl("MOD", None, IntLiteral(2004))])),
                ForEach(Id("idx"), Id("value"), ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("arr"), "t"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), "x"), "y"), [IntLiteral(5)]), Block([ConstDecl("MOD", None, IntLiteral(2004))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_042(self):
        """test_042"""
        input = """
            type Person struct {
                name string
            }

            func (p Person) Greeting() {
                for idx, value := range arr[100].t[1][2][3][4].x.y[5].z {
                    const MOD = 2004;
                }

                for idx, value := range h.arr[100].t[1][2][3][4].x.y[5].z {
                    const MOD = 2004;
                }
            }
        """
        expect = str(Program([
            StructType("Person", [("name", StringType())], []),
            MethodDecl("p", Id("Person"), FuncDecl("Greeting", [], VoidType(), Block([
                ForEach(Id("idx"), Id("value"), FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("arr"), [IntLiteral(100)]), "t"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), "x"), "y"), [IntLiteral(5)]), "z"), Block([ConstDecl("MOD", None, IntLiteral(2004))])),
                ForEach(Id("idx"), Id("value"), FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("h"), "arr"), [IntLiteral(100)]), "t"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), "x"), "y"), [IntLiteral(5)]), "z"), Block([ConstDecl("MOD", None, IntLiteral(2004))]))
            ])))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_043(self):
        """test_043"""        
        input = """func Add(x int, y int) {
            for idx, value := range arr[100].t(abc)[1][2][3][4].x.y[5].z {
                const MOD = 2004;
            }

            for idx, value := range getArr() {
                const MOD = 2004;
            }
        }"""
        expect = str(Program([
            FuncDecl("Add", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], VoidType(), Block([
                ForEach(Id("idx"), Id("value"), FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(MethCall(ArrayCell(Id("arr"), [IntLiteral(100)]), "t", [Id("abc")]), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), "x"), "y"), [IntLiteral(5)]), "z"), Block([ConstDecl("MOD", None, IntLiteral(2004))])),
                ForEach(Id("idx"), Id("value"), FuncCall("getArr", []), Block([ConstDecl("MOD", None, IntLiteral(2004))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_044(self):
        """test_044"""
        input = """
            func Add(x int, y int) int {
                return x + y;
            }

            func getInt()float {
                return value;
            }
        """
        expect = str(Program([
            FuncDecl("Add", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], IntType(), Block([Return(BinaryOp("+", Id("x"), Id("y")))])),
            FuncDecl("getInt", [], FloatType(), Block([Return(Id("value"))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_045(self):
        """test_045"""
        input = """
            func putLn() string {
                return self.str;
            }

            func getString() {
                a := this.value;
            }

            func getFloat() boolean {
                this.bool := !false + true;
            }
        """
        expect = str(Program([
            FuncDecl("putLn", [], StringType(), Block([Return(FieldAccess(Id("self"), "str"))])),
            FuncDecl("getString", [], VoidType(), Block([Assign(Id("a"), FieldAccess(Id("this"), "value"))])),
            FuncDecl("getFloat", [], BoolType(), Block([Assign(FieldAccess(Id("this"), "bool"), BinaryOp("+", UnaryOp("!", BooleanLiteral("false")), BooleanLiteral("true")))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_046(self):
        """test_046"""
        input = """
            func Add(x int, y int) [100][50]int {
                return x + y;
            }

            func Sub(x int, y int) [100][50]Cal {
                return x - y;
            }
        """
        expect = str(Program([
            FuncDecl("Add", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], ArrayType([IntLiteral(100), IntLiteral(50)], IntType()), Block([Return(BinaryOp("+", Id("x"), Id("y")))])),
            FuncDecl("Sub", [ParamDecl("x", IntType()), ParamDecl("y", IntType())], ArrayType([IntLiteral(100), IntLiteral(50)], Id("Cal")), Block([Return(BinaryOp("-", Id("x"), Id("y")))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_047(self):
        """test_047"""
        input = """
            type Calculator struct {
                value int;
            }
                
            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }
        """
        expect = str(Program([
            StructType("Calculator", [("value", IntType())], []),
            MethodDecl("c", Id("Calculator"), FuncDecl("Add", [ParamDecl("x", IntType())], IntType(), Block([
                Assign(FieldAccess(Id("c"), "value"), BinaryOp("+", FieldAccess(Id("c"), "value"), Id("x"))), 
                Return(FieldAccess(Id("c"), "value"))
            ])))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_048(self):
        """test_048"""
        input = """
            type Calculator struct {
                value int;
            }
                
            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }

            func (c Calculator) Greeting() {
                putStringLn(\"Welcome to the best Calculator in the world!\");
            }
        """
        expect = str(Program([
            StructType("Calculator", [("value", IntType())], []),
            MethodDecl("c", Id("Calculator"), FuncDecl("Add", [ParamDecl("x", IntType())], IntType(), Block([
                Assign(FieldAccess(Id("c"), "value"), BinaryOp("+", FieldAccess(Id("c"), "value"), Id("x"))), 
                Return(FieldAccess(Id("c"), "value"))
            ]))),
            MethodDecl("c", Id("Calculator"), FuncDecl("Greeting", [], VoidType(), Block([
                FuncCall("putStringLn", [StringLiteral("\"Welcome to the best Calculator in the world!\"")])
            ])))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_049(self):
        """test_049"""
        input = """func main() {
            for a := 1; callFunction().arr[1]; i += i {
                var x int = 10.0;
            }
        }"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(Assign(Id("a"), IntLiteral(1)), ArrayCell(FieldAccess(FuncCall("callFunction", []), "arr"), [IntLiteral(1)]), Assign(Id("i"), BinaryOp("+", Id("i"), Id("i"))), Block([VarDecl("x", IntType(), FloatLiteral(10.0))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_050(self):
        """test_050"""
        input = """
            func main() {
                if (x > 10) {
                    println(\"x is greater than 10\");
                } 
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
                ]), None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_051(self):
        """test_051"""
        input = """
            func main() {
                if (x > 10) {
                    println(\"x is greater than 10\");
                } else if (10 == x) {
                    println(\"x is equal to 10\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
                ]), If(BinaryOp("==", IntLiteral(10), Id("x")), Block([
                    FuncCall("println", [StringLiteral("\"x is equal to 10\"")])
                ]), None))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_052(self):
        """test_052"""
        input = """
            func main() {
                if (x > 10) {
                    println(\"x is greater than 10\");
                } else if (10 == x) {
                    println(\"x is equal to 10\");
                } else {
                    println(\"x is less than 10\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
                ]),  If(BinaryOp("==", IntLiteral(10), Id("x")), Block([
                    FuncCall("println", [StringLiteral("\"x is equal to 10\"")])
                ]), Block([
                    FuncCall("println", [StringLiteral("\"x is less than 10\"")])
                ]))) 
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_053(self):
        """test_053"""
        input = """
            func main() {
                if (x > 10) {
                    println(\"x is greater than 10\");
                } else if (10 == x) {
                    println(\"x is equal to 10\");
                } else if (10 >= x + 2 + 10) {
                    println(\"x is x and 10 is 10\");
                } else {
                    println(\"x is less than 10\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
                ]), If(BinaryOp("==", IntLiteral(10), Id("x")), Block([
                    FuncCall("println", [StringLiteral("\"x is equal to 10\"")])
                ]), If(BinaryOp(">=", IntLiteral(10), BinaryOp("+", BinaryOp("+", Id("x"), IntLiteral(2)), IntLiteral(10))), Block([
                    FuncCall("println", [StringLiteral("\"x is x and 10 is 10\"")])
                ]), Block([
                    FuncCall("println", [StringLiteral("\"x is less than 10\"")])
                ]))))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_054(self):
        """test_054"""
        input = """
            func main() {
                if (x > 10) {
                    println(\"x is greater than 10\");

                    if(1 + 1) {
                        var x = y;
                    }
                } else if (10 == x) {
                    if(1 == 1) {
                        return 100;
                    } else {
                        break;
                    }

                    println(\"x is equal to 10\");

                    for i, v := range arr {
                        if(1 == 2) {
                            return \"Hello\";
                        }

                        return v;
                    }
                } else {
                    println(\"x is less than 10\");

                    if(2 == 4 >= 8) {
                        continue;
                    }
                }

                return 0;
            }            
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("println", [StringLiteral("\"x is greater than 10\"")]),
                    If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([
                        VarDecl("x", None, Id("y"))
                    ]), None)
                ]), If(BinaryOp("==", IntLiteral(10), Id("x")), Block([
                    If(BinaryOp("==", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(100))]), Block([
                        Break()
                    ])),
                    FuncCall("println", [StringLiteral("\"x is equal to 10\"")]),
                    ForEach(Id("i"), Id("v"), Id("arr"), Block([
                        If(BinaryOp("==", IntLiteral(1), IntLiteral(2)), Block([
                            Return(StringLiteral("\"Hello\""))
                        ]), None),
                        Return(Id("v"))
                    ]))
                ]), Block([
                    FuncCall("println", [StringLiteral("\"x is less than 10\"")]),
                    If(BinaryOp(">=", BinaryOp("==", IntLiteral(2), IntLiteral(4)), IntLiteral(8)), Block([
                        Continue()
                    ]), None)
                ]))),
                Return(IntLiteral(0))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_055(self):
        """test_055"""
        input = """ 
            func main() {
                foo(2 + x, 4 / y); m.goo();
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("foo", [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("/", IntLiteral(4), Id("y"))]),
                MethCall(Id("m"), "goo", [])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_056(self):
        """test_056"""
        input = """ 
            const a = [ID][2][VT]int{{{1}, {2, {{1, 2, 3}, {4, 5, 6}}, 4}}, {\"abcd\", abcdef}, {Person{name: \"Alice\", age: 30}}}
        """
        expect = str(Program([
            ConstDecl("a", None, ArrayLiteral([Id("ID"), IntLiteral(2), Id("VT")], IntType(), [
                [
                    [
                        IntLiteral(1)
                    ], 
                    [
                        IntLiteral(2), 
                        [
                            [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                            [IntLiteral(4), IntLiteral(5), IntLiteral(6)],
                        ],
                        IntLiteral(4)
                    ]
                ],
                [
                    StringLiteral("\"abcd\""),
                    Id("abcdef")
                ],
                [
                    StructLiteral("Person", [
                        ("name", StringLiteral("\"Alice\"")),
                        ("age", IntLiteral(30))
                    ])
                ]
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_057(self):
        """test_057"""
        input = """
            var x int = 10;
            var y = 20;
            func main() {
                putIntLn(x + y);
            }
        """
        expect = str(Program([
            VarDecl("x", IntType(), IntLiteral(10)),
            VarDecl("y", None, IntLiteral(20)),
            FuncDecl("main", [], VoidType(), Block([FuncCall("putIntLn", [
                BinaryOp("+", Id("x"), Id("y"))
            ])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_058(self):
        """test_058"""
        input = """
            const Pi = 3.14;
            func main() {
                putFloatLn(Pi);
            }

        """
        expect = str(Program([
            ConstDecl("Pi", None, FloatLiteral("3.14")),
            FuncDecl("main", [], VoidType(), Block([FuncCall("putFloatLn", [
                Id("Pi")
            ])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_059(self):
        """test_059"""
        input = """
            func add(a int, b int) int {
                return a + b;
            }
            func main() {
                var result = add(5, 7);
                putIntLn(result);
            }
        """
        expect = str(Program([
            FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("result", None, FuncCall("add", [IntLiteral(5), IntLiteral(7)])),
                FuncCall("putIntLn", [Id("result")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_060(self):
        """test_060"""
        input = """
            func main() {
                var x int = 15;
                if (x > 10) {
                    putStringLn(\"Greater\");
                } else {
                    putStringLn(\"Smaller\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(15)),
                If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                    FuncCall("putStringLn", [StringLiteral("\"Greater\"")])
                ]), Block([
                    FuncCall("putStringLn", [StringLiteral("\"Smaller\"")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_061(self):
        """test_061"""
        input = """
            func main() {
                var i int = 0;
                for i < 5 {
                    putIntLn(i);
                    i += 1;
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("i", IntType(), IntLiteral(0)),
                ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)), Block([
                    FuncCall("putIntLn", [Id("i")]),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_062(self):
        """test_062"""
        input = """
            func main() {
                for i := 0; i < 5; i += 1 {
                    putIntLn(i);
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(5)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    FuncCall("putIntLn", [Id("i")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_063(self):
        """test_063"""
        input = """
            var arr [3]int = [3]int{10, 20, 30};
            func main() {
                for i, val := range arr {
                    putIntLn(val);
                }
            }
        """
        expect = str(Program([
            VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(10), IntLiteral(20), IntLiteral(30)])),
            FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("i"), Id("val"), Id("arr"), Block([
                    FuncCall("putIntLn", [Id("val")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_064(self):
        """test_064"""
        input = """
            func main() {
                var a int = 10;
                var b int = 5;
                var c int = a * (b + 2) - 3;
                putIntLn(c);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(10)), 
                VarDecl("b", IntType(), IntLiteral(5)), 
                VarDecl("c", IntType(), BinaryOp("-", BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), IntLiteral(2))), IntLiteral(3))), 
                FuncCall("putIntLn", [Id("c")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_065(self):
        """test_065"""
        input = """
            func main() {
                var a int = 10;
                var b int = 20;
                if (a < b) {
                    putStringLn(\"a is less than b\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(10)), 
                VarDecl("b", IntType(), IntLiteral(20)), 
                If(BinaryOp("<", Id("a"), Id("b")), Block([
                    FuncCall("putStringLn", [StringLiteral("\"a is less than b\"")])
                ]), None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_066(self):
        """test_066"""
        input = """
            func main() {
                var flag boolean = true && false || !false;
                if (flag) {
                    putStringLn(\"True\");
                } else {
                    putStringLn(\"False\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("flag", BoolType(), BinaryOp("||", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)), UnaryOp("!", BooleanLiteral(False)))), 
                If(Id("flag"), Block([
                    FuncCall("putStringLn", [StringLiteral("\"True\"")])
                ]), Block([
                    FuncCall("putStringLn", [StringLiteral("\"False\"")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_067(self):
        """test_067"""
        input = """
            func main() {
                var arr [4]int = [4]int{1, 2, 3, 4};
                for _, v := range arr {
                    putIntLn(v);
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(4)], IntType()), ArrayLiteral([IntLiteral(4)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])),
                ForEach(Id("_"), Id("v"), Id("arr"), Block([
                    FuncCall("putIntLn", [Id("v")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_068(self):
        """test_068"""
        input = """
            type Point struct {
                x int;
                y int;
            }
            func main() {
                var p = Point{x: 3, y: 4};
                putIntLn(p.x);
                putIntLn(p.y);
            }
        """
        expect = str(Program([
            StructType("Point", [("x", IntType()), ("y", IntType())], []),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("p", None, StructLiteral("Point", [("x", IntLiteral(3)), ("y", IntLiteral(4))])),
                FuncCall("putIntLn", [FieldAccess(Id("p"), "x")]),
                FuncCall("putIntLn", [FieldAccess(Id("p"), "y")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_069(self):
        """test_069"""
        input = """
            type Person struct {
                name string;
                age int;
            }

            func main() {
                var person = Person{name: \"Alice\", age: 30};
                putStringLn(person.name);
                putIntLn(person.age);
            }
        """
        expect = str(Program([
            StructType("Person", [("name", StringType()), ("age", IntType())], []),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("person", None, StructLiteral("Person", [("name", StringLiteral("\"Alice\"")), ("age", IntLiteral(30))])),
                FuncCall("putStringLn", [FieldAccess(Id("person"), "name")]),
                FuncCall("putIntLn", [FieldAccess(Id("person"), "age")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_070(self):
        """test_070"""
        input = """
            type Speaker interface {
                Speak();
            }

            func main() {
                putStringLn(\"Interface test\");
            }
        """
        expect = str(Program([
            InterfaceType("Speaker", [
                Prototype("Speak", [], VoidType())
            ]),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putStringLn", [StringLiteral("\"Interface test\"")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_071(self):
        """test_071"""
        input = """
            func square(n int) int {
                return n * n;
            }
            func main() {
                var result = square(6);
                putIntLn(result);
            }
        """
        expect = str(Program([
            FuncDecl("square", [ParamDecl("n", IntType())], IntType(), Block([
                Return(BinaryOp("*", Id("n"), Id("n")))
            ])),            
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("result", None, FuncCall("square", [IntLiteral(6)])),
                FuncCall("putIntLn", [Id("result")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_072(self):
        """test_072"""
        input = """
            func multiply(a int, b int) int {
                return a * b;
            }
            func main() {
                var res = multiply(4, 5);
                putIntLn(res);
            }
        """
        expect = str(Program([
            FuncDecl("multiply", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("*", Id("a"), Id("b")))
            ])),            
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("res", None, FuncCall("multiply", [IntLiteral(4), IntLiteral(5)])),
                FuncCall("putIntLn", [Id("res")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_073(self):
        """test_073"""
        input = """
            func main() {
                var a int = 10;
                if (0 < a) {
                    if (a < 20) {
                        putStringLn(\"a is between 1 and 19\");
                    }
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(10)),
                If(BinaryOp("<", IntLiteral(0), Id("a")), Block([
                    If(BinaryOp("<", Id("a"), IntLiteral(20)), Block([
                        FuncCall("putStringLn", [StringLiteral("\"a is between 1 and 19\"")])
                    ]), None)
                ]), None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_074(self):
        """test_074"""
        input = """
            func main() {
                for var i int = 0; i < 3; i += 1 {
                    for var j = 1; 2 > j; j += 1 {
                        putIntLn(i * 10 + j);
                    }
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(VarDecl("i", IntType(), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(3)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    ForStep(VarDecl("j", None, IntLiteral(1)), BinaryOp(">", IntLiteral(2), Id("j")), Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))), Block([
                        FuncCall("putIntLn", [BinaryOp("+", BinaryOp("*", Id("i"), IntLiteral(10)), Id("j"))])
                    ]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_075(self):
        """test_075"""
        input = """
            func main() {
                for i := 0; i < 10; i += 1 {
                    if (i == 3) {
                        continue;
                    }
                    if (i == 7) {
                        break;
                    }
                    putIntLn(i);
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    If(BinaryOp("==", Id("i"), IntLiteral(3)), Block([
                        Continue()
                    ]), None), 
                    If(BinaryOp("==", Id("i"), IntLiteral(7)), Block([
                        Break()
                    ]), None), 
                    FuncCall("putIntLn", [Id("i")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_076(self):
        """test_076"""
        input = """
            /* Multi-line
               comment */
            func main() {
                // Single line comment
                var a int = 5; // initialize a
                putIntLn(a);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(5)), 
                FuncCall("putIntLn", [Id("a")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_077(self):
        """test_077"""
        input = """
            func main() {
                var result int = 2 + 3 * 4 - 5;
                putIntLn(result);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("result", IntType(), BinaryOp("-", BinaryOp("+", IntLiteral(2), BinaryOp("*", IntLiteral(3), IntLiteral(4))), IntLiteral(5))), 
                FuncCall("putIntLn", [Id("result")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_078(self):
        """test_078"""
        input = """
            func main() {
                var s string = \"Number: \" + \"42\";
                var num int = 10 + 32;
                putStringLn(s);
                putIntLn(num);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("s", StringType(), BinaryOp("+", StringLiteral("\"Number: \""), StringLiteral("\"42\""))), 
                VarDecl("num", IntType(), BinaryOp("+", IntLiteral(10), IntLiteral(32))), 
                FuncCall("putStringLn", [Id("s")]), 
                FuncCall("putIntLn", [Id("num")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_079(self):
        """test_079"""
        input = """
            const MAX = 100;
            var x int = 10;
            type Dummy struct {
                val int;
            }
            func helper() int {
                return x * 2;
            }
            func main() {
                var d = Dummy{val: helper()};
                putIntLn(d.val);
            }
        """
        expect = str(Program([
            ConstDecl("MAX", None, IntLiteral(100)),
            VarDecl("x", IntType(), IntLiteral(10)),
            StructType("Dummy", [("val", IntType())], []),
            FuncDecl("helper", [], IntType(), Block([
                Return(BinaryOp("*", Id("x"), IntLiteral(2)))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("d", None, StructLiteral("Dummy", [("val", FuncCall("helper", []))])),
                FuncCall("putIntLn", [FieldAccess(Id("d"), "val")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_080(self):
        """test_080"""
        input = """
            func main() {
                var x int = 5;
                x += 3;
                x *= 2;
                x %= x;
                x /= x;
                x -= x;                
                putIntLn(x);

                var matrix [2][3]int = [2][3]int{{1,2,3}, {4,5,6}};
                for _, row := range matrix {
                    for __, val := range row {
                        putIntLn(val);
                    }
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(3))),
                Assign(Id("x"), BinaryOp("*", Id("x"), IntLiteral(2))),
                Assign(Id("x"), BinaryOp("%", Id("x"), Id("x"))),
                Assign(Id("x"), BinaryOp("/", Id("x"), Id("x"))),
                Assign(Id("x"), BinaryOp("-", Id("x"), Id("x"))),
                FuncCall("putIntLn", [Id("x")]),
                VarDecl("matrix", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), ArrayLiteral([IntLiteral(2), IntLiteral(3)], IntType(), [[IntLiteral(1), IntLiteral(2), IntLiteral(3)], [IntLiteral(4), IntLiteral(5), IntLiteral(6)]])),
                ForEach(Id("_"), Id("row"), Id("matrix"), Block([
                    ForEach(Id("__"), Id("val"), Id("row"), Block([
                        FuncCall("putIntLn", [Id("val")])
                    ]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_081(self):
        """test_081"""
        input = """
            func add(a int, b int) int {
                return a + b;
            }

            func subtract(a int, b int) int {
                return a - b;
            }

            func main() {
                putIntLn(subtract(10, 4));
                putIntLn(add(add(2,3), 4));
            }
        """
        expect = str(Program([
            FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])),
            FuncDecl("subtract", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("-", Id("a"), Id("b")))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putIntLn", [FuncCall("subtract", [IntLiteral(10), IntLiteral(4)])]), 
                FuncCall("putIntLn", [FuncCall("add", [FuncCall("add", [IntLiteral(2), IntLiteral(3)]), IntLiteral(4)])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_082(self):
        """test_082"""
        input = """
            type Counter struct {
                count int;
            }

            func (c Counter) increment() int {
                c.count += 1;
                return c.count;
            }
            
            func main() {
                var c Counter = Counter{count: 0};
                putIntLn(c.increment());
            }
        """
        expect = str(Program([
            StructType("Counter", [("count", IntType())], []),
            MethodDecl("c", Id("Counter"), FuncDecl("increment", [], IntType(), Block([
                Assign(FieldAccess(Id("c"), "count"), BinaryOp("+", FieldAccess(Id("c"), "count"), IntLiteral(1))), 
                Return(FieldAccess(Id("c"), "count"))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("c", Id("Counter"), StructLiteral("Counter", [("count", IntLiteral(0))])), 
                FuncCall("putIntLn", [MethCall(Id("c"), "increment", [])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_083(self):
        """test_083"""
        input = """
            type Greeter struct {
                name string;
            }

            func (g Greeter) greet() string {
                return \"Hello, \" + g.name;
            }
            
            func main() {
                var g = Greeter{name: \"Bob\"};
                putStringLn(g.greet());
            }
        """
        expect = str(Program([
            StructType("Greeter", [("name", StringType())], []),
            MethodDecl("g", Id("Greeter"), FuncDecl("greet", [], StringType(), Block([
                Return(BinaryOp("+", StringLiteral("\"Hello, \""), FieldAccess(Id("g"), "name")))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("g", None, StructLiteral("Greeter", [("name", StringLiteral("\"Bob\""))])), 
                FuncCall("putStringLn", [MethCall(Id("g"), "greet", [])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_084(self):
        """test_084"""
        input = """
            var unused int = 42;
            func main() {
                putStringLn(\"Testing unused global variable\");
                var result int = (3 + 5) * (2 - 1);
                putIntLn(result);
            }
        """
        expect = str(Program([
            VarDecl("unused", IntType(), IntLiteral(42)),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putStringLn", [StringLiteral("\"Testing unused global variable\"")]), 
                VarDecl("result", IntType(), BinaryOp("*", BinaryOp("+", IntLiteral(3), IntLiteral(5)), BinaryOp("-", IntLiteral(2), IntLiteral(1)))),
                FuncCall("putIntLn", [Id("result")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_085(self):
        """test_085"""
        input = """
            func main() {
                var nums [3]int = [3]int{7,8,9};
                for _, num := range nums {
                    putIntLn(num);
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("nums", ArrayType([IntLiteral(3)], IntType()), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(7), IntLiteral(8), IntLiteral(9)])), 
                ForEach(Id("_"), Id("num"), Id("nums"), Block([
                    FuncCall("putIntLn", [Id("num")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_086(self):
        """test_086"""
        input = """
            func main() {
                var x int = 10;
                var y int = 20;
                putIntLn(x);
                putIntLn(y);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(10)), 
                VarDecl("y", IntType(), IntLiteral(20)), 
                FuncCall("putIntLn", [Id("x")]),
                FuncCall("putIntLn", [Id("y")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_087(self):
        """test_087"""
        input = """
            func main() {
                var x int = 5;
                if (x > 0) {
                    var x int = 10;
                    putIntLn(x);
                }
                putIntLn(x);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(5)), 
                If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([
                    VarDecl("x", IntType(), IntLiteral(10)), 
                    FuncCall("putIntLn", [Id("x")])
                ]), None),
                FuncCall("putIntLn", [Id("x")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_088(self):
        """test_088"""
        input = """
            const BASE = 10;
            const HEIGHT = 5;
            func main() {
                const AREA = (BASE * HEIGHT) / 2;
                putIntLn(AREA);
            }
        """
        expect = str(Program([
            ConstDecl("BASE", None, IntLiteral(10)),
            ConstDecl("HEIGHT", None, IntLiteral(5)),
            FuncDecl("main", [], VoidType(), Block([
                ConstDecl("AREA", None, BinaryOp("/", BinaryOp("*", Id("BASE"), Id("HEIGHT")), IntLiteral(2))),
                FuncCall("putIntLn", [Id("AREA")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_089(self):
        """test_089"""
        input = """
            func main() {
                var score int = 85;
                if (score >= 90) {
                    putStringLn(\"A\");
                } else if (80 <= score) {
                    putStringLn(\"B\");
                } else {
                    putStringLn(\"C\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("score", IntType(), IntLiteral(85)), 
                If(BinaryOp(">=", Id("score"), IntLiteral(90)), Block([
                    FuncCall("putStringLn", [StringLiteral("\"A\"")])
                ]), If(BinaryOp("<=", IntLiteral(80), Id("score")), Block([
                    FuncCall("putStringLn", [StringLiteral("\"B\"")])
                ]), Block([
                    FuncCall("putStringLn", [StringLiteral("\"C\"")])
                ])))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_090(self):
        """test_090"""
        input = """
            func main() {
                var f float = 3.1415;
                putFloatLn(f);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("f", FloatType(), FloatLiteral(3.1415)),
                FuncCall("putFloatLn", [Id("f")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_091(self):
        """test_091"""
        input = """
            func main() {
                var a int = 0x1A;
                var b int = 0b1010;
                var c int = 0o12 + 1.2e5;
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral("0x1A")),
                VarDecl("b", IntType(), IntLiteral("0b1010")),
                VarDecl("c", IntType(), BinaryOp("+", IntLiteral("0o12"), FloatLiteral("1.2e5"))),
                FuncCall("putIntLn", [Id("a")]),
                FuncCall("putIntLn", [Id("b")]),
                FuncCall("putIntLn", [Id("c")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_092(self):
        """test_092"""
        input = """
            func main() {
                var s string = \"Hello\\nWorld\\t!\";
                putStringLn(s);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("s", StringType(), StringLiteral("\"Hello\\nWorld\\t!\"")),
                FuncCall("putStringLn", [Id("s")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_093(self):
        """test_093"""
        input = """
            func main() {
                putIntLn(123);
                putFloatLn(3.14);
                putBoolLn(true);
                putStringLn(\"Test\");
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putIntLn", [IntLiteral(123)]),
                FuncCall("putFloatLn", [FloatLiteral(3.14)]),
                FuncCall("putBoolLn", [BooleanLiteral(True)]),
                FuncCall("putStringLn", [StringLiteral("\"Test\"")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_094(self):
        """test_094"""
        input = """
            func factorial(n int) int {
                if (n <= 1) {
                    return 1;
                }
                return n * factorial(n - 1);
            }

            func main() {
                putIntLn(factorial(5));
            }
        """
        expect = str(Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("<=", Id("n"), IntLiteral(1)), Block([
                    Return(IntLiteral(1))
                ]), None), 
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putIntLn", [FuncCall("factorial", [IntLiteral(5)])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_095(self):
        """test_095"""
        input = """
            func factorial(n int) int {
                if (n <= 1) {
                    return 1;
                }
                return n * factorial(n - 1);
            }

            func main() {
                putIntLn(factorial(5));
            }
        """
        expect = str(Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("<=", Id("n"), IntLiteral(1)), Block([
                    Return(IntLiteral(1))
                ]), None), 
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("putIntLn", [FuncCall("factorial", [IntLiteral(5)])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_096(self):
        """test_096"""
        input = """
            func main() {
                for i := 1; i >= 3; i += 1 {
                    for 100 + 1 >= 3 {
                        for _, __ := range arr[1].a.b.c(1).d {
                            if (i == j) {
                                putIntLn(i * j);
                            } else {
                                putStringLn(\"Not equal\");
                            }
                        }
                    }
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(1)), BinaryOp(">=", Id("i"), IntLiteral(3)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    ForBasic(BinaryOp(">=", BinaryOp("+", IntLiteral(100), IntLiteral(1)), IntLiteral("3")), Block([
                        ForEach(Id("_"), Id("__"), FieldAccess(MethCall(FieldAccess(FieldAccess(ArrayCell(Id("arr"), [IntLiteral(1)]), "a"), "b"), "c", [IntLiteral(1)]), "d"), Block([
                            If(BinaryOp("==", Id("i"), Id("j")), Block([
                                FuncCall("putIntLn", [BinaryOp("*", Id("i"), Id("j"))])
                            ]), Block([
                                FuncCall("putStringLn", [StringLiteral("\"Not equal\"")])
                            ]))
                        ]))
                    ]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_097(self):
        """test_097"""
        input = """
            func main() {
                var arr [5]int = [5]int{0,1,2,3,4};
                arr[2] += 10;
                putIntLn(arr[2]);
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), ArrayLiteral([IntLiteral(5)], IntType(), [IntLiteral(0), IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])), 
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), BinaryOp("+", ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(10))), 
                FuncCall("putIntLn", [ArrayCell(Id("arr"), [IntLiteral(2)])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_098(self):
        """test_098"""
        input = """
            func main() {
                var a int = -5;
                var b boolean = !true;
                putIntLn(a);
                if (b) {
                    putStringLn(\"b is true\");
                } else {
                    putStringLn(\"b is false\");
                }

                var n Node = nil;
                if (n == nil) {
                    putStringLn(\"n is nil\");
                }
            }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), UnaryOp("-", IntLiteral(5))), 
                VarDecl("b", BoolType(), UnaryOp("!", BooleanLiteral(True))), 
                FuncCall("putIntLn", [Id("a")]), 
                If(Id("b"), Block([
                    FuncCall("putStringLn", [StringLiteral("\"b is true\"")])
                ]), Block([
                    FuncCall("putStringLn", [StringLiteral("\"b is false\"")])
                ])), 
                VarDecl("n", Id("Node"), NilLiteral()),
                If(BinaryOp("==", Id("n"), NilLiteral()), Block([
                    FuncCall("putStringLn", [StringLiteral("\"n is nil\"")])
                ]), None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_099(self):
        """test_099"""
        input = """
            type Point struct {
                x int;
                y int;
            }
            
            func distance(p Point) int {
                return p.x * p.x + p.y * p.y;
            }
            
            func main() {
                var points [3]Point = [3]Point{Point{x:1, y:2}, Point{x:3, y:4}, Point{x:5, y:6}};
                for _, p := range points {
                    if (distance(p) > 20) {
                        putStringLn(\"Far\");
                    } else {
                        putStringLn(\"Near\");
                    }
                }
            }
        """
        expect = str(Program([
            StructType("Point", [("x", IntType()), ("y", IntType())], []),
            FuncDecl("distance", [ParamDecl("p", Id("Point"))], IntType(), Block([
                Return(BinaryOp("+", BinaryOp("*", FieldAccess(Id("p"), "x"), FieldAccess(Id("p"), "x")), BinaryOp("*", FieldAccess(Id("p"), "y"), FieldAccess(Id("p"), "y"))))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("points", ArrayType([IntLiteral(3)], Id("Point")), ArrayLiteral([IntLiteral(3)], Id("Point"), [
                    StructLiteral("Point", [("x", IntLiteral(1)), ("y", IntLiteral(2))]), 
                    StructLiteral("Point", [("x", IntLiteral(3)), ("y", IntLiteral(4))]),
                    StructLiteral("Point", [("x", IntLiteral(5)), ("y", IntLiteral(6))])
                ])), 
                ForEach(Id("_"), Id("p"), Id("points"), Block([
                    If(BinaryOp(">", FuncCall("distance", [Id("p")]), IntLiteral(20)), Block([
                        FuncCall("putStringLn", [StringLiteral("\"Far\"")])
                    ]), Block([
                        FuncCall("putStringLn", [StringLiteral("\"Near\"")])
                    ]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_100(self):
        """test_100"""
        input = """
            const MAX_COUNT = 3;
            type Student struct {
                name  string;
                score int;
            }

            func printStudent(s Student) {
                putStringLn(s.name);
                putIntLn(s.score);
            }

            func main() {
                var students [MAX_COUNT]Student = [MAX_COUNT]Student{
                    Student{name: \"Alice\", score: 90}, 
                    Student{name: \"Bob\", score: 80}, 
                    Student{name: \"Charlie\", score: 85}};

                for _, s := range students {
                    if (s.score >= 85) {
                        printStudent(s);
                    } else {
                        putStringLn(\"Below average\");
                    }
                }
            }
        """
        expect = str(Program([
            ConstDecl("MAX_COUNT", None, IntLiteral(3)),
            StructType("Student", [("name", StringType()), ("score", IntType())], []),
            FuncDecl("printStudent", [ParamDecl("s", Id("Student"))], VoidType(), Block([
                FuncCall("putStringLn", [FieldAccess(Id("s"), "name")]), 
                FuncCall("putIntLn", [FieldAccess(Id("s"), "score")])
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("students", ArrayType([Id("MAX_COUNT")], Id("Student")), ArrayLiteral([Id("MAX_COUNT")], Id("Student"), [
                    StructLiteral("Student", [("name", StringLiteral("\"Alice\"")), ("score", IntLiteral(90))]), 
                    StructLiteral("Student", [("name", StringLiteral("\"Bob\"")), ("score", IntLiteral(80))]),
                    StructLiteral("Student", [("name", StringLiteral("\"Charlie\"")), ("score", IntLiteral(85))])
                ])), 
                ForEach(Id("_"), Id("s"), Id("students"), Block([
                    If(BinaryOp(">=", FieldAccess(Id("s"), "score"), IntLiteral(85)), Block([
                        FuncCall("printStudent", [Id("s")])
                    ]), Block([
                        FuncCall("putStringLn", [StringLiteral("\"Below average\"")])
                    ]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))