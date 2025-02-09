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
            if (x > 10) {} else if (x == 10) { var z str;} 
            else if (x >= 20) {} else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_statement_7(self):
        input = """
        func foo() {
            if (x > 10) {} else { var z ID;}
            if (x > 10) {} 
            else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
        
    def test_statement_8(self):
        input = """    
            func test() {                           
                for i < 10 {break;}                  
             }                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))
        
    def test_statement_9(self):
        input = """
        func test(){
            for i := 0; i < 10000; i+=1 {}   
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))
        
    def test_statement_10(self):
        input = """
        func test(){
            for index, value := range array {}   
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 247))
        
    def test_statement_11(self):
        input = """
        func primeCheck(n int) bool{
            if (n < 2) {
                return false;
            }
            
            for i := 0; i < n; i += 1 {
                if (n % i == 0) {
                    return false;
                }
            }   
            
            return true;
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 248))
        
    def test_statement_12(self):
        input = """
        func sort(){
            var array = [5]int{5, 3, 1, 4, 2}
            var size = 5
            for var i = 0; i < size - 1; i+=1 {
                for var j = 0; j < size - i - 1; j+=1{
                    if (array[j] > array[j + 1]) {
                        swap(v[j], v[j + 1])
                    }
                }
            }
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 249))
        
    def test_statement_13(self):
        input = """
        func nthFibonacci(n int) int{
            if (n <= 1) {
                return n;
            }
            
            return nthFibonacci(n - 1) + nthFibonacci(n - 2);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 250))
        
    def test_statement_14(self):
        input = """
        func test(){
            for const i := 0; i < 10000; i+=1 {}   
        };"""
        expect = """Error on line 3 col 17: const"""
        self.assertTrue(TestParser.checkParser(input, expect, 251))
        
    def test_statement_15(self):
        input = """
        func binarySearch(arr [10]int, low int, high int, x int) int{
            if (high >= low) {
                var mid = low + (high - low) / 2;
                
                if (arr[mid] == x) {
                    return mid;
                }
                
                if (arr[mid] > x){
                    return binarySearch(arr, low, mid - 1, x);
                }
                
                return binarySearch(arr, mid + 1, high, x);
            }   
            
            return -1;
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 252))
        
    def test_statement_16(self):
        input = """
        const PI = 3.14;
        
        func calcCircleArea(radius float) float {
            return radius * radius * PI;  
        };
        
        func main(){
            calcCircleArea(5.0)
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 253))
        
    def test_statement_17(self):
        input = """
        const PI = 3.14;
        
        func calcCircleArea(radius float) float {
            return radius * radius * PI;  
        };
        
        func main(){
            calcCircleArea(5.0)
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 254))
        
    def test_statement_18(self):
        input = """
        type Shape interface {
            Area() float
            Perimeter() float
            Scale(factor float) float
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 255))
        
    def test_statement_19(self):
        input = """
        func linearSearch(x int, arr [10]int) int{
            var result = -1;
            
            for var i = 0; i < 10; i+=1{
                if (arr[i] == x){
                    result := i;
                    break;
                }
            }
            
            return result;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 256))
        
    def test_statement_20(self):
        input = """
        func Power(base int, exp int) int {
            if (exp == 0) {
                return 1
            }
            return base * Power(base, exp - 1)
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 257))
        
    def test_statement_21(self):
        input = """
        func isPalindrome(s string, left int, right int) bool {
          if (left >= right) {
              return true
          }  
          
          if (s[left] != s[right]) {
              return false
          }
          
          return isPalindrome(s, left + 1, right - 1)
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 258))
        
    def test_statement_22(self):
        input = """func Factorial(n int) int {if (n == 0){return 1;};return isPalindrome(s, left + 1, right - 1);};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 259))
        
    def test_statement_23(self):
        input = """
        func fibonacciIterative(n int) int {
          if (n <= 1) {return n;}
          var a = 0; var b = 1;
          for i := 2; i <= n; i+=1{
              var temp = a
              a := b
              b := temp + a;
          }
          
          return b;
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 260))
        
    def test_statement_24(self):
        input = """
        var z = [3][2]int{1, 2, 3}; 
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 261))