import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
        
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_const_declaration(self):
        "test const declare"
        input = """const tuanhanhdeptrai = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
        
    def test_const_declaration_1(self):
        "test const declare"
        input = """const tuanhanhdeptrai = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
        
    def test_const_declaration_2(self):
        "test const declare"
        input = """const tuanhanhdeptrai = [5][0]int{1, \"tuananhdeptrai\", 4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
        
    def test_const_declaration_3(self):
        "test const declare"
        input = """const tuanhanhdeptrai = Person{name: \"Tuanemtramtinh\", university: HCMUT, age: 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
        
    def test_const_declaration_4(self):
        "test const declare"
        input = """const tuanhanhdeptrai = -1 + 2 * 2 / 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
        
    def test_const_declaration_5(self):
        "test const declare"
        input = """const tuanhanhdeptrai = a[1].c.b[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_const_declaration_6(self):
        "test const declare"
        input = """const tuanhanhdeptrai = a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
        
    def test_const_declaration_7(self):
        "test const declare"
        input = """const tuanhanhdeptrai = c[5][6];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
        
    def test_const_declaration_8(self):
        "test const declare"
        input = """const tuanhanhdeptrai = c[5][6].a[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
        
    def test_const_declaration_9(self):
        "test const declare"
        input = """const tuanhanhdeptrai = d(1, 2);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
        
    def test_const_declaration_10(self):
        "test const declare"
        input = """const tuanhanhdeptrai = d();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
        
    def test_const_declaration_11(self):
        "test const declare"
        input = """const tuanhanhdeptrai = a[1].b.d(1,2);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
        
    def test_const_declaration_12(self):
        "test const declare"
        input = """const tuanhanhdeptrai = 1 + b * a[1].b.d(1,2) / a[1][2] - foo(2)[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_var_declaration(self):
        input = """var y = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
        
    def test_var_declaration_1(self):
        input = """var x int = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
        
    def test_var_declaration_2(self):
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_func_declaration(self):
        input = """
        func Add(x int, y int) int {
            return x + y;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
        
    def test_func_declaration_1(self):
        input = """
        func Add(x int, y int) int {
            return x + y;
        }
        func Sub(x int, y int) int {
            return x - y;
        }
        func Mul(x int, y int) int {
            return x * y;
        }
        func Div(x int, y int) float {
            return x / y;
        }
        func Mod(x int, y int) int {
            return x % y;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
        
    def test_func_declaration_2(self):
        input = """
        func Add(x int, y int) [1][1]int {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
        
    def test_func_declaration_3(self):
        input = """
        func Add(x tuanemdeptrai) tuananhdeptrai{}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
        
    def test_method_declaration(self):
        input = """
        func (s Student) Submit(x int) int {
            var form = s.form;
            return form;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
        
    def test_method_declaration_1(self):
        input = """
        func (s Student) Submit() Student {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
        
    def test_struct_declaration(self):
        input = """
        type Student struct {
            name string;
            age int;
            school string;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
        
    def test_struct_declaration_1(self):
        input = """
        type Student struct {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
        
    def test_struct_declaration_2(self):
        input = """
        type Student struct {
            maze [100][100] int;
            scholarship Scholar;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
        
    def test_interface_declaration(self):
        input = """
        type Student interface {
            Add(x, y int) int;
            
            Subtract(a, b float, c int) float;
            
            
            
            Reset()
            
            
            SayHello(name string)
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
        
    def test_interface_declaration_1(self):
        input = """
        type Student interface {}; type S interface {}
        type K interface{}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
        
    def test_illegal_var_declaration(self):
        input = """
        const tuanhanhdeptrai = a[1].b.d(1,);
        """
        expect = "Error on line 2 col 44: )"
        self.assertTrue(TestParser.checkParser(input,expect,233))
        
    def test_illegal_var_declaration_1(self):
        input = """
        const tuanhanhdeptrai = a[1].b.d.;
        """
        expect = "Error on line 2 col 42: ;"
        self.assertTrue(TestParser.checkParser(input,expect,234))
        
    def test_illegal_var_declaration_2(self):
        input = """
        const tuanhanhdeptrai = Student {student hcmut};
        """
        expect = "Error on line 2 col 41: {"
        self.assertTrue(TestParser.checkParser(input,expect,235))
        
    def test_illegal_var_declaration_3(self):
        input = """
        const tuanhanhdeptrai = a[1,2,4][2];
        """
        expect = "Error on line 2 col 36: ,"
        self.assertTrue(TestParser.checkParser(input,expect,236))
        
    def test_statement(self):
        input = """
        func foo() {
            var x int = 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
        
    def test_statement_1(self):
        input = """
        func foo() {
            var x string = "Tuananh";
            var y int = 6;
            var z = 0.5;
            const x = 3.15;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
        
    def test_statement_2(self):
        input = """
        func foo() {
            a := 5 + 6;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
        
    def test_statement_3(self):
        input = """
        func foo() {
            a[1][2] := c[1]
            for i := 0; i < 10; i += 1 {}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
        
    def test_statement_4(self):
        input = """
        func foo() {
            if (x > 10) {} 
            if (x > 10) {
                
            }
            else if (x == 10) {
                var z str;
            } else {
                var z ID;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    
    def test_statement_5(self):
        input = """
        func foo() {
            if (x > 10) {} 
            if (x > 10) {} else if (x == 10) { var z str;} else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
        
    def test_statement_6(self):
        input = """
        func foo() {
            if (x > 10) {} 
            if (x > 10) {} else if (x == 10) { var z str;} 
            else if (x >= 20) {} else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
        
    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", 243))