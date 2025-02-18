# """
#  * Initial code for Assignment 1, 2
#  * Programming Language Principles
#  * Author: Võ Tiến
#  * Link FB : https://www.facebook.com/Shiba.Vo.Tien
#  * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
#  * Date: 07.01.2025
# """

# import unittest
# from TestUtils import TestParser
# import inspect

# class ParserSuite(unittest.TestCase):
#     def test_001(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

#     def test_002(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

#     def test_003(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

#     def test_004(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

#     def test_005(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

#     def test_006(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

#     def test_007(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

#     def test_008(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

#     def test_009(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

#     def test_010(self):
#         """declared variables"""
#         self.assertTrue(TestParser.test("""
#             var x int = foo() + 3 / 4;
#             var y = "Hello" / 4;   
#             var z str;
#         ""","successful", inspect.stack()[0].function))

#     def test_011(self):
#         """declared constants"""
#         self.assertTrue(TestParser.test("""
#             const VoTien = a.b() + 2;
#         ""","successful", inspect.stack()[0].function))

#     def test_012(self):
#         """declared function"""
#         self.assertTrue(TestParser.test("""
#             func VoTien(x int, y int) int {}
#             func VoTien1() [2][3] ID {}         
#             func VoTien2() {}                                       
#         ""","successful", inspect.stack()[0].function))

#     def test_013(self):
#         """declared method"""
#         self.assertTrue(TestParser.test("""
#             func (c Calculator) VoTien(x int) int {}  
#             func (c Calculator) VoTien() ID {}      
#             func (c Calculator) VoTien(x int, y [2]VoTien) {}                                                      
#         ""","successful", inspect.stack()[0].function))

#     def test_014(self):
#         """declared struct"""
#         self.assertTrue(TestParser.test("""
#             type VoTien struct {
#                 VoTien string ;
#                 VoTien [1][3]VoTien ;                     
#             }
#             type VoTien struct {}                                                                       
#         ""","successful", inspect.stack()[0].function))

#     def test_015(self):
#         """declared Interface"""
#         self.assertTrue(TestParser.test("""
#             type VoTien struct {
#                 VoTien string ;
#                 VoTien [1][3]VoTien ;                     
#             }
#             type VoTien struct {}                                                                       
#         ""","successful", inspect.stack()[0].function))

#     def test_016(self):
#         """declared Interface"""
#         self.assertTrue(TestParser.test("""
#             type Calculator interface {
                                        
#                 Add(x, y int) int;
#                 Subtract(a, b float, c int) [3]ID;
#                 Reset()
                                        
#                 SayHello(name string);
                                        
#             }
#             type VoTien interface {}                                                                       
#         ""","successful", inspect.stack()[0].function))

#     def test_017(self):
#         """declared_statement"""
#         self.assertTrue(TestParser.test("""    
#             func VoTien() {
#                 var x int = foo() + 3 / 4;
#                 var y = "Hello" / 4;   
#                 var z str;
                                        
#                 const VoTien = a.b() + 2;
#             }                                       
#         ""","successful", inspect.stack()[0].function))


#     def test_018(self):
#         """assign_statement"""
#         self.assertTrue(TestParser.test("""    
#             func VoTien() {
#                 x  := foo() + 3 / 4;
#                 x.c[2][4] := 1 + 2;                       
#             }                                       
#         ""","successful", inspect.stack()[0].function))

#     def test_019(self):
#         """for_statement"""
#         self.assertTrue(TestParser.test("""    
#             func VoTien() {
#                 if (x > 10) {} 
#                 if (x > 10) {
                  
#                 } else if (x == 10) {
#                     var z str;
#                 } else {
#                     var z ID;
#                 }
#             }
#         ""","successful", inspect.stack()[0].function))

#     def test_020(self):
#         """if_statement"""
#         self.assertTrue(TestParser.test("""    
#             func VoTien() {
#                 for i < 10 {}
#                 for i := 0; i < 10; i += 1 {}
#                 for index, value := range array {}
#             }
#         ""","successful", inspect.stack()[0].function))


#     def test_021(self):
#         """break and continue, return, Call  statement"""
#         self.assertTrue(TestParser.test("""    
#             func VoTien() {                           
#                 for i < 10 {break;}
#                 break;
#                 continue;
#                 return 1;
#                 return
#                 foo(2 + x, 4 / y); m.goo();                        
#              }
                                        
#         ""","successful", inspect.stack()[0].function))

#     def test_022(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             const a = 0b11;                         
#         ""","successful", inspect.stack()[0].function))

#     def test_023(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
#         ""","successful", inspect.stack()[0].function))

#     def test_024(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = a[2][3][a + 2];                         
#         ""","successful", inspect.stack()[0].function))

#     def test_025(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = int{1};                         
#         ""","Error on line 2 col 27: int", inspect.stack()[0].function))

#     def test_026(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
#         ""","successful", inspect.stack()[0].function))

#     def test_027(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
#         ""","successful", inspect.stack()[0].function))

#     def test_028(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
#         ""","successful", inspect.stack()[0].function))

#     def test_029(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             const k = -a + -!-!c - ---[2]int{2};                         
#         ""","successful", inspect.stack()[0].function))

#     def test_030(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""    
#             var a [2][3]int = 2 + 3 / 4;
#         ""","successful", inspect.stack()[0].function))

#     def test_031(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""    
#             var a = a.foo()[2];
#         ""","successful", inspect.stack()[0].function))

#     def test_032(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""    
#             var c [2][3]ID
#         ""","Error on line 2 col 26: \n", inspect.stack()[0].function))

#     def test_033(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""    
#             func Add(x int, y int) int  {};
# ""","Error on line 2 col 42: ;", inspect.stack()[0].function))
        
#     def test_034(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""
#             func (c c) Add(x, c int) {}
# ""","Error on line 2 col 28: ,", inspect.stack()[0].function))
        
#     def test_035(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""
#             func (c c) Add(x int) {};
# ""","Error on line 2 col 36: ;", inspect.stack()[0].function))
        
#     def test_036(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         a.c[2].e[3].k += 2;       
#                                     }""","successful", inspect.stack()[0].function))
    
#     def test_037(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = a[2, 3];                         
#         ""","Error on line 2 col 30: ,", inspect.stack()[0].function))

#     def test_038(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = [2]int{};                         
#         ""","Error on line 2 col 34: }", inspect.stack()[0].function))

#     def test_039(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = ID {};                         
#         ""","successful", inspect.stack()[0].function))

#     def test_040(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""    
#             type Calculator struct {
#                 c Calculator
#                 c Cal a int;         
#             }
# ""","Error on line 4 col 22: a", inspect.stack()[0].function))
        
#     def test_041(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         a.foo() += 2;       
#                                     }""","Error on line 3 col 48: +=", inspect.stack()[0].function))
        
#     def test_042(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         a[2].b := 2;       
#                                     }""","successful", inspect.stack()[0].function))
        
#     def test_043(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         if (x.foo().b[2]) 
#                                         {
#                                             if (){}
#                                         } 
#                                     }""","Error on line 5 col 48: )", inspect.stack()[0].function))
    
#     def test_044(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         if (x.foo().b[2]) 
#                                         {
#                                             if (1){} else {}

#                                         } else if(2)
#                                         {
#                                         }
#                                     }""","successful", inspect.stack()[0].function))
        
#     def test_045(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         if (x.foo().b[2]) 
#                                         {
#                                         } else if(1)
#                                         {
#                                         }else if(1)
#                                         {
#                                         }else if(2)
#                                         {
#                                         }else 
#                                         {
#                                         }
#                                     }""","successful", inspect.stack()[0].function))
        
#     def test_046(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         for true {}
#                                     }""","successful", inspect.stack()[0].function))
        
#     def test_047(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         for const i = 0; i < 10; i += 1 {
#                                             // loop body
#                                         }
#                                     }""","Error on line 3 col 44: const", inspect.stack()[0].function))
        
#     def test_048(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         for var i = 0; i < 10; i += 1 {
#                                             // loop body
#                                         }
#                                     }""","successful", inspect.stack()[0].function))
        
#     def test_049(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         for index, value := range arr[2] {
#                                         }
#                                     }""","successful", inspect.stack()[0].function))
    
#     def test_050(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         a[2][3].foo(2 + 3, a {a:2})
#                                     }""","successful", inspect.stack()[0].function))
       
#     def test_051(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         if (1) {}
#                                         else if(2) {return string;}
#                                         else if(3) {reutrn int;}
#                                     }""","Error on line 4 col 59: string", inspect.stack()[0].function))

"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
#     def test_001(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

#     def test_002(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

#     def test_003(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

#     def test_004(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

#     def test_005(self):
#         """Literal"""
#         self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

#     def test_006(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

#     def test_007(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

#     def test_008(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

#     def test_009(self):
#         """expression"""
#         self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))
    
#     def test_015(self):
#         """declared Interface"""
#         self.assertTrue(TestParser.test("""
#             type VoTien struct {}                                                                       
#         ""","Error on line 2 col 32: }", inspect.stack()[0].function))
        
#     def test_016(self):
#         """declared Interface"""
#         self.assertTrue(TestParser.test("""
#             type Calculator interface {
                                        
#                 Add(x, y int) int;
#                 Subtract(a, b float, c int) [3]ID;
#                 Reset()
                                        
#                 SayHello(name string);
                                        
#             }
#             type VoTien interface {}                                                                       
#         ""","Error on line 11 col 35: }", inspect.stack()[0].function))
        
#     def test_030(self):
#         """Expressions"""
#         self.assertTrue(TestParser.test("""    
#             var z VOTIEN = [2]int{};                         
#         ""","Error on line 2 col 34: }", inspect.stack()[0].function))
        

        
#     def test_089(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""
#             func (c int) Add(x int) int {return ;}
# ""","Error on line 2 col 20: int", inspect.stack()[0].function))
    
#     def test_091(self):
#         """Declared"""
#         self.assertTrue(TestParser.test("""
#             func (c c) Add(x, c int) {return ;}
# ""","successful", inspect.stack()[0].function))
    
#     def test_100(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#             func Add() {
#                                         }
# ""","Error on line 3 col 40: }", inspect.stack()[0].function))
    
#     def test_126(self):
#         """Statement"""
#         self.assertTrue(TestParser.test("""
#                                     func Add() {
#                                         for var i [2] int = 0; foo().a.b(); i[3] := 1 {
#                                             return; 
#                                         }
#                                     };""","Error on line 3 col 77: [", inspect.stack()[0].function))
    
#     def test_151(self):
#         """array_literal"""
#         self.assertTrue(TestParser.test("""const a = [1]int{1+1}                    
# ""","Error on line 1 col 18: +", inspect.stack()[0].function))
        
#     def test_152(self):
#         """array_literal"""
#         self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
# ""","successful", inspect.stack()[0].function))
        
#     def test_154(self):
#         """array_literal"""
#         self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
# ""","Error on line 1 col 17: [", inspect.stack()[0].function))
        
# #     def test_158(self):
# #         self.assertTrue(TestParser.test("""
# #         type Person struct {
# #             func (p Person) Greet() string {
# #                 return "Hello, " + p.name
# #             }; c c;
# #             func (p Person) Greet() string {
# #                 return "Hello, " + p.name
# #             } c c;                                                    
# #         }      
# # ""","Error on line 8 col 14: c", inspect.stack()[0].function))
        
#     def test_159(self):
#         self.assertTrue(TestParser.test("""
#             func (p Person) Greet() string {
#                 for i := 0
#                     i < 10
#                     i += 1 {
#                     return
#                 }
#                 for i := 0
#                     i < 10
#                     i += 1 
#                 {
#                     return
#                 }
#             };  
# ""","Error on line 10 col 27: ;", inspect.stack()[0].function))    
        
#     def test_160(self):
#         self.assertTrue(TestParser.test("""
#             func (p Person) Greet() string {
#                 if (1) {return;}
#                 else if (1)
#                 {}
#             };  
# ""","Error on line 4 col 16: else", inspect.stack()[0].function))
    
#     def test_161(self):
#         self.assertTrue(TestParser.test("""
#             func (p Person) Greet() string {
#                 if (1) {return;
#                 }else if (1) {}
#             };  
# ""","Error on line 4 col 30: }", inspect.stack()[0].function))
        
#     def test_164(self):
#         self.assertTrue(TestParser.test("""
#             func (p Person) Greet() string {
#                 for i < 10 {
# // loop body
# }
#             };  
# ""","Error on line 5 col 0: }", inspect.stack()[0].function))
        
#     def test_176(self):
#         self.assertTrue(TestParser.test("""
#         type Person struct {
#             func (p Person) Greet() string {
#                 return "Hello, " + p.name
#             };                                                 
#         }      
# ""","Error on line 3 col 12: func", inspect.stack()[0].function))
    
# #     def test_043(self):
# #         self.assertTrue(TestParser.test("""
# #             func Add(x int, y int) int {};                                        
# # """), inspect.stack()[0].function)

    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}                                                                       
        ""","Error on line 2 col 32: }", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","Error on line 11 col 35: }", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
       
    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const a = 0b11;                         
        ""","successful", inspect.stack()[0].function))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {};                         
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", inspect.stack()[0].function))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", inspect.stack()[0].function))
    
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", inspect.stack()[0].function))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", inspect.stack()[0].function))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", inspect.stack()[0].function))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a =;
        ""","Error on line 2 col 21: ;", inspect.stack()[0].function))
        
    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add() {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", inspect.stack()[0].function))
        
    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 22: =", inspect.stack()[0].function))
        
    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", inspect.stack()[0].function))
        
    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", inspect.stack()[0].function))
        
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))
        
    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y int) int  {return ;};
""","successful", inspect.stack()[0].function))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", inspect.stack()[0].function))
        
    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.test("""

""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", inspect.stack()[0].function))
        
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", inspect.stack()[0].function))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", inspect.stack()[0].function))

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", inspect.stack()[0].function))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 48: +=", inspect.stack()[0].function))

    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", inspect.stack()[0].function))
        
    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", inspect.stack()[0].function))

    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", inspect.stack()[0].function))
   
    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
    
    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", inspect.stack()[0].function))
        
    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", inspect.stack()[0].function))
        
    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", inspect.stack()[0].function))
        
    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))
        
    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", inspect.stack()[0].function))
        
    def test_179(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_180(self):
        self.assertTrue(TestParser.test("""
                                            const a = [ID][2][VT]int{{{1}}, ID, a, {b}}                              
                                        ""","successful", inspect.stack()[0].function))

    def test_181(self):
        self.assertTrue(TestParser.test("""
                                            var a;
                                        ""","Error on line 2 col 49: ;", inspect.stack()[0].function))
    def test_182(self):
        self.assertTrue(TestParser.test("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))
        
    def test_183(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 30: ,", inspect.stack()[0].function))
        
  