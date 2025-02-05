"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 20.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.test("ab?sVN","ab,ErrorToken ?",102))
        
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.test("var abc int ;","var,abc,int,;,<EOF>",103))
        
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.test("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))