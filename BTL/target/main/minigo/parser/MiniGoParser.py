# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u028e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a3\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u00aa\n\6\3\6\3\6\5\6\u00ae\n")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\6\b\u00b9\n\b\r")
        buf.write("\b\16\b\u00ba\3\t\3\t\3\t\3\t\3\t\5\t\u00c2\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u00cd\n\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d5\n\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00dd\n\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u00e6\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ed\n\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00fe\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0110\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u0118\n\26\3\26\3\26\3\27\3\27\5\27\u011e\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u0125\n\30\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u012e\n\32\3\33\3\33\5\33")
        buf.write("\u0132\n\33\3\34\3\34\3\34\3\34\5\34\u0138\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0143\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0154\n\37\7\37\u0156\n\37\f")
        buf.write("\37\16\37\u0159\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3!\3!\5!\u0168\n!\3\"\3\"\3\"\3\"\5\"\u016e\n\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3$\3$\5$\u017b\n$\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\5&\u0185\n&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\5(\u0192\n(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3+\3+\3+\3+\5+\u01a9\n+\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3.\5.\u01b8\n.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\5/\u01c3\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u01cf\n\60\3\61\3\61\5\61\u01d3\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u01da\n\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u01e3\n\63\3\64\3\64\5\64\u01e7")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u01ee\n\65\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01fa")
        buf.write("\n\67\38\38\38\38\38\58\u0201\n8\39\39\39\39\59\u0207")
        buf.write("\n9\3:\3:\3:\3:\3;\3;\3<\3<\3<\3<\3<\3=\3=\5=\u0216\n")
        buf.write("=\3>\3>\3>\3>\3>\5>\u021d\n>\3?\3?\3?\3?\5?\u0223\n?\3")
        buf.write("@\3@\3@\3@\3@\3A\3A\5A\u022c\nA\3B\3B\3B\3B\3B\5B\u0233")
        buf.write("\nB\3C\3C\3C\3C\3C\3C\7C\u023b\nC\fC\16C\u023e\13C\3D")
        buf.write("\3D\3D\3D\3D\3D\7D\u0246\nD\fD\16D\u0249\13D\3E\3E\3E")
        buf.write("\3E\3E\3E\7E\u0251\nE\fE\16E\u0254\13E\3F\3F\3F\3F\3F")
        buf.write("\3F\7F\u025c\nF\fF\16F\u025f\13F\3G\3G\3G\3G\3G\3G\7G")
        buf.write("\u0267\nG\fG\16G\u026a\13G\3H\3H\3H\5H\u026f\nH\3I\3I")
        buf.write("\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u027c\nI\5I\u027e\nI\7")
        buf.write("I\u0280\nI\fI\16I\u0283\13I\3J\3J\3J\3J\3J\3J\3J\5J\u028c")
        buf.write("\nJ\3J\2\t<\u0084\u0086\u0088\u008a\u008c\u0090K\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\b\3\2&+\4")
        buf.write("\2\13\16\66\66\3\2\34!\3\2\27\30\3\2\31\33\4\2\30\30$")
        buf.write("$\2\u0295\2\u0094\3\2\2\2\4\u0097\3\2\2\2\6\u0099\3\2")
        buf.write("\2\2\b\u00a2\3\2\2\2\n\u00a4\3\2\2\2\f\u00b1\3\2\2\2\16")
        buf.write("\u00b8\3\2\2\2\20\u00c1\3\2\2\2\22\u00c3\3\2\2\2\24\u00cc")
        buf.write("\3\2\2\2\26\u00ce\3\2\2\2\30\u00d1\3\2\2\2\32\u00e5\3")
        buf.write("\2\2\2\34\u00ec\3\2\2\2\36\u00ee\3\2\2\2 \u00f1\3\2\2")
        buf.write("\2\"\u00fd\3\2\2\2$\u00ff\3\2\2\2&\u0103\3\2\2\2(\u010f")
        buf.write("\3\2\2\2*\u0111\3\2\2\2,\u011d\3\2\2\2.\u0124\3\2\2\2")
        buf.write("\60\u0126\3\2\2\2\62\u012d\3\2\2\2\64\u0131\3\2\2\2\66")
        buf.write("\u0137\3\2\2\28\u0142\3\2\2\2:\u0144\3\2\2\2<\u0149\3")
        buf.write("\2\2\2>\u015a\3\2\2\2@\u0167\3\2\2\2B\u016d\3\2\2\2D\u016f")
        buf.write("\3\2\2\2F\u017a\3\2\2\2H\u017c\3\2\2\2J\u0184\3\2\2\2")
        buf.write("L\u018b\3\2\2\2N\u018e\3\2\2\2P\u0198\3\2\2\2R\u01a0\3")
        buf.write("\2\2\2T\u01a4\3\2\2\2V\u01ad\3\2\2\2X\u01b0\3\2\2\2Z\u01b7")
        buf.write("\3\2\2\2\\\u01bf\3\2\2\2^\u01ce\3\2\2\2`\u01d2\3\2\2\2")
        buf.write("b\u01d9\3\2\2\2d\u01e2\3\2\2\2f\u01e6\3\2\2\2h\u01ed\3")
        buf.write("\2\2\2j\u01ef\3\2\2\2l\u01f9\3\2\2\2n\u0200\3\2\2\2p\u0206")
        buf.write("\3\2\2\2r\u0208\3\2\2\2t\u020c\3\2\2\2v\u020e\3\2\2\2")
        buf.write("x\u0215\3\2\2\2z\u021c\3\2\2\2|\u0222\3\2\2\2~\u0224\3")
        buf.write("\2\2\2\u0080\u022b\3\2\2\2\u0082\u0232\3\2\2\2\u0084\u0234")
        buf.write("\3\2\2\2\u0086\u023f\3\2\2\2\u0088\u024a\3\2\2\2\u008a")
        buf.write("\u0255\3\2\2\2\u008c\u0260\3\2\2\2\u008e\u026e\3\2\2\2")
        buf.write("\u0090\u0270\3\2\2\2\u0092\u028b\3\2\2\2\u0094\u0095\5")
        buf.write("\16\b\2\u0095\u0096\7\2\2\3\u0096\3\3\2\2\2\u0097\u0098")
        buf.write("\7\65\2\2\u0098\5\3\2\2\2\u0099\u009a\5p9\2\u009a\u009b")
        buf.write("\5t;\2\u009b\7\3\2\2\2\u009c\u00a3\5\6\4\2\u009d\u00a3")
        buf.write("\7\16\2\2\u009e\u00a3\7\f\2\2\u009f\u00a3\7\r\2\2\u00a0")
        buf.write("\u00a3\7\13\2\2\u00a1\u00a3\7\66\2\2\u00a2\u009c\3\2\2")
        buf.write("\2\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2\u009f")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\t\3\2\2\2\u00a4\u00a5\7\20\2\2\u00a5\u00ad\7\66\2\2\u00a6")
        buf.write("\u00ae\5\b\5\2\u00a7\u00aa\5\b\5\2\u00a8\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00ac\7%\2\2\u00ac\u00ae\5\u0084C\2\u00ad")
        buf.write("\u00a6\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b0\5\4\3\2\u00b0\13\3\2\2\2\u00b1\u00b2\7\17")
        buf.write("\2\2\u00b2\u00b3\7\66\2\2\u00b3\u00b4\7%\2\2\u00b4\u00b5")
        buf.write("\5\u0084C\2\u00b5\u00b6\5\4\3\2\u00b6\r\3\2\2\2\u00b7")
        buf.write("\u00b9\5\20\t\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2")
        buf.write("\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\17\3")
        buf.write("\2\2\2\u00bc\u00c2\5\n\6\2\u00bd\u00c2\5\f\7\2\u00be\u00c2")
        buf.write("\5\30\r\2\u00bf\u00c2\5 \21\2\u00c0\u00c2\5&\24\2\u00c1")
        buf.write("\u00bc\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\21\3\2")
        buf.write("\2\2\u00c3\u00c4\7-\2\2\u00c4\u00c5\5\24\13\2\u00c5\u00c6")
        buf.write("\7.\2\2\u00c6\23\3\2\2\2\u00c7\u00c8\5\26\f\2\u00c8\u00c9")
        buf.write("\7\64\2\2\u00c9\u00ca\5\24\13\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00cd\5\26\f\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cd\25\3\2\2\2\u00ce\u00cf\7\66\2\2\u00cf\u00d0\7")
        buf.write("\66\2\2\u00d0\27\3\2\2\2\u00d1\u00d4\7\7\2\2\u00d2\u00d5")
        buf.write("\5\22\n\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7\66\2")
        buf.write("\2\u00d7\u00d8\7-\2\2\u00d8\u00d9\5\32\16\2\u00d9\u00dc")
        buf.write("\7.\2\2\u00da\u00dd\5\b\5\2\u00db\u00dd\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00df\7/\2\2\u00df\u00e0\5\66\34\2\u00e0\u00e1")
        buf.write("\7\60\2\2\u00e1\u00e2\5\4\3\2\u00e2\31\3\2\2\2\u00e3\u00e6")
        buf.write("\5\34\17\2\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\5\36\20\2")
        buf.write("\u00e8\u00e9\7\64\2\2\u00e9\u00ea\5\34\17\2\u00ea\u00ed")
        buf.write("\3\2\2\2\u00eb\u00ed\5\36\20\2\u00ec\u00e7\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\35\3\2\2\2\u00ee\u00ef\5\62\32\2")
        buf.write("\u00ef\u00f0\5\b\5\2\u00f0\37\3\2\2\2\u00f1\u00f2\7\b")
        buf.write("\2\2\u00f2\u00f3\7\66\2\2\u00f3\u00f4\7\t\2\2\u00f4\u00f5")
        buf.write("\7/\2\2\u00f5\u00f6\5\"\22\2\u00f6\u00f7\7\60\2\2\u00f7")
        buf.write("\u00f8\5\4\3\2\u00f8!\3\2\2\2\u00f9\u00fa\5$\23\2\u00fa")
        buf.write("\u00fb\5\"\22\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5$\23")
        buf.write("\2\u00fd\u00f9\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe#\3\2")
        buf.write("\2\2\u00ff\u0100\7\66\2\2\u0100\u0101\5\b\5\2\u0101\u0102")
        buf.write("\5\4\3\2\u0102%\3\2\2\2\u0103\u0104\7\b\2\2\u0104\u0105")
        buf.write("\7\66\2\2\u0105\u0106\7\n\2\2\u0106\u0107\7/\2\2\u0107")
        buf.write("\u0108\5(\25\2\u0108\u0109\7\60\2\2\u0109\u010a\5\4\3")
        buf.write("\2\u010a\'\3\2\2\2\u010b\u010c\5*\26\2\u010c\u010d\5(")
        buf.write("\25\2\u010d\u0110\3\2\2\2\u010e\u0110\5*\26\2\u010f\u010b")
        buf.write("\3\2\2\2\u010f\u010e\3\2\2\2\u0110)\3\2\2\2\u0111\u0112")
        buf.write("\7\66\2\2\u0112\u0113\7-\2\2\u0113\u0114\5,\27\2\u0114")
        buf.write("\u0117\7.\2\2\u0115\u0118\5\b\5\2\u0116\u0118\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118\u0119\3")
        buf.write("\2\2\2\u0119\u011a\5\4\3\2\u011a+\3\2\2\2\u011b\u011e")
        buf.write("\5.\30\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e-\3\2\2\2\u011f\u0120\5\60\31\2\u0120")
        buf.write("\u0121\7\64\2\2\u0121\u0122\5.\30\2\u0122\u0125\3\2\2")
        buf.write("\2\u0123\u0125\5\60\31\2\u0124\u011f\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125/\3\2\2\2\u0126\u0127\5\62\32\2\u0127\u0128")
        buf.write("\5\b\5\2\u0128\61\3\2\2\2\u0129\u012a\7\66\2\2\u012a\u012b")
        buf.write("\7\64\2\2\u012b\u012e\5\62\32\2\u012c\u012e\7\66\2\2\u012d")
        buf.write("\u0129\3\2\2\2\u012d\u012c\3\2\2\2\u012e\63\3\2\2\2\u012f")
        buf.write("\u0132\5\66\34\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132\65\3\2\2\2\u0133\u0134\5")
        buf.write("8\35\2\u0134\u0135\5\66\34\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0138\58\35\2\u0137\u0133\3\2\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0138\67\3\2\2\2\u0139\u0143\5\f\7\2\u013a\u0143\5\n")
        buf.write("\6\2\u013b\u0143\5:\36\2\u013c\u0143\5> \2\u013d\u0143")
        buf.write("\5J&\2\u013e\u0143\5V,\2\u013f\u0143\5X-\2\u0140\u0143")
        buf.write("\5Z.\2\u0141\u0143\5\\/\2\u0142\u0139\3\2\2\2\u0142\u013a")
        buf.write("\3\2\2\2\u0142\u013b\3\2\2\2\u0142\u013c\3\2\2\2\u0142")
        buf.write("\u013d\3\2\2\2\u0142\u013e\3\2\2\2\u0142\u013f\3\2\2\2")
        buf.write("\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u01439\3\2\2")
        buf.write("\2\u0144\u0145\5<\37\2\u0145\u0146\t\2\2\2\u0146\u0147")
        buf.write("\5\u0084C\2\u0147\u0148\7\65\2\2\u0148;\3\2\2\2\u0149")
        buf.write("\u014a\b\37\1\2\u014a\u014b\7\66\2\2\u014b\u0157\3\2\2")
        buf.write("\2\u014c\u0153\f\4\2\2\u014d\u014e\7\61\2\2\u014e\u014f")
        buf.write("\5\u0084C\2\u014f\u0150\7\62\2\2\u0150\u0154\3\2\2\2\u0151")
        buf.write("\u0152\7,\2\2\u0152\u0154\7\66\2\2\u0153\u014d\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u014c\3")
        buf.write("\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158=\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b")
        buf.write("\7\3\2\2\u015b\u015c\7-\2\2\u015c\u015d\5\u0084C\2\u015d")
        buf.write("\u015e\7.\2\2\u015e\u015f\7/\2\2\u015f\u0160\5\66\34\2")
        buf.write("\u0160\u0161\7\60\2\2\u0161\u0162\5@!\2\u0162\u0163\5")
        buf.write("F$\2\u0163\u0164\5\4\3\2\u0164?\3\2\2\2\u0165\u0168\5")
        buf.write("B\"\2\u0166\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168A\3\2\2\2\u0169\u016a\5D#\2\u016a\u016b")
        buf.write("\5B\"\2\u016b\u016e\3\2\2\2\u016c\u016e\5D#\2\u016d\u0169")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016eC\3\2\2\2\u016f\u0170")
        buf.write("\7\4\2\2\u0170\u0171\7\3\2\2\u0171\u0172\7-\2\2\u0172")
        buf.write("\u0173\5\u0084C\2\u0173\u0174\7.\2\2\u0174\u0175\7/\2")
        buf.write("\2\u0175\u0176\5\66\34\2\u0176\u0177\7\60\2\2\u0177E\3")
        buf.write("\2\2\2\u0178\u017b\5H%\2\u0179\u017b\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u0179\3\2\2\2\u017bG\3\2\2\2\u017c\u017d")
        buf.write("\7\4\2\2\u017d\u017e\7/\2\2\u017e\u017f\5\66\34\2\u017f")
        buf.write("\u0180\7\60\2\2\u0180I\3\2\2\2\u0181\u0185\5L\'\2\u0182")
        buf.write("\u0185\5N(\2\u0183\u0185\5P)\2\u0184\u0181\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\7/\2\2\u0187\u0188\5\66\34\2\u0188\u0189")
        buf.write("\7\60\2\2\u0189\u018a\5\4\3\2\u018aK\3\2\2\2\u018b\u018c")
        buf.write("\7\5\2\2\u018c\u018d\5\u0084C\2\u018dM\3\2\2\2\u018e\u0191")
        buf.write("\7\5\2\2\u018f\u0192\5R*\2\u0190\u0192\5T+\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\5\4\3\2\u0194\u0195\5\u0084C\2\u0195\u0196\5\4")
        buf.write("\3\2\u0196\u0197\5R*\2\u0197O\3\2\2\2\u0198\u0199\7\5")
        buf.write("\2\2\u0199\u019a\7\66\2\2\u019a\u019b\7\64\2\2\u019b\u019c")
        buf.write("\7\66\2\2\u019c\u019d\7&\2\2\u019d\u019e\7\23\2\2\u019e")
        buf.write("\u019f\5\u0084C\2\u019fQ\3\2\2\2\u01a0\u01a1\7\66\2\2")
        buf.write("\u01a1\u01a2\t\2\2\2\u01a2\u01a3\5\u0084C\2\u01a3S\3\2")
        buf.write("\2\2\u01a4\u01a5\7\20\2\2\u01a5\u01a8\7\66\2\2\u01a6\u01a9")
        buf.write("\5\b\5\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7%\2\2")
        buf.write("\u01ab\u01ac\5\u0084C\2\u01acU\3\2\2\2\u01ad\u01ae\7\22")
        buf.write("\2\2\u01ae\u01af\5\4\3\2\u01afW\3\2\2\2\u01b0\u01b1\7")
        buf.write("\21\2\2\u01b1\u01b2\5\4\3\2\u01b2Y\3\2\2\2\u01b3\u01b4")
        buf.write("\5<\37\2\u01b4\u01b5\7,\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b8\3\2\2\2\u01b7\u01b3\3\2\2\2\u01b7\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01ba\7\66\2\2\u01ba\u01bb")
        buf.write("\7-\2\2\u01bb\u01bc\5\u0080A\2\u01bc\u01bd\7.\2\2\u01bd")
        buf.write("\u01be\5\4\3\2\u01be[\3\2\2\2\u01bf\u01c2\7\6\2\2\u01c0")
        buf.write("\u01c3\5\u0084C\2\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3\2")
        buf.write("\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5")
        buf.write("\5\4\3\2\u01c5]\3\2\2\2\u01c6\u01cf\7\67\2\2\u01c7\u01cf")
        buf.write("\78\2\2\u01c8\u01cf\79\2\2\u01c9\u01cf\7\25\2\2\u01ca")
        buf.write("\u01cf\7\26\2\2\u01cb\u01cf\7\24\2\2\u01cc\u01cf\5v<\2")
        buf.write("\u01cd\u01cf\5j\66\2\u01ce\u01c6\3\2\2\2\u01ce\u01c7\3")
        buf.write("\2\2\2\u01ce\u01c8\3\2\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca")
        buf.write("\3\2\2\2\u01ce\u01cb\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf_\3\2\2\2\u01d0\u01d3\5b\62\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2")
        buf.write("\u01d3a\3\2\2\2\u01d4\u01d5\5^\60\2\u01d5\u01d6\7\64\2")
        buf.write("\2\u01d6\u01d7\5b\62\2\u01d7\u01da\3\2\2\2\u01d8\u01da")
        buf.write("\5^\60\2\u01d9\u01d4\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("c\3\2\2\2\u01db\u01e3\7\67\2\2\u01dc\u01e3\78\2\2\u01dd")
        buf.write("\u01e3\79\2\2\u01de\u01e3\7\25\2\2\u01df\u01e3\7\26\2")
        buf.write("\2\u01e0\u01e3\7\24\2\2\u01e1\u01e3\5v<\2\u01e2\u01db")
        buf.write("\3\2\2\2\u01e2\u01dc\3\2\2\2\u01e2\u01dd\3\2\2\2\u01e2")
        buf.write("\u01de\3\2\2\2\u01e2\u01df\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e1\3\2\2\2\u01e3e\3\2\2\2\u01e4\u01e7\5h\65")
        buf.write("\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7g\3\2\2\2\u01e8\u01e9\5d\63\2\u01e9\u01ea")
        buf.write("\7\64\2\2\u01ea\u01eb\5h\65\2\u01eb\u01ee\3\2\2\2\u01ec")
        buf.write("\u01ee\5d\63\2\u01ed\u01e8\3\2\2\2\u01ed\u01ec\3\2\2\2")
        buf.write("\u01eei\3\2\2\2\u01ef\u01f0\5\6\4\2\u01f0\u01f1\7/\2\2")
        buf.write("\u01f1\u01f2\5l\67\2\u01f2\u01f3\7\60\2\2\u01f3k\3\2\2")
        buf.write("\2\u01f4\u01f5\5n8\2\u01f5\u01f6\7\64\2\2\u01f6\u01f7")
        buf.write("\5l\67\2\u01f7\u01fa\3\2\2\2\u01f8\u01fa\5n8\2\u01f9\u01f4")
        buf.write("\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fam\3\2\2\2\u01fb\u0201")
        buf.write("\5h\65\2\u01fc\u01fd\7/\2\2\u01fd\u01fe\5n8\2\u01fe\u01ff")
        buf.write("\7\60\2\2\u01ff\u0201\3\2\2\2\u0200\u01fb\3\2\2\2\u0200")
        buf.write("\u01fc\3\2\2\2\u0201o\3\2\2\2\u0202\u0203\5r:\2\u0203")
        buf.write("\u0204\5p9\2\u0204\u0207\3\2\2\2\u0205\u0207\5r:\2\u0206")
        buf.write("\u0202\3\2\2\2\u0206\u0205\3\2\2\2\u0207q\3\2\2\2\u0208")
        buf.write("\u0209\7\61\2\2\u0209\u020a\7\67\2\2\u020a\u020b\7\62")
        buf.write("\2\2\u020bs\3\2\2\2\u020c\u020d\t\3\2\2\u020du\3\2\2\2")
        buf.write("\u020e\u020f\7\66\2\2\u020f\u0210\7/\2\2\u0210\u0211\5")
        buf.write("x=\2\u0211\u0212\7\60\2\2\u0212w\3\2\2\2\u0213\u0216\5")
        buf.write("z>\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0214")
        buf.write("\3\2\2\2\u0216y\3\2\2\2\u0217\u0218\5|?\2\u0218\u0219")
        buf.write("\7\64\2\2\u0219\u021a\5z>\2\u021a\u021d\3\2\2\2\u021b")
        buf.write("\u021d\5|?\2\u021c\u0217\3\2\2\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("{\3\2\2\2\u021e\u021f\7\66\2\2\u021f\u0220\7\63\2\2\u0220")
        buf.write("\u0223\5\u0084C\2\u0221\u0223\5\30\r\2\u0222\u021e\3\2")
        buf.write("\2\2\u0222\u0221\3\2\2\2\u0223}\3\2\2\2\u0224\u0225\7")
        buf.write("\66\2\2\u0225\u0226\7-\2\2\u0226\u0227\5\u0080A\2\u0227")
        buf.write("\u0228\7.\2\2\u0228\177\3\2\2\2\u0229\u022c\5\u0082B\2")
        buf.write("\u022a\u022c\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022a\3")
        buf.write("\2\2\2\u022c\u0081\3\2\2\2\u022d\u022e\5\u0084C\2\u022e")
        buf.write("\u022f\7\64\2\2\u022f\u0230\5\u0082B\2\u0230\u0233\3\2")
        buf.write("\2\2\u0231\u0233\5\u0084C\2\u0232\u022d\3\2\2\2\u0232")
        buf.write("\u0231\3\2\2\2\u0233\u0083\3\2\2\2\u0234\u0235\bC\1\2")
        buf.write("\u0235\u0236\5\u0086D\2\u0236\u023c\3\2\2\2\u0237\u0238")
        buf.write("\f\4\2\2\u0238\u0239\7#\2\2\u0239\u023b\5\u0086D\2\u023a")
        buf.write("\u0237\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u0085\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0240\bD\1\2\u0240\u0241\5\u0088E\2\u0241")
        buf.write("\u0247\3\2\2\2\u0242\u0243\f\4\2\2\u0243\u0244\7\"\2\2")
        buf.write("\u0244\u0246\5\u0088E\2\u0245\u0242\3\2\2\2\u0246\u0249")
        buf.write("\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248")
        buf.write("\u0087\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\bE\1\2")
        buf.write("\u024b\u024c\5\u008aF\2\u024c\u0252\3\2\2\2\u024d\u024e")
        buf.write("\f\4\2\2\u024e\u024f\t\4\2\2\u024f\u0251\5\u008aF\2\u0250")
        buf.write("\u024d\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2")
        buf.write("\u0252\u0253\3\2\2\2\u0253\u0089\3\2\2\2\u0254\u0252\3")
        buf.write("\2\2\2\u0255\u0256\bF\1\2\u0256\u0257\5\u008cG\2\u0257")
        buf.write("\u025d\3\2\2\2\u0258\u0259\f\4\2\2\u0259\u025a\t\5\2\2")
        buf.write("\u025a\u025c\5\u008cG\2\u025b\u0258\3\2\2\2\u025c\u025f")
        buf.write("\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write("\u008b\3\2\2\2\u025f\u025d\3\2\2\2\u0260\u0261\bG\1\2")
        buf.write("\u0261\u0262\5\u008eH\2\u0262\u0268\3\2\2\2\u0263\u0264")
        buf.write("\f\4\2\2\u0264\u0265\t\6\2\2\u0265\u0267\5\u008eH\2\u0266")
        buf.write("\u0263\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269\u008d\3\2\2\2\u026a\u0268\3")
        buf.write("\2\2\2\u026b\u026c\t\7\2\2\u026c\u026f\5\u008eH\2\u026d")
        buf.write("\u026f\5\u0090I\2\u026e\u026b\3\2\2\2\u026e\u026d\3\2")
        buf.write("\2\2\u026f\u008f\3\2\2\2\u0270\u0271\bI\1\2\u0271\u0272")
        buf.write("\5\u0092J\2\u0272\u0281\3\2\2\2\u0273\u027d\f\4\2\2\u0274")
        buf.write("\u0275\7\61\2\2\u0275\u0276\5\u0084C\2\u0276\u0277\7\62")
        buf.write("\2\2\u0277\u027e\3\2\2\2\u0278\u027b\7,\2\2\u0279\u027c")
        buf.write("\7\66\2\2\u027a\u027c\5~@\2\u027b\u0279\3\2\2\2\u027b")
        buf.write("\u027a\3\2\2\2\u027c\u027e\3\2\2\2\u027d\u0274\3\2\2\2")
        buf.write("\u027d\u0278\3\2\2\2\u027e\u0280\3\2\2\2\u027f\u0273\3")
        buf.write("\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0282")
        buf.write("\3\2\2\2\u0282\u0091\3\2\2\2\u0283\u0281\3\2\2\2\u0284")
        buf.write("\u0285\7-\2\2\u0285\u0286\5\u0084C\2\u0286\u0287\7.\2")
        buf.write("\2\u0287\u028c\3\2\2\2\u0288\u028c\5^\60\2\u0289\u028c")
        buf.write("\7\66\2\2\u028a\u028c\5~@\2\u028b\u0284\3\2\2\2\u028b")
        buf.write("\u0288\3\2\2\2\u028b\u0289\3\2\2\2\u028b\u028a\3\2\2\2")
        buf.write("\u028c\u0093\3\2\2\2\67\u00a2\u00a9\u00ad\u00ba\u00c1")
        buf.write("\u00cc\u00d4\u00dc\u00e5\u00ec\u00fd\u010f\u0117\u011d")
        buf.write("\u0124\u012d\u0131\u0137\u0142\u0153\u0157\u0167\u016d")
        buf.write("\u017a\u0184\u0191\u01a8\u01b7\u01c2\u01ce\u01d2\u01d9")
        buf.write("\u01e2\u01e6\u01ed\u01f9\u0200\u0206\u0215\u021c\u0222")
        buf.write("\u022b\u0232\u023c\u0247\u0252\u025d\u0268\u026e\u027b")
        buf.write("\u027d\u0281\u028b")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "':'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "IS_EQUAL", "IS_DIFF", "LT", "LT_EQUAL", "GT", 
                      "GT_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN_COLON", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "DOT", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_CURLY", "RIGHT_CURLY", "LEFT_SQUARE", "RIGHT_SQUARE", 
                      "COLON", "COMMA", "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "BOOL_LIT", "NIL_LIT", "WS", "NEWLINE", 
                      "COMMENT_BLOCK", "COMMENT_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_terminate = 1
    RULE_array_type = 2
    RULE_all_types = 3
    RULE_var_declaration = 4
    RULE_const_declaration = 5
    RULE_list_declaration = 6
    RULE_declaration = 7
    RULE_method_declaration = 8
    RULE_list_method_element = 9
    RULE_method_element = 10
    RULE_func_declaration = 11
    RULE_list_func_arguments_prime = 12
    RULE_list_func_arguments = 13
    RULE_func_arguments = 14
    RULE_struct_declaration = 15
    RULE_list_struct_argument = 16
    RULE_struct_argument = 17
    RULE_interface_declaration = 18
    RULE_list_interface_method_declaration = 19
    RULE_interface_method_declaration = 20
    RULE_list_interface_method_element_prime = 21
    RULE_list_interface_method_element = 22
    RULE_interface_method_element = 23
    RULE_list_ID = 24
    RULE_list_statement_prime = 25
    RULE_list_statement = 26
    RULE_statement = 27
    RULE_assignment_statement = 28
    RULE_assignment_lhs = 29
    RULE_if_statement = 30
    RULE_list_elseif_prime = 31
    RULE_list_elseif = 32
    RULE_elseif = 33
    RULE_else_statement_prime = 34
    RULE_else_statement = 35
    RULE_for_statement = 36
    RULE_basic_for = 37
    RULE_init_for = 38
    RULE_range_for = 39
    RULE_assignment_stmt_for = 40
    RULE_var_declaration_for = 41
    RULE_break_statement = 42
    RULE_continue_statement = 43
    RULE_call_statement = 44
    RULE_return_statement = 45
    RULE_literal = 46
    RULE_list_literal_prime = 47
    RULE_list_literal = 48
    RULE_literal_primitive = 49
    RULE_list_literal_primitive_prime = 50
    RULE_list_literal_primitive = 51
    RULE_array_literal = 52
    RULE_list_array_element = 53
    RULE_array_element = 54
    RULE_list_array_specific = 55
    RULE_array_specific = 56
    RULE_array_declare_type = 57
    RULE_struct_literal = 58
    RULE_list_struct_element_prime = 59
    RULE_list_struct_element = 60
    RULE_struct_element = 61
    RULE_function_call = 62
    RULE_list_expression_prime = 63
    RULE_list_expression = 64
    RULE_expression = 65
    RULE_expression1 = 66
    RULE_expression2 = 67
    RULE_expression3 = 68
    RULE_expression4 = 69
    RULE_expression5 = 70
    RULE_expression6 = 71
    RULE_expression7 = 72

    ruleNames =  [ "program", "terminate", "array_type", "all_types", "var_declaration", 
                   "const_declaration", "list_declaration", "declaration", 
                   "method_declaration", "list_method_element", "method_element", 
                   "func_declaration", "list_func_arguments_prime", "list_func_arguments", 
                   "func_arguments", "struct_declaration", "list_struct_argument", 
                   "struct_argument", "interface_declaration", "list_interface_method_declaration", 
                   "interface_method_declaration", "list_interface_method_element_prime", 
                   "list_interface_method_element", "interface_method_element", 
                   "list_ID", "list_statement_prime", "list_statement", 
                   "statement", "assignment_statement", "assignment_lhs", 
                   "if_statement", "list_elseif_prime", "list_elseif", "elseif", 
                   "else_statement_prime", "else_statement", "for_statement", 
                   "basic_for", "init_for", "range_for", "assignment_stmt_for", 
                   "var_declaration_for", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "literal", "list_literal_prime", 
                   "list_literal", "literal_primitive", "list_literal_primitive_prime", 
                   "list_literal_primitive", "array_literal", "list_array_element", 
                   "array_element", "list_array_specific", "array_specific", 
                   "array_declare_type", "struct_literal", "list_struct_element_prime", 
                   "list_struct_element", "struct_element", "function_call", 
                   "list_expression_prime", "list_expression", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    IS_EQUAL=26
    IS_DIFF=27
    LT=28
    LT_EQUAL=29
    GT=30
    GT_EQUAL=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ASSIGN_COLON=36
    ADD_ASSIGN=37
    SUB_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    DOT=42
    LEFT_PAREN=43
    RIGHT_PAREN=44
    LEFT_CURLY=45
    RIGHT_CURLY=46
    LEFT_SQUARE=47
    RIGHT_SQUARE=48
    COLON=49
    COMMA=50
    SEMICOLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    BOOL_LIT=56
    NIL_LIT=57
    WS=58
    NEWLINE=59
    COMMENT_BLOCK=60
    COMMENT_LINE=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.list_declaration()
            self.state = 147
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_terminate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminate" ):
                return visitor.visitTerminate(self)
            else:
                return visitor.visitChildren(self)




    def terminate(self):

        localctx = MiniGoParser.TerminateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_terminate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_array_specific(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_specificContext,0)


        def array_declare_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declare_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.list_array_specific()
            self.state = 152
            self.array_declare_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_all_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_types" ):
                return visitor.visitAll_types(self)
            else:
                return visitor.visitChildren(self)




    def all_types(self):

        localctx = MiniGoParser.All_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_all_types)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.array_type()
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = MiniGoParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(MiniGoParser.VAR)
            self.state = 163
            self.match(MiniGoParser.ID)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 164
                self.all_types()
                pass

            elif la_ == 2:
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                    self.state = 165
                    self.all_types()
                    pass
                elif token in [MiniGoParser.ASSIGN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self.match(MiniGoParser.ASSIGN)
                self.state = 170
                self.expression(0)
                pass


            self.state = 173
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration" ):
                return visitor.visitConst_declaration(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration(self):

        localctx = MiniGoParser.Const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MiniGoParser.CONST)
            self.state = 176
            self.match(MiniGoParser.ID)
            self.state = 177
            self.match(MiniGoParser.ASSIGN)
            self.state = 178
            self.expression(0)
            self.state = 179
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declaration" ):
                return visitor.visitList_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_declaration(self):

        localctx = MiniGoParser.List_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 181
                self.declaration()
                self.state = 184 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


        def struct_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaration)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.var_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.const_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.interface_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def list_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_elementContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = MiniGoParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 194
            self.list_method_element()
            self.state = 195
            self.match(MiniGoParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_element(self):
            return self.getTypedRuleContext(MiniGoParser.Method_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_element" ):
                return visitor.visitList_method_element(self)
            else:
                return visitor.visitChildren(self)




    def list_method_element(self):

        localctx = MiniGoParser.List_method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_method_element)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.method_element()
                self.state = 198
                self.match(MiniGoParser.COMMA)
                self.state = 199
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.method_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_element" ):
                return visitor.visitMethod_element(self)
            else:
                return visitor.visitChildren(self)




    def method_element(self):

        localctx = MiniGoParser.Method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.ID)
            self.state = 205
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def list_func_arguments_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_func_arguments_primeContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declarationContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declaration" ):
                return visitor.visitFunc_declaration(self)
            else:
                return visitor.visitChildren(self)




    def func_declaration(self):

        localctx = MiniGoParser.Func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.FUNC)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_PAREN]:
                self.state = 208
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 213
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 214
            self.list_func_arguments_prime()
            self.state = 215
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 216
                self.all_types()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 220
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 221
            self.list_statement()
            self.state = 222
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 223
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_func_arguments_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_func_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.List_func_argumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_func_arguments_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_func_arguments_prime" ):
                return visitor.visitList_func_arguments_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_func_arguments_prime(self):

        localctx = MiniGoParser.List_func_arguments_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_func_arguments_prime)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.list_func_arguments()
                pass
            elif token in [MiniGoParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_func_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.Func_argumentsContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_func_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.List_func_argumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_func_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_func_arguments" ):
                return visitor.visitList_func_arguments(self)
            else:
                return visitor.visitChildren(self)




    def list_func_arguments(self):

        localctx = MiniGoParser.List_func_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_func_arguments)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.func_arguments()
                self.state = 230
                self.match(MiniGoParser.COMMA)
                self.state = 231
                self.list_func_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.func_arguments()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_arguments" ):
                return visitor.visitFunc_arguments(self)
            else:
                return visitor.visitChildren(self)




    def func_arguments(self):

        localctx = MiniGoParser.Func_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.list_ID()
            self.state = 237
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_struct_argument(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_argumentContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(MiniGoParser.TYPE)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 241
            self.match(MiniGoParser.STRUCT)
            self.state = 242
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 243
            self.list_struct_argument()
            self.state = 244
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 245
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_argument(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_argumentContext,0)


        def list_struct_argument(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_argumentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_argument" ):
                return visitor.visitList_struct_argument(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_argument(self):

        localctx = MiniGoParser.List_struct_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_struct_argument)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.struct_argument()
                self.state = 248
                self.list_struct_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.struct_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_argument" ):
                return visitor.visitStruct_argument(self)
            else:
                return visitor.visitChildren(self)




    def struct_argument(self):

        localctx = MiniGoParser.Struct_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MiniGoParser.ID)
            self.state = 254
            self.all_types()
            self.state = 255
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_interface_method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_declarationContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MiniGoParser.TYPE)
            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 259
            self.match(MiniGoParser.INTERFACE)
            self.state = 260
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 261
            self.list_interface_method_declaration()
            self.state = 262
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 263
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_declarationContext,0)


        def list_interface_method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_method_declaration" ):
                return visitor.visitList_interface_method_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_method_declaration(self):

        localctx = MiniGoParser.List_interface_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_interface_method_declaration)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.interface_method_declaration()
                self.state = 266
                self.list_interface_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.interface_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def list_interface_method_element_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_element_primeContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_declaration" ):
                return visitor.visitInterface_method_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_declaration(self):

        localctx = MiniGoParser.Interface_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_interface_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.ID)
            self.state = 272
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 273
            self.list_interface_method_element_prime()
            self.state = 274
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 275
                self.all_types()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 279
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_method_element_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_interface_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_method_element_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_method_element_prime" ):
                return visitor.visitList_interface_method_element_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_method_element_prime(self):

        localctx = MiniGoParser.List_interface_method_element_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_interface_method_element_prime)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.list_interface_method_element()
                pass
            elif token in [MiniGoParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_method_element" ):
                return visitor.visitList_interface_method_element(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_method_element(self):

        localctx = MiniGoParser.List_interface_method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_interface_method_element)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.interface_method_element()
                self.state = 286
                self.match(MiniGoParser.COMMA)
                self.state = 287
                self.list_interface_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.interface_method_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_element" ):
                return visitor.visitInterface_method_element(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_element(self):

        localctx = MiniGoParser.Interface_method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interface_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.list_ID()
            self.state = 293
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_ID)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(MiniGoParser.ID)
                self.state = 296
                self.match(MiniGoParser.COMMA)
                self.state = 297
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_prime" ):
                return visitor.visitList_statement_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_prime(self):

        localctx = MiniGoParser.List_statement_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_statement_prime)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.list_statement()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_statement)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.statement()
                self.state = 306
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.var_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 315
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 316
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 317
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 318
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 319
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def ASSIGN_COLON(self):
            return self.getToken(MiniGoParser.ASSIGN_COLON, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.assignment_lhs(0)
            self.state = 323
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 324
            self.expression(0)
            self.state = 325
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def LEFT_SQUARE(self):
            return self.getToken(MiniGoParser.LEFT_SQUARE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RIGHT_SQUARE(self):
            return self.getToken(MiniGoParser.RIGHT_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assignment_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 331
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 332
                        self.expression(0)
                        self.state = 333
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 335
                        self.match(MiniGoParser.DOT)
                        self.state = 336
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def list_elseif_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_elseif_primeContext,0)


        def else_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statement_primeContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.IF)
            self.state = 345
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 346
            self.expression(0)
            self.state = 347
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 348
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 349
            self.list_statement()
            self.state = 350
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 351
            self.list_elseif_prime()
            self.state = 352
            self.else_statement_prime()
            self.state = 353
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elseif_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_elseif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elseifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elseif_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elseif_prime" ):
                return visitor.visitList_elseif_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_elseif_prime(self):

        localctx = MiniGoParser.List_elseif_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_list_elseif_prime)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.list_elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elseifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif(self):
            return self.getTypedRuleContext(MiniGoParser.ElseifContext,0)


        def list_elseif(self):
            return self.getTypedRuleContext(MiniGoParser.List_elseifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elseif" ):
                return visitor.visitList_elseif(self)
            else:
                return visitor.visitChildren(self)




    def list_elseif(self):

        localctx = MiniGoParser.List_elseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_list_elseif)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.elseif()
                self.state = 360
                self.list_elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.elseif()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif" ):
                return visitor.visitElseif(self)
            else:
                return visitor.visitChildren(self)




    def elseif(self):

        localctx = MiniGoParser.ElseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.ELSE)
            self.state = 366
            self.match(MiniGoParser.IF)
            self.state = 367
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 368
            self.expression(0)
            self.state = 369
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 370
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 371
            self.list_statement()
            self.state = 372
            self.match(MiniGoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statement_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement_prime" ):
                return visitor.visitElse_statement_prime(self)
            else:
                return visitor.visitChildren(self)




    def else_statement_prime(self):

        localctx = MiniGoParser.Else_statement_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_else_statement_prime)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.else_statement()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.ELSE)
            self.state = 379
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 380
            self.list_statement()
            self.state = 381
            self.match(MiniGoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def basic_for(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_forContext,0)


        def init_for(self):
            return self.getTypedRuleContext(MiniGoParser.Init_forContext,0)


        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 383
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 384
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 385
                self.range_for()
                pass


            self.state = 388
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 389
            self.list_statement()
            self.state = 390
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 391
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for" ):
                return visitor.visitBasic_for(self)
            else:
                return visitor.visitChildren(self)




    def basic_for(self):

        localctx = MiniGoParser.Basic_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.FOR)
            self.state = 394
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def terminate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TerminateContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TerminateContext,i)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assignment_stmt_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_stmt_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_stmt_forContext,i)


        def var_declaration_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaration_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = MiniGoParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MiniGoParser.FOR)
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 397
                self.assignment_stmt_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 398
                self.var_declaration_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 401
            self.terminate()
            self.state = 402
            self.expression(0)
            self.state = 403
            self.terminate()
            self.state = 404
            self.assignment_stmt_for()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN_COLON(self):
            return self.getToken(MiniGoParser.ASSIGN_COLON, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.FOR)
            self.state = 407
            self.match(MiniGoParser.ID)
            self.state = 408
            self.match(MiniGoParser.COMMA)
            self.state = 409
            self.match(MiniGoParser.ID)
            self.state = 410
            self.match(MiniGoParser.ASSIGN_COLON)
            self.state = 411
            self.match(MiniGoParser.RANGE)
            self.state = 412
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmt_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN_COLON(self):
            return self.getToken(MiniGoParser.ASSIGN_COLON, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt_for" ):
                return visitor.visitAssignment_stmt_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt_for(self):

        localctx = MiniGoParser.Assignment_stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignment_stmt_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(MiniGoParser.ID)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 416
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaration_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_for" ):
                return visitor.visitVar_declaration_for(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_for(self):

        localctx = MiniGoParser.Var_declaration_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_var_declaration_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MiniGoParser.VAR)
            self.state = 419
            self.match(MiniGoParser.ID)
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 420
                self.all_types()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 424
            self.match(MiniGoParser.ASSIGN)
            self.state = 425
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(MiniGoParser.BREAK)
            self.state = 428
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.CONTINUE)
            self.state = 431
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def list_expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_primeContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 433
                self.assignment_lhs(0)
                self.state = 434
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 439
            self.match(MiniGoParser.ID)
            self.state = 440
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 441
            self.list_expression_prime()
            self.state = 442
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 443
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(MiniGoParser.RETURN)
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 446
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 450
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 456
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 457
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 458
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 459
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_prime" ):
                return visitor.visitList_literal_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_prime(self):

        localctx = MiniGoParser.List_literal_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_literal_prime)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.list_literal()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = MiniGoParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_literal)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.literal()
                self.state = 467
                self.match(MiniGoParser.COMMA)
                self.state = 468
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_primitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_primitive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_primitive" ):
                return visitor.visitLiteral_primitive(self)
            else:
                return visitor.visitChildren(self)




    def literal_primitive(self):

        localctx = MiniGoParser.Literal_primitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal_primitive)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 476
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 477
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 478
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 479
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_primitive_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_primitiveContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_primitive_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_primitive_prime" ):
                return visitor.visitList_literal_primitive_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_primitive_prime(self):

        localctx = MiniGoParser.List_literal_primitive_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_list_literal_primitive_prime)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.list_literal_primitive()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_primitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_primitiveContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_primitiveContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_primitive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_primitive" ):
                return visitor.visitList_literal_primitive(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_primitive(self):

        localctx = MiniGoParser.List_literal_primitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_literal_primitive)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.literal_primitive()
                self.state = 487
                self.match(MiniGoParser.COMMA)
                self.state = 488
                self.list_literal_primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.literal_primitive()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.array_type()
            self.state = 494
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 495
            self.list_array_element()
            self.state = 496
            self.match(MiniGoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_element" ):
                return visitor.visitList_array_element(self)
            else:
                return visitor.visitChildren(self)




    def list_array_element(self):

        localctx = MiniGoParser.List_array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_list_array_element)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.array_element()
                self.state = 499
                self.match(MiniGoParser.COMMA)
                self.state = 500
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_primitiveContext,0)


        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_element)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.list_literal_primitive()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(MiniGoParser.LEFT_CURLY)
                self.state = 507
                self.array_element()
                self.state = 508
                self.match(MiniGoParser.RIGHT_CURLY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_specificContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_specific(self):
            return self.getTypedRuleContext(MiniGoParser.Array_specificContext,0)


        def list_array_specific(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_specificContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_specific

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_specific" ):
                return visitor.visitList_array_specific(self)
            else:
                return visitor.visitChildren(self)




    def list_array_specific(self):

        localctx = MiniGoParser.List_array_specificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_list_array_specific)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.array_specific()
                self.state = 513
                self.list_array_specific()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.array_specific()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_specificContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE(self):
            return self.getToken(MiniGoParser.LEFT_SQUARE, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RIGHT_SQUARE(self):
            return self.getToken(MiniGoParser.RIGHT_SQUARE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_specific

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_specific" ):
                return visitor.visitArray_specific(self)
            else:
                return visitor.visitChildren(self)




    def array_specific(self):

        localctx = MiniGoParser.Array_specificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array_specific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.LEFT_SQUARE)
            self.state = 519
            self.match(MiniGoParser.INT_LIT)
            self.state = 520
            self.match(MiniGoParser.RIGHT_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declare_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_declare_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare_type" ):
                return visitor.visitArray_declare_type(self)
            else:
                return visitor.visitChildren(self)




    def array_declare_type(self):

        localctx = MiniGoParser.Array_declare_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_array_declare_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_struct_element_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_element_primeContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(MiniGoParser.ID)
            self.state = 525
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 526
            self.list_struct_element_prime()
            self.state = 527
            self.match(MiniGoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_element_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_element_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_element_prime" ):
                return visitor.visitList_struct_element_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_element_prime(self):

        localctx = MiniGoParser.List_struct_element_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_list_struct_element_prime)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.list_struct_element()
                pass
            elif token in [MiniGoParser.RIGHT_CURLY]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_element" ):
                return visitor.visitList_struct_element(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_element(self):

        localctx = MiniGoParser.List_struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_list_struct_element)
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.struct_element()
                self.state = 534
                self.match(MiniGoParser.COMMA)
                self.state = 535
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.struct_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_struct_element)
        try:
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(MiniGoParser.ID)
                self.state = 541
                self.match(MiniGoParser.COLON)
                self.state = 542
                self.expression(0)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.func_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def list_expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_primeContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(MiniGoParser.ID)
            self.state = 547
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 548
            self.list_expression_prime()
            self.state = 549
            self.match(MiniGoParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expression_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression_prime" ):
                return visitor.visitList_expression_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_expression_prime(self):

        localctx = MiniGoParser.List_expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_list_expression_prime)
        try:
            self.state = 553
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.list_expression()
                pass
            elif token in [MiniGoParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_list_expression)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.expression(0)
                self.state = 556
                self.match(MiniGoParser.COMMA)
                self.state = 557
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 565
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 566
                    self.match(MiniGoParser.OR)
                    self.state = 567
                    self.expression1(0) 
                self.state = 572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 576
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 577
                    self.match(MiniGoParser.AND)
                    self.state = 578
                    self.expression2(0) 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def IS_EQUAL(self):
            return self.getToken(MiniGoParser.IS_EQUAL, 0)

        def IS_DIFF(self):
            return self.getToken(MiniGoParser.IS_DIFF, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LT_EQUAL(self):
            return self.getToken(MiniGoParser.LT_EQUAL, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GT_EQUAL(self):
            return self.getToken(MiniGoParser.GT_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 592
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 587
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 588
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IS_EQUAL) | (1 << MiniGoParser.IS_DIFF) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LT_EQUAL) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GT_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 589
                    self.expression3(0) 
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 598
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 599
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 600
                    self.expression4(0) 
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 614
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 609
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 610
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 611
                    self.expression5() 
                self.state = 616
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 620
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 618
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LEFT_SQUARE(self):
            return self.getToken(MiniGoParser.LEFT_SQUARE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RIGHT_SQUARE(self):
            return self.getToken(MiniGoParser.RIGHT_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 625
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 635
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 626
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 627
                        self.expression(0)
                        self.state = 628
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 630
                        self.match(MiniGoParser.DOT)
                        self.state = 633
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                        if la_ == 1:
                            self.state = 631
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 632
                            self.function_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(MiniGoParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MiniGoParser.RIGHT_PAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_expression7)
        try:
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                self.match(MiniGoParser.LEFT_PAREN)
                self.state = 643
                self.expression(0)
                self.state = 644
                self.match(MiniGoParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 647
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 648
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.assignment_lhs_sempred
        self._predicates[65] = self.expression_sempred
        self._predicates[66] = self.expression1_sempred
        self._predicates[67] = self.expression2_sempred
        self._predicates[68] = self.expression3_sempred
        self._predicates[69] = self.expression4_sempred
        self._predicates[71] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assignment_lhs_sempred(self, localctx:Assignment_lhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




