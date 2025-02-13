# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
      
#     def test_lower_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
#     def test_wrong_token(self):
#         self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
        
#     def test_keyword_var(self):
#         """test keyword var"""
#         self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
        
#     def test_keyword_func(self):
#         """test keyword func"""
#         self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
#     def test_keyword_interface(self):
#         """test keyword interface"""
#         self.assertTrue(TestLexer.checkLexeme("""type interface {}""","""type,interface,{,},<EOF>""",105))
        
#     def test_inline_comment(self):
#         """test inline-comment"""
#         self.assertTrue(TestLexer.checkLexeme("//TuanAnh","<EOF>",106))
    
#     def test_inline_comment_1(self):
#         """test inline comment"""
#         self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh
#                                               s""","s,<EOF>",107))
#     def test_unclose_string(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(""""Dep trai
#                                               ""","""Unclosed string: "Dep trai""",108))
#     def test_keyword_struct(self):
#         """test keyword struct"""
#         self.assertTrue(TestLexer.checkLexeme("""type Person struct {}""","type,Person,struct,{,},<EOF>",109))
        
#     def test_keyword_struct_1(self):
#         """test keyword struct"""
#         self.assertTrue(TestLexer.checkLexeme("""type Person struct {
#              name string ;
#              age int ;
#             }""","type,Person,struct,{,name,string,;,age,int,;,},<EOF>",110))
        
#     def test_keyword_assignment(self):
#         """test keyword assignment"""
#         self.assertTrue(TestLexer.checkLexeme("""p := Person{}""","p,:=,Person,{,},<EOF>",111))
        
#     def test_keyword_assignment_1(self):
#         """test keyword assignment"""
#         self.assertTrue(TestLexer.checkLexeme(""" p := Person{name: "Alice", age: 30}""","p,:=,Person,{,name,:,Alice,,,age,:,30,},<EOF>",112))
        
#     def test_keyword_const(self):
#         """test keyword const"""
#         self.assertTrue(TestLexer.checkLexeme("""const Pi = 3.14;""","const,Pi,=,3.14,;,<EOF>",113))
        
#     def test_float_literal(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0.""","0.,<EOF>",114))
        
#     def test_float_literal_1(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""2.0e10""","2.0e10,<EOF>",115))
        
#     def test_float_literal_2(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""3.14""","3.14,<EOF>",116))

#     def test_string_literal_3(self):
#         """test string literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "hello" ""","hello,<EOF>",117))
        
#     def test_string_literal_4(self):
#         """test string literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "This is a string with a newline \\n" ""","This is a string with a newline \\n,<EOF>",118))
        
#     def test_array_literal_5(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" arr := [3]int{10, 20, 30}""","arr,:=,[,3,],int,{,10,,,20,,,30,},<EOF>",119))
        
#     def test_nested_comment(self):
#         """test nested comment"""
#         self.assertTrue(TestLexer.checkLexeme("""/*
#                                               Tuan Anh // dep trai
#                                               */""","<EOF>",120))
        
#     def test_nested_comment_1(self):
#         """test nested comment"""
#         self.assertTrue(TestLexer.checkLexeme("""/*
#                                               /*aaaa*/
#                                               */ //b
#                                               ""","<EOF>",121))
        
#     def test_operator(self):
#         """test operator"""
#         self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 122))
        
#     def test_operator_1(self):
#         """test operator"""
#         self.assertTrue(TestLexer.checkLexeme(" == != < <= > >=", "==,!=,<,<=,>,>=,<EOF>", 123))
        
#     def test_operator_2(self):
#         """test operator"""
#         self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 124))
        
#     def test_operator_3(self):
#         """test operator"""
#         self.assertTrue(TestLexer.checkLexeme(":= +=-= *= /= %=", ":=,+=,-=,*=,/=,%=,<EOF>", 125))
        
#     def test_separator(self):
#         """test separator"""
#         self.assertTrue(TestLexer.checkLexeme("[] {} () , ;", "[,],{,},(,),,,;,<EOF>", 126))
        
#     def test_nil_lit(self):
#         """test nil"""
#         self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 127))
        
#     def test_white_space(self):
#         """test whitespace"""
#         self.assertTrue(TestLexer.checkLexeme("""\t\f\r ""","<EOF>",128))
        
#     def test_illegal_esacpe(self):
#         """illegal_escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\f" ""","""Illegal escape in string: "tuanhanhdeptrai\\f""", 129))
        
#     def test_illegal_esacpe_1(self):
#         """illegal_escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\b" ""","""Illegal escape in string: "tuanhanhdeptrai\\b""", 130))
        
#     def test_illegal_identifiers(self):
#         """illegal_identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("@varName","ErrorToken @", 131))
        
#     def test_illegal_identifiers_1(self):
#         """illegal_identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("#hashTag","ErrorToken #", 132))
        
#     def test_illegal_identifiers_2(self):
#         """illegal_identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("$tuananhdeptrai","ErrorToken $", 133))
        
#     def test_illegal_identifiers_3(self):
#         """illegal_identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("*pointer","*,pointer,<EOF>", 134))
    
#     def test_illegal_identifiers_4(self):
#         """illegal_identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("my-variable","my,-,variable,<EOF>", 135))
        
#     def test_identifiers(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("myVariable","myVariable,<EOF>", 136))
        
#     def test_identifiers_1(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("data_1_2_3","data_1_2_3,<EOF>", 137))
        
#     def test_identifiers_2(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("_underscore_start","_underscore_start,<EOF>", 138))
        
#     def test_identifiers_3(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("A1B2C3_var","A1B2C3_var,<EOF>", 139))
        
#     def test_unclose_string_1(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Dep trai ""","""Unclosed string: "Dep trai """,140))
        
#     def test_unclose_string_2(self):
#         """test unclose string"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Dep trai\r ""","""Unclosed string: "Dep trai""",141))
        
#     def test_float_literal_3(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""5.7e+-9""","5.7,e,+,-,9,<EOF>",142))
        
#     def test_float_literal_4(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""000005.7e+00009""","000005.7e+00009,<EOF>",143))
        
#     def test_float_literal_5(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""000005.7e00009""","000005.7e00009,<EOF>",144))
        
#     def test_float_literal_6(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""000005.7e-00009""","000005.7e-00009,<EOF>",145))
        
#     def test_int_literal(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""042""","0,42,<EOF>",146))
        
#     def test_int_literal_1(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0b11001 0B11001""","0b11001,0B11001,<EOF>",147))
        
#     def test_int_literal_2(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0b99""","0,b99,<EOF>",148))
        
#     def test_int_literal_3(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0B99""","0,B99,<EOF>",149))
        
#     def test_int_literal_4(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0o01234567 0O01234567""","0o01234567,0O01234567,<EOF>",150))
        
#     def test_int_literal_5(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0o088 0O088""","0o0,88,0O0,88,<EOF>",151))
        
#     def test_int_literal_6(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0x123F 0x459f""","0x123F,0x459f,<EOF>",152))
        
#     def test_int_literal_7(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""0x123FG 0x459fG""","0x123F,G,0x459f,G,<EOF>",153))
        
#     def test_newline(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""if{}
#                                               ""","if,{,},;,<EOF>",154))
        
#     def test_newline_1(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = "Tuan Anh"
#                                               ""","const,a,=,Tuan Anh,;,<EOF>",155))
        
#     def test_newline_2(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = a[2]
                                              
                                              
#                                               ""","const,a,=,a,[,2,],;,<EOF>",156))
        
#     def test_newline_3(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = foo()
#                                               ""","const,a,=,foo,(,),;,<EOF>",157))
        
#     def test_newline_4(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = _ab
#                                               ""","const,a,=,_ab,;,<EOF>",158))
        
#     def test_newline_5(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 9
#                                               ""","const,a,=,9,;,<EOF>",159))
        
#     def test_newline_6(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 0x11AF
#                                               ""","const,a,=,0x11AF,;,<EOF>",160))
        
#     def test_newline_7(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 0o07
#                                               ""","const,a,=,0o07,;,<EOF>",161))
        
#     def test_newline_8(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 0B111000
#                                               ""","const,a,=,0B111000,;,<EOF>",162))
        
#     def test_newline_9(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 0.87
#                                               ""","const,a,=,0.87,;,<EOF>",163))
        
#     def test_newline_10(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = 0.87e9
#                                               ""","const,a,=,0.87e9,;,<EOF>",164))
        
#     def test_newline_11(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = true
#                                               ""","const,a,=,true,;,<EOF>",165))
        
#     def test_newline_12(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""const a = false
#                                               ""","const,a,=,false,;,<EOF>",166))
        
#     def test_newline_13(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""var z int
#                                               ""","var,z,int,;,<EOF>",167))
        
#     def test_newline_14(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""var z string
#                                               ""","var,z,string,;,<EOF>",168))
        
#     def test_newline_15(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""var z float
#                                               ""","var,z,float,;,<EOF>",169))
        
#     def test_newline_16(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""var z bool
#                                               ""","var,z,bool,;,<EOF>",170))
        
#     def test_newline_17(self):
#         """test newline"""
#         self.assertTrue(TestLexer.checkLexeme("""return
#                                               continue
#                                               break
#                                               nil
#                                               ""","return,;,continue,;,break,;,nil,;,<EOF>",171))
        
#     def test_wrong_token_1(self):
#         """test wrong token"""
#         self.assertTrue(TestLexer.checkLexeme("""2 ^ 3""","2,ErrorToken ^",172))
        
#     def test_wrong_token_2(self):
#         """test wrong token"""
#         self.assertTrue(TestLexer.checkLexeme("""abc,#tuananhdeptrai""","abc,,,ErrorToken #",173))
        
#     def test_wrong_token_3(self):
#         """test wrong token"""
#         self.assertTrue(TestLexer.checkLexeme("""@private""","ErrorToken @",174))
        
#     def test_wrong_token_4(self):
#         """test wrong token"""
#         self.assertTrue(TestLexer.checkLexeme(""" `tuananhdeptrai` ""","ErrorToken `",175))
        
#     def test_wrong_token_5(self):
#         """test wrong token"""
#         self.assertTrue(TestLexer.checkLexeme(""" a == b ? 5 : 6 ""","a,==,b,ErrorToken ?",176))
        
#     def test_string_literal_6(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\t" ""","tuananhdeptrai \\t,<EOF>",177))
        
#     def test_string_literal_7(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\r" ""","tuananhdeptrai \\r,<EOF>",178))
        
#     def test_string_literal_8(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\" " ""","""tuananhdeptrai \\" ,<EOF>""",179))
        
#     def test_string_literal_9(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "\\\This is a backslash:" ""","""\\\This is a backslash:,<EOF>""",180))
        
#     def test_float_literal_10(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" .5 """,""".,5,<EOF>""",181))
        
#     def test_inline_comment_2(self):
#         """test inline comment"""
#         self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh //Tuanh Em // wibu""","<EOF>",182))
        
#     def test_inline_comment_3(self):
#         """test inline comment"""
#         self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh /*Brother*/""","<EOF>",183))
        
#     def test_nested_comment_2(self):
#         """test nested comment"""
#         self.assertTrue(TestLexer.checkLexeme("""/*
#                                               /*aaaa*/
#                                               */
#                                               //b //a
#                                               /*sos /**/
#                                               ""","<EOF>",184))
        
#     def test_unterminated_comment(self):
#         """test unterminated comment"""
#         self.assertTrue(TestLexer.checkLexeme("/* This is an unclosed comment ", "/,*,This,is,an,unclosed,comment,<EOF>", 185))
        
#     def test_unterminated_comment_1(self):
#         """test unterminated comment"""
#         self.assertTrue(TestLexer.checkLexeme("/* This is an /*nested*/ unclosed comment ", "unclosed,comment,<EOF>", 186))
        
#     def test_invalid_float_exponent(self):
#         """test float literal with misplaced exponent"""
#         self.assertTrue(TestLexer.checkLexeme("3.5e+", "3.5,e,+,<EOF>", 187))
        
#     def test_string_literal_10(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "          " ""","""          ,<EOF>""",188))
        
#     def test_string_literal_11(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(""" "\\"@#$%^&*()\\"" ""","""\\"@#$%^&*()\\",<EOF>""",189))
        
#     def test_complex_expression(self):
#         """test complex expression"""
#         self.assertTrue(TestLexer.checkLexeme("x = (a + b) * (c - d) / e", "x,=,(,a,+,b,),*,(,c,-,d,),/,e,<EOF>", 190))
        
#     def test_string_literal_12(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme('"This is a \\"quoted\\" word"', 'This is a \\"quoted\\" word,<EOF>', 191))

#     def test_while_loop(self):
#         """test while loop"""
#         self.assertTrue(TestLexer.checkLexeme("while (i < 10) { i++ }", "while,(,i,<,10,),{,i,+,+,},<EOF>", 192))

#     def test_int_literal_8(self):
#         """test int literal"""
#         self.assertTrue(TestLexer.checkLexeme("""9999999999999999""","9999999999999999,<EOF>",193))
        
#     def test_string_literal_13(self):
#         """test array literal"""
#         self.assertTrue(TestLexer.checkLexeme(' "Hell" "Way" ', 'Hell,Way,<EOF>', 194))
        
#     def test_inline_comment_4(self):
#         """test inline comment"""
#         self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh \n bro""","bro,<EOF>",195))
        
#     def test_white_space_1(self):
#         """test mixed spaces and tabs"""
#         self.assertTrue(TestLexer.checkLexeme(" \t  x  \t=   5", "x,=,5,<EOF>", 196))

#     def test_extreme_nested_parentheses(self):
#         """test deeply nested parentheses beyond normal levels"""
#         self.assertTrue(TestLexer.checkLexeme("((((((((((((((((((((((((x))))))))))))))))))))))))", "(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,x,),),),),),),),),),),),),),),),),),),),),),),),),<EOF>", 197))
        
#     def test_operator_4(self):
#         """test operator"""
#         self.assertTrue(TestLexer.checkLexeme(">>> === !==", ">,>,>,==,=,!=,=,<EOF>", 198))
        
#     def test_float_literal_11(self):
#         """test float literal"""
#         self.assertTrue(TestLexer.checkLexeme("""1.2.3.4.5.6""","""1.2,.,3.4,.,5.6,<EOF>""",199))
        
#     def test_super_complex(self):
#         self.assertTrue(TestLexer.checkLexeme("""
#             var x = 42;
#             var y = 3.14;
#             z := x + y;
#             result := "Test";
#             z == y;
#             if x > 10 { x = 5; }
#         ""","""var,x,=,42,;,var,y,=,3.14,;,z,:=,x,+,y,;,result,:=,Test,;,z,==,y,;,if,x,>,10,{,x,=,5,;,},;,<EOF>""",200))


import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_skip(self):
        """test skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>",105))
    def test_cmline(self):
        """test comment line"""
        self.assertTrue(TestLexer.checkLexeme("""// abc""", "<EOF>",106))
    def test_cm(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""
            /* sbcsdfdf
            */ a
    """, "a,;,<EOF>",107))
    def test_intlit(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("-002750","-,0,0,2750,<EOF>",108))
    def test_newline(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>",109))
    def test_floatlit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("123.456","123.456,<EOF>",110))
    def test_stringlit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"abcde\"","abcde,<EOF>",111))
    def test_floatlite(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("27.e-5","27.e-5,<EOF>",112))
    def test_illegal_es(self):
        """test illegal escape sequence"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f",113))
    def test_operator_add(self):
        """test operators add"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",114))
    def test_operator_sub(self):
        """test operators sub"""
        self.assertTrue(TestLexer.checkLexeme("-","-,<EOF>",115))
    def test_operator_mul(self):
        """test operators mul"""
        self.assertTrue(TestLexer.checkLexeme("*","*,<EOF>",116))
    def test_operator_div(self):
        """test operators div"""
        self.assertTrue(TestLexer.checkLexeme("/","/,<EOF>",117))
    def test_operator_mod(self):
        """test operators mod"""
        self.assertTrue(TestLexer.checkLexeme("%","%,<EOF>",118))
    def test_if(self):
        """test keyword if"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",119))
    def test_else(self):
        """test keyword else"""
        self.assertTrue(TestLexer.checkLexeme("else","else,<EOF>",120))
    def test_for(self):
        """test keyword for"""
        self.assertTrue(TestLexer.checkLexeme("for","for,<EOF>",121))
    def test_return(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",122))
    def test_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("func","func,<EOF>",123))
    def test_type(self):
        """test keyword type"""
        self.assertTrue(TestLexer.checkLexeme("type","type,<EOF>",124))
    def test_struct(self):
        """test keyword struct"""
        self.assertTrue(TestLexer.checkLexeme("struct","struct,<EOF>",125))
    def test_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("interface","interface,<EOF>",126))
    def test_string(self):
        """test keyword string"""
        self.assertTrue(TestLexer.checkLexeme("string","string,<EOF>",127))
    def test_int(self):
        """test keyword int"""
        self.assertTrue(TestLexer.checkLexeme("int","int,<EOF>",128))
    def test_float(self):
        """test keyword float"""
        self.assertTrue(TestLexer.checkLexeme("float","float,<EOF>",129))
    def test_bool(self):
        """test keyword bool"""
        self.assertTrue(TestLexer.checkLexeme("boolean","boolean,<EOF>",130))
    def test_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("const","const,<EOF>",131))
    def test_true(self):
        """test keyword true"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",132))
    def test_false(self):
        """test keyword false"""
        self.assertTrue(TestLexer.checkLexeme("false","false,<EOF>",133))
    def test_nil(self):
        """test keyword nil"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",134))
    def test_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var","var,<EOF>",135))
    def test_continue(self):
        """test keyword continue"""
        self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",136))
    def test_break(self):
        """test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("break","break,<EOF>",137))
    def test_range(self):
        """test keyword range"""
        self.assertTrue(TestLexer.checkLexeme("range","range,<EOF>",138))
    def test_int_bin(self):
        """test integer binary literal"""
        self.assertTrue(TestLexer.checkLexeme("0b1010","0b1010,<EOF>",139))
    def test_int_oct(self):
        """test integer octal literal"""
        self.assertTrue(TestLexer.checkLexeme("0o77","0o77,<EOF>",140))
    def test_int_hex(self):
        """test integer hexadecimal literal"""
        self.assertTrue(TestLexer.checkLexeme("0x1A","0x1A,<EOF>",141))
    def test_combined_symbols(self):
        """test multiple symbols"""
        self.assertTrue(TestLexer.checkLexeme("!= == <= >= && ||","!=,==,<=,>=,&&,||,<EOF>",142))
    def test_mixed_operators_and_literals(self):
        """test mixed operators and literals"""
        self.assertTrue(TestLexer.checkLexeme("10 + 20.5 * (5 - 3)","10,+,20.5,*,(,5,-,3,),<EOF>",143))
    def test_mixed_comments_and_code(self):
        """test mixed comments and code"""
        self.assertTrue(TestLexer.checkLexeme("""
            // This is a comment
            var x = 10; /* multi\nline comment */
            ""","var,x,=,10,;,<EOF>",144))
    def test_uses_functions(self):
        """test uses functions"""
        self.assertTrue(TestLexer.checkLexeme("""
            func add(a, b int) int {
                return a + b;
            }
            func main() {
                println(add(5, 10));
            }
            ""","func,add,(,a,,,b,int,),int,{,return,a,+,b,;,},;,func,main,(,),{,println,(,add,(,5,,,10,),),;,},;,<EOF>",145))
    def test_mixed_identifiers_keywords(self):
        """test mixed identifiers and keywords"""
        self.assertTrue(TestLexer.checkLexeme("""
                var x = 10; if (x > 0) return
            ""","var,x,=,10,;,if,(,x,>,0,),return,;,<EOF>",146))
    def test_int_lit(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>",147))
    def test_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("123.456", "123.456,<EOF>",148))
    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme(""" 
            /* a * */
    """, "<EOF>",149))
    def test_keyword_struct(self):
        """test keyword struct"""
        self.assertTrue(TestLexer.checkLexeme("""type Person struct {
                name string ;
                age int ;
            }""","type,Person,struct,{,name,string,;,age,int,;,},<EOF>",150))
    def test_keyword_assignment(self):
        """test keyword assignment"""
        self.assertTrue(TestLexer.checkLexeme("""p := Trieuman{}""","p,:=,Trieuman,{,},<EOF>",151))
    def test_keyword_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("""const Pi = 3.14;""","const,Pi,=,3.14,;,<EOF>",152))
    def test_keyword_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("""type interface {
                draw() ;
            }""","type,interface,{,draw,(,),;,},<EOF>",153))
    def test_wrong_token_1(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""2 ^ 3""","2,ErrorToken ^",154))
    def test_wrong_token_2(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""&&^%$#@""","&&,ErrorToken ^",155))
    def test_wrong_token_3(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""@Trieuman""","ErrorToken @",156))
    def test_string_literal_1(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "Trieuman \\" " ""","""Trieuman \\" ,<EOF>""",157))
    def test_string_literal_2(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "Trieuman \\\t" ""","""Illegal escape in string: "Trieuman \	""",158))
    def test_float_literal_1(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme(""" .5 """,""".,5,<EOF>""",159))
    def test_nested_comment_1(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                              /*aaaa*/
                                              */
                                              //b //a
                                              /*sos /**/
                                              ""","<EOF>",160))
    
    def test_complex_expression(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("x = (a + b) * (c - d) / e", "x,=,(,a,+,b,),*,(,c,-,d,),/,e,<EOF>", 161))
    def test_complex_expression_2(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("x = ((a + b) * (c - d) / e) + f", "x,=,(,(,a,+,b,),*,(,c,-,d,),/,e,),+,f,<EOF>", 162))
    def test_int_decimal_zero(self):
        """Test integer"""
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 163))

    def test_int_decimal_123(self):
        """Test integer"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 164))

    def test_int_binary(self):
        """Test integer"""
        self.assertTrue(TestLexer.checkLexeme("0b1010", "0b1010,<EOF>", 165))

    def test_int_octal(self):
        """Test integer"""
        self.assertTrue(TestLexer.checkLexeme("0o77", "0o77,<EOF>", 166))

    def test_int_hexadecimal(self):
        """TTest integer"""
        self.assertTrue(TestLexer.checkLexeme("0x1A2B", "0x1A2B,<EOF>", 167))

    def test_float_literal_no_exponent(self):
        """Test float"""
        self.assertTrue(TestLexer.checkLexeme("123.456", "123.456,<EOF>", 168))

    def test_float_literal_with_exponent(self):
        """Test float"""
        self.assertTrue(TestLexer.checkLexeme("123.456e7", "123.456e7,<EOF>", 169))

    def test_float_literal_leading_zeros(self):
        """Test float"""
        self.assertTrue(TestLexer.checkLexeme("000123.456", "000123.456,<EOF>", 170))

    def test_float_literal_no_fractional_part(self):
        """Test float"""
        self.assertTrue(TestLexer.checkLexeme("123.", "123.,<EOF>", 171))

    def test_float_literal_with_signed_exponent(self):
        """Test float"""
        self.assertTrue(TestLexer.checkLexeme("0.1E-10", "0.1E-10,<EOF>", 172))
    def test_string_literal_3(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello" """, """hello,<EOF>""", 173))

    def test_string_literal_4(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\nworld" """, """hello\\nworld,<EOF>""", 174))

    def test_string_literal_5(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\tworld" """, "hello\\tworld,<EOF>", 175))

    def test_string_literal_6(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "She said \\\"Hi\\\"" """, """She said \\\"Hi\\\",<EOF>""", 176))

    def test_string_literal_7(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Path: C:\\\\Program Files\\\\" """, """Path: C:\\\\Program Files\\\\,<EOF>""", 177))

    def test_string_literal_8(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Line1\\nLine2\\tTabbed" """, """Line1\\nLine2\\tTabbed,<EOF>""", 178))

    def test_string_literal_9(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """, """,<EOF>""", 179))

    def test_string_literal_10(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Hello, World!\\rThis is a test." """, """Hello, World!\\rThis is a test.,<EOF>""", 180))
    def test_string_literal_11(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Hello, World!\\nThis is a test." """, """Hello, World!\\nThis is a test.,<EOF>""", 181))

    def test_string_literal_12(self):
        """Test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Line1\\rLine2" """, "Line1\\rLine2,<EOF>", 182))
    def test_id_1(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("abc123_def", "abc123_def,<EOF>", 183))

    def test_id_2(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("a__b", "a__b,<EOF>", 184))

    def test_id_3(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("AbCdEf", "AbCdEf,<EOF>", 185))

    def test_id_4(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("HelloWorld", "HelloWorld,<EOF>", 186))

    def test_id_5(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("x9y", "x9y,<EOF>", 187))

    def test_id_6(self):
        """Test id"""
        self.assertTrue(TestLexer.checkLexeme("this_is_a_long_identifier123", "this_is_a_long_identifier123,<EOF>", 188))
    def test_newline_1(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = _trieuman
                                              ""","const,a,=,_trieuman,;,<EOF>",189))
        
    def test_newline_2(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 19.24
                                              ""","const,a,=,19.24,;,<EOF>",190))
        
    def test_newline_3(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0x11
                                              ""","const,a,=,0x11,;,<EOF>",191))
        
    def test_newline_4(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0o07
                                              ""","const,a,=,0o07,;,<EOF>",192))
        
    def test_newline_5(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0B111000
                                              ""","const,a,=,0B111000,;,<EOF>",193))    
    def test_newline_6(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = "Hello, World!"
                                              ""","const,a,=,Hello, World!,;,<EOF>",194))
    def test_identifiers(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("myVariable","myVariable,<EOF>", 195))
        
    def test_identifiers_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("data_1_2_3","data_1_2_3,<EOF>", 196))
        
    def test_identifiers_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_underscore_start","_underscore_start,<EOF>", 197))
        
    def test_identifiers_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A1B2C3_var","A1B2C3_var,<EOF>", 198))
        
    def test_unclose_string_1(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Trieu Man ""","Unclosed string: \"Trieu Man ",199))
        
    def test_illegal_string_1(self):
        """test illegal string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Trieu Man\ ""","""Illegal escape in string: "Trieu Man\ """,200))


    
    
    

    

    