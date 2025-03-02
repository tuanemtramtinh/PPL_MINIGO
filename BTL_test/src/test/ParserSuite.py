import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {const a = 5;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
            const bar = foo;

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
        func Add(x int, y int) [1][1]int {const a = [1][2]int{5};}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
        
    def test_func_declaration_3(self):
        input = """
        func Add(x tuanemdeptrai) tuananhdeptrai{const a = 5 * 3;}
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
        func (s Student) Submit() Student {const point = 100000;}
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
        type Student struct {
            age int;
        }
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
        type Student interface {Add(x, y int) int;}; type S interface {Add(x, y int) int;}
        type K interface{Add(x, y int) int;}
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
        input = """const tuanhanh = Student {student hcmut};"""
        expect = "Error on line 1 col 35: hcmut"
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
            for i := 0; i < 10; i += 1 {
                print(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
        
    def test_statement_4(self):
        input = """
        func foo() {
            if (x > 10) {
                var t string;
            } 
            if (x > 10) {
                var x float;
            } else if (x == 10) {
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
            if (x > 10) {var z s;} 
            if (x > 10) {var b school;} else if (x == 10) { var z str;} else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
        
    def test_statement_6(self):
        input = """
        func foo() {
            if (x > 10) {var b x;} else if (x == 10) { 
                var z str;
            } else if (x >= 20) { const b = 10; } else { var z ID;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_statement_7(self):
        input = """
        func foo() {
            if (x > 10) { const b = 5; } else { var z ID;}
            if (x > 10) {
                const a = 5;    
            } else { var z ID;}
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
            for i := 0; i < 10000; i+=1 {
                print(i)
            }   
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))
        
    def test_statement_10(self):
        input = """
        func test(){
            for index, value := range array {
                x.append(value)
            }   
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
        
    def test_statement_25(self):
        """Statement"""
        input = """
        func Add() {
            const a = a[2].b
            var a = a[2].b; var a = "s";           
        }"""
        expect = "Error on line 5 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 262))
        
    def test_statement_26(self):
        """Statement"""
        input = """
        func Add() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
        
    def test_statement_27(self):
        """Statement"""
        input = """func Add() {
            if (5 - 1) {}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
        
    def test_statement_28(self):
        """Statement"""
        input = """func Add() {
            for i:=0; i < 10000; i+=1 {}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
        
    def test_statement_29(self):
        """Statement"""
        input = """func Add() {
            for i < 5 {}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))
        
    def test_statement_30(self):
        """Statement"""
        input = """func Add() {
            for i < 5 {}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))
        
    def test_statement_31(self):
        """Statement"""
        input = """func Add() {
            for index, value := range array {}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
        
    def test_statement_32(self):
        """Statement"""
        input = """const a = [1][2]int{[1][2]int};"""
        expect = "Error on line 1 col 21: ["
        self.assertTrue(TestParser.checkParser(input, expect, 269))
        
    def test_statement_33(self):
        """Statement"""
        input = """const a = [1][2]int{};"""
        expect = "Error on line 1 col 21: }"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
        
    def test_statement_34(self):
        """Statement"""
        input = """const a = [1][2]int{{}};"""
        expect = "Error on line 1 col 22: }"
        self.assertTrue(TestParser.checkParser(input, expect, 271))
        
    def test_statement_35(self):
        """Statement"""
        input = """type Student interface {}"""
        expect = "Error on line 1 col 25: }"
        self.assertTrue(TestParser.checkParser(input, expect, 272))
        
    def test_statement_36(self):
        """Statement"""
        input = """type Student struct {}"""
        expect = "Error on line 1 col 22: }"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
        
    def test_statement_37(self):
        """Statement"""
        input = """
        func foo(){
            if (1) {
                const a = 10;
            } else {}
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))
        
    def test_statement_38(self):
        """Statement"""
        input = """
        func foo(){
            if (1) {
                const a = 10;
            } else if {
                
            } else {
                const b = 10;
            }
        };
        """
        expect = "Error on line 5 col 23: {"
        self.assertTrue(TestParser.checkParser(input, expect, 275))
        
    def test_statement_39(self):
        """Statement"""
        input = """
        func foo(){
            if (1) {
                const a = 10;
            } else if {
                const b = 100;
            } else {
                
            }
        };
        """
        expect = "Error on line 5 col 23: {"
        self.assertTrue(TestParser.checkParser(input, expect, 276))
        
    def test_statement_40(self):
        """Statement"""
        input = """
        func foo() {
            for i := 0; i < 10; i += 1 {
                for j := 0; j < 10; j += 1 {
                    for k := 0; k < 10; k += 1 {
                        print(i, j, k);
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
        
    def test_statement_41(self):
        """Statement"""
        input = """
        func foo() {
            var arr = [5][5]int{
                {1, 2, 3, 4, 5},
                {6, 7, 8, 9, 10},
                {11, 12, 13, 14, 15},
                {16, 17, 18, 19, 20},
                {21, 22, 23, 24, 25}};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))
        
    def test_statement_42(self):
        """Invalid array index"""
        input = """
        func foo() {
            var x = 5;
            var y = 10;
        """
        expect = "Error on line 5 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 279))
        
    def test_statement_43(self):
        """Invalid array index"""
        input = """
        func foo() {
            var p = Person{name: "John", age: 30,};
        }
        """
        expect = "Error on line 3 col 50: }"
        self.assertTrue(TestParser.checkParser(input, expect, 280))
        
    def test_statement_44(self):
        """Invalid array index"""
        input = """
        func testIfElse() {
            if (a > b) {
                if (b > c) {
                    return a;
                } else {
                    return b;
                }
            } else {
                return c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))
        
    def test_statement_45(self):
        """Invalid array index"""
        input = """
        // This is a single-line comment
        func commentTest() {
            /* This is a 
               multi-line comment */
            var a = 5; // inline comment
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
        
    def test_statement_46(self):
        """Invalid array index"""
        input = """
        func isPalindrome(s string) bool {
            var i = 0;
            var j = len(s) - 1;
            for i < j {
                if (s[i] != s[j]) {
                    return false;
                }
                i += 1;
                j -= 1;
            }
            return true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))
        
    def test_statement_47(self):
        """Invalid array index"""
        input = """
        func reverseArray(arr [10]int) {
            var left = 0;
            var right = len(arr) - 1;
            for left < right {
                var temp = arr[left];
                arr[left] := arr[right];
                arr[right] := temp;
                left += 1;
                right -= 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))
        
    def test_statement_48(self):
        """Invalid array index"""
        input = """
        func findMax(arr [10]int) int {
            var max = arr[0];
            for i := 1; i < len(arr); i += 1 {
                if (arr[i] > max) {
                    max := arr[i];
                }
            }
            return max;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
        
    def test_statement_49(self):
        input = """
        func absoluteValue(x int) int {
            if (x < 0) {
                return -x;
            }
            return x;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
        
    def test_statement_50(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))
        
    def test_statement_51(self):
        input = """
        func sumDigits(n int) int {
            var sum = 0;
            for n > 0 {
                sum += n % 10;
                n /= 10;
            }
            return sum;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
        
    def test_statement_52(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
        
    def test_statement_53(self):
        input = """
        func isPerfectNumber(n int) bool {
            var sum = 1;
            for i := 2; i * i <= n; i += 1 {
                if (n % i == 0) {
                    sum += i;
                    if (i != n / i) {
                        sum += n / i;
                    }
                }
            }
            return sum == n;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
        
    def test_statement_54(self):
        input = """
        func foo (n int) bool {
            if (n % 2) return true;
            return false;
        }
        """
        expect = "Error on line 3 col 24: return"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    
    def test_statement_55(self):
        input = """
        func foo (n int) bool {
            if (n % 2) {
                return true;
            } else return false;
        }
        """
        expect = "Error on line 5 col 20: return"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    
    def test_statement_56(self):
        input = """
        func quickSort(arr [10]int, left int, right int) {
            if (left >= right) {return;}
            var pivot = arr[(left + right) / 2];
            var i = left;
            var j = right;
            for i <= j {
                for arr[i] < pivot {i += 1;}
                for arr[j] > pivot {j -= 1;}
                if (i <= j) {
                    var temp = arr[i];
                    arr[i] := arr[j];
                    arr[j] := temp;
                    i += 1;
                    j -= 1;
                }
            }
            quickSort(arr, left, j);
            quickSort(arr, i, right);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
        
    def test_statement_57(self):
        input = """
        func nestedLoop() {
            for i := 0; i < 5; i += 1 {
                for j := 0; j < 5; j += 1 {
                    if (i * j % 3 == 0) {
                        continue;
                    }
                    if (i + j > 6) {
                        break;
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
        
    def test_statement_58(self):
        input = """
        type Address struct {
            street string;
            city string;
        }
        
        type Person struct {
            name string;
            age int;
            address Address;
        }
        
        func (p Person) GetAddress() Address{
            return p.address;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
        
    def test_statement_59(self):
        input = """
        type Address struct {
            street string;
            city string;
        }"""
        expect = "Error on line 5 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
        
    def test_statement_60(self):
        input = """
        type Address interface {
            getAddress()
        }"""
        expect = "Error on line 4 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
        
    def test_statement_61(self):
        input = """
        func gcd(a int, b int) int {
            if (b == 0) {
                return a
            }
            return gcd(b, a % b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
        
    def test_statement_62(self):
        input = """
        func lcm(a int, b int) int {
            return (a * b) / gcd(a, b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
        
    # def test_statement_63(self):
    #     input = """
    #     func nthFibonacci(n int) int {
    #         var a = 0;
    #         var b = 1;
    #         for i := 2; i <= n; i += 1 {
    #             var temp = a + b;
    #             a := b;
    #             b := temp;
    #         }
    #         return b;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 300))
        
    def test_statement_63(self):
        input = """
        const a = 4.e10[1][2].5[1][2].c;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
        