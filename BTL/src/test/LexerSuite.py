import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""]
                                              ""","],;,<EOF>",101))
      
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
                                              ""","Unclosed string: Dep trai",108))
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

    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello" ""","hello,<EOF>",117))
        
    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string with a newline \\n" ""","This is a string with a newline \\n,<EOF>",118))
        
    def test_array_literal(self):
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
        
    # def test_float_literal_3(self):
    #     """test float literal"""
    #     self.assertTrue(TestLexer.checkLexeme("""5.7e+-9""","5.7,e,+,-,9,<EOF>",115))
        
    def test_white_space(self):
        """test whitespace"""
        self.assertTrue(TestLexer.checkLexeme("""\t\f\r ""","<EOF>",128))
        
    def test_illegal_esacpe(self):
        """illegal_escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\f" ""","Illegal escape in string: tuanhanhdeptrai\\f", 129))
        
    def test_illegal_esacpe_1(self):
        """illegal_escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "tuanhanhdeptrai\\b" ""","Illegal escape in string: tuanhanhdeptrai\\b", 130))
        
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
        
    def test_identifiers_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A1B2C3_var","A1B2C3_var,<EOF>", 139))
        
    def test_unclose_string_1(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Dep trai ""","Unclosed string: Dep trai ",140))
        
    def test_unclose_string_2(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Dep trai\r ""","Unclosed string: Dep trai",141))