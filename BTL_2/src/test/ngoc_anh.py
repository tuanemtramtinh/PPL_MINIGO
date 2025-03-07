import unittest
from TestUtils import TestAST
from AST import * 


class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const x = bar(5);"""
        expect = Program([ConstDecl("x", None, FuncCall("bar", [IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 301))
    
    def test_002(self):
        input = """const y = baz(3.14, false, true, nil, "hello");"""
        expect = Program([ConstDecl("y", None, FuncCall("baz", [
            FloatLiteral(3.14), BooleanLiteral(False), BooleanLiteral(True), NilLiteral(), StringLiteral("\"hello\"")
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 302))
    
    def test_003(self):
        input = """const y = waldo(func1(), obj.method(6, 7));"""
        expect = Program([ConstDecl("y", None, FuncCall("waldo", [
            FuncCall("func1", []), MethCall(Id("obj"), "method", [IntLiteral(6), IntLiteral(7)])
        ]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))
        
    def test_004(self):
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        """
        expect = str(Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
            
    def test_005(self):
        input = """
        func foo() {
            var a int = 5;
        }
        """
        expect = str(Program([
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(5))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
        
    def test_006(self):
        input = """
        func foo(a int) {
            if (a > 10) {
                return a;
            } else {
                return 10;
            }
        }
        """
        expect = str(Program([
            FuncDecl("foo", [
                ParamDecl("a", IntType())
            ], VoidType(), Block([
                If(BinaryOp(">", Id("a"), IntLiteral(10)), 
                Block([Return(Id("a"))]), 
                Block([Return(IntLiteral(10))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
        
    def test_007(self):
        input = """const _123arr = [3]int {1,2,3};"""
        expect = str(Program([ConstDecl("_123arr",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 307)) 
        
    
    def test_008(self):
        input = """
        func main() {
            var p = Person{name: "Alice", age: 30};
        }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("p", None, StructLiteral("Person", [("name", StringLiteral("\"Alice\"")), ("age", IntLiteral(30))]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308)) 
        
    def test_009(self):
        input = """const numbers = [2][3]int {{1, 2, 3}, {4, 5, 6}};"""
        expect = str(Program([
            ConstDecl("numbers", None, 
                ArrayLiteral(
                    [IntLiteral(2), IntLiteral(3)], 
                    IntType(), 
                    [[IntLiteral(1), IntLiteral(2), IntLiteral(3)], 
                    [IntLiteral(4), IntLiteral(5), IntLiteral(6)]]
                )
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
 
        
    def test_010(self):
        input = """
        func main() {
            print(add(3, mul(4, 5)));
        }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("print", [
                    FuncCall("add", [IntLiteral(3), FuncCall("mul", [IntLiteral(4), IntLiteral(5)])])
                ])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
        
    def test_011(self):
        input = """var y float;"""
        expect = str(Program([
            VarDecl("y", FloatType(), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

        
    def test_012(self):
        input = """var name string = "MiniGo";"""
        expect = str(Program([
            VarDecl("name", StringType(), StringLiteral("\"MiniGo\""))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
        
    def test_013(self):
        input = """var numbers [5]int;"""
        expect = str(Program([
            VarDecl("numbers", ArrayType([IntLiteral(5)], IntType()), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))
        
    def test_014(self):
        input = """var matrix [3][3]float;"""
        expect = str(Program([
            VarDecl("matrix", ArrayType([IntLiteral(3), IntLiteral(3)], FloatType()), None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314)) 
        
    def test_015(self):
        input = """func add(a int, b int) int { 
        return a+b; 
        }
        """
        expect = str(Program([
            FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_016(self):
        input = """func sayHello(name string) { 
            putString("Hello, " + name); 
            }
            """
        expect = str(Program([
            FuncDecl("sayHello", [ParamDecl("name", StringType())], VoidType(), Block([
                FuncCall("putString", [BinaryOp("+", StringLiteral("\"Hello, \""), Id("name"))])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_017(self):
        input = """func main() { 
        for index, value := range arr { putInt(value); 
        } 
        }
        """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("index"), Id("value"), Id("arr"), Block([
                    FuncCall("putInt", [Id("value")])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

        
    def test_018(self):
        input = """type Person struct {name string; age int;} 
                func main() { var p Person = Person{name: "Alice", age: 0b101};}
                """
        expect = str(Program([
            StructType("Person", [("name", StringType()), ("age", IntType())], []),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("p", Id("Person"), StructLiteral("Person", [
                    ("name", StringLiteral("\"Alice\"")),
                    ("age", IntLiteral("0b101"))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
        
    def test_019(self):
        input = """
        func main() { p.age := 31; }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(FieldAccess(Id("p"), "age"), IntLiteral(31))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))
        
    def test_020(self):
        input = """func (p Person) greet() string { return "Hello, " + p.name; }
        """
        expect = str(Program([
            MethodDecl("p", Id("Person"), FuncDecl("greet", [], StringType(), Block([
                Return(BinaryOp("+", StringLiteral("\"Hello, \""), FieldAccess(Id("p"), "name")))
            ])))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
        
    def test_021(self):
        input = """func outer(x int) int {  
                    return y * 2; 
                    return inner(x) + 5;
                }
                """
        expect = str(Program([
            FuncDecl("outer", [ParamDecl("x", IntType())], IntType(), Block([
                Return(BinaryOp("*", Id("y"), IntLiteral(2))),
                Return(BinaryOp("+", FuncCall("inner", [Id("x")]), IntLiteral(5)))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321)) 
        
    def test_022(self):
        input = """type Car struct { brand string; speed int; } 
                func main() { 
                    var myCar Car = Car{brand: "Toyota", speed: 120}; 
                    putString(myCar.brand);
                }
                """
        expect = str(Program([
            StructType("Car", [("brand", StringType()), ("speed", IntType())], []),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("myCar", Id("Car"), StructLiteral("Car", [
                    ("brand", StringLiteral("\"Toyota\"")),
                    ("speed", IntLiteral(120))
                ])),
                FuncCall("putString", [FieldAccess(Id("myCar"), "brand")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
        
    def test_023(self):
        input = """func main() { 
                    for i := 0; i < 5; i += 1 { 
                        for j := 0; j < 3; j += 1 { 
                            putInt(i * j);
                        }
                    }
                }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(5)), 
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                        ForStep(Assign(Id("j"), IntLiteral(0)), BinaryOp("<", Id("j"), IntLiteral(3)), 
                            Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))), Block([
                                FuncCall("putInt", [BinaryOp("*", Id("i"), Id("j"))])
                            ])
                        )
                    ])
                )
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_024(self):
        input = """func main() { 
                    result := (factorial(5) + 2) * (3 - 1) / 2;
                    putInt(result);
                }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("result"), 
                    BinaryOp("/", 
                        BinaryOp("*", 
                            BinaryOp("+", FuncCall("factorial", [IntLiteral(5)]), IntLiteral(2)), 
                            BinaryOp("-", IntLiteral(3), IntLiteral(1))
                        ), IntLiteral(2)
                    )
                ),
                FuncCall("putInt", [Id("result")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

        
    def test_025(self):
        input = """func main() { 
                    x := square(add(2, 3));
                    putInt(x);
                }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("x"), FuncCall("square", [FuncCall("add", [IntLiteral(2), IntLiteral(3)])])),
                FuncCall("putInt", [Id("x")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))
 
        
    def test_026(self):
        input = """func main() { 
                    a := 10;
                    b := a * 2 + (3 - 1);
                    putInt(b);
                }
                """
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), IntLiteral(10)),
                Assign(Id("b"), BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), BinaryOp("-", IntLiteral(3), IntLiteral(1)))),
                FuncCall("putInt", [Id("b")])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

        
    def test_027(self):
        input = """
            const a = (1 + 2) * (3 - 4) / (5 % 6) && (7 > 8) || (9 <= 10);
        """
        expect = Program([ConstDecl("a", None, 
            BinaryOp("||", 
                BinaryOp("&&", 
                    BinaryOp("/", 
                        BinaryOp("*", 
                            BinaryOp("+", IntLiteral(1), IntLiteral(2)), 
                        BinaryOp("-", IntLiteral(3), IntLiteral(4))), 
                    BinaryOp("%", IntLiteral(5), IntLiteral(6))), 
                BinaryOp(">", IntLiteral(7), IntLiteral(8))), 
            BinaryOp("<=", IntLiteral(9), IntLiteral(10))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))

    def test_028(self):
        input = """
            const a = ID{a: 1, b: [2]float{1.0, 2.0}, c: hell {d: "hello", e: [1]int{1}}};
        """
        expect = Program([ConstDecl("a", None, 
            StructLiteral("ID", [
                ("a", IntLiteral(1)),
                ("b", ArrayLiteral([IntLiteral(2)], FloatType(), [FloatLiteral(1.0), FloatLiteral(2.0)])),
                ("c", StructLiteral("hell",[
                    ("d", StringLiteral("\"hello\"")),
                    ("e", ArrayLiteral([IntLiteral(1)], IntType(), [IntLiteral(1)]))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))
        
    def test_029(self):
        input = """
        func fun(){
            continue;
            break;
            return;
        }
        """
        expect = str(Program([FuncDecl("fun",[],VoidType(),Block([Continue(),Break(),Return(None)]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 329)) 
        
    def test_030(self):
        input = """
            func foo() {
                bar(1, 2, 3, "hello", true);
            }
        """
        expect = Program([FuncDecl("foo", [], VoidType(), Block([
            FuncCall("bar", [
                IntLiteral(1), 
                IntLiteral(2), 
                IntLiteral(3), 
                StringLiteral("\"hello\""), 
                BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))

    def test_031(self):
        input = """
            func bubbleSort(){
            var nums = [6]int{9, 7, 5, 3, 1, 2}
            var length = 6
            for var i = 0; i < length - 1; i+=1 {
                for var j = 0; j < length - i - 1; j+=1{
                    if (nums[j] > nums[j + 1]) {
                        swap(nums[j], nums[j + 1])
                    }
                }
            }
        };"""
        expect = Program([FuncDecl("bubbleSort", [], VoidType(), Block([
		VarDecl("nums", None,
			ArrayLiteral([IntLiteral(6)], IntType(), [IntLiteral(9), IntLiteral(7), IntLiteral(5), IntLiteral(3), IntLiteral(1), IntLiteral(2)])
		),
		VarDecl("length", None, IntLiteral(6)),
		ForStep(
			VarDecl("i", None, IntLiteral(0)),
			BinaryOp("<", Id("i"), BinaryOp("-", Id("length"), IntLiteral(1))),
			Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
			Block([
				ForStep(
					VarDecl("j", None, IntLiteral(0)),
					BinaryOp("<", Id("j"), BinaryOp("-", BinaryOp("-", Id("length"), Id("i")), IntLiteral(1))),
					Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
					Block([
						If(
							BinaryOp(">", 
								ArrayCell(Id("nums"), [Id("j")]),
								ArrayCell(Id("nums"), [BinaryOp("+", Id("j"), IntLiteral(1))])
							),
							Block([
								FuncCall("swap", [
									ArrayCell(Id("nums"), [Id("j")]),
									ArrayCell(Id("nums"), [BinaryOp("+", Id("j"), IntLiteral(1))])
								])
							]),
							None
						)
					])
				)
			])
		)
	]))
])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))
        
    def test_032(self):
        input = """
            func foo() {
                if (a > b) {
                    if (c < d) {
                        return 1;
                    } else if (e == f) {
                        if (g != h) {
                            return 2;
                        } else {
                            return 3;
                        }
                    } else {
                        if (i >= j) {
                            return 4;
                        } else if (k <= l) {
                            return 5;
                        } else {
                            return 6;
                        }
                    }
                } else if (m == n) {
                    if (o > p) {
                        return 7;
                    } else if (q < r) {
                        if (s != t) {
                            return 8;
                        } else {
                            return 9;
                        }
                    } else {
                        return 10;
                    }
                } else {
                    if (u >= v) {
                        if (w <= x) {
                            return 11;
                        } else if (y == z) {
                            return 12;
                        } else {
                            return 13;
                        }
                    } else {
                        return 14;
                    }
                }
            }
        """
        expect = Program([
    FuncDecl("foo", [], VoidType(), Block([
        If(
            BinaryOp(">", Id("a"), Id("b")),
            Block([
                If(
                    BinaryOp("<", Id("c"), Id("d")),
                    Block([Return(IntLiteral(1))]),
                    If(
                        BinaryOp("==", Id("e"), Id("f")),
                        Block([
                            If(
                                BinaryOp("!=", Id("g"), Id("h")),
                                Block([Return(IntLiteral(2))]),
                                Block([Return(IntLiteral(3))])
                            )
                        ]),
                        Block([
                            If(
                                BinaryOp(">=", Id("i"), Id("j")),
                                Block([Return(IntLiteral(4))]),
                                If(
                                    BinaryOp("<=", Id("k"), Id("l")),
                                    Block([Return(IntLiteral(5))]),
                                    Block([Return(IntLiteral(6))])
                                )
                            )
                        ])
                    )
                )
            ]),
            # else-part for outer if: else if (m == n) { ... } else { ... }
            If(
                BinaryOp("==", Id("m"), Id("n")),
                Block([
                    If(
                        BinaryOp(">", Id("o"), Id("p")),
                        Block([Return(IntLiteral(7))]),
                        If(
                            BinaryOp("<", Id("q"), Id("r")),
                            Block([
                                If(
                                    BinaryOp("!=", Id("s"), Id("t")),
                                    Block([Return(IntLiteral(8))]),
                                    Block([Return(IntLiteral(9))])
                                )
                            ]),
                            Block([Return(IntLiteral(10))])
                        )
                    )
                ]),
                Block([
                    If(
                        BinaryOp(">=", Id("u"), Id("v")),
                        Block([
                            If(
                                BinaryOp("<=", Id("w"), Id("x")),
                                Block([Return(IntLiteral(11))]),
                                If(
                                    BinaryOp("==", Id("y"), Id("z")),
                                    Block([Return(IntLiteral(12))]),
                                    Block([Return(IntLiteral(13))])
                                )
                            )
                        ]),
                        Block([Return(IntLiteral(14))])
                    )
                ])
            )
        )
    ]))
])

        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))

    def test_033(self):
        input = """
            func StmCheck() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
            }
        """
        expect = Program([
    FuncDecl("StmCheck", [], VoidType(), Block([
   
        ForBasic(
            BinaryOp("<", Id("i"), IntLiteral(10)),
            Block([Break()])
        ),

        Break(),
     
        Continue(),

        Return(IntLiteral(1)),
 
        Return(None),

        FuncCall("foo", [
            BinaryOp("+", IntLiteral(2), Id("x")),
            BinaryOp("/", IntLiteral(4), Id("y"))
        ]),
   
        MethCall(Id("m"), "goo", [])
    ]))
])


        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))
        
    def test_034(self):
        input = """
            type Calculator interface {
                SayHi (c Calculator)         
            }
             type Person struct{
                name string;
                age int
            };
        """
        expect = Program([InterfaceType("Calculator",[Prototype("SayHi",[Id("Calculator")],VoidType())]),
			StructType("Person",[("name",StringType()),("age",IntType())],[])
		])

        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))
        
    def test_035(self):
        input = """
        func linearSearch(arr [15]int, n int, key int) int{
            for var i = 0; i < n; i+=1 {
                if (arr[i] == key) {
                    return i;
                }
            }   
            return -1;
        };"""
        expect = Program([
    FuncDecl(
        "linearSearch",
        [
            ParamDecl("arr", ArrayType([IntLiteral(15)], IntType())),
            ParamDecl("n", IntType()),
            ParamDecl("key", IntType())
        ],
        IntType(),
        Block([
            ForStep(
                VarDecl("i", None, IntLiteral(0)),
                BinaryOp("<", Id("i"), Id("n")),
                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                Block([
                    If(
                        BinaryOp("==", ArrayCell(Id("arr"), [Id("i")]), Id("key")),
                        Block([Return(Id("i"))]),
                        None
                    )
                ])
            ),
            Return(UnaryOp("-",IntLiteral(1)))
        ])
    )
])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))

        
    def test_036(self):
        input = """
            func mergeSort(arr [15]int, left int, right int) {
                if (left >= right) {return;}
                var mid = (left + right) / 2;
                mergeSort(arr, left, mid);
                mergeSort(arr, mid + 1, right);
                var temp = arr[mid];
            }
        """
        expect = Program([FuncDecl("mergeSort",[ParamDecl("arr",ArrayType([IntLiteral(15)],IntType())),ParamDecl("left",IntType()),ParamDecl("right",IntType())],VoidType(),Block([If(BinaryOp(">=", Id("left"), Id("right")), Block([Return(None)]), None),VarDecl("mid", None,BinaryOp("/", BinaryOp("+", Id("left"), Id("right")), IntLiteral(2))),FuncCall("mergeSort",[Id("arr"),Id("left"),Id("mid")]),FuncCall("mergeSort",[Id("arr"),BinaryOp("+", Id("mid"), IntLiteral(1)),Id("right")]),VarDecl("temp", None,ArrayCell(Id("arr"),[Id("mid")]))]))
		])

        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336)) 
        
    def test_037(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1 + 2 * 3;
            } 
        """
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                Assign(
                    ArrayCell(
                        FieldAccess(
                            FieldAccess(
                                ArrayCell(Id("a"), [IntLiteral(2)]
                            ), "b"
                        ), "c"
                    ), [IntLiteral(2)]
                    ),
                    BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3))))
                ]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))

        
    def test_038(self):
        input = """
            func main() {
                var x int = 10;
                var y float = 5.5;
                var arr [5]int;
                for i := 0; i < 5; i := i + 1 {
                    arr[i] := i * x;
                }
                return;
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                VarDecl("y", FloatType(), FloatLiteral(5.5)),
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(5)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(ArrayCell(Id("arr"), [Id("i")]), BinaryOp("*", Id("i"), Id("x")))
                    ])
                ),
                Return(None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))
        
    def test_039(self):
        input = """
            func computeSum(a int, b int) int {
                return a + b;
            }
            func main() {
                var result int;
                result := computeSum(10, 20);
            }
        """
        expect = Program([
            FuncDecl("computeSum", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], IntType(), Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("result", IntType(), None),
                Assign(Id("result"), FuncCall("computeSum", [IntLiteral(10), IntLiteral(20)]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339)) 
        
    def test_040(self):
        input = """
            func factorial(n int) int {
                if(n == 0) {
                    return 1;
                }
                return n * factorial(n - 1);
            }
        """
        expect = Program([
            FuncDecl("factorial", [
                ParamDecl("n", IntType())
            ], IntType(), Block([
                If(
                    BinaryOp("==", Id("n"), IntLiteral(0)),
                    Block([Return(IntLiteral(1))]),
                    None
                ),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))
    
    def test_041(self):
        input = """
            func checkEvenOdd(n int) {
                if(n % 2 == 0) {
                    print("Even");
                } else {
                    print("Odd");
                }
            }
        """
        expect = Program([
            FuncDecl("checkEvenOdd", [
                ParamDecl("n", IntType())
            ], VoidType(), Block([
                If(
                    BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)),
                    Block([FuncCall("print", [StringLiteral("\"Even\"")])]),
                    Block([FuncCall("print", [StringLiteral("\"Odd\"")])])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))
        
    def test_042(self):
        input = """
            func fibonacci(n int) int {
                if(n == 0){
                    return 0;
                }
                if(n == 1){
                    return 1;
                }
                return fibonacci(n - 1) + fibonacci(n - 2);
            }
        """
        expect = Program([
            FuncDecl("fibonacci", [
                ParamDecl("n", IntType())
            ], IntType(), Block([
                If(
                    BinaryOp("==", Id("n"), IntLiteral(0)),
                    Block([Return(IntLiteral(0))]),
                    None
                ),
                If(
                    BinaryOp("==", Id("n"), IntLiteral(1)),
                    Block([Return(IntLiteral(1))]),
                    None
                ),
                Return(
                    BinaryOp("+",
                        FuncCall("fibonacci", [BinaryOp("-", Id("n"), IntLiteral(1))]),
                        FuncCall("fibonacci", [BinaryOp("-", Id("n"), IntLiteral(2))])
                    )
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 442))
 
        
    def test_043(self):
        input = """
            func swap(a int, b int) {
                var temp int;
                temp := a;
                a := b;
                b := temp;
            }
        """
        expect = Program([
            FuncDecl("swap", [
                ParamDecl("a", IntType()),
                ParamDecl("b", IntType())
            ], VoidType(), Block([
                VarDecl("temp", IntType(), None),
                Assign(Id("temp"), Id("a")),
                Assign(Id("a"), Id("b")),
                Assign(Id("b"), Id("temp"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343)) 
        
    def test_044(self):
        input = """
            func main() {
                // Multiple variable declarations and assignments
                var a int = 5;
                var b float = 3.14;
                var s string = "hello";
                a := a + 1;
                b := b * 2.0;
                s := s + " world";
                return;
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", IntType(), IntLiteral(5)),
                VarDecl("b", FloatType(), FloatLiteral(3.14)),
                VarDecl("s", StringType(), StringLiteral("\"hello\"")),
                Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                Assign(Id("b"), BinaryOp("*", Id("b"), FloatLiteral(2.0))),
                Assign(Id("s"), BinaryOp("+", Id("s"), StringLiteral("\" world\""))),
                Return(None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344)) 
        
    def test_045(self):
        input = """
            func process(arr [10]int) int {
                var sum int = 0;
                for var i = 0; i < 10; i := i + 1 {
                    sum := sum + arr[i];
                }
                return sum;
            }
        """
        expect = Program([
            FuncDecl("process", [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType()))], IntType(), Block([
                VarDecl("sum", IntType(), IntLiteral(0)),
                ForStep(
                    VarDecl("i", None, IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"), [Id("i")])))
                    ])
                ),
                Return(Id("sum"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345)) 
    
    def test_046(self):
        input = """
            func testComplex() {
                var x int = 10;
                var y int = 20;
                var z int;
                // Nested if and for with function calls and field accesses
                if (x < y) {
                    for var i = 0; i < x; i := i + 1 {
                        z := z + i;
                    }
                    print(z);
                } else {
                    print("No update");
                }
                return;
            }
        """
        expect = Program([
            FuncDecl("testComplex", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                VarDecl("y", IntType(), IntLiteral(20)),
                VarDecl("z", IntType(), None),
                If(
                    BinaryOp("<", Id("x"), Id("y")),
                    Block([
                        ForStep(
                            VarDecl("i", None, IntLiteral(0)),
                            BinaryOp("<", Id("i"), Id("x")),
                            Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                            Block([
                                Assign(Id("z"), BinaryOp("+", Id("z"), Id("i")))
                            ])
                        ),
                        FuncCall("print", [Id("z")])
                    ]),
                    Block([
                        FuncCall("print", [StringLiteral("\"No update\"")])
                    ])
                ),
                Return(None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346)) 
        
    def test_047(self):
        input = """
            type Calculator interface {
                Add(a int, b int) int;
                Subtract(a int, b int) int;
                Multiply(a int, b int) int;
            }
        """
        expect = Program([
            InterfaceType("Calculator", [
                Prototype("Add", [IntType(), IntType()], IntType()),
                Prototype("Subtract", [IntType(), IntType()], IntType()),
                Prototype("Multiply", [IntType(), IntType()], IntType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))
        
    def test_048(self):
        input = """
            type Shape interface {
                Area() float;
                Perimeter() float;
            }
        """
        expect = Program([
            
                InterfaceType("Shape", [
                    Prototype("Area", [], FloatType()),
                    Prototype("Perimeter", [], FloatType())
                ]
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348)) 
        
    def test_049(self):
        input = """
            type Circle struct {
                radius float;
            }
            func (c Circle) GetRadius() float {
                return c.radius;
            }
        """
        expect = Program([
            
                StructType("Circle", [
                    ("radius", FloatType())
                ], [])
            ,
            MethodDecl("c", Id("Circle"),
                FuncDecl("GetRadius", [], FloatType(),
                    Block([Return(FieldAccess(Id("c"), "radius"))])
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))
        
    def test_050(self):
        input = """
            func main() {
                result := add(10, 20, 30);
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(),
                Block([
                    Assign(Id("result"),
                        FuncCall("add", [IntLiteral(10), IntLiteral(20), IntLiteral(30)])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350)) 
        
    def test_051(self):
        input = """
            func processData() {
                obj.compute(5, "hello", true);
            }
        """
        expect = Program([
            FuncDecl("processData", [], VoidType(),
                Block([
                    MethCall(Id("obj"), "compute", [
                        IntLiteral(5),
                        StringLiteral("\"hello\""),
                        BooleanLiteral(True)
                    ])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351)) 
        
    def test_052(self):
        input = """
            func compute() int {
                return - (a + b * (c - 2)) / foo();
            }
        """
        expect = Program([
            FuncDecl("compute", [], IntType(), Block([
                Return(
                    BinaryOp("/",
                        UnaryOp("-", 
                            BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), BinaryOp("-", Id("c"), IntLiteral(2))))
                        ),
                        FuncCall("foo", [])
                    )
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 352))
        
    def test_053(self):
        input = """
            func foo() {
                var s = Struct{a: [2]int{1, 2},b: Struct{c: "hello",d: [3]float{1.0, 2.0, 3.0}}};
                s.b.d[1] := 4.0;
            }
        """
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("s", None, StructLiteral("Struct", [
                    ("a", ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)])),
                    ("b", StructLiteral("Struct", [
                        ("c", StringLiteral("\"hello\"")),
                        ("d", ArrayLiteral([IntLiteral(3)], FloatType(), [FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0)]))
                    ]))
                ])),
                Assign(
                    ArrayCell(FieldAccess(FieldAccess(Id("s"), "b"), "d"), [IntLiteral(1)]),
                    FloatLiteral(4.0)
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 353)) 
        
    def test_054(self):
        input = """
            func foo() {
                if (a > b && c < d || e == f) {
                    return 1;
                } else if (g != h || i >= j) {
                    return 2;
                } else {
                    return 3;
                }
            }
        """
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(
                    BinaryOp("||",
                        BinaryOp("&&",
                            BinaryOp(">", Id("a"), Id("b")),
                            BinaryOp("<", Id("c"), Id("d"))
                        ),
                        BinaryOp("==", Id("e"), Id("f"))
                    ),
                    Block([Return(IntLiteral(1))]),
                    If(
                        BinaryOp("||",
                            BinaryOp("!=", Id("g"), Id("h")),
                            BinaryOp(">=", Id("i"), Id("j"))
                        ),
                        Block([Return(IntLiteral(2))]),
                        Block([Return(IntLiteral(3))])
                    )
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))
        
    def test_055(self):
        input = """
            func decision(x int) string {
                if (x > 100) {
                    if (x > 1000) {
                        return "Huge";
                    } else {
                        return "Big";
                    }
                } else if (x > 10) {
                    if (x == 50) {
                        return "Fifty";
                    } else {
                        return "Medium";
                    }
                } else {
                    return "Small";
                }
            }
        """
        expect = Program([
            FuncDecl("decision", [ParamDecl("x", IntType())], StringType(), Block([
                If(
                    BinaryOp(">", Id("x"), IntLiteral(100)),
                    Block([
                        If(
                            BinaryOp(">", Id("x"), IntLiteral(1000)),
                            Block([Return(StringLiteral("\"Huge\""))]),
                            Block([Return(StringLiteral("\"Big\""))])
                        )
                    ]),
                    If(
                        BinaryOp(">", Id("x"), IntLiteral(10)),
                        Block([
                            If(
                                BinaryOp("==", Id("x"), IntLiteral(50)),
                                Block([Return(StringLiteral("\"Fifty\""))]),
                                Block([Return(StringLiteral("\"Medium\""))])
                            )
                        ]),
                        Block([Return(StringLiteral("\"Small\""))])
                    )
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))
        
    def test_056(self):
        input = """
            func iterate() {
                for x < 100 {
                    if (x % 2 == 0) {
                        continue;
                    }
                    x := x + 1;
                }
                return;
            }
        """
        expect = Program([
            FuncDecl("iterate", [], VoidType(), Block([
                ForBasic(
                    BinaryOp("<", Id("x"), IntLiteral(100)),
                    Block([
                        If(
                            BinaryOp("==", BinaryOp("%", Id("x"), IntLiteral(2)), IntLiteral(0)),
                            Block([Continue()]),
                            None
                        ),
                        Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))
                    ])
                ),
                Return(None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))
        
    def test_057(self):
        input = """
            type Worker interface {
                Work();
                Report() string;
            }
            type Employee struct {
                id int;
                name string;
            }
            func (e Employee) Work() {
                putString("Working...");
            }
            func (e Employee) Report() string {
                return e.name;
            }
            func main() {
                var w Worker = Employee{id: 1001, name: "John Doe"};
                w.Work();
                var r string = w.Report();
                return;
            }
        """
        expect = Program([InterfaceType("Worker",[Prototype("Work",[],VoidType()),Prototype("Report",[],StringType())]),
			StructType("Employee",[("id",IntType()),("name",StringType())],[]),
			MethodDecl("e",Id("Employee"),FuncDecl("Work",[],VoidType(),Block([FuncCall("putString",[StringLiteral("\"Working...\"")])]))),
			MethodDecl("e",Id("Employee"),FuncDecl("Report",[],StringType(),Block([Return(FieldAccess(Id("e"),"name"))]))),
			FuncDecl("main",[],VoidType(),Block([VarDecl("w",Id("Worker"),StructLiteral("Employee",[("id",IntLiteral(1001)),("name",StringLiteral("\"John Doe\""))])),MethCall(Id("w"),"Work",[]),VarDecl("r",StringType(),MethCall(Id("w"),"Report",[])),Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 357))

        
    def test_058(self):
        input = """
        func checkLeapYear(x int) bool {
            if (n % 4 == 0){
                if (n % 100 == 0){
                    return n % 400 == 0;
                }
                return true;
            }
            return false;
        }
        """
        expect = str(Program([FuncDecl("checkLeapYear",[ParamDecl("x",IntType())],Id("bool"),Block([If(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(4)), IntLiteral(0)), Block([If(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(100)), IntLiteral(0)), Block([Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(400)), IntLiteral(0)))]), None),Return(BooleanLiteral(True))]), None),Return(BooleanLiteral(False))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358)) 
        
    def test_059(self):
        input = """func Compute(x int, y int) [2][3]float {
                    const matrix = [2][3]float{1.1, 2.2, 3.3, 4.4, 5.5, 6.6};
                }
                """
        expect = str(Program([
            FuncDecl("Compute", 
                [ParamDecl("x", IntType()), ParamDecl("y", IntType())], 
                ArrayType([IntLiteral(2), IntLiteral(3)], FloatType()), 
                Block([
                    ConstDecl("matrix", None, 
                        ArrayLiteral([IntLiteral(2), IntLiteral(3)], FloatType(), 
                            [FloatLiteral(1.1), FloatLiteral(2.2), FloatLiteral(3.3), 
                            FloatLiteral(4.4), FloatLiteral(5.5), FloatLiteral(6.6)]
                        )
                    )
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
 
        
    def test_060(self):
        input = """
        func mergeSort(arr [10]int, left int, right int) {
            if (left < right) {
                var mid = (left + right) / 2;
                mergeSort(arr, left, mid);
                mergeSort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }
        """
        expect = str(Program([FuncDecl("mergeSort",[ParamDecl("arr",ArrayType([IntLiteral(10)],IntType())),ParamDecl("left",IntType()),ParamDecl("right",IntType())],VoidType(),Block([If(BinaryOp("<", Id("left"), Id("right")), Block([VarDecl("mid", None,BinaryOp("/", BinaryOp("+", Id("left"), Id("right")), IntLiteral(2))),FuncCall("mergeSort",[Id("arr"),Id("left"),Id("mid")]),FuncCall("mergeSort",[Id("arr"),BinaryOp("+", Id("mid"), IntLiteral(1)),Id("right")]),FuncCall("merge",[Id("arr"),Id("left"),Id("mid"),Id("right")])]), None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360)) 
        
    def test_061(self):
        input = """
            func isSorted(arr [5]int) boolean {
                for i := 1; i < 5; i += 1 {
                    if(arr[i-1] > arr[i]) {
                        return false;
                    }
                }
                return true;
            }
        """
        expect = str(Program([
            FuncDecl("isSorted", 
                [ParamDecl("arr", ArrayType([IntLiteral(5)], IntType()))], 
                BoolType(), 
                Block([
                    ForStep(
                        Assign(Id("i"), IntLiteral(1)), 
                        BinaryOp("<", Id("i"), IntLiteral(5)), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            If(BinaryOp(">", ArrayCell(Id("arr"), [BinaryOp("-", Id("i"), IntLiteral(1))]), 
                                        ArrayCell(Id("arr"), [Id("i")])), 
                            Block([Return(BooleanLiteral(False))]), None)
                        ])
                    ),
                    Return(BooleanLiteral(True))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

        
    def test_062(self):
        input = """
            func arraySortedOrNot(arr [2]int, n int) int {
                if(n == 0 || n == 1) {
                    return 1;
                }
                for i := 1; i < 5; i += 1 {
                    if(arr[i - 1] > arr[i]) {
                        return 0;
                    }
                }
                return 1;
            }
        """
        expect = str(Program([
            FuncDecl("arraySortedOrNot", 
                [ParamDecl("arr", ArrayType([IntLiteral(2)], IntType())), 
                ParamDecl("n", IntType())], 
                IntType(), 
                Block([
                    If(BinaryOp("||", BinaryOp("==", Id("n"), IntLiteral(0)), 
                                    BinaryOp("==", Id("n"), IntLiteral(1))), 
                    Block([Return(IntLiteral(1))]), None),
                    ForStep(
                        Assign(Id("i"), IntLiteral(1)), 
                        BinaryOp("<", Id("i"), IntLiteral(5)), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            If(BinaryOp(">", ArrayCell(Id("arr"), [BinaryOp("-", Id("i"), IntLiteral(1))]), 
                                        ArrayCell(Id("arr"), [Id("i")])), 
                            Block([Return(IntLiteral(0))]), None)
                        ])
                    ),
                    Return(IntLiteral(1))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

        
    def test_063(self):
        input = """
        func isIntersect(arr [10]Interval, n int) boolean {
            sort(arr, n, compareInterval);
            for var i int = 1; i < n; i+=1 {
                if (arr[i - 1].end > arr[i].start) {
                    return true;
                }
            }
            return false;
        }
        """
        expect = str(Program([
            FuncDecl("isIntersect",
                [ParamDecl("arr", ArrayType([IntLiteral(10)], Id("Interval"))),
                ParamDecl("n", IntType())],
                BoolType(),
                Block([
                    FuncCall("sort", [Id("arr"), Id("n"), Id("compareInterval")]),  # Sửa cách gọi sort
                    ForStep(
                        VarDecl("i",IntType(),IntLiteral(1)), 
                        BinaryOp("<", Id("i"), Id("n")), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp(">", 
                                    FieldAccess(ArrayCell(Id("arr"), [BinaryOp("-", Id("i"), IntLiteral(1))]), "end"), 
                                    FieldAccess(ArrayCell(Id("arr"), [Id("i")]), "start")
                                ),
                                Block([Return(BooleanLiteral(True))]), 
                                None
                            )
                        ])
                    ),
                    Return(BooleanLiteral(False))
                ])
            )
        ]))
        
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

        
    def test_064(self):
        input = """
        func hasTripletSum(arr [10]int,target int) boolean {
            var n int = arr.size();
            for i := 0; i < n - 2; i+=1 {
                for j := i + 1; j < n - 1; j+=1 {
                    for k := j + 1; k < n; k+=1 { 
                        if (arr[i] + arr[j] + arr[k] == target){
                            return true;
                        } 
                    } 
                } 
            } 
            return false; 
        } 
        """
        expect = str(Program([
    FuncDecl("hasTripletSum", 
        [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType())), 
         ParamDecl("target", IntType())], 
        BoolType(), 
        Block([
            VarDecl("n", IntType(), MethCall(Id("arr"), "size", [])),
            ForStep(
                Assign(Id("i"), IntLiteral(0)), 
                BinaryOp("<", Id("i"), BinaryOp("-", Id("n"), IntLiteral(2))), 
                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                Block([
                    ForStep(
                        Assign(Id("j"), BinaryOp("+", Id("i"), IntLiteral(1))), 
                        BinaryOp("<", Id("j"), BinaryOp("-", Id("n"), IntLiteral(1))), 
                        Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
                        Block([
                            ForStep(
                                Assign(Id("k"), BinaryOp("+", Id("j"), IntLiteral(1))), 
                                BinaryOp("<", Id("k"), Id("n")), 
                                Assign(Id("k"), BinaryOp("+", Id("k"), IntLiteral(1))),
                                Block([
                                    If(BinaryOp("==", 
                                                BinaryOp("+", BinaryOp("+", 
                                                                        ArrayCell(Id("arr"), [Id("i")]), 
                                                                        ArrayCell(Id("arr"), [Id("j")])
                                                                    ), 
                                                            ArrayCell(Id("arr"), [Id("k")])
                                                        ), 
                                                Id("target")), 
                                       Block([Return(BooleanLiteral(True))]), None)
                                ])
                            )
                        ])
                    )
                ])
            ),
            Return(BooleanLiteral(False))
        ])
    )
]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
        
    def test_065(self):
        input = """
            func if_test(){
                if(6) {
                  return;
                }else if(4) {
                    return 6;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("if_test",[],VoidType(),Block([
            If(IntLiteral(6), Block([Return(None)]), 
                If(IntLiteral(4), Block([Return(IntLiteral(6)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))
        
    def test_066(self):
        input = """
            func main(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))
        
    def test_067(self):
        input = """
            func main(){
                a["hi"][take()] := a[10][3][5];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("\"hi\""),FuncCall("take",[])]),ArrayCell(Id("a"),[IntLiteral(10),IntLiteral(3),IntLiteral(5)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))
        
    def test_068(self):
        input = """
        func lcm(a int, b int) int {
            return (a * b) / gcd(a, b);
        }
        """
        expect = str(Program([FuncDecl("lcm",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([Return(BinaryOp("/", BinaryOp("*", Id("a"), Id("b")), FuncCall("gcd",[Id("a"),Id("b")])))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
        
    def test_069(self):
        input = """
        func nthFibonacci(n int) int {
            var a = 0;
            var b = 1;
            for i := 2; i <= n; i += 1 {
                var temp = a + b;
                a := b;
                b := temp;
            }
            return b;
        }
        """
        expect = str(Program([FuncDecl("nthFibonacci",[ParamDecl("n",IntType())],IntType(),Block([VarDecl("a", None,IntLiteral(0)),VarDecl("b", None,IntLiteral(1)),ForStep(Assign(Id("i"),IntLiteral(2)),BinaryOp("<=", Id("i"), Id("n")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([VarDecl("temp", None,BinaryOp("+", Id("a"), Id("b"))),Assign(Id("a"),Id("b")),Assign(Id("b"),Id("temp"))])),Return(Id("b"))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
        
    def test_070(self):
        input = """
            func findMinDiff(arr [10]int, m int) int {
                n := 10;
                sort(arr);
                minDiff := INT_MAX;

                for i := 0; i + m - 1 < n; i += 1 {
                    diff := arr[i + m - 1] - arr[i];
                    if (diff < minDiff) {
                        minDiff := diff;
                    }
                }
                return minDiff;
            }
        """
        expect = str(Program([
            FuncDecl("findMinDiff", 
                [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType())), 
                ParamDecl("m", IntType())], 
                IntType(), 
                Block([
                    Assign(Id("n"), IntLiteral(10)),  
                    FuncCall("sort", [Id("arr")]),  
                    Assign(Id("minDiff"), Id("INT_MAX")),  
                    ForStep(
                        Assign(Id("i"), IntLiteral(0)), 
                        BinaryOp("<", BinaryOp("-", BinaryOp("+", Id("i"), Id("m")), IntLiteral(1)), Id("n")),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            Assign(Id("diff"), 
                                BinaryOp("-", 
                                    ArrayCell(Id("arr"), [BinaryOp("-", BinaryOp("+", Id("i"), Id("m")), IntLiteral(1))]),
                                    ArrayCell(Id("arr"), [Id("i")])
                                )
                            ),
                            If(BinaryOp("<", Id("diff"), Id("minDiff")),
                            Block([
                                Assign(Id("minDiff"), Id("diff"))
                            ]), 
                            None)
                        ])
                    ),
                    Return(Id("minDiff"))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

        
    def test_071(self):
        input = """
            func search(arr [20]int,x int) int {
                for i := 0; i < arr.size(); i+=1{
                    if (arr[i] == x){
                        return i;
                    }
                }
                return -1;
            }
        """
        expect = str(Program([
    FuncDecl("search",
        [ParamDecl("arr", ArrayType([IntLiteral(20)], IntType())),
         ParamDecl("x", IntType())],
        IntType(),
        Block([
            ForStep(
                Assign(Id("i"), IntLiteral(0)),
                BinaryOp("<", Id("i"), MethCall(Id("arr"),"size", [])),
                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                Block([
                    If(BinaryOp("==", ArrayCell(Id("arr"), [Id("i")]), Id("x")),
                        Block([Return(Id("i"))]), None)
                ])
            ),
            Return(UnaryOp("-", IntLiteral(1)))
        ])
    )
]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
        
    def test_072(self):
        input = """
            func binarySearch(arr [5]int, low int,high int,x int) int {
                if (high >= low) {
                    var mid int = low + (high - low) / 2;
                    if (arr[mid] == x){
                        return mid;
                    }
                    if (arr[mid] > x){
                        return binarySearch(arr, low, mid - 1, x);
                    }
                    return binarySearch(arr, mid + 1, high, x);
                }
            return -1;
            }
        """
        expect = str(Program([
    FuncDecl("binarySearch",
        [ParamDecl("arr", ArrayType([IntLiteral(5)], IntType())),
         ParamDecl("low", IntType()),
         ParamDecl("high", IntType()),
         ParamDecl("x", IntType())],
        IntType(),
        Block([
            If(BinaryOp(">=", Id("high"), Id("low")),
                Block([
                    VarDecl("mid", IntType(),
                        BinaryOp("+", Id("low"),
                            BinaryOp("/", BinaryOp("-", Id("high"), Id("low")), IntLiteral(2)))
                    ),
                    If(BinaryOp("==", ArrayCell(Id("arr"), [Id("mid")]), Id("x")),
                        Block([Return(Id("mid"))]), None
                    ),
                    If(BinaryOp(">", ArrayCell(Id("arr"), [Id("mid")]), Id("x")),
                        Block([Return(FuncCall("binarySearch", [
                            Id("arr"), Id("low"),
                            BinaryOp("-", Id("mid"), IntLiteral(1)), Id("x")
                        ]))]), None
                    ),
                    Return(FuncCall("binarySearch", [
                        Id("arr"),
                        BinaryOp("+", Id("mid"), IntLiteral(1)),
                        Id("high"), Id("x")
                    ]))
                ]),None
            ),
            Return(UnaryOp("-", IntLiteral(1)))
        ])
    )
]))


        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
        
    def test_073(self):
        input = """
        func twoSum(arr [10]int, target int) boolean {
            var n int = arr.size();
            for i := 0; i < n; i+=1 {
                for j := i + 1; j < n; j+=1 {
                    if (arr[i] + arr[j] == target) {
                        return true;
                    }
                }
            }
            return false;
        }
        """
        expect = str(Program([
    FuncDecl("twoSum",
        [ParamDecl("arr", ArrayType([IntLiteral(10)], IntType())),
         ParamDecl("target", IntType())],
        BoolType(),
        Block([
            VarDecl("n", IntType(), MethCall(Id("arr"), "size", [])),
            ForStep(
                Assign(Id("i"), IntLiteral(0)),
                BinaryOp("<", Id("i"), Id("n")),
                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                Block([
                    ForStep(
                        Assign(Id("j"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        BinaryOp("<", Id("j"), Id("n")),
                        Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
                        Block([
                            If(BinaryOp("==", BinaryOp("+", ArrayCell(Id("arr"), [Id("i")]), 
                                                    ArrayCell(Id("arr"), [Id("j")])), 
                                        Id("target")),
                                Block([Return(BooleanLiteral(True))])
                            ,None)
                        ])
                    )
                ])
            ),
            Return(BooleanLiteral(False))
        ])
    )
]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
        
    def test_074(self):
        input = """
        func foo(){
            execute("hello");
            execute1(execute("hello"));
            execute2(execute1(execute("hello")));
            execute3(execute2(execute1(execute("hello"))));
            execute4(execute3(execute2(execute1(execute("hello")))))
            execute5(execute4(execute3(execute2(execute1(execute("hello"))))))
            execute6(execute5(execute4(execute3(execute2(execute1(execute("hello")))))))
            execute7(execute6(execute5(execute4(execute3(execute2(execute1(execute("hello"))))))))
            execute8(execute7(execute6(execute5(execute4(execute3(execute2(execute1(execute("hello")))))))))
            execute9(execute8(execute7(execute6(execute5(execute4(execute3(execute2(execute1(execute("hello"))))))))))
        } 
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("execute",[StringLiteral("\"hello\"")]),FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])]),FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])]),FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])]),FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])]),FuncCall("execute5",[FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])])]),FuncCall("execute6",[FuncCall("execute5",[FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])])])]),FuncCall("execute7",[FuncCall("execute6",[FuncCall("execute5",[FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])])])])]),FuncCall("execute8",[FuncCall("execute7",[FuncCall("execute6",[FuncCall("execute5",[FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])])])])])]),FuncCall("execute9",[FuncCall("execute8",[FuncCall("execute7",[FuncCall("execute6",[FuncCall("execute5",[FuncCall("execute4",[FuncCall("execute3",[FuncCall("execute2",[FuncCall("execute1",[FuncCall("execute",[StringLiteral("\"hello\"")])])])])])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))
        
    def test_075(self):
        input = """
        func get3largest(arr [20]int) [4]int {
            var fst int = INT_MIN; 
            var sec int = INT_MIN; 
            var thd int = INT_MIN;
            
            for x, _ := range arr {
                if (x > fst){
                    thd := sec;
                    sec := fst;
                    fst := x;
                } else if (x > sec && x != fst){
                    thd := sec;
                    sec := x;
                } else if (x > thd && x != sec && x != fst){
                    thd := x;
                }
            }

            var res = [6]int{1,2,3};
            if (fst == INT_MIN){
                return res;
            }
            res.push_back(fst);
            if (sec == INT_MIN){
                return res;
            }
            res.push_back(sec);
            if (thd == INT_MIN){
                return res;
            }
            res.push_back(thd);
            return res;
        }
        """
        expect = "Program([FuncDecl(get3largest,[ParDecl(arr,ArrayType(IntType,[IntLiteral(20)]))],ArrayType(IntType,[IntLiteral(4)]),Block([VarDecl(fst,IntType,Id(INT_MIN)),VarDecl(sec,IntType,Id(INT_MIN)),VarDecl(thd,IntType,Id(INT_MIN)),ForEach(Id(x),Id(_),Id(arr),Block([If(BinaryOp(Id(x),>,Id(fst)),Block([Assign(Id(thd),Id(sec)),Assign(Id(sec),Id(fst)),Assign(Id(fst),Id(x))]),If(BinaryOp(BinaryOp(Id(x),>,Id(sec)),&&,BinaryOp(Id(x),!=,Id(fst))),Block([Assign(Id(thd),Id(sec)),Assign(Id(sec),Id(x))]),If(BinaryOp(BinaryOp(BinaryOp(Id(x),>,Id(thd)),&&,BinaryOp(Id(x),!=,Id(sec))),&&,BinaryOp(Id(x),!=,Id(fst))),Block([Assign(Id(thd),Id(x))]))))])),VarDecl(res,ArrayLiteral([IntLiteral(6)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),If(BinaryOp(Id(fst),==,Id(INT_MIN)),Block([Return(Id(res))])),MethodCall(Id(res),push_back,[Id(fst)]),If(BinaryOp(Id(sec),==,Id(INT_MIN)),Block([Return(Id(res))])),MethodCall(Id(res),push_back,[Id(sec)]),If(BinaryOp(Id(thd),==,Id(INT_MIN)),Block([Return(Id(res))])),MethodCall(Id(res),push_back,[Id(thd)]),Return(Id(res))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
        
    def test_076(self):
        input = """
        func anhinla(a [10]int) {
            a[2 + 3 * (4 - 1)] := a[1] + a[2 * 3] / 2;
            a[a[3] % 5] := a[a[4]] + 10;
        }
        """
        expect = str(Program([FuncDecl("anhinla",[ParamDecl("a",ArrayType([IntLiteral(10)],IntType()))],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(2), BinaryOp("*", IntLiteral(3), BinaryOp("-", IntLiteral(4), IntLiteral(1))))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(1)]), BinaryOp("/", ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(2), IntLiteral(3))]), IntLiteral(2)))),Assign(ArrayCell(Id("a"),[BinaryOp("%", ArrayCell(Id("a"),[IntLiteral(3)]), IntLiteral(5))]),BinaryOp("+", ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(4)])]), IntLiteral(10)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
        
    def test_077(self):
        input = """
        var x int = 10;
        var y float = 20.5;
        var z string = "hello";
        """
        expect = str(Program([
            VarDecl("x", IntType(), IntLiteral(10)),
            VarDecl("y", FloatType(), FloatLiteral(20.5)),
            VarDecl("z", StringType(), StringLiteral("\"hello\""))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
        
        
    def test_078(self):
        input = """
        func hi(a int, b int, c int, d int, e int) int {
            if (a > b && (c > d || e > a) && !(a == c)) {
                if (a % 2 == 0 && b % 2 == 0) {
                    if (c % 3 == 0 || d % 3 == 0) {
                        if (e % 5 == 0) {
                            return a * b + c * d - e;
                        } else if (e % 4 == 0) {
                            if (a > c + d) {
                                return a - b + c;
                            } else {
                                return b - a + d;
                            }
                        }
                    } else if (c % 5 == 0 && d % 5 != 0) {
                        return c * d / (a + 1);
                    }
                } else if (a % 3 == 0 || b % 3 == 0) {
                    if (c * d > a * b && e < a + b + c) {
                        return (a + b) * (c - d) / (e + 1);
                    } else {
                        return (a - b) * (c + d) / (e - 1);
                    }
                }
            } else if (b > a && (d > c || e > b) && !(b == d)) {
                return b * c + a * d - e * e;
            } else if (c > a && c > b && (d > a || e > b)) {
                return c * c - a * b + d * e;
            } else {
                return (a + b + c + d + e) / 5;
            }
            return 0;
        }
        """

        expect = str(Program([FuncDecl("hi",[ParamDecl("a",IntType()),ParamDecl("b",IntType()),ParamDecl("c",IntType()),ParamDecl("d",IntType()),ParamDecl("e",IntType())],IntType(),Block([If(BinaryOp("&&", BinaryOp("&&", BinaryOp(">", Id("a"), Id("b")), BinaryOp("||", BinaryOp(">", Id("c"), Id("d")), BinaryOp(">", Id("e"), Id("a")))), UnaryOp("!",BinaryOp("==", Id("a"), Id("c")))), Block([If(BinaryOp("&&", BinaryOp("==", BinaryOp("%", Id("a"), IntLiteral(2)), IntLiteral(0)), BinaryOp("==", BinaryOp("%", Id("b"), IntLiteral(2)), IntLiteral(0))), Block([If(BinaryOp("||", BinaryOp("==", BinaryOp("%", Id("c"), IntLiteral(3)), IntLiteral(0)), BinaryOp("==", BinaryOp("%", Id("d"), IntLiteral(3)), IntLiteral(0))), Block([If(BinaryOp("==", BinaryOp("%", Id("e"), IntLiteral(5)), IntLiteral(0)), Block([Return(BinaryOp("-", BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), BinaryOp("*", Id("c"), Id("d"))), Id("e")))]), If(BinaryOp("==", BinaryOp("%", Id("e"), IntLiteral(4)), IntLiteral(0)), Block([If(BinaryOp(">", Id("a"), BinaryOp("+", Id("c"), Id("d"))), Block([Return(BinaryOp("+", BinaryOp("-", Id("a"), Id("b")), Id("c")))]), Block([Return(BinaryOp("+", BinaryOp("-", Id("b"), Id("a")), Id("d")))]))]), None))]), If(BinaryOp("&&", BinaryOp("==", BinaryOp("%", Id("c"), IntLiteral(5)), IntLiteral(0)), BinaryOp("!=", BinaryOp("%", Id("d"), IntLiteral(5)), IntLiteral(0))), Block([Return(BinaryOp("/", BinaryOp("*", Id("c"), Id("d")), BinaryOp("+", Id("a"), IntLiteral(1))))]), None))]), If(BinaryOp("||", BinaryOp("==", BinaryOp("%", Id("a"), IntLiteral(3)), IntLiteral(0)), BinaryOp("==", BinaryOp("%", Id("b"), IntLiteral(3)), IntLiteral(0))), Block([If(BinaryOp("&&", BinaryOp(">", BinaryOp("*", Id("c"), Id("d")), BinaryOp("*", Id("a"), Id("b"))), BinaryOp("<", Id("e"), BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("c")))), Block([Return(BinaryOp("/", BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))), BinaryOp("+", Id("e"), IntLiteral(1))))]), Block([Return(BinaryOp("/", BinaryOp("*", BinaryOp("-", Id("a"), Id("b")), BinaryOp("+", Id("c"), Id("d"))), BinaryOp("-", Id("e"), IntLiteral(1))))]))]), None))]), If(BinaryOp("&&", BinaryOp("&&", BinaryOp(">", Id("b"), Id("a")), BinaryOp("||", BinaryOp(">", Id("d"), Id("c")), BinaryOp(">", Id("e"), Id("b")))), UnaryOp("!",BinaryOp("==", Id("b"), Id("d")))), Block([Return(BinaryOp("-", BinaryOp("+", BinaryOp("*", Id("b"), Id("c")), BinaryOp("*", Id("a"), Id("d"))), BinaryOp("*", Id("e"), Id("e"))))]), If(BinaryOp("&&", BinaryOp("&&", BinaryOp(">", Id("c"), Id("a")), BinaryOp(">", Id("c"), Id("b"))), BinaryOp("||", BinaryOp(">", Id("d"), Id("a")), BinaryOp(">", Id("e"), Id("b")))), Block([Return(BinaryOp("+", BinaryOp("-", BinaryOp("*", Id("c"), Id("c")), BinaryOp("*", Id("a"), Id("b"))), BinaryOp("*", Id("d"), Id("e"))))]), Block([Return(BinaryOp("/", BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), Id("c")), Id("d")), Id("e")), IntLiteral(5)))])))),Return(IntLiteral(0))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
        
    def test_079(self):
        input = """
        func getFirstElement(arr [5]int) int {
            return arr[0];
        }
        """
        expect = str(Program([
            FuncDecl("getFirstElement", [ParamDecl("arr", ArrayType([IntLiteral(5)], IntType()))], IntType(),
                Block([
                    Return(ArrayCell(Id("arr"), [IntLiteral(0)]))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))


        
    def test_080(self):
        input = """
        func sumToN(n int) int {
            var sum int = 0;
            for i := 1; i <= n; i += 1 {
                sum += i;
            }
            return sum;
        }
        """
        expect = str(Program([
            FuncDecl("sumToN", [ParamDecl("n", IntType())], IntType(), 
                Block([
                    VarDecl("sum", IntType(), IntLiteral(0)),
                    ForStep(
                        Assign(Id("i"), IntLiteral(1)),
                        BinaryOp("<=", Id("i"), Id("n")),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))
                        ])
                    ),
                    Return(Id("sum"))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

        
    def test_081(self):
        input = """
        func main() {
            var result int = add(multiply(2, 3), subtract(10, 5));
        }
        """
        expect = str(Program([
            FuncDecl("main",
                [],
                VoidType(),
                Block([
                    VarDecl("result", IntType(),
                        FuncCall("add", [
                            FuncCall("multiply", [IntLiteral(2), IntLiteral(3)]),
                            FuncCall("subtract", [IntLiteral(10), IntLiteral(5)])
                        ]))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))
        
    def test_082(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
            var p Person;
            p.name := "John";
            p.age := 30;
        }
        """
        expect = str(Program([
            StructType("Person",
                [("name", StringType()), ("age", IntType())],
                []),
            FuncDecl("main",
                [],
                VoidType(),
                Block([
                    VarDecl("p", Id("Person"),None),
                    Assign(FieldAccess(Id("p"), "name"), StringLiteral("\"John\"")),
                    Assign(FieldAccess(Id("p"), "age"), IntLiteral(30))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))
        
    def test_083(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 383))

    def test_084(self):
        input = """
            func bar(){
                x[2 + 3] := 5;
            } 
        """
        expect = Program([
            FuncDecl("bar", [], VoidType(), Block([
                Assign(ArrayCell(Id("x"), [BinaryOp("+", IntLiteral(2), IntLiteral(3))]), IntLiteral(5))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 384))
        
    def test_085(self):
        input = """
            func bar(){
                y[3].z.w[4] := 10;
            } 
        """
        expect = Program([
            FuncDecl("bar", [], VoidType(), Block([
                Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("y"), [IntLiteral(3)]), "z"), "w"), [IntLiteral(4)]), IntLiteral(10))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 385))
        
    def test_086(self):
        input = """
            const b = (10 + 20) * (30 - 40) / (50 % 60) && (70 > 80) || (90 <= 100);
        """
        expect = Program([
            ConstDecl("b", None, 
                BinaryOp("||", 
                    BinaryOp("&&", 
                        BinaryOp("/", 
                            BinaryOp("*", 
                                BinaryOp("+", IntLiteral(10), IntLiteral(20)), 
                            BinaryOp("-", IntLiteral(30), IntLiteral(40))), 
                        BinaryOp("%", IntLiteral(50), IntLiteral(60))), 
                    BinaryOp(">", IntLiteral(70), IntLiteral(80))), 
                BinaryOp("<=", IntLiteral(90), IntLiteral(100))))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 386))

    def test_087(self):
        input = """
        func foo() {
            for _, v := range ID{} {
                aa := 1;
                for _, v := range ID{} {
                    aa := 1;
                    for _, v := range ID{} {
                        aa := 1;
                        for _, v := range ID{} {
                            aa := 1;
                        }
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("_"),Id("v"),StructLiteral("ID",[]),Block([Assign(Id("aa"),IntLiteral(1)),ForEach(Id("_"),Id("v"),StructLiteral("ID",[]),Block([Assign(Id("aa"),IntLiteral(1)),ForEach(Id("_"),Id("v"),StructLiteral("ID",[]),Block([Assign(Id("aa"),IntLiteral(1)),ForEach(Id("_"),Id("v"),StructLiteral("ID",[]),Block([Assign(Id("aa"),IntLiteral(1))]))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
        
    def test_088(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 388))
        
    
    def test_089(self):
        input = """
            func checkEvenOdd(num int) string {
                if (num % 2 == 0) {
                    return "Even";
                } else {
                    return "Odd";
                }
            }
        """
        expect = Program([
            FuncDecl("checkEvenOdd",
                [ParamDecl("num", IntType())],
                StringType(),
                Block([
                    If(
                        BinaryOp("==", BinaryOp("%", Id("num"), IntLiteral(2)), IntLiteral(0)),
                        Block([Return(StringLiteral("\"Even\""))]),
                        Block([Return(StringLiteral("\"Odd\""))])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 389))
        
    def test_090(self):
        input = """
            func main() {
                var matrix [2][2]int = [2][2]int{{1, 2}, {3, 4}};
                var result int = matrix[1][1];
            }
        """
        expect = Program([
            FuncDecl("main",
                [],
                VoidType(),
                Block([
                    VarDecl("matrix", ArrayType([IntLiteral(2), IntLiteral(2)], IntType()),
                        ArrayLiteral([IntLiteral(2), IntLiteral(2)],IntType(),[
                            [IntLiteral(1), IntLiteral(2)],
                            [IntLiteral(3), IntLiteral(4)]]
                        )),
                    VarDecl("result", IntType(), ArrayCell(Id("matrix"), [IntLiteral(1), IntLiteral(1)]))
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 390))
        
    def test_091(self):
        input = """
            func printArray(arr [5]int) {
                for i := 0; i < 5; i := i + 1 {
                    print(arr[i]);
                }
            }
        """
        expect = Program([
            FuncDecl("printArray",
                [ParamDecl("arr", ArrayType([IntLiteral(5)], IntType()))],
                VoidType(),
                Block([
                    ForStep(
                        Assign(Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(5)),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            FuncCall("print", [ArrayCell(Id("arr"), [Id("i")])])
                        ])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 391))
        
    def test_110(self):
        input = """
            func isPrime(n int) boolean {
                if (n <= 1) {
                    return false;
                }
                for i := 2; i * i <= n; i := i + 1 {
                    if (n % i == 0) {
                        return false;
                    }
                }
                return true;
            }
        """
        expect = Program([
            FuncDecl("isPrime",
                [ParamDecl("n", IntType())],
                BoolType(),
                Block([
                    If(
                        BinaryOp("<=", Id("n"), IntLiteral(1)),
                        Block([Return(BooleanLiteral(False))]),
                        None
                    ),
                    ForStep(
                        Assign(Id("i"), IntLiteral(2)),
                        BinaryOp("<=", BinaryOp("*", Id("i"), Id("i")), Id("n")),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), IntLiteral(0)),
                                Block([Return(BooleanLiteral(False))]),
                                None
                            )
                        ])
                    ),
                    Return(BooleanLiteral(True))
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 392))
        
    def test_093(self):
        input = """
        func getNumber() int {
            return 42;
        }
        """
        expect = str(Program([
            FuncDecl("getNumber", [], IntType(), 
                Block([
                    Return(IntLiteral(42))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

        
    def test_094(self):
        input = """
        func min(a int, b int) int {
            if (a < b) {
                return a;
            }
            return b;
        }
        """
        expect = str(Program([
            FuncDecl("min", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(),
                Block([
                    If(BinaryOp("<", Id("a"), Id("b")),
                        Block([Return(Id("a"))]),
                        None
                    ),
                    Return(Id("b"))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

        
    def test_095(self):
        input = """
        func matrixSum(mat [3][3]int) int {
            var sum int = 0;
            for i := 0; i < 3; i+=1 {
                for j := 0; j < 3; j+=1 {
                    sum += mat[i][j];
                }
            }
            return sum;
        }
        """
        expect = str(Program([
            FuncDecl("matrixSum", [ParamDecl("mat", ArrayType([IntLiteral(3), IntLiteral(3)], IntType()))], IntType(),
                Block([
                    VarDecl("sum", IntType(), IntLiteral(0)),
                    ForStep(
                        Assign(Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(3)),
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            ForStep(
                                Assign(Id("j"), IntLiteral(0)),
                                BinaryOp("<", Id("j"), IntLiteral(3)),
                                Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
                                Block([
                                    Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("mat"), [Id("i"), Id("j")])))
                                ])
                            )
                        ])
                    ),
                    Return(Id("sum"))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

        
    def test_096(self):
        input = """
            func printHello() {
                print("Hello, World!");
            }
        """
        expect = Program([
            FuncDecl("printHello",
                [],
                VoidType(),
                Block([
                    FuncCall("print", [StringLiteral("\"Hello, World!\"")])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 396))
        
    def test_097(self):
        input = """
        func isEven(n int) bool {
            return n % 2 == 0;
        }
        """
        expect = str(Program([
            FuncDecl("isEven", [ParamDecl("n", IntType())], Id("bool"),
                Block([
                    Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

        
    def test_098(self):
        input = """
        func greet(name string) string {
            return "Hello, " + name + "!";
        }
        """
        expect = str(Program([
            FuncDecl("greet", [ParamDecl("name", StringType())], StringType(),
                Block([
                    Return(BinaryOp("+", BinaryOp("+", StringLiteral("\"Hello, \""), Id("name")), StringLiteral("\"!\"")))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_099(self):
        input = """
        func getPi() float {
            return 3.14159;
        }
        """
        expect = str(Program([
            FuncDecl("getPi", [], FloatType(),
                Block([
                    Return(FloatLiteral(3.14159))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_100(self):
        input = """
        func isValid(a boolean, b boolean) boolean {
            return a && !b;
        }
        """
        expect = str(Program([
            FuncDecl("isValid", [ParamDecl("a", BoolType()), ParamDecl("b", BoolType())], BoolType(),
                Block([
                    Return(BinaryOp("&&", Id("a"), UnaryOp("!", Id("b"))))
                ])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))


    