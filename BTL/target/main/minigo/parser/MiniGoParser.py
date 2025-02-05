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
        buf.write("\u0286\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\6\b\u00b6\n\b\r\b\16\b\u00b7")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00bf\n\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00d0")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00d8\n\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00e0\n\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\5\20\u00e9\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00f0\n\21\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00fb\n\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u0104\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u0110\n\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u0119\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u0121\n\30\3\30\3\30\3\31\3\31")
        buf.write("\5\31\u0127\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u012e\n")
        buf.write("\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0137\n\34")
        buf.write("\3\35\3\35\5\35\u013b\n\35\3\36\3\36\3\36\3\36\5\36\u0141")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u014c\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u0159\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0165\n#\7")
        buf.write("#\u0167\n#\f#\16#\u016a\13#\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u0177\n%\3%\3%\3%\3%\3&\3&\5&\u017f\n&\3\'")
        buf.write("\3\'\3\'\5\'\u0184\n\'\3\'\3\'\3\'\5\'\u0189\n\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3)\3)\5)\u0196\n)\3*\3*\3*\3*\3")
        buf.write("*\3+\3+\3+\5+\u01a0\n+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write("-\5-\u01ad\n-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u01c6")
        buf.write("\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\5\62")
        buf.write("\u01d1\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01dd\n\63\3\64\3\64\5\64\u01e1\n\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u01e8\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01f4\n\67\38\3")
        buf.write("8\38\38\38\58\u01fb\n8\39\39\39\39\59\u0201\n9\3:\3:\3")
        buf.write(":\3:\3;\3;\3<\3<\3<\3<\3<\3=\3=\5=\u0210\n=\3>\3>\3>\3")
        buf.write(">\3>\5>\u0217\n>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\5A\u0224")
        buf.write("\nA\3B\3B\3B\3B\3B\5B\u022b\nB\3C\3C\3C\3C\3C\3C\7C\u0233")
        buf.write("\nC\fC\16C\u0236\13C\3D\3D\3D\3D\3D\3D\7D\u023e\nD\fD")
        buf.write("\16D\u0241\13D\3E\3E\3E\3E\3E\3E\7E\u0249\nE\fE\16E\u024c")
        buf.write("\13E\3F\3F\3F\3F\3F\3F\7F\u0254\nF\fF\16F\u0257\13F\3")
        buf.write("G\3G\3G\3G\3G\3G\7G\u025f\nG\fG\16G\u0262\13G\3H\3H\3")
        buf.write("H\5H\u0267\nH\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0274")
        buf.write("\nI\5I\u0276\nI\7I\u0278\nI\fI\16I\u027b\13I\3J\3J\3J")
        buf.write("\3J\3J\3J\3J\5J\u0284\nJ\3J\2\tD\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u0090K\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("xz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\2\b\3\2&+\4\2\13\16\66\66\3\2\34!\3\2\27\30\3\2")
        buf.write("\31\33\4\2\30\30$$\2\u0288\2\u0094\3\2\2\2\4\u0097\3\2")
        buf.write("\2\2\6\u0099\3\2\2\2\b\u00a2\3\2\2\2\n\u00a4\3\2\2\2\f")
        buf.write("\u00af\3\2\2\2\16\u00b5\3\2\2\2\20\u00be\3\2\2\2\22\u00c0")
        buf.write("\3\2\2\2\24\u00c3\3\2\2\2\26\u00c6\3\2\2\2\30\u00cf\3")
        buf.write("\2\2\2\32\u00d1\3\2\2\2\34\u00d4\3\2\2\2\36\u00e8\3\2")
        buf.write("\2\2 \u00ef\3\2\2\2\"\u00f1\3\2\2\2$\u00f4\3\2\2\2&\u0103")
        buf.write("\3\2\2\2(\u0105\3\2\2\2*\u0109\3\2\2\2,\u0118\3\2\2\2")
        buf.write(".\u011a\3\2\2\2\60\u0126\3\2\2\2\62\u012d\3\2\2\2\64\u012f")
        buf.write("\3\2\2\2\66\u0136\3\2\2\28\u013a\3\2\2\2:\u0140\3\2\2")
        buf.write("\2<\u014b\3\2\2\2>\u014d\3\2\2\2@\u0150\3\2\2\2B\u0153")
        buf.write("\3\2\2\2D\u015a\3\2\2\2F\u016b\3\2\2\2H\u016d\3\2\2\2")
        buf.write("J\u017e\3\2\2\2L\u0188\3\2\2\2N\u018a\3\2\2\2P\u0195\3")
        buf.write("\2\2\2R\u0197\3\2\2\2T\u019f\3\2\2\2V\u01a6\3\2\2\2X\u01a9")
        buf.write("\3\2\2\2Z\u01b3\3\2\2\2\\\u01bb\3\2\2\2^\u01be\3\2\2\2")
        buf.write("`\u01c5\3\2\2\2b\u01cd\3\2\2\2d\u01dc\3\2\2\2f\u01e0\3")
        buf.write("\2\2\2h\u01e7\3\2\2\2j\u01e9\3\2\2\2l\u01f3\3\2\2\2n\u01fa")
        buf.write("\3\2\2\2p\u0200\3\2\2\2r\u0202\3\2\2\2t\u0206\3\2\2\2")
        buf.write("v\u0208\3\2\2\2x\u020f\3\2\2\2z\u0216\3\2\2\2|\u0218\3")
        buf.write("\2\2\2~\u021c\3\2\2\2\u0080\u0223\3\2\2\2\u0082\u022a")
        buf.write("\3\2\2\2\u0084\u022c\3\2\2\2\u0086\u0237\3\2\2\2\u0088")
        buf.write("\u0242\3\2\2\2\u008a\u024d\3\2\2\2\u008c\u0258\3\2\2\2")
        buf.write("\u008e\u0266\3\2\2\2\u0090\u0268\3\2\2\2\u0092\u0283\3")
        buf.write("\2\2\2\u0094\u0095\5\16\b\2\u0095\u0096\7\2\2\3\u0096")
        buf.write("\3\3\2\2\2\u0097\u0098\7\65\2\2\u0098\5\3\2\2\2\u0099")
        buf.write("\u009a\5p9\2\u009a\u009b\5t;\2\u009b\7\3\2\2\2\u009c\u00a3")
        buf.write("\5\6\4\2\u009d\u00a3\7\16\2\2\u009e\u00a3\7\f\2\2\u009f")
        buf.write("\u00a3\7\r\2\2\u00a0\u00a3\7\13\2\2\u00a1\u00a3\7\66\2")
        buf.write("\2\u00a2\u009c\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2\u009e")
        buf.write("\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\t\3\2\2\2\u00a4\u00a5\7\20\2\2\u00a5")
        buf.write("\u00ad\7\66\2\2\u00a6\u00ae\5\b\5\2\u00a7\u00aa\5\b\5")
        buf.write("\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7%\2\2\u00ac")
        buf.write("\u00ae\5\u0084C\2\u00ad\u00a6\3\2\2\2\u00ad\u00a9\3\2")
        buf.write("\2\2\u00ae\13\3\2\2\2\u00af\u00b0\7\17\2\2\u00b0\u00b1")
        buf.write("\7\66\2\2\u00b1\u00b2\7%\2\2\u00b2\u00b3\5\u0084C\2\u00b3")
        buf.write("\r\3\2\2\2\u00b4\u00b6\5\20\t\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\17\3\2\2\2\u00b9\u00bf\5\22\n\2\u00ba\u00bf\5\24")
        buf.write("\13\2\u00bb\u00bf\5\34\17\2\u00bc\u00bf\5$\23\2\u00bd")
        buf.write("\u00bf\5*\26\2\u00be\u00b9\3\2\2\2\u00be\u00ba\3\2\2\2")
        buf.write("\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3")
        buf.write("\2\2\2\u00bf\21\3\2\2\2\u00c0\u00c1\5\n\6\2\u00c1\u00c2")
        buf.write("\5\4\3\2\u00c2\23\3\2\2\2\u00c3\u00c4\5\f\7\2\u00c4\u00c5")
        buf.write("\5\4\3\2\u00c5\25\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7\u00c8")
        buf.write("\5\30\r\2\u00c8\u00c9\7.\2\2\u00c9\27\3\2\2\2\u00ca\u00cb")
        buf.write("\5\32\16\2\u00cb\u00cc\7\64\2\2\u00cc\u00cd\5\30\r\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00d0\5\32\16\2\u00cf\u00ca\3\2\2")
        buf.write("\2\u00cf\u00ce\3\2\2\2\u00d0\31\3\2\2\2\u00d1\u00d2\7")
        buf.write("\66\2\2\u00d2\u00d3\5\b\5\2\u00d3\33\3\2\2\2\u00d4\u00d7")
        buf.write("\7\7\2\2\u00d5\u00d8\5\26\f\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\7\66\2\2\u00da\u00db\7-\2\2\u00db\u00dc\5")
        buf.write("\36\20\2\u00dc\u00df\7.\2\2\u00dd\u00e0\5\b\5\2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7/\2\2\u00e2\u00e3\5")
        buf.write("8\35\2\u00e3\u00e4\7\60\2\2\u00e4\u00e5\5\4\3\2\u00e5")
        buf.write("\35\3\2\2\2\u00e6\u00e9\5 \21\2\u00e7\u00e9\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\37\3\2\2\2\u00ea")
        buf.write("\u00eb\5\"\22\2\u00eb\u00ec\7\64\2\2\u00ec\u00ed\5 \21")
        buf.write("\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5\"\22\2\u00ef\u00ea")
        buf.write("\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0!\3\2\2\2\u00f1\u00f2")
        buf.write("\7\66\2\2\u00f2\u00f3\5\b\5\2\u00f3#\3\2\2\2\u00f4\u00f5")
        buf.write("\7\b\2\2\u00f5\u00f6\7\66\2\2\u00f6\u00f7\7\t\2\2\u00f7")
        buf.write("\u00fa\7/\2\2\u00f8\u00fb\5&\24\2\u00f9\u00fb\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\u00fd\7\60\2\2\u00fd\u00fe\5\4\3\2\u00fe")
        buf.write("%\3\2\2\2\u00ff\u0100\5(\25\2\u0100\u0101\5&\24\2\u0101")
        buf.write("\u0104\3\2\2\2\u0102\u0104\5(\25\2\u0103\u00ff\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104\'\3\2\2\2\u0105\u0106\7\66")
        buf.write("\2\2\u0106\u0107\5\b\5\2\u0107\u0108\5\4\3\2\u0108)\3")
        buf.write("\2\2\2\u0109\u010a\7\b\2\2\u010a\u010b\7\66\2\2\u010b")
        buf.write("\u010c\7\n\2\2\u010c\u010f\7/\2\2\u010d\u0110\5,\27\2")
        buf.write("\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u010e\3")
        buf.write("\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\7\60\2\2\u0112")
        buf.write("\u0113\5\4\3\2\u0113+\3\2\2\2\u0114\u0115\5.\30\2\u0115")
        buf.write("\u0116\5,\27\2\u0116\u0119\3\2\2\2\u0117\u0119\5.\30\2")
        buf.write("\u0118\u0114\3\2\2\2\u0118\u0117\3\2\2\2\u0119-\3\2\2")
        buf.write("\2\u011a\u011b\7\66\2\2\u011b\u011c\7-\2\2\u011c\u011d")
        buf.write("\5\60\31\2\u011d\u0120\7.\2\2\u011e\u0121\5\b\5\2\u011f")
        buf.write("\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0123\5\4\3\2\u0123/\3\2\2")
        buf.write("\2\u0124\u0127\5\62\32\2\u0125\u0127\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127\61\3\2\2\2\u0128\u0129")
        buf.write("\5\64\33\2\u0129\u012a\7\64\2\2\u012a\u012b\5\62\32\2")
        buf.write("\u012b\u012e\3\2\2\2\u012c\u012e\5\64\33\2\u012d\u0128")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012e\63\3\2\2\2\u012f\u0130")
        buf.write("\5\66\34\2\u0130\u0131\5\b\5\2\u0131\65\3\2\2\2\u0132")
        buf.write("\u0133\7\66\2\2\u0133\u0134\7\64\2\2\u0134\u0137\5\66")
        buf.write("\34\2\u0135\u0137\7\66\2\2\u0136\u0132\3\2\2\2\u0136\u0135")
        buf.write("\3\2\2\2\u0137\67\3\2\2\2\u0138\u013b\5:\36\2\u0139\u013b")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("9\3\2\2\2\u013c\u013d\5<\37\2\u013d\u013e\5:\36\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u0141\5<\37\2\u0140\u013c\3\2\2\2")
        buf.write("\u0140\u013f\3\2\2\2\u0141;\3\2\2\2\u0142\u014c\5@!\2")
        buf.write("\u0143\u014c\5> \2\u0144\u014c\5B\"\2\u0145\u014c\5H%")
        buf.write("\2\u0146\u014c\5T+\2\u0147\u014c\5\\/\2\u0148\u014c\5")
        buf.write("^\60\2\u0149\u014c\5`\61\2\u014a\u014c\5b\62\2\u014b\u0142")
        buf.write("\3\2\2\2\u014b\u0143\3\2\2\2\u014b\u0144\3\2\2\2\u014b")
        buf.write("\u0145\3\2\2\2\u014b\u0146\3\2\2\2\u014b\u0147\3\2\2\2")
        buf.write("\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a\3")
        buf.write("\2\2\2\u014c=\3\2\2\2\u014d\u014e\5\n\6\2\u014e\u014f")
        buf.write("\5\4\3\2\u014f?\3\2\2\2\u0150\u0151\5\f\7\2\u0151\u0152")
        buf.write("\5\4\3\2\u0152A\3\2\2\2\u0153\u0154\5D#\2\u0154\u0155")
        buf.write("\t\2\2\2\u0155\u0158\5\u0084C\2\u0156\u0159\7\65\2\2\u0157")
        buf.write("\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2")
        buf.write("\u0159C\3\2\2\2\u015a\u015b\b#\1\2\u015b\u015c\5F$\2\u015c")
        buf.write("\u0168\3\2\2\2\u015d\u0164\f\4\2\2\u015e\u015f\7\61\2")
        buf.write("\2\u015f\u0160\5\u0084C\2\u0160\u0161\7\62\2\2\u0161\u0165")
        buf.write("\3\2\2\2\u0162\u0163\7,\2\2\u0163\u0165\7\66\2\2\u0164")
        buf.write("\u015e\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u015d\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u0169E\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016b\u016c\7\66\2\2\u016cG\3\2\2\2\u016d\u016e")
        buf.write("\7\3\2\2\u016e\u016f\7-\2\2\u016f\u0170\5\u0084C\2\u0170")
        buf.write("\u0171\7.\2\2\u0171\u0172\7/\2\2\u0172\u0173\58\35\2\u0173")
        buf.write("\u0176\7\60\2\2\u0174\u0177\5\4\3\2\u0175\u0177\3\2\2")
        buf.write("\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u0179\5J&\2\u0179\u017a\5P)\2\u017a\u017b")
        buf.write("\5\4\3\2\u017bI\3\2\2\2\u017c\u017f\5L\'\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("K\3\2\2\2\u0180\u0183\5N(\2\u0181\u0184\5\4\3\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\5L\'\2\u0186\u0189\3")
        buf.write("\2\2\2\u0187\u0189\5N(\2\u0188\u0180\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189M\3\2\2\2\u018a\u018b\7\4\2\2\u018b\u018c")
        buf.write("\7\3\2\2\u018c\u018d\7-\2\2\u018d\u018e\5\u0084C\2\u018e")
        buf.write("\u018f\7.\2\2\u018f\u0190\7/\2\2\u0190\u0191\58\35\2\u0191")
        buf.write("\u0192\7\60\2\2\u0192O\3\2\2\2\u0193\u0196\5R*\2\u0194")
        buf.write("\u0196\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196Q\3\2\2\2\u0197\u0198\7\4\2\2\u0198\u0199\7/\2\2")
        buf.write("\u0199\u019a\58\35\2\u019a\u019b\7\60\2\2\u019bS\3\2\2")
        buf.write("\2\u019c\u01a0\5V,\2\u019d\u01a0\5X-\2\u019e\u01a0\5Z")
        buf.write(".\2\u019f\u019c\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\7/\2\2\u01a2")
        buf.write("\u01a3\58\35\2\u01a3\u01a4\7\60\2\2\u01a4\u01a5\5\4\3")
        buf.write("\2\u01a5U\3\2\2\2\u01a6\u01a7\7\5\2\2\u01a7\u01a8\5\u0084")
        buf.write("C\2\u01a8W\3\2\2\2\u01a9\u01ac\7\5\2\2\u01aa\u01ad\5B")
        buf.write("\"\2\u01ab\u01ad\5\n\6\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\7\65\2\2\u01af")
        buf.write("\u01b0\5\u0084C\2\u01b0\u01b1\7\65\2\2\u01b1\u01b2\5B")
        buf.write("\"\2\u01b2Y\3\2\2\2\u01b3\u01b4\7\5\2\2\u01b4\u01b5\7")
        buf.write("\66\2\2\u01b5\u01b6\7\64\2\2\u01b6\u01b7\7\66\2\2\u01b7")
        buf.write("\u01b8\7&\2\2\u01b8\u01b9\7\23\2\2\u01b9\u01ba\5\u0084")
        buf.write("C\2\u01ba[\3\2\2\2\u01bb\u01bc\7\22\2\2\u01bc\u01bd\5")
        buf.write("\4\3\2\u01bd]\3\2\2\2\u01be\u01bf\7\21\2\2\u01bf\u01c0")
        buf.write("\5\4\3\2\u01c0_\3\2\2\2\u01c1\u01c2\5D#\2\u01c2\u01c3")
        buf.write("\7,\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5")
        buf.write("\u01c1\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c8\7\66\2\2\u01c8\u01c9\7-\2\2\u01c9\u01ca\5")
        buf.write("\u0080A\2\u01ca\u01cb\7.\2\2\u01cb\u01cc\5\4\3\2\u01cc")
        buf.write("a\3\2\2\2\u01cd\u01d0\7\6\2\2\u01ce\u01d1\5\u0084C\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d3\5\4\3\2\u01d3c\3\2\2")
        buf.write("\2\u01d4\u01dd\7\67\2\2\u01d5\u01dd\78\2\2\u01d6\u01dd")
        buf.write("\79\2\2\u01d7\u01dd\7\25\2\2\u01d8\u01dd\7\26\2\2\u01d9")
        buf.write("\u01dd\7\24\2\2\u01da\u01dd\5v<\2\u01db\u01dd\5j\66\2")
        buf.write("\u01dc\u01d4\3\2\2\2\u01dc\u01d5\3\2\2\2\u01dc\u01d6\3")
        buf.write("\2\2\2\u01dc\u01d7\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9")
        buf.write("\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("e\3\2\2\2\u01de\u01e1\5h\65\2\u01df\u01e1\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e0\u01df\3\2\2\2\u01e1g\3\2\2\2\u01e2")
        buf.write("\u01e3\5d\63\2\u01e3\u01e4\7\64\2\2\u01e4\u01e5\5h\65")
        buf.write("\2\u01e5\u01e8\3\2\2\2\u01e6\u01e8\5d\63\2\u01e7\u01e2")
        buf.write("\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8i\3\2\2\2\u01e9\u01ea")
        buf.write("\5\6\4\2\u01ea\u01eb\7/\2\2\u01eb\u01ec\5l\67\2\u01ec")
        buf.write("\u01ed\7\60\2\2\u01edk\3\2\2\2\u01ee\u01ef\5n8\2\u01ef")
        buf.write("\u01f0\7\64\2\2\u01f0\u01f1\5l\67\2\u01f1\u01f4\3\2\2")
        buf.write("\2\u01f2\u01f4\5n8\2\u01f3\u01ee\3\2\2\2\u01f3\u01f2\3")
        buf.write("\2\2\2\u01f4m\3\2\2\2\u01f5\u01fb\5d\63\2\u01f6\u01f7")
        buf.write("\7/\2\2\u01f7\u01f8\5f\64\2\u01f8\u01f9\7\60\2\2\u01f9")
        buf.write("\u01fb\3\2\2\2\u01fa\u01f5\3\2\2\2\u01fa\u01f6\3\2\2\2")
        buf.write("\u01fbo\3\2\2\2\u01fc\u01fd\5r:\2\u01fd\u01fe\5p9\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u0201\5r:\2\u0200\u01fc\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201q\3\2\2\2\u0202\u0203\7\61\2\2\u0203")
        buf.write("\u0204\7\67\2\2\u0204\u0205\7\62\2\2\u0205s\3\2\2\2\u0206")
        buf.write("\u0207\t\3\2\2\u0207u\3\2\2\2\u0208\u0209\7\66\2\2\u0209")
        buf.write("\u020a\7/\2\2\u020a\u020b\5x=\2\u020b\u020c\7\60\2\2\u020c")
        buf.write("w\3\2\2\2\u020d\u0210\5z>\2\u020e\u0210\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210y\3\2\2\2\u0211")
        buf.write("\u0212\5|?\2\u0212\u0213\7\64\2\2\u0213\u0214\5z>\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0217\5|?\2\u0216\u0211\3\2\2\2\u0216")
        buf.write("\u0215\3\2\2\2\u0217{\3\2\2\2\u0218\u0219\7\66\2\2\u0219")
        buf.write("\u021a\7\63\2\2\u021a\u021b\5\u0084C\2\u021b}\3\2\2\2")
        buf.write("\u021c\u021d\7\66\2\2\u021d\u021e\7-\2\2\u021e\u021f\5")
        buf.write("\u0080A\2\u021f\u0220\7.\2\2\u0220\177\3\2\2\2\u0221\u0224")
        buf.write("\5\u0082B\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0081\3\2\2\2\u0225\u0226\5\u0084")
        buf.write("C\2\u0226\u0227\7\64\2\2\u0227\u0228\5\u0082B\2\u0228")
        buf.write("\u022b\3\2\2\2\u0229\u022b\5\u0084C\2\u022a\u0225\3\2")
        buf.write("\2\2\u022a\u0229\3\2\2\2\u022b\u0083\3\2\2\2\u022c\u022d")
        buf.write("\bC\1\2\u022d\u022e\5\u0086D\2\u022e\u0234\3\2\2\2\u022f")
        buf.write("\u0230\f\4\2\2\u0230\u0231\7#\2\2\u0231\u0233\5\u0086")
        buf.write("D\2\u0232\u022f\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232")
        buf.write("\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0085\3\2\2\2\u0236")
        buf.write("\u0234\3\2\2\2\u0237\u0238\bD\1\2\u0238\u0239\5\u0088")
        buf.write("E\2\u0239\u023f\3\2\2\2\u023a\u023b\f\4\2\2\u023b\u023c")
        buf.write("\7\"\2\2\u023c\u023e\5\u0088E\2\u023d\u023a\3\2\2\2\u023e")
        buf.write("\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240\u0087\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243\b")
        buf.write("E\1\2\u0243\u0244\5\u008aF\2\u0244\u024a\3\2\2\2\u0245")
        buf.write("\u0246\f\4\2\2\u0246\u0247\t\4\2\2\u0247\u0249\5\u008a")
        buf.write("F\2\u0248\u0245\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248")
        buf.write("\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u0089\3\2\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024d\u024e\bF\1\2\u024e\u024f\5\u008c")
        buf.write("G\2\u024f\u0255\3\2\2\2\u0250\u0251\f\4\2\2\u0251\u0252")
        buf.write("\t\5\2\2\u0252\u0254\5\u008cG\2\u0253\u0250\3\2\2\2\u0254")
        buf.write("\u0257\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0256\u008b\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\b")
        buf.write("G\1\2\u0259\u025a\5\u008eH\2\u025a\u0260\3\2\2\2\u025b")
        buf.write("\u025c\f\4\2\2\u025c\u025d\t\6\2\2\u025d\u025f\5\u008e")
        buf.write("H\2\u025e\u025b\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e")
        buf.write("\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u008d\3\2\2\2\u0262")
        buf.write("\u0260\3\2\2\2\u0263\u0264\t\7\2\2\u0264\u0267\5\u008e")
        buf.write("H\2\u0265\u0267\5\u0090I\2\u0266\u0263\3\2\2\2\u0266\u0265")
        buf.write("\3\2\2\2\u0267\u008f\3\2\2\2\u0268\u0269\bI\1\2\u0269")
        buf.write("\u026a\5\u0092J\2\u026a\u0279\3\2\2\2\u026b\u0275\f\4")
        buf.write("\2\2\u026c\u026d\7\61\2\2\u026d\u026e\5\u0084C\2\u026e")
        buf.write("\u026f\7\62\2\2\u026f\u0276\3\2\2\2\u0270\u0273\7,\2\2")
        buf.write("\u0271\u0274\7\66\2\2\u0272\u0274\5~@\2\u0273\u0271\3")
        buf.write("\2\2\2\u0273\u0272\3\2\2\2\u0274\u0276\3\2\2\2\u0275\u026c")
        buf.write("\3\2\2\2\u0275\u0270\3\2\2\2\u0276\u0278\3\2\2\2\u0277")
        buf.write("\u026b\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2")
        buf.write("\u0279\u027a\3\2\2\2\u027a\u0091\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027c\u027d\7-\2\2\u027d\u027e\5\u0084C\2\u027e")
        buf.write("\u027f\7.\2\2\u027f\u0284\3\2\2\2\u0280\u0284\5d\63\2")
        buf.write("\u0281\u0284\7\66\2\2\u0282\u0284\5~@\2\u0283\u027c\3")
        buf.write("\2\2\2\u0283\u0280\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0282")
        buf.write("\3\2\2\2\u0284\u0093\3\2\2\2\67\u00a2\u00a9\u00ad\u00b7")
        buf.write("\u00be\u00cf\u00d7\u00df\u00e8\u00ef\u00fa\u0103\u010f")
        buf.write("\u0118\u0120\u0126\u012d\u0136\u013a\u0140\u014b\u0158")
        buf.write("\u0164\u0168\u0176\u017e\u0183\u0188\u0195\u019f\u01ac")
        buf.write("\u01c5\u01d0\u01dc\u01e0\u01e7\u01f3\u01fa\u0200\u020f")
        buf.write("\u0216\u0223\u022a\u0234\u023f\u024a\u0255\u0260\u0266")
        buf.write("\u0273\u0275\u0279\u0283")
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
    RULE_var_declaration_global = 8
    RULE_const_declaration_global = 9
    RULE_method_declaration = 10
    RULE_list_method_element = 11
    RULE_method_element = 12
    RULE_func_declaration = 13
    RULE_list_func_arguments_prime = 14
    RULE_list_func_arguments = 15
    RULE_func_arguments = 16
    RULE_struct_declaration = 17
    RULE_list_struct_argument = 18
    RULE_struct_argument = 19
    RULE_interface_declaration = 20
    RULE_list_interface_method_declaration = 21
    RULE_interface_method_declaration = 22
    RULE_list_interface_method_element_prime = 23
    RULE_list_interface_method_element = 24
    RULE_interface_method_element = 25
    RULE_list_ID = 26
    RULE_list_statement_prime = 27
    RULE_list_statement = 28
    RULE_statement = 29
    RULE_var_declaration_stmt = 30
    RULE_const_declaration_stmt = 31
    RULE_assignment_statement = 32
    RULE_assignment_lhs = 33
    RULE_assignment_lhs_element = 34
    RULE_if_statement = 35
    RULE_list_elseif_prime = 36
    RULE_list_elseif = 37
    RULE_elseif = 38
    RULE_else_statement_prime = 39
    RULE_else_statement = 40
    RULE_for_statement = 41
    RULE_basic_for = 42
    RULE_init_for = 43
    RULE_range_for = 44
    RULE_break_statement = 45
    RULE_continue_statement = 46
    RULE_call_statement = 47
    RULE_return_statement = 48
    RULE_literal = 49
    RULE_list_literal_prime = 50
    RULE_list_literal = 51
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
                   "var_declaration_global", "const_declaration_global", 
                   "method_declaration", "list_method_element", "method_element", 
                   "func_declaration", "list_func_arguments_prime", "list_func_arguments", 
                   "func_arguments", "struct_declaration", "list_struct_argument", 
                   "struct_argument", "interface_declaration", "list_interface_method_declaration", 
                   "interface_method_declaration", "list_interface_method_element_prime", 
                   "list_interface_method_element", "interface_method_element", 
                   "list_ID", "list_statement_prime", "list_statement", 
                   "statement", "var_declaration_stmt", "const_declaration_stmt", 
                   "assignment_statement", "assignment_lhs", "assignment_lhs_element", 
                   "if_statement", "list_elseif_prime", "list_elseif", "elseif", 
                   "else_statement_prime", "else_statement", "for_statement", 
                   "basic_for", "init_for", "range_for", "break_statement", 
                   "continue_statement", "call_statement", "return_statement", 
                   "literal", "list_literal_prime", "list_literal", "array_literal", 
                   "list_array_element", "array_element", "list_array_specific", 
                   "array_specific", "array_declare_type", "struct_literal", 
                   "list_struct_element_prime", "list_struct_element", "struct_element", 
                   "function_call", "list_expression_prime", "list_expression", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7" ]

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
            self.state = 173
            self.match(MiniGoParser.CONST)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.ASSIGN)
            self.state = 176
            self.expression(0)
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
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.declaration()
                self.state = 181 
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

        def var_declaration_global(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaration_globalContext,0)


        def const_declaration_global(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaration_globalContext,0)


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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.var_declaration_global()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.const_declaration_global()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.interface_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaration_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration_global

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_global" ):
                return visitor.visitVar_declaration_global(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_global(self):

        localctx = MiniGoParser.Var_declaration_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_declaration_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.var_declaration()
            self.state = 191
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaration_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration_global

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration_global" ):
                return visitor.visitConst_declaration_global(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration_global(self):

        localctx = MiniGoParser.Const_declaration_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_const_declaration_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.const_declaration()
            self.state = 194
            self.terminate()
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
        self.enterRule(localctx, 20, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 197
            self.list_method_element()
            self.state = 198
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
        self.enterRule(localctx, 22, self.RULE_list_method_element)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.method_element()
                self.state = 201
                self.match(MiniGoParser.COMMA)
                self.state = 202
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_element" ):
                return visitor.visitMethod_element(self)
            else:
                return visitor.visitChildren(self)




    def method_element(self):

        localctx = MiniGoParser.Method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.ID)
            self.state = 208
            self.all_types()
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
        self.enterRule(localctx, 26, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MiniGoParser.FUNC)
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_PAREN]:
                self.state = 211
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 216
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 217
            self.list_func_arguments_prime()
            self.state = 218
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 219
                self.all_types()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 223
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 224
            self.list_statement_prime()
            self.state = 225
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 226
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
        self.enterRule(localctx, 28, self.RULE_list_func_arguments_prime)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
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
        self.enterRule(localctx, 30, self.RULE_list_func_arguments)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.func_arguments()
                self.state = 233
                self.match(MiniGoParser.COMMA)
                self.state = 234
                self.list_func_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self.enterRule(localctx, 32, self.RULE_func_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 240
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

        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def list_struct_argument(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_argumentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.TYPE)
            self.state = 243
            self.match(MiniGoParser.ID)
            self.state = 244
            self.match(MiniGoParser.STRUCT)
            self.state = 245
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 246
                self.list_struct_argument()
                pass
            elif token in [MiniGoParser.RIGHT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 250
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 251
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
        self.enterRule(localctx, 36, self.RULE_list_struct_argument)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.struct_argument()
                self.state = 254
                self.list_struct_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
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
        self.enterRule(localctx, 38, self.RULE_struct_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MiniGoParser.ID)
            self.state = 260
            self.all_types()
            self.state = 261
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

        def RIGHT_CURLY(self):
            return self.getToken(MiniGoParser.RIGHT_CURLY, 0)

        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def list_interface_method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_method_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.TYPE)
            self.state = 264
            self.match(MiniGoParser.ID)
            self.state = 265
            self.match(MiniGoParser.INTERFACE)
            self.state = 266
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 267
                self.list_interface_method_declaration()
                pass
            elif token in [MiniGoParser.RIGHT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 271
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 272
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
        self.enterRule(localctx, 42, self.RULE_list_interface_method_declaration)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.interface_method_declaration()
                self.state = 275
                self.list_interface_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
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
        self.enterRule(localctx, 44, self.RULE_interface_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.ID)
            self.state = 281
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 282
            self.list_interface_method_element_prime()
            self.state = 283
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 284
                self.all_types()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 288
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
        self.enterRule(localctx, 46, self.RULE_list_interface_method_element_prime)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
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
        self.enterRule(localctx, 48, self.RULE_list_interface_method_element)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.interface_method_element()
                self.state = 295
                self.match(MiniGoParser.COMMA)
                self.state = 296
                self.list_interface_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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
        self.enterRule(localctx, 50, self.RULE_interface_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.list_ID()
            self.state = 302
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
        self.enterRule(localctx, 52, self.RULE_list_ID)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(MiniGoParser.ID)
                self.state = 305
                self.match(MiniGoParser.COMMA)
                self.state = 306
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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
        self.enterRule(localctx, 54, self.RULE_list_statement_prime)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
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
        self.enterRule(localctx, 56, self.RULE_list_statement)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.statement()
                self.state = 315
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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

        def const_declaration_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaration_stmtContext,0)


        def var_declaration_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaration_stmtContext,0)


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
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.const_declaration_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.var_declaration_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 325
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 327
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 328
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_stmt" ):
                return visitor.visitVar_declaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_stmt(self):

        localctx = MiniGoParser.Var_declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.var_declaration()
            self.state = 332
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration_stmt" ):
                return visitor.visitConst_declaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration_stmt(self):

        localctx = MiniGoParser.Const_declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_const_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.const_declaration()
            self.state = 335
            self.terminate()
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.assignment_lhs(0)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 339
            self.expression(0)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 340
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                pass


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

        def assignment_lhs_element(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhs_elementContext,0)


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.assignment_lhs_element()
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 348
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 349
                        self.expression(0)
                        self.state = 350
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 352
                        self.match(MiniGoParser.DOT)
                        self.state = 353
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_lhs_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs_element" ):
                return visitor.visitAssignment_lhs_element(self)
            else:
                return visitor.visitChildren(self)




    def assignment_lhs_element(self):

        localctx = MiniGoParser.Assignment_lhs_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignment_lhs_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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


        def terminate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TerminateContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TerminateContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
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
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 370
                self.terminate()
                pass

            elif la_ == 2:
                pass


            self.state = 374
            self.list_elseif_prime()
            self.state = 375
            self.else_statement_prime()
            self.state = 376
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
        self.enterRule(localctx, 72, self.RULE_list_elseif_prime)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
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


        def terminate(self):
            return self.getTypedRuleContext(MiniGoParser.TerminateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elseif" ):
                return visitor.visitList_elseif(self)
            else:
                return visitor.visitChildren(self)




    def list_elseif(self):

        localctx = MiniGoParser.List_elseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_elseif)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.elseif()
                self.state = 385
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.SEMICOLON]:
                    self.state = 383
                    self.terminate()
                    pass
                elif token in [MiniGoParser.ELSE]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 387
                self.list_elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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
        self.enterRule(localctx, 76, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.ELSE)
            self.state = 393
            self.match(MiniGoParser.IF)
            self.state = 394
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 395
            self.expression(0)
            self.state = 396
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 397
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 398
            self.list_statement_prime()
            self.state = 399
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
        self.enterRule(localctx, 78, self.RULE_else_statement_prime)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
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
        self.enterRule(localctx, 80, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MiniGoParser.ELSE)
            self.state = 406
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 407
            self.list_statement_prime()
            self.state = 408
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
        self.enterRule(localctx, 82, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 410
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 411
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 412
                self.range_for()
                pass


            self.state = 415
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 416
            self.list_statement_prime()
            self.state = 417
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 418
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
        self.enterRule(localctx, 84, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.FOR)
            self.state = 421
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


        def assignment_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,i)


        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = MiniGoParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(MiniGoParser.FOR)
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 424
                self.assignment_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 425
                self.var_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 428
            self.match(MiniGoParser.SEMICOLON)
            self.state = 429
            self.expression(0)
            self.state = 430
            self.match(MiniGoParser.SEMICOLON)
            self.state = 431
            self.assignment_statement()
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
        self.enterRule(localctx, 88, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.FOR)
            self.state = 434
            self.match(MiniGoParser.ID)
            self.state = 435
            self.match(MiniGoParser.COMMA)
            self.state = 436
            self.match(MiniGoParser.ID)
            self.state = 437
            self.match(MiniGoParser.ASSIGN_COLON)
            self.state = 438
            self.match(MiniGoParser.RANGE)
            self.state = 439
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
        self.enterRule(localctx, 90, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MiniGoParser.BREAK)
            self.state = 442
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
        self.enterRule(localctx, 92, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.CONTINUE)
            self.state = 445
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
        self.enterRule(localctx, 94, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 447
                self.assignment_lhs(0)
                self.state = 448
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 453
            self.match(MiniGoParser.ID)
            self.state = 454
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 455
            self.list_expression_prime()
            self.state = 456
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 457
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
        self.enterRule(localctx, 96, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.RETURN)
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 460
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 464
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
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 468
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 469
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 470
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 472
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 473
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
        self.enterRule(localctx, 100, self.RULE_list_literal_prime)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.list_literal()
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
        self.enterRule(localctx, 102, self.RULE_list_literal)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.literal()
                self.state = 481
                self.match(MiniGoParser.COMMA)
                self.state = 482
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.literal()
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
            self.state = 487
            self.array_type()
            self.state = 488
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 489
            self.list_array_element()
            self.state = 490
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
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.array_element()
                self.state = 493
                self.match(MiniGoParser.COMMA)
                self.state = 494
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LEFT_CURLY(self):
            return self.getToken(MiniGoParser.LEFT_CURLY, 0)

        def list_literal_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_primeContext,0)


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
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.literal()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MiniGoParser.LEFT_CURLY)
                self.state = 501
                self.list_literal_prime()
                self.state = 502
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
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.array_specific()
                self.state = 507
                self.list_array_specific()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
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
            self.state = 512
            self.match(MiniGoParser.LEFT_SQUARE)
            self.state = 513
            self.match(MiniGoParser.INT_LIT)
            self.state = 514
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
            self.state = 516
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
            self.state = 518
            self.match(MiniGoParser.ID)
            self.state = 519
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 520
            self.list_struct_element_prime()
            self.state = 521
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
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
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
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.struct_element()
                self.state = 528
                self.match(MiniGoParser.COMMA)
                self.state = 529
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
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
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.ID)
            self.state = 535
            self.match(MiniGoParser.COLON)
            self.state = 536
            self.expression(0)
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
            self.state = 538
            self.match(MiniGoParser.ID)
            self.state = 539
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 540
            self.list_expression_prime()
            self.state = 541
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
            self.state = 545
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
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
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.expression(0)
                self.state = 548
                self.match(MiniGoParser.COMMA)
                self.state = 549
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
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
            self.state = 555
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 562
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 557
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 558
                    self.match(MiniGoParser.OR)
                    self.state = 559
                    self.expression1(0) 
                self.state = 564
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
            self.state = 566
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 573
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 568
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 569
                    self.match(MiniGoParser.AND)
                    self.state = 570
                    self.expression2(0) 
                self.state = 575
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
            self.state = 577
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 584
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 579
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 580
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IS_EQUAL) | (1 << MiniGoParser.IS_DIFF) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LT_EQUAL) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GT_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 581
                    self.expression3(0) 
                self.state = 586
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
            self.state = 588
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 590
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 591
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 592
                    self.expression4(0) 
                self.state = 597
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
            self.state = 599
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 606
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 601
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 602
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 603
                    self.expression5() 
                self.state = 608
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
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 610
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
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
            self.state = 615
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 631
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 617
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 627
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 618
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 619
                        self.expression(0)
                        self.state = 620
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 622
                        self.match(MiniGoParser.DOT)
                        self.state = 625
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                        if la_ == 1:
                            self.state = 623
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 624
                            self.function_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 633
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
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.match(MiniGoParser.LEFT_PAREN)
                self.state = 635
                self.expression(0)
                self.state = 636
                self.match(MiniGoParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 639
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 640
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
        self._predicates[33] = self.assignment_lhs_sempred
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
         




