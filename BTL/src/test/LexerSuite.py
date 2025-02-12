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
    
    def test_keyword_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("""type interface {}""","""type,interface,{,},<EOF>""",105))
        
    def test_inline_comment(self):
        """test inline-comment"""
        self.assertTrue(TestLexer.checkLexeme("//TuanAnh","<EOF>",106))
    
    def test_inline_comment_1(self):
        """test inline comment"""
        self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh
                                              s""","s,<EOF>",107))
    def test_unclose_string(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""""Dep trai
                                              ""","""Unclosed string: "Dep trai""",108))
    def test_keyword_struct(self):
        """test keyword struct"""
        self.assertTrue(TestLexer.checkLexeme("""type Person struct {}""","type,Person,struct,{,},<EOF>",109))
        
    def test_keyword_struct_1(self):
        """test keyword struct"""
        self.assertTrue(TestLexer.checkLexeme("""type Person struct {
             name string ;
             age int ;
            }""","type,Person,struct,{,name,string,;,age,int,;,},<EOF>",110))
        
    def test_keyword_assignment(self):
        """test keyword assignment"""
        self.assertTrue(TestLexer.checkLexeme("""p := Person{}""","p,:=,Person,{,},<EOF>",111))
        
    def test_keyword_assignment_1(self):
        """test keyword assignment"""
        self.assertTrue(TestLexer.checkLexeme(""" p := Person{name: "Alice", age: 30}""","p,:=,Person,{,name,:,Alice,,,age,:,30,},<EOF>",112))
        
    def test_keyword_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("""const Pi = 3.14;""","const,Pi,=,3.14,;,<EOF>",113))
        
    def test_float_literal(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""0.""","0.,<EOF>",114))
        
    def test_float_literal_1(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""2.0e10""","2.0e10,<EOF>",115))
        
    def test_float_literal_2(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""3.14""","3.14,<EOF>",116))

    def test_string_literal_3(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello" ""","hello,<EOF>",117))
        
    def test_string_literal_4(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string with a newline \\n" ""","This is a string with a newline \\n,<EOF>",118))
        
    def test_array_literal_5(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" arr := [3]int{10, 20, 30}""","arr,:=,[,3,],int,{,10,,,20,,,30,},<EOF>",119))
        
    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                              Tuan Anh // dep trai
                                              */""","<EOF>",120))
        
    def test_nested_comment_1(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                              /*aaaa*/
                                              */ //b
                                              ""","<EOF>",121))
        
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 122))
        
    def test_operator_1(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(" == != < <= > >=", "==,!=,<,<=,>,>=,<EOF>", 123))
        
    def test_operator_2(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 124))
        
    def test_operator_3(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(":= +=-= *= /= %=", ":=,+=,-=,*=,/=,%=,<EOF>", 125))
        
    def test_separator(self):
        """test separator"""
        self.assertTrue(TestLexer.checkLexeme("[] {} () , ;", "[,],{,},(,),,,;,<EOF>", 126))
        
    def test_nil_lit(self):
        """test nil"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 127))
        
    def test_white_space(self):
        """test whitespace"""
        self.assertTrue(TestLexer.checkLexeme("""\t\f\r ""","<EOF>",128))
        
    def test_illegal_esacpe(self):
        """illegal_escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\f" ""","""Illegal escape in string: "tuanhanhdeptrai\\f""", 129))
        
    def test_illegal_esacpe_1(self):
        """illegal_escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\b" ""","""Illegal escape in string: "tuanhanhdeptrai\\b""", 130))
        
    def test_illegal_identifiers(self):
        """illegal_identifiers"""
        self.assertTrue(TestLexer.checkLexeme("@varName","ErrorToken @", 131))
        
    def test_illegal_identifiers_1(self):
        """illegal_identifiers"""
        self.assertTrue(TestLexer.checkLexeme("#hashTag","ErrorToken #", 132))
        
    def test_illegal_identifiers_2(self):
        """illegal_identifiers"""
        self.assertTrue(TestLexer.checkLexeme("$tuananhdeptrai","ErrorToken $", 133))
        
    def test_illegal_identifiers_3(self):
        """illegal_identifiers"""
        self.assertTrue(TestLexer.checkLexeme("*pointer","*,pointer,<EOF>", 134))
    
    def test_illegal_identifiers_4(self):
        """illegal_identifiers"""
        self.assertTrue(TestLexer.checkLexeme("my-variable","my,-,variable,<EOF>", 135))
        
    def test_identifiers(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("myVariable","myVariable,<EOF>", 136))
        
    def test_identifiers_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("data_1_2_3","data_1_2_3,<EOF>", 137))
        
    def test_identifiers_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_underscore_start","_underscore_start,<EOF>", 138))
        
    def test_identifiers_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A1B2C3_var","A1B2C3_var,<EOF>", 139))
        
    def test_unclose_string_1(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Dep trai ""","""Unclosed string: "Dep trai """,140))
        
    def test_unclose_string_2(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Dep trai\r ""","""Unclosed string: "Dep trai""",141))
        
    def test_float_literal_3(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""5.7e+-9""","5.7,e,+,-,9,<EOF>",142))
        
    def test_float_literal_4(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""000005.7e+00009""","000005.7e+00009,<EOF>",143))
        
    def test_float_literal_5(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""000005.7e00009""","000005.7e00009,<EOF>",144))
        
    def test_float_literal_6(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""000005.7e-00009""","000005.7e-00009,<EOF>",145))
        
    def test_int_literal(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""042""","0,42,<EOF>",146))
        
    def test_int_literal_1(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0b11001 0B11001""","0b11001,0B11001,<EOF>",147))
        
    def test_int_literal_2(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0b99""","0,b99,<EOF>",148))
        
    def test_int_literal_3(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0B99""","0,B99,<EOF>",149))
        
    def test_int_literal_4(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0o01234567 0O01234567""","0o01234567,0O01234567,<EOF>",150))
        
    def test_int_literal_5(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0o088 0O088""","0o0,88,0O0,88,<EOF>",151))
        
    def test_int_literal_6(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0x123F 0x459f""","0x123F,0x459f,<EOF>",152))
        
    def test_int_literal_7(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""0x123FG 0x459fG""","0x123F,G,0x459f,G,<EOF>",153))
        
    def test_newline(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""if{}
                                              ""","if,{,},;,<EOF>",154))
        
    def test_newline_1(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = "Tuan Anh"
                                              ""","const,a,=,Tuan Anh,;,<EOF>",155))
        
    def test_newline_2(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = a[2]
                                              
                                              
                                              ""","const,a,=,a,[,2,],;,<EOF>",156))
        
    def test_newline_3(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = foo()
                                              ""","const,a,=,foo,(,),;,<EOF>",157))
        
    def test_newline_4(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = _ab
                                              ""","const,a,=,_ab,;,<EOF>",158))
        
    def test_newline_5(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 9
                                              ""","const,a,=,9,;,<EOF>",159))
        
    def test_newline_6(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0x11AF
                                              ""","const,a,=,0x11AF,;,<EOF>",160))
        
    def test_newline_7(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0o07
                                              ""","const,a,=,0o07,;,<EOF>",161))
        
    def test_newline_8(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0B111000
                                              ""","const,a,=,0B111000,;,<EOF>",162))
        
    def test_newline_9(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0.87
                                              ""","const,a,=,0.87,;,<EOF>",163))
        
    def test_newline_10(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = 0.87e9
                                              ""","const,a,=,0.87e9,;,<EOF>",164))
        
    def test_newline_11(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = true
                                              ""","const,a,=,true,;,<EOF>",165))
        
    def test_newline_12(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""const a = false
                                              ""","const,a,=,false,;,<EOF>",166))
        
    def test_newline_13(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""var z int
                                              ""","var,z,int,;,<EOF>",167))
        
    def test_newline_14(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""var z string
                                              ""","var,z,string,;,<EOF>",168))
        
    def test_newline_15(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""var z float
                                              ""","var,z,float,;,<EOF>",169))
        
    def test_newline_16(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""var z bool
                                              ""","var,z,bool,;,<EOF>",170))
        
    def test_newline_17(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("""return
                                              continue
                                              break
                                              nil
                                              ""","return,;,continue,;,break,;,nil,;,<EOF>",171))
        
    def test_wrong_token_1(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""2 ^ 3""","2,ErrorToken ^",172))
        
    def test_wrong_token_2(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""abc,#tuananhdeptrai""","abc,,,ErrorToken #",173))
        
    def test_wrong_token_3(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("""@private""","ErrorToken @",174))
        
    def test_wrong_token_4(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme(""" `tuananhdeptrai` ""","ErrorToken `",175))
        
    def test_wrong_token_5(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme(""" a == b ? 5 : 6 ""","a,==,b,ErrorToken ?",176))
        
    def test_string_literal_6(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\t" ""","tuananhdeptrai \\t,<EOF>",177))
        
    def test_string_literal_7(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\r" ""","tuananhdeptrai \\r,<EOF>",178))
        
    def test_string_literal_8(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuananhdeptrai \\" " ""","""tuananhdeptrai \\" ,<EOF>""",179))
        
    def test_string_literal_9(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\This is a backslash:" ""","""\\\This is a backslash:,<EOF>""",180))
        
    def test_float_literal_10(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme(""" .5 """,""".,5,<EOF>""",181))
        
    def test_inline_comment_2(self):
        """test inline comment"""
        self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh //Tuanh Em // wibu""","<EOF>",182))
        
    def test_inline_comment_3(self):
        """test inline comment"""
        self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh /*Brother*/""","<EOF>",183))
        
    def test_nested_comment_2(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                              /*aaaa*/
                                              */
                                              //b //a
                                              /*sos /**/
                                              ""","<EOF>",184))
        
    def test_unterminated_comment(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is an unclosed comment ", "/,*,This,is,an,unclosed,comment,<EOF>", 185))
        
    def test_unterminated_comment_1(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is an /*nested*/ unclosed comment ", "unclosed,comment,<EOF>", 186))
        
    def test_invalid_float_exponent(self):
        """test float literal with misplaced exponent"""
        self.assertTrue(TestLexer.checkLexeme("3.5e+", "3.5,e,+,<EOF>", 187))
        
    def test_string_literal_10(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "          " ""","""          ,<EOF>""",188))
        
    def test_string_literal_11(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\"@#$%^&*()\\"" ""","""\\"@#$%^&*()\\",<EOF>""",189))
        
    def test_complex_expression(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("x = (a + b) * (c - d) / e", "x,=,(,a,+,b,),*,(,c,-,d,),/,e,<EOF>", 190))
        
    def test_string_literal_12(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme('"This is a \\"quoted\\" word"', 'This is a \\"quoted\\" word,<EOF>', 191))

    def test_while_loop(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme("while (i < 10) { i++ }", "while,(,i,<,10,),{,i,+,+,},<EOF>", 192))

    def test_int_literal_8(self):
        """test int literal"""
        self.assertTrue(TestLexer.checkLexeme("""9999999999999999""","9999999999999999,<EOF>",193))
        
    def test_string_literal_13(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(' "Hell" "Way" ', 'Hell,Way,<EOF>', 194))
        
    def test_inline_comment_4(self):
        """test inline comment"""
        self.assertTrue(TestLexer.checkLexeme("""//Tuan Anh \n bro""","bro,<EOF>",195))
        
    def test_white_space_1(self):
        """test mixed spaces and tabs"""
        self.assertTrue(TestLexer.checkLexeme(" \t  x  \t=   5", "x,=,5,<EOF>", 196))

    def test_extreme_nested_parentheses(self):
        """test deeply nested parentheses beyond normal levels"""
        self.assertTrue(TestLexer.checkLexeme("((((((((((((((((((((((((x))))))))))))))))))))))))", "(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,(,x,),),),),),),),),),),),),),),),),),),),),),),),),<EOF>", 197))
        
    def test_operator_4(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(">>> === !==", ">,>,>,==,=,!=,=,<EOF>", 198))
        
    def test_float_literal_11(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("""1.2.3.4.5.6""","""1.2,.,3.4,.,5.6,<EOF>""",199))
        
    def test_super_complex(self):
        self.assertTrue(TestLexer.checkLexeme("""
            var x = 42;
            var y = 3.14;
            z := x + y;
            result := "Test";
            z == y;
            if x > 10 { x = 5; }
        ""","""var,x,=,42,;,var,y,=,3.14,;,z,:=,x,+,y,;,result,:=,Test,;,z,==,y,;,if,x,>,10,{,x,=,5,;,},;,<EOF>""",200))
