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
        buf.write("\u028a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u009a\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u00a1\n\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ac\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00b3\n\7\3\7\3\7\5\7\u00b7\n\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00ca\n\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\5\f\u00d2\n\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00da\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00e3\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00ea\n\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00fb\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u010d\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0115\n\25\3\25\3")
        buf.write("\25\3\26\3\26\5\26\u011b\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0122\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u012b\n\31\3\32\3\32\5\32\u012f\n\32\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0135\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0140\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0151\n\36\7\36\u0153\n\36\f\36\16\36\u0156\13\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \5 \u0165\n \3!\3!\3!\3!\5!\u016b\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\5#\u0178\n#\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\5%\u0182\n%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\5\'\u018f\n\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\5*\u01a6\n*\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\5-\u01b5\n-\3-\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\5.\u01c0\n.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\5/\u01cb\n/\3\60\3\60\5\60\u01cf\n\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u01d6\n\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01df\n\62\3\63\3\63\5\63\u01e3\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01ea\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u01f6\n\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u01fd\n\67\38\38\38\38\58\u0203")
        buf.write("\n8\39\39\39\39\3:\3:\3;\3;\3;\3;\3;\3<\3<\5<\u0212\n")
        buf.write("<\3=\3=\3=\3=\3=\5=\u0219\n=\3>\3>\3>\3>\5>\u021f\n>\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\5@\u0228\n@\3A\3A\3A\3A\3A\5A\u022f")
        buf.write("\nA\3B\3B\3B\3B\3B\3B\7B\u0237\nB\fB\16B\u023a\13B\3C")
        buf.write("\3C\3C\3C\3C\3C\7C\u0242\nC\fC\16C\u0245\13C\3D\3D\3D")
        buf.write("\3D\3D\3D\7D\u024d\nD\fD\16D\u0250\13D\3E\3E\3E\3E\3E")
        buf.write("\3E\7E\u0258\nE\fE\16E\u025b\13E\3F\3F\3F\3F\3F\3F\7F")
        buf.write("\u0263\nF\fF\16F\u0266\13F\3G\3G\3G\5G\u026b\nG\3H\3H")
        buf.write("\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u0278\nH\5H\u027a\nH\7")
        buf.write("H\u027c\nH\fH\16H\u027f\13H\3I\3I\3I\3I\3I\3I\3I\5I\u0288")
        buf.write("\nI\3I\2\t:\u0082\u0084\u0086\u0088\u008a\u008eJ\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\2\t\3\2(-\3\289\4")
        buf.write("\2\r\2088\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\2\u0291")
        buf.write("\2\u0092\3\2\2\2\4\u0099\3\2\2\2\6\u00a0\3\2\2\2\b\u00a2")
        buf.write("\3\2\2\2\n\u00ab\3\2\2\2\f\u00ad\3\2\2\2\16\u00ba\3\2")
        buf.write("\2\2\20\u00c0\3\2\2\2\22\u00c9\3\2\2\2\24\u00cb\3\2\2")
        buf.write("\2\26\u00ce\3\2\2\2\30\u00e2\3\2\2\2\32\u00e9\3\2\2\2")
        buf.write("\34\u00eb\3\2\2\2\36\u00ee\3\2\2\2 \u00fa\3\2\2\2\"\u00fc")
        buf.write("\3\2\2\2$\u0100\3\2\2\2&\u010c\3\2\2\2(\u010e\3\2\2\2")
        buf.write("*\u011a\3\2\2\2,\u0121\3\2\2\2.\u0123\3\2\2\2\60\u012a")
        buf.write("\3\2\2\2\62\u012e\3\2\2\2\64\u0134\3\2\2\2\66\u013f\3")
        buf.write("\2\2\28\u0141\3\2\2\2:\u0146\3\2\2\2<\u0157\3\2\2\2>\u0164")
        buf.write("\3\2\2\2@\u016a\3\2\2\2B\u016c\3\2\2\2D\u0177\3\2\2\2")
        buf.write("F\u0179\3\2\2\2H\u0181\3\2\2\2J\u0188\3\2\2\2L\u018b\3")
        buf.write("\2\2\2N\u0195\3\2\2\2P\u019d\3\2\2\2R\u01a1\3\2\2\2T\u01aa")
        buf.write("\3\2\2\2V\u01ad\3\2\2\2X\u01b4\3\2\2\2Z\u01bc\3\2\2\2")
        buf.write("\\\u01ca\3\2\2\2^\u01ce\3\2\2\2`\u01d5\3\2\2\2b\u01de")
        buf.write("\3\2\2\2d\u01e2\3\2\2\2f\u01e9\3\2\2\2h\u01eb\3\2\2\2")
        buf.write("j\u01f5\3\2\2\2l\u01fc\3\2\2\2n\u0202\3\2\2\2p\u0204\3")
        buf.write("\2\2\2r\u0208\3\2\2\2t\u020a\3\2\2\2v\u0211\3\2\2\2x\u0218")
        buf.write("\3\2\2\2z\u021e\3\2\2\2|\u0220\3\2\2\2~\u0227\3\2\2\2")
        buf.write("\u0080\u022e\3\2\2\2\u0082\u0230\3\2\2\2\u0084\u023b\3")
        buf.write("\2\2\2\u0086\u0246\3\2\2\2\u0088\u0251\3\2\2\2\u008a\u025c")
        buf.write("\3\2\2\2\u008c\u026a\3\2\2\2\u008e\u026c\3\2\2\2\u0090")
        buf.write("\u0287\3\2\2\2\u0092\u0093\5\4\3\2\u0093\u0094\7\2\2\3")
        buf.write("\u0094\3\3\2\2\2\u0095\u0096\5\6\4\2\u0096\u0097\5\4\3")
        buf.write("\2\u0097\u009a\3\2\2\2\u0098\u009a\5\6\4\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\5\3\2\2\2\u009b\u00a1")
        buf.write("\5\f\7\2\u009c\u00a1\5\16\b\2\u009d\u00a1\5\26\f\2\u009e")
        buf.write("\u00a1\5\36\20\2\u009f\u00a1\5$\23\2\u00a0\u009b\3\2\2")
        buf.write("\2\u00a0\u009c\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\7\3\2\2\2\u00a2\u00a3")
        buf.write("\5n8\2\u00a3\u00a4\5r:\2\u00a4\t\3\2\2\2\u00a5\u00ac\5")
        buf.write("\b\5\2\u00a6\u00ac\7\20\2\2\u00a7\u00ac\7\16\2\2\u00a8")
        buf.write("\u00ac\7\17\2\2\u00a9\u00ac\7\r\2\2\u00aa\u00ac\78\2\2")
        buf.write("\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3")
        buf.write("\2\2\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\13\3\2\2\2\u00ad\u00ae\7\22\2\2\u00ae\u00b6")
        buf.write("\78\2\2\u00af\u00b7\5\n\6\2\u00b0\u00b3\5\n\6\2\u00b1")
        buf.write("\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b5\7\'\2\2\u00b5\u00b7\5")
        buf.write("\u0082B\2\u00b6\u00af\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\7\67\2\2\u00b9\r\3\2\2\2\u00ba")
        buf.write("\u00bb\7\21\2\2\u00bb\u00bc\78\2\2\u00bc\u00bd\7\'\2\2")
        buf.write("\u00bd\u00be\5\u0082B\2\u00be\u00bf\7\67\2\2\u00bf\17")
        buf.write("\3\2\2\2\u00c0\u00c1\7/\2\2\u00c1\u00c2\5\22\n\2\u00c2")
        buf.write("\u00c3\7\60\2\2\u00c3\21\3\2\2\2\u00c4\u00c5\5\24\13\2")
        buf.write("\u00c5\u00c6\7\66\2\2\u00c6\u00c7\5\22\n\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00ca\5\24\13\2\u00c9\u00c4\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\23\3\2\2\2\u00cb\u00cc\78\2\2\u00cc")
        buf.write("\u00cd\78\2\2\u00cd\25\3\2\2\2\u00ce\u00d1\7\t\2\2\u00cf")
        buf.write("\u00d2\5\20\t\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\78\2\2\u00d4\u00d5\7/\2\2\u00d5\u00d6\5\30\r\2\u00d6")
        buf.write("\u00d9\7\60\2\2\u00d7\u00da\5\n\6\2\u00d8\u00da\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\u00dc\7\61\2\2\u00dc\u00dd\5\62\32\2\u00dd")
        buf.write("\u00de\7\62\2\2\u00de\u00df\7\67\2\2\u00df\27\3\2\2\2")
        buf.write("\u00e0\u00e3\5\32\16\2\u00e1\u00e3\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\31\3\2\2\2\u00e4\u00e5")
        buf.write("\5\34\17\2\u00e5\u00e6\7\66\2\2\u00e6\u00e7\5\32\16\2")
        buf.write("\u00e7\u00ea\3\2\2\2\u00e8\u00ea\5\34\17\2\u00e9\u00e4")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\33\3\2\2\2\u00eb\u00ec")
        buf.write("\5\60\31\2\u00ec\u00ed\5\n\6\2\u00ed\35\3\2\2\2\u00ee")
        buf.write("\u00ef\7\n\2\2\u00ef\u00f0\78\2\2\u00f0\u00f1\7\13\2\2")
        buf.write("\u00f1\u00f2\7\61\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f4")
        buf.write("\7\62\2\2\u00f4\u00f5\7\67\2\2\u00f5\37\3\2\2\2\u00f6")
        buf.write("\u00f7\5\"\22\2\u00f7\u00f8\5 \21\2\u00f8\u00fb\3\2\2")
        buf.write("\2\u00f9\u00fb\5\"\22\2\u00fa\u00f6\3\2\2\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb!\3\2\2\2\u00fc\u00fd\78\2\2\u00fd\u00fe")
        buf.write("\5\n\6\2\u00fe\u00ff\7\67\2\2\u00ff#\3\2\2\2\u0100\u0101")
        buf.write("\7\n\2\2\u0101\u0102\78\2\2\u0102\u0103\7\f\2\2\u0103")
        buf.write("\u0104\7\61\2\2\u0104\u0105\5&\24\2\u0105\u0106\7\62\2")
        buf.write("\2\u0106\u0107\7\67\2\2\u0107%\3\2\2\2\u0108\u0109\5(")
        buf.write("\25\2\u0109\u010a\5&\24\2\u010a\u010d\3\2\2\2\u010b\u010d")
        buf.write("\5(\25\2\u010c\u0108\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\'\3\2\2\2\u010e\u010f\78\2\2\u010f\u0110\7/\2\2\u0110")
        buf.write("\u0111\5*\26\2\u0111\u0114\7\60\2\2\u0112\u0115\5\n\6")
        buf.write("\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\7\67\2\2\u0117")
        buf.write(")\3\2\2\2\u0118\u011b\5,\27\2\u0119\u011b\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b+\3\2\2\2\u011c")
        buf.write("\u011d\5.\30\2\u011d\u011e\7\66\2\2\u011e\u011f\5,\27")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u0122\5.\30\2\u0121\u011c")
        buf.write("\3\2\2\2\u0121\u0120\3\2\2\2\u0122-\3\2\2\2\u0123\u0124")
        buf.write("\5\60\31\2\u0124\u0125\5\n\6\2\u0125/\3\2\2\2\u0126\u0127")
        buf.write("\78\2\2\u0127\u0128\7\66\2\2\u0128\u012b\5\60\31\2\u0129")
        buf.write("\u012b\78\2\2\u012a\u0126\3\2\2\2\u012a\u0129\3\2\2\2")
        buf.write("\u012b\61\3\2\2\2\u012c\u012f\5\64\33\2\u012d\u012f\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012f\63")
        buf.write("\3\2\2\2\u0130\u0131\5\66\34\2\u0131\u0132\5\64\33\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0135\5\66\34\2\u0134\u0130\3\2\2")
        buf.write("\2\u0134\u0133\3\2\2\2\u0135\65\3\2\2\2\u0136\u0140\5")
        buf.write("\16\b\2\u0137\u0140\5\f\7\2\u0138\u0140\58\35\2\u0139")
        buf.write("\u0140\5<\37\2\u013a\u0140\5H%\2\u013b\u0140\5T+\2\u013c")
        buf.write("\u0140\5V,\2\u013d\u0140\5X-\2\u013e\u0140\5Z.\2\u013f")
        buf.write("\u0136\3\2\2\2\u013f\u0137\3\2\2\2\u013f\u0138\3\2\2\2")
        buf.write("\u013f\u0139\3\2\2\2\u013f\u013a\3\2\2\2\u013f\u013b\3")
        buf.write("\2\2\2\u013f\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140\67\3\2\2\2\u0141\u0142\5:\36\2\u0142\u0143")
        buf.write("\t\2\2\2\u0143\u0144\5\u0082B\2\u0144\u0145\7\67\2\2\u0145")
        buf.write("9\3\2\2\2\u0146\u0147\b\36\1\2\u0147\u0148\78\2\2\u0148")
        buf.write("\u0154\3\2\2\2\u0149\u0150\f\4\2\2\u014a\u014b\7\63\2")
        buf.write("\2\u014b\u014c\5\u0082B\2\u014c\u014d\7\64\2\2\u014d\u0151")
        buf.write("\3\2\2\2\u014e\u014f\7.\2\2\u014f\u0151\78\2\2\u0150\u014a")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0153\3\2\2\2\u0152")
        buf.write("\u0149\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155;\3\2\2\2\u0156\u0154\3\2\2")
        buf.write("\2\u0157\u0158\7\5\2\2\u0158\u0159\7/\2\2\u0159\u015a")
        buf.write("\5\u0082B\2\u015a\u015b\7\60\2\2\u015b\u015c\7\61\2\2")
        buf.write("\u015c\u015d\5\62\32\2\u015d\u015e\7\62\2\2\u015e\u015f")
        buf.write("\5> \2\u015f\u0160\5D#\2\u0160\u0161\7\67\2\2\u0161=\3")
        buf.write("\2\2\2\u0162\u0165\5@!\2\u0163\u0165\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165?\3\2\2\2\u0166\u0167")
        buf.write("\5B\"\2\u0167\u0168\5@!\2\u0168\u016b\3\2\2\2\u0169\u016b")
        buf.write("\5B\"\2\u016a\u0166\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("A\3\2\2\2\u016c\u016d\7\6\2\2\u016d\u016e\7\5\2\2\u016e")
        buf.write("\u016f\7/\2\2\u016f\u0170\5\u0082B\2\u0170\u0171\7\60")
        buf.write("\2\2\u0171\u0172\7\61\2\2\u0172\u0173\5\62\32\2\u0173")
        buf.write("\u0174\7\62\2\2\u0174C\3\2\2\2\u0175\u0178\5F$\2\u0176")
        buf.write("\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3\2\2\2")
        buf.write("\u0178E\3\2\2\2\u0179\u017a\7\6\2\2\u017a\u017b\7\61\2")
        buf.write("\2\u017b\u017c\5\62\32\2\u017c\u017d\7\62\2\2\u017dG\3")
        buf.write("\2\2\2\u017e\u0182\5J&\2\u017f\u0182\5L\'\2\u0180\u0182")
        buf.write("\5N(\2\u0181\u017e\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\7\61\2\2\u0184")
        buf.write("\u0185\5\62\32\2\u0185\u0186\7\62\2\2\u0186\u0187\7\67")
        buf.write("\2\2\u0187I\3\2\2\2\u0188\u0189\7\7\2\2\u0189\u018a\5")
        buf.write("\u0082B\2\u018aK\3\2\2\2\u018b\u018e\7\7\2\2\u018c\u018f")
        buf.write("\5P)\2\u018d\u018f\5R*\2\u018e\u018c\3\2\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\7\67\2\2\u0191")
        buf.write("\u0192\5\u0082B\2\u0192\u0193\7\67\2\2\u0193\u0194\5P")
        buf.write(")\2\u0194M\3\2\2\2\u0195\u0196\7\7\2\2\u0196\u0197\78")
        buf.write("\2\2\u0197\u0198\7\66\2\2\u0198\u0199\78\2\2\u0199\u019a")
        buf.write("\7(\2\2\u019a\u019b\7\25\2\2\u019b\u019c\5\u0082B\2\u019c")
        buf.write("O\3\2\2\2\u019d\u019e\78\2\2\u019e\u019f\t\2\2\2\u019f")
        buf.write("\u01a0\5\u0082B\2\u01a0Q\3\2\2\2\u01a1\u01a2\7\22\2\2")
        buf.write("\u01a2\u01a5\78\2\2\u01a3\u01a6\5\n\6\2\u01a4\u01a6\3")
        buf.write("\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a8\7\'\2\2\u01a8\u01a9\5\u0082B\2\u01a9")
        buf.write("S\3\2\2\2\u01aa\u01ab\7\24\2\2\u01ab\u01ac\7\67\2\2\u01ac")
        buf.write("U\3\2\2\2\u01ad\u01ae\7\23\2\2\u01ae\u01af\7\67\2\2\u01af")
        buf.write("W\3\2\2\2\u01b0\u01b1\5:\36\2\u01b1\u01b2\7.\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b0\3\2\2\2")
        buf.write("\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\7")
        buf.write("8\2\2\u01b7\u01b8\7/\2\2\u01b8\u01b9\5~@\2\u01b9\u01ba")
        buf.write("\7\60\2\2\u01ba\u01bb\7\67\2\2\u01bbY\3\2\2\2\u01bc\u01bf")
        buf.write("\7\b\2\2\u01bd\u01c0\5\u0082B\2\u01be\u01c0\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c2\7\67\2\2\u01c2[\3\2\2\2\u01c3\u01cb\79\2")
        buf.write("\2\u01c4\u01cb\7:\2\2\u01c5\u01cb\7;\2\2\u01c6\u01cb\7")
        buf.write("\3\2\2\u01c7\u01cb\7\4\2\2\u01c8\u01cb\5t;\2\u01c9\u01cb")
        buf.write("\5h\65\2\u01ca\u01c3\3\2\2\2\u01ca\u01c4\3\2\2\2\u01ca")
        buf.write("\u01c5\3\2\2\2\u01ca\u01c6\3\2\2\2\u01ca\u01c7\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb]\3\2\2")
        buf.write("\2\u01cc\u01cf\5`\61\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf_\3\2\2\2\u01d0\u01d1")
        buf.write("\5\\/\2\u01d1\u01d2\7\66\2\2\u01d2\u01d3\5`\61\2\u01d3")
        buf.write("\u01d6\3\2\2\2\u01d4\u01d6\5\\/\2\u01d5\u01d0\3\2\2\2")
        buf.write("\u01d5\u01d4\3\2\2\2\u01d6a\3\2\2\2\u01d7\u01df\78\2\2")
        buf.write("\u01d8\u01df\79\2\2\u01d9\u01df\7:\2\2\u01da\u01df\7;")
        buf.write("\2\2\u01db\u01df\7\3\2\2\u01dc\u01df\7\4\2\2\u01dd\u01df")
        buf.write("\5t;\2\u01de\u01d7\3\2\2\2\u01de\u01d8\3\2\2\2\u01de\u01d9")
        buf.write("\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfc\3\2\2\2\u01e0")
        buf.write("\u01e3\5f\64\2\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e1\3\2\2\2\u01e3e\3\2\2\2\u01e4\u01e5\5b\62")
        buf.write("\2\u01e5\u01e6\7\66\2\2\u01e6\u01e7\5f\64\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01ea\5b\62\2\u01e9\u01e4\3\2\2\2\u01e9")
        buf.write("\u01e8\3\2\2\2\u01eag\3\2\2\2\u01eb\u01ec\5\b\5\2\u01ec")
        buf.write("\u01ed\7\61\2\2\u01ed\u01ee\5j\66\2\u01ee\u01ef\7\62\2")
        buf.write("\2\u01efi\3\2\2\2\u01f0\u01f1\5l\67\2\u01f1\u01f2\7\66")
        buf.write("\2\2\u01f2\u01f3\5j\66\2\u01f3\u01f6\3\2\2\2\u01f4\u01f6")
        buf.write("\5l\67\2\u01f5\u01f0\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("k\3\2\2\2\u01f7\u01fd\5f\64\2\u01f8\u01f9\7\61\2\2\u01f9")
        buf.write("\u01fa\5l\67\2\u01fa\u01fb\7\62\2\2\u01fb\u01fd\3\2\2")
        buf.write("\2\u01fc\u01f7\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fdm\3\2")
        buf.write("\2\2\u01fe\u01ff\5p9\2\u01ff\u0200\5n8\2\u0200\u0203\3")
        buf.write("\2\2\2\u0201\u0203\5p9\2\u0202\u01fe\3\2\2\2\u0202\u0201")
        buf.write("\3\2\2\2\u0203o\3\2\2\2\u0204\u0205\7\63\2\2\u0205\u0206")
        buf.write("\t\3\2\2\u0206\u0207\7\64\2\2\u0207q\3\2\2\2\u0208\u0209")
        buf.write("\t\4\2\2\u0209s\3\2\2\2\u020a\u020b\78\2\2\u020b\u020c")
        buf.write("\7\61\2\2\u020c\u020d\5v<\2\u020d\u020e\7\62\2\2\u020e")
        buf.write("u\3\2\2\2\u020f\u0212\5x=\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0210\3\2\2\2\u0212w\3\2\2\2\u0213")
        buf.write("\u0214\5z>\2\u0214\u0215\7\66\2\2\u0215\u0216\5x=\2\u0216")
        buf.write("\u0219\3\2\2\2\u0217\u0219\5z>\2\u0218\u0213\3\2\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0219y\3\2\2\2\u021a\u021b\78\2\2\u021b")
        buf.write("\u021c\7\65\2\2\u021c\u021f\5\u0082B\2\u021d\u021f\5\26")
        buf.write("\f\2\u021e\u021a\3\2\2\2\u021e\u021d\3\2\2\2\u021f{\3")
        buf.write("\2\2\2\u0220\u0221\78\2\2\u0221\u0222\7/\2\2\u0222\u0223")
        buf.write("\5~@\2\u0223\u0224\7\60\2\2\u0224}\3\2\2\2\u0225\u0228")
        buf.write("\5\u0080A\2\u0226\u0228\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0226\3\2\2\2\u0228\177\3\2\2\2\u0229\u022a\5\u0082B")
        buf.write("\2\u022a\u022b\7\66\2\2\u022b\u022c\5\u0080A\2\u022c\u022f")
        buf.write("\3\2\2\2\u022d\u022f\5\u0082B\2\u022e\u0229\3\2\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0081\3\2\2\2\u0230\u0231\bB\1\2")
        buf.write("\u0231\u0232\5\u0084C\2\u0232\u0238\3\2\2\2\u0233\u0234")
        buf.write("\f\4\2\2\u0234\u0235\7%\2\2\u0235\u0237\5\u0084C\2\u0236")
        buf.write("\u0233\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2")
        buf.write("\u0238\u0239\3\2\2\2\u0239\u0083\3\2\2\2\u023a\u0238\3")
        buf.write("\2\2\2\u023b\u023c\bC\1\2\u023c\u023d\5\u0086D\2\u023d")
        buf.write("\u0243\3\2\2\2\u023e\u023f\f\4\2\2\u023f\u0240\7$\2\2")
        buf.write("\u0240\u0242\5\u0086D\2\u0241\u023e\3\2\2\2\u0242\u0245")
        buf.write("\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u0085\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\bD\1\2")
        buf.write("\u0247\u0248\5\u0088E\2\u0248\u024e\3\2\2\2\u0249\u024a")
        buf.write("\f\4\2\2\u024a\u024b\t\5\2\2\u024b\u024d\5\u0088E\2\u024c")
        buf.write("\u0249\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024e\u024f\3\2\2\2\u024f\u0087\3\2\2\2\u0250\u024e\3")
        buf.write("\2\2\2\u0251\u0252\bE\1\2\u0252\u0253\5\u008aF\2\u0253")
        buf.write("\u0259\3\2\2\2\u0254\u0255\f\4\2\2\u0255\u0256\t\6\2\2")
        buf.write("\u0256\u0258\5\u008aF\2\u0257\u0254\3\2\2\2\u0258\u025b")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u0089\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\bF\1\2")
        buf.write("\u025d\u025e\5\u008cG\2\u025e\u0264\3\2\2\2\u025f\u0260")
        buf.write("\f\4\2\2\u0260\u0261\t\7\2\2\u0261\u0263\5\u008cG\2\u0262")
        buf.write("\u025f\3\2\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2")
        buf.write("\u0264\u0265\3\2\2\2\u0265\u008b\3\2\2\2\u0266\u0264\3")
        buf.write("\2\2\2\u0267\u0268\t\b\2\2\u0268\u026b\5\u008cG\2\u0269")
        buf.write("\u026b\5\u008eH\2\u026a\u0267\3\2\2\2\u026a\u0269\3\2")
        buf.write("\2\2\u026b\u008d\3\2\2\2\u026c\u026d\bH\1\2\u026d\u026e")
        buf.write("\5\u0090I\2\u026e\u027d\3\2\2\2\u026f\u0279\f\4\2\2\u0270")
        buf.write("\u0271\7\63\2\2\u0271\u0272\5\u0082B\2\u0272\u0273\7\64")
        buf.write("\2\2\u0273\u027a\3\2\2\2\u0274\u0277\7.\2\2\u0275\u0278")
        buf.write("\78\2\2\u0276\u0278\5|?\2\u0277\u0275\3\2\2\2\u0277\u0276")
        buf.write("\3\2\2\2\u0278\u027a\3\2\2\2\u0279\u0270\3\2\2\2\u0279")
        buf.write("\u0274\3\2\2\2\u027a\u027c\3\2\2\2\u027b\u026f\3\2\2\2")
        buf.write("\u027c\u027f\3\2\2\2\u027d\u027b\3\2\2\2\u027d\u027e\3")
        buf.write("\2\2\2\u027e\u008f\3\2\2\2\u027f\u027d\3\2\2\2\u0280\u0281")
        buf.write("\7/\2\2\u0281\u0282\5\u0082B\2\u0282\u0283\7\60\2\2\u0283")
        buf.write("\u0288\3\2\2\2\u0284\u0288\5\\/\2\u0285\u0288\78\2\2\u0286")
        buf.write("\u0288\5|?\2\u0287\u0280\3\2\2\2\u0287\u0284\3\2\2\2\u0287")
        buf.write("\u0285\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u0091\3\2\2\2")
        buf.write("\67\u0099\u00a0\u00ab\u00b2\u00b6\u00c9\u00d1\u00d9\u00e2")
        buf.write("\u00e9\u00fa\u010c\u0114\u011a\u0121\u012a\u012e\u0134")
        buf.write("\u013f\u0150\u0154\u0164\u016a\u0177\u0181\u018e\u01a5")
        buf.write("\u01b4\u01bf\u01ca\u01ce\u01d5\u01de\u01e2\u01e9\u01f5")
        buf.write("\u01fc\u0202\u0211\u0218\u021e\u0227\u022e\u0238\u0243")
        buf.write("\u024e\u0259\u0264\u026a\u0277\u0279\u027d\u0287")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'.'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "':'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "BOOL_LIT", "NIL_LIT", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "IS_EQUAL", "IS_DIFF", 
                      "LT", "LT_EQUAL", "GT", "GT_EQUAL", "AND", "OR", "NOT", 
                      "ASSIGN", "ASSIGN_COLON", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_CURLY", "RIGHT_CURLY", "LEFT_SQUARE", 
                      "RIGHT_SQUARE", "COLON", "COMMA", "SEMICOLON", "ID", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "NEWLINE", 
                      "COMMENT_BLOCK", "COMMENT_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declaration = 1
    RULE_declaration = 2
    RULE_array_type = 3
    RULE_all_types = 4
    RULE_var_declaration = 5
    RULE_const_declaration = 6
    RULE_method_declaration = 7
    RULE_list_method_element = 8
    RULE_method_element = 9
    RULE_func_declaration = 10
    RULE_list_func_arguments_prime = 11
    RULE_list_func_arguments = 12
    RULE_func_arguments = 13
    RULE_struct_declaration = 14
    RULE_list_struct_argument = 15
    RULE_struct_argument = 16
    RULE_interface_declaration = 17
    RULE_list_interface_method_declaration = 18
    RULE_interface_method_declaration = 19
    RULE_list_interface_method_element_prime = 20
    RULE_list_interface_method_element = 21
    RULE_interface_method_element = 22
    RULE_list_ID = 23
    RULE_list_statement_prime = 24
    RULE_list_statement = 25
    RULE_statement = 26
    RULE_assignment_statement = 27
    RULE_assignment_lhs = 28
    RULE_if_statement = 29
    RULE_list_elseif_prime = 30
    RULE_list_elseif = 31
    RULE_elseif = 32
    RULE_else_statement_prime = 33
    RULE_else_statement = 34
    RULE_for_statement = 35
    RULE_basic_for = 36
    RULE_init_for = 37
    RULE_range_for = 38
    RULE_assignment_stmt_for = 39
    RULE_var_declaration_for = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42
    RULE_call_statement = 43
    RULE_return_statement = 44
    RULE_literal = 45
    RULE_list_literal_prime = 46
    RULE_list_literal = 47
    RULE_literal_primitive = 48
    RULE_list_literal_primitive_prime = 49
    RULE_list_literal_primitive = 50
    RULE_array_literal = 51
    RULE_list_array_element = 52
    RULE_array_element = 53
    RULE_list_array_specific = 54
    RULE_array_specific = 55
    RULE_array_declare_type = 56
    RULE_struct_literal = 57
    RULE_list_struct_element_prime = 58
    RULE_list_struct_element = 59
    RULE_struct_element = 60
    RULE_function_call = 61
    RULE_list_expression_prime = 62
    RULE_list_expression = 63
    RULE_expression = 64
    RULE_expression1 = 65
    RULE_expression2 = 66
    RULE_expression3 = 67
    RULE_expression4 = 68
    RULE_expression5 = 69
    RULE_expression6 = 70
    RULE_expression7 = 71

    ruleNames =  [ "program", "list_declaration", "declaration", "array_type", 
                   "all_types", "var_declaration", "const_declaration", 
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
    BOOL_LIT=1
    NIL_LIT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    NIL=20
    TRUE=21
    FALSE=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    IS_EQUAL=28
    IS_DIFF=29
    LT=30
    LT_EQUAL=31
    GT=32
    GT_EQUAL=33
    AND=34
    OR=35
    NOT=36
    ASSIGN=37
    ASSIGN_COLON=38
    ADD_ASSIGN=39
    SUB_ASSIGN=40
    MUL_ASSIGN=41
    DIV_ASSIGN=42
    MOD_ASSIGN=43
    DOT=44
    LEFT_PAREN=45
    RIGHT_PAREN=46
    LEFT_CURLY=47
    RIGHT_CURLY=48
    LEFT_SQUARE=49
    RIGHT_SQUARE=50
    COLON=51
    COMMA=52
    SEMICOLON=53
    ID=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
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
            self.state = 144
            self.list_declaration()
            self.state = 145
            self.match(MiniGoParser.EOF)
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

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declaration" ):
                return visitor.visitList_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_declaration(self):

        localctx = MiniGoParser.List_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declaration)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.declaration()
                self.state = 148
                self.list_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.declaration()
                pass


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
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.var_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.const_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 157
                self.interface_declaration()
                pass


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
        self.enterRule(localctx, 6, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.list_array_specific()
            self.state = 161
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
        self.enterRule(localctx, 8, self.RULE_all_types)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.array_type()
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 10, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MiniGoParser.VAR)
            self.state = 172
            self.match(MiniGoParser.ID)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 173
                self.all_types()
                pass

            elif la_ == 2:
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                    self.state = 174
                    self.all_types()
                    pass
                elif token in [MiniGoParser.ASSIGN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 178
                self.match(MiniGoParser.ASSIGN)
                self.state = 179
                self.expression(0)
                pass


            self.state = 182
            self.match(MiniGoParser.SEMICOLON)
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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration" ):
                return visitor.visitConst_declaration(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration(self):

        localctx = MiniGoParser.Const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.CONST)
            self.state = 185
            self.match(MiniGoParser.ID)
            self.state = 186
            self.match(MiniGoParser.ASSIGN)
            self.state = 187
            self.expression(0)
            self.state = 188
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 191
            self.list_method_element()
            self.state = 192
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
        self.enterRule(localctx, 16, self.RULE_list_method_element)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.method_element()
                self.state = 195
                self.match(MiniGoParser.COMMA)
                self.state = 196
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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
        self.enterRule(localctx, 18, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.ID)
            self.state = 202
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

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 20, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.FUNC)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_PAREN]:
                self.state = 205
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            self.match(MiniGoParser.ID)
            self.state = 210
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 211
            self.list_func_arguments_prime()
            self.state = 212
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 213
                self.all_types()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 217
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 218
            self.list_statement_prime()
            self.state = 219
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 220
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 22, self.RULE_list_func_arguments_prime)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
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
        self.enterRule(localctx, 24, self.RULE_list_func_arguments)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.func_arguments()
                self.state = 227
                self.match(MiniGoParser.COMMA)
                self.state = 228
                self.list_func_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
        self.enterRule(localctx, 26, self.RULE_func_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.list_ID()
            self.state = 234
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MiniGoParser.TYPE)
            self.state = 237
            self.match(MiniGoParser.ID)
            self.state = 238
            self.match(MiniGoParser.STRUCT)
            self.state = 239
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 240
            self.list_struct_argument()
            self.state = 241
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 242
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 30, self.RULE_list_struct_argument)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.struct_argument()
                self.state = 245
                self.list_struct_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_argument" ):
                return visitor.visitStruct_argument(self)
            else:
                return visitor.visitChildren(self)




    def struct_argument(self):

        localctx = MiniGoParser.Struct_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.all_types()
            self.state = 252
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.TYPE)
            self.state = 255
            self.match(MiniGoParser.ID)
            self.state = 256
            self.match(MiniGoParser.INTERFACE)
            self.state = 257
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 258
            self.list_interface_method_declaration()
            self.state = 259
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 260
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 36, self.RULE_list_interface_method_declaration)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.interface_method_declaration()
                self.state = 263
                self.list_interface_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 38, self.RULE_interface_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.ID)
            self.state = 269
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 270
            self.list_interface_method_element_prime()
            self.state = 271
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 272
                self.all_types()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 276
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 40, self.RULE_list_interface_method_element_prime)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
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
        self.enterRule(localctx, 42, self.RULE_list_interface_method_element)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.interface_method_element()
                self.state = 283
                self.match(MiniGoParser.COMMA)
                self.state = 284
                self.list_interface_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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
        self.enterRule(localctx, 44, self.RULE_interface_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.list_ID()
            self.state = 290
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
        self.enterRule(localctx, 46, self.RULE_list_ID)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(MiniGoParser.ID)
                self.state = 293
                self.match(MiniGoParser.COMMA)
                self.state = 294
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
        self.enterRule(localctx, 48, self.RULE_list_statement_prime)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.list_statement()
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
        self.enterRule(localctx, 50, self.RULE_list_statement)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.statement()
                self.state = 303
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.var_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 312
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 313
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 314
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 315
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 316
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
        self.enterRule(localctx, 54, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.assignment_lhs(0)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 321
            self.expression(0)
            self.state = 322
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 334
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 328
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 329
                        self.expression(0)
                        self.state = 330
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 332
                        self.match(MiniGoParser.DOT)
                        self.state = 333
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 340
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

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def list_elseif_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_elseif_primeContext,0)


        def else_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statement_primeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MiniGoParser.IF)
            self.state = 342
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 343
            self.expression(0)
            self.state = 344
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 345
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 346
            self.list_statement_prime()
            self.state = 347
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 348
            self.list_elseif_prime()
            self.state = 349
            self.else_statement_prime()
            self.state = 350
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 60, self.RULE_list_elseif_prime)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
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
        self.enterRule(localctx, 62, self.RULE_list_elseif)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.elseif()
                self.state = 357
                self.list_elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


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
        self.enterRule(localctx, 64, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.ELSE)
            self.state = 363
            self.match(MiniGoParser.IF)
            self.state = 364
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 365
            self.expression(0)
            self.state = 366
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 367
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 368
            self.list_statement_prime()
            self.state = 369
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
        self.enterRule(localctx, 66, self.RULE_else_statement_prime)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
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

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


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
        self.enterRule(localctx, 68, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MiniGoParser.ELSE)
            self.state = 376
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 377
            self.list_statement_prime()
            self.state = 378
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

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 70, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 380
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 381
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 382
                self.range_for()
                pass


            self.state = 385
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 386
            self.list_statement_prime()
            self.state = 387
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 388
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 72, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.FOR)
            self.state = 391
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

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

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
        self.enterRule(localctx, 74, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.FOR)
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 394
                self.assignment_stmt_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 395
                self.var_declaration_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 398
            self.match(MiniGoParser.SEMICOLON)
            self.state = 399
            self.expression(0)
            self.state = 400
            self.match(MiniGoParser.SEMICOLON)
            self.state = 401
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
        self.enterRule(localctx, 76, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.FOR)
            self.state = 404
            self.match(MiniGoParser.ID)
            self.state = 405
            self.match(MiniGoParser.COMMA)
            self.state = 406
            self.match(MiniGoParser.ID)
            self.state = 407
            self.match(MiniGoParser.ASSIGN_COLON)
            self.state = 408
            self.match(MiniGoParser.RANGE)
            self.state = 409
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
        self.enterRule(localctx, 78, self.RULE_assignment_stmt_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(MiniGoParser.ID)
            self.state = 412
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 413
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
        self.enterRule(localctx, 80, self.RULE_var_declaration_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.VAR)
            self.state = 416
            self.match(MiniGoParser.ID)
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 417
                self.all_types()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 421
            self.match(MiniGoParser.ASSIGN)
            self.state = 422
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.BREAK)
            self.state = 425
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(MiniGoParser.CONTINUE)
            self.state = 428
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 86, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 430
                self.assignment_lhs(0)
                self.state = 431
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 436
            self.match(MiniGoParser.ID)
            self.state = 437
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 438
            self.list_expression_prime()
            self.state = 439
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 440
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 88, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.RETURN)
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 443
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 447
            self.match(MiniGoParser.SEMICOLON)
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

        def BOOL_LIT(self):
            return self.getToken(MiniGoParser.BOOL_LIT, 0)

        def NIL_LIT(self):
            return self.getToken(MiniGoParser.NIL_LIT, 0)

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
        self.enterRule(localctx, 90, self.RULE_literal)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
                self.match(MiniGoParser.BOOL_LIT)
                pass
            elif token in [MiniGoParser.NIL_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 453
                self.match(MiniGoParser.NIL_LIT)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 454
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 455
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
        self.enterRule(localctx, 92, self.RULE_list_literal_prime)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
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
        self.enterRule(localctx, 94, self.RULE_list_literal)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.literal()
                self.state = 463
                self.match(MiniGoParser.COMMA)
                self.state = 464
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(MiniGoParser.BOOL_LIT, 0)

        def NIL_LIT(self):
            return self.getToken(MiniGoParser.NIL_LIT, 0)

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
        self.enterRule(localctx, 96, self.RULE_literal_primitive)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 472
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 473
                self.match(MiniGoParser.BOOL_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 474
                self.match(MiniGoParser.NIL_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 475
                self.struct_literal()
                pass


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
        self.enterRule(localctx, 98, self.RULE_list_literal_primitive_prime)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
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
        self.enterRule(localctx, 100, self.RULE_list_literal_primitive)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.literal_primitive()
                self.state = 483
                self.match(MiniGoParser.COMMA)
                self.state = 484
                self.list_literal_primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
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
        self.enterRule(localctx, 102, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.array_type()
            self.state = 490
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 491
            self.list_array_element()
            self.state = 492
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
        self.enterRule(localctx, 104, self.RULE_list_array_element)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.array_element()
                self.state = 495
                self.match(MiniGoParser.COMMA)
                self.state = 496
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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
        self.enterRule(localctx, 106, self.RULE_array_element)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.list_literal_primitive()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.match(MiniGoParser.LEFT_CURLY)
                self.state = 503
                self.array_element()
                self.state = 504
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
        self.enterRule(localctx, 108, self.RULE_list_array_specific)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.array_specific()
                self.state = 509
                self.list_array_specific()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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

        def RIGHT_SQUARE(self):
            return self.getToken(MiniGoParser.RIGHT_SQUARE, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_specific

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_specific" ):
                return visitor.visitArray_specific(self)
            else:
                return visitor.visitChildren(self)




    def array_specific(self):

        localctx = MiniGoParser.Array_specificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array_specific)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LEFT_SQUARE)
            self.state = 515
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 516
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
        self.enterRule(localctx, 112, self.RULE_array_declare_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
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
        self.enterRule(localctx, 114, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.ID)
            self.state = 521
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 522
            self.list_struct_element_prime()
            self.state = 523
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
        self.enterRule(localctx, 116, self.RULE_list_struct_element_prime)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
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
        self.enterRule(localctx, 118, self.RULE_list_struct_element)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.struct_element()
                self.state = 530
                self.match(MiniGoParser.COMMA)
                self.state = 531
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
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
        self.enterRule(localctx, 120, self.RULE_struct_element)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.match(MiniGoParser.ID)
                self.state = 537
                self.match(MiniGoParser.COLON)
                self.state = 538
                self.expression(0)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
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
        self.enterRule(localctx, 122, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.ID)
            self.state = 543
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 544
            self.list_expression_prime()
            self.state = 545
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
        self.enterRule(localctx, 124, self.RULE_list_expression_prime)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
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
        self.enterRule(localctx, 126, self.RULE_list_expression)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.expression(0)
                self.state = 552
                self.match(MiniGoParser.COMMA)
                self.state = 553
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 561
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 562
                    self.match(MiniGoParser.OR)
                    self.state = 563
                    self.expression1(0) 
                self.state = 568
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
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 572
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 573
                    self.match(MiniGoParser.AND)
                    self.state = 574
                    self.expression2(0) 
                self.state = 579
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
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 588
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 583
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 584
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IS_EQUAL) | (1 << MiniGoParser.IS_DIFF) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LT_EQUAL) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GT_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 585
                    self.expression3(0) 
                self.state = 590
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
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 599
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 594
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 595
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 596
                    self.expression4(0) 
                self.state = 601
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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 610
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 605
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 606
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 607
                    self.expression5() 
                self.state = 612
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
        self.enterRule(localctx, 138, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 614
                self.expression5()
                pass
            elif token in [MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 635
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 621
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 631
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 622
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 623
                        self.expression(0)
                        self.state = 624
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 626
                        self.match(MiniGoParser.DOT)
                        self.state = 629
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                        if la_ == 1:
                            self.state = 627
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 628
                            self.function_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 637
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
        self.enterRule(localctx, 142, self.RULE_expression7)
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.match(MiniGoParser.LEFT_PAREN)
                self.state = 639
                self.expression(0)
                self.state = 640
                self.match(MiniGoParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 643
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 644
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
        self._predicates[28] = self.assignment_lhs_sempred
        self._predicates[64] = self.expression_sempred
        self._predicates[65] = self.expression1_sempred
        self._predicates[66] = self.expression2_sempred
        self._predicates[67] = self.expression3_sempred
        self._predicates[68] = self.expression4_sempred
        self._predicates[70] = self.expression6_sempred
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
         




