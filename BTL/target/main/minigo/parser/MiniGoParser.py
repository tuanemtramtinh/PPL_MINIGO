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
        buf.write("\u029b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u00ab\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00b2")
        buf.write("\n\6\3\6\3\6\5\6\u00b6\n\6\3\7\3\7\3\7\3\7\3\7\3\b\6\b")
        buf.write("\u00be\n\b\r\b\16\b\u00bf\3\t\3\t\3\t\3\t\3\t\5\t\u00c7")
        buf.write("\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00d8\n\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\5\17\u00e0\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00e8\n\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u00f1\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00f8\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u0109\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u0110\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u011e\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0126\n\30\3\30\3\30\3\31")
        buf.write("\3\31\5\31\u012c\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0133")
        buf.write("\n\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u013c\n")
        buf.write("\34\3\35\3\35\5\35\u0140\n\35\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0146\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0151\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\5#\u0160\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5")
        buf.write("$\u016c\n$\7$\u016e\n$\f$\16$\u0171\13$\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\5\'\u0182\n\'\3(\3(")
        buf.write("\3(\3(\5(\u0188\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\5")
        buf.write("*\u0195\n*\3+\3+\3+\3+\3+\3,\3,\3,\5,\u019f\n,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\5.\u01ac\n.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u01c5\n\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\5\63\u01d0\n\63\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01dc\n\64")
        buf.write("\3\65\3\65\5\65\u01e0\n\65\3\66\3\66\3\66\3\66\3\66\5")
        buf.write("\66\u01e7\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01f0\n\67\38\38\58\u01f4\n8\39\39\39\39\39\59\u01fb")
        buf.write("\n9\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\5;\u0207\n;\3<\3<\3")
        buf.write("<\3<\3<\5<\u020e\n<\3=\3=\3=\3=\5=\u0214\n=\3>\3>\3>\3")
        buf.write(">\3?\3?\3@\3@\3@\3@\3@\3A\3A\5A\u0223\nA\3B\3B\3B\3B\3")
        buf.write("B\5B\u022a\nB\3C\3C\3C\3C\5C\u0230\nC\3D\3D\3D\3D\3D\3")
        buf.write("E\3E\5E\u0239\nE\3F\3F\3F\3F\3F\5F\u0240\nF\3G\3G\3G\3")
        buf.write("G\3G\3G\7G\u0248\nG\fG\16G\u024b\13G\3H\3H\3H\3H\3H\3")
        buf.write("H\7H\u0253\nH\fH\16H\u0256\13H\3I\3I\3I\3I\3I\3I\7I\u025e")
        buf.write("\nI\fI\16I\u0261\13I\3J\3J\3J\3J\3J\3J\7J\u0269\nJ\fJ")
        buf.write("\16J\u026c\13J\3K\3K\3K\3K\3K\3K\7K\u0274\nK\fK\16K\u0277")
        buf.write("\13K\3L\3L\3L\5L\u027c\nL\3M\3M\3M\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\5M\u0289\nM\5M\u028b\nM\7M\u028d\nM\fM\16M\u0290")
        buf.write("\13M\3N\3N\3N\3N\3N\3N\3N\5N\u0299\nN\3N\2\tF\u008c\u008e")
        buf.write("\u0090\u0092\u0094\u0098O\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\2\b\3\2&+\4")
        buf.write("\2\13\16\66\66\3\2\34!\3\2\27\30\3\2\31\33\4\2\30\30$")
        buf.write("$\2\u029f\2\u009c\3\2\2\2\4\u009f\3\2\2\2\6\u00a1\3\2")
        buf.write("\2\2\b\u00aa\3\2\2\2\n\u00ac\3\2\2\2\f\u00b7\3\2\2\2\16")
        buf.write("\u00bd\3\2\2\2\20\u00c6\3\2\2\2\22\u00c8\3\2\2\2\24\u00cb")
        buf.write("\3\2\2\2\26\u00ce\3\2\2\2\30\u00d7\3\2\2\2\32\u00d9\3")
        buf.write("\2\2\2\34\u00dc\3\2\2\2\36\u00f0\3\2\2\2 \u00f7\3\2\2")
        buf.write("\2\"\u00f9\3\2\2\2$\u00fc\3\2\2\2&\u0108\3\2\2\2(\u010f")
        buf.write("\3\2\2\2*\u0111\3\2\2\2,\u011d\3\2\2\2.\u011f\3\2\2\2")
        buf.write("\60\u012b\3\2\2\2\62\u0132\3\2\2\2\64\u0134\3\2\2\2\66")
        buf.write("\u013b\3\2\2\28\u013f\3\2\2\2:\u0145\3\2\2\2<\u0150\3")
        buf.write("\2\2\2>\u0152\3\2\2\2@\u0155\3\2\2\2B\u0158\3\2\2\2D\u015c")
        buf.write("\3\2\2\2F\u0161\3\2\2\2H\u0172\3\2\2\2J\u0174\3\2\2\2")
        buf.write("L\u0181\3\2\2\2N\u0187\3\2\2\2P\u0189\3\2\2\2R\u0194\3")
        buf.write("\2\2\2T\u0196\3\2\2\2V\u019e\3\2\2\2X\u01a5\3\2\2\2Z\u01a8")
        buf.write("\3\2\2\2\\\u01b2\3\2\2\2^\u01ba\3\2\2\2`\u01bd\3\2\2\2")
        buf.write("b\u01c4\3\2\2\2d\u01cc\3\2\2\2f\u01db\3\2\2\2h\u01df\3")
        buf.write("\2\2\2j\u01e6\3\2\2\2l\u01ef\3\2\2\2n\u01f3\3\2\2\2p\u01fa")
        buf.write("\3\2\2\2r\u01fc\3\2\2\2t\u0206\3\2\2\2v\u020d\3\2\2\2")
        buf.write("x\u0213\3\2\2\2z\u0215\3\2\2\2|\u0219\3\2\2\2~\u021b\3")
        buf.write("\2\2\2\u0080\u0222\3\2\2\2\u0082\u0229\3\2\2\2\u0084\u022f")
        buf.write("\3\2\2\2\u0086\u0231\3\2\2\2\u0088\u0238\3\2\2\2\u008a")
        buf.write("\u023f\3\2\2\2\u008c\u0241\3\2\2\2\u008e\u024c\3\2\2\2")
        buf.write("\u0090\u0257\3\2\2\2\u0092\u0262\3\2\2\2\u0094\u026d\3")
        buf.write("\2\2\2\u0096\u027b\3\2\2\2\u0098\u027d\3\2\2\2\u009a\u0298")
        buf.write("\3\2\2\2\u009c\u009d\5\16\b\2\u009d\u009e\7\2\2\3\u009e")
        buf.write("\3\3\2\2\2\u009f\u00a0\7\65\2\2\u00a0\5\3\2\2\2\u00a1")
        buf.write("\u00a2\5x=\2\u00a2\u00a3\5|?\2\u00a3\7\3\2\2\2\u00a4\u00ab")
        buf.write("\5\6\4\2\u00a5\u00ab\7\16\2\2\u00a6\u00ab\7\f\2\2\u00a7")
        buf.write("\u00ab\7\r\2\2\u00a8\u00ab\7\13\2\2\u00a9\u00ab\7\66\2")
        buf.write("\2\u00aa\u00a4\3\2\2\2\u00aa\u00a5\3\2\2\2\u00aa\u00a6")
        buf.write("\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\t\3\2\2\2\u00ac\u00ad\7\20\2\2\u00ad")
        buf.write("\u00b5\7\66\2\2\u00ae\u00b6\5\b\5\2\u00af\u00b2\5\b\5")
        buf.write("\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7%\2\2\u00b4")
        buf.write("\u00b6\5\u008cG\2\u00b5\u00ae\3\2\2\2\u00b5\u00b1\3\2")
        buf.write("\2\2\u00b6\13\3\2\2\2\u00b7\u00b8\7\17\2\2\u00b8\u00b9")
        buf.write("\7\66\2\2\u00b9\u00ba\7%\2\2\u00ba\u00bb\5\u008cG\2\u00bb")
        buf.write("\r\3\2\2\2\u00bc\u00be\5\20\t\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\17\3\2\2\2\u00c1\u00c7\5\22\n\2\u00c2\u00c7\5\24")
        buf.write("\13\2\u00c3\u00c7\5\34\17\2\u00c4\u00c7\5$\23\2\u00c5")
        buf.write("\u00c7\5*\26\2\u00c6\u00c1\3\2\2\2\u00c6\u00c2\3\2\2\2")
        buf.write("\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3")
        buf.write("\2\2\2\u00c7\21\3\2\2\2\u00c8\u00c9\5\n\6\2\u00c9\u00ca")
        buf.write("\5\4\3\2\u00ca\23\3\2\2\2\u00cb\u00cc\5\f\7\2\u00cc\u00cd")
        buf.write("\5\4\3\2\u00cd\25\3\2\2\2\u00ce\u00cf\7-\2\2\u00cf\u00d0")
        buf.write("\5\30\r\2\u00d0\u00d1\7.\2\2\u00d1\27\3\2\2\2\u00d2\u00d3")
        buf.write("\5\32\16\2\u00d3\u00d4\7\64\2\2\u00d4\u00d5\5\30\r\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d8\5\32\16\2\u00d7\u00d2\3\2\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\31\3\2\2\2\u00d9\u00da\7")
        buf.write("\66\2\2\u00da\u00db\7\66\2\2\u00db\33\3\2\2\2\u00dc\u00df")
        buf.write("\7\7\2\2\u00dd\u00e0\5\26\f\2\u00de\u00e0\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\7\66\2\2\u00e2\u00e3\7-\2\2\u00e3\u00e4\5")
        buf.write("\36\20\2\u00e4\u00e7\7.\2\2\u00e5\u00e8\5\b\5\2\u00e6")
        buf.write("\u00e8\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7/\2\2\u00ea\u00eb\5")
        buf.write(":\36\2\u00eb\u00ec\7\60\2\2\u00ec\u00ed\5\4\3\2\u00ed")
        buf.write("\35\3\2\2\2\u00ee\u00f1\5 \21\2\u00ef\u00f1\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\37\3\2\2\2\u00f2")
        buf.write("\u00f3\5\"\22\2\u00f3\u00f4\7\64\2\2\u00f4\u00f5\5 \21")
        buf.write("\2\u00f5\u00f8\3\2\2\2\u00f6\u00f8\5\"\22\2\u00f7\u00f2")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8!\3\2\2\2\u00f9\u00fa")
        buf.write("\5\66\34\2\u00fa\u00fb\5\b\5\2\u00fb#\3\2\2\2\u00fc\u00fd")
        buf.write("\7\b\2\2\u00fd\u00fe\7\66\2\2\u00fe\u00ff\7\t\2\2\u00ff")
        buf.write("\u0100\7/\2\2\u0100\u0101\5&\24\2\u0101\u0102\7\60\2\2")
        buf.write("\u0102\u0103\5\4\3\2\u0103%\3\2\2\2\u0104\u0105\5(\25")
        buf.write("\2\u0105\u0106\5&\24\2\u0106\u0109\3\2\2\2\u0107\u0109")
        buf.write("\5(\25\2\u0108\u0104\3\2\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\'\3\2\2\2\u010a\u010b\7\66\2\2\u010b\u010c\5\b\5\2\u010c")
        buf.write("\u010d\5\4\3\2\u010d\u0110\3\2\2\2\u010e\u0110\5\34\17")
        buf.write("\2\u010f\u010a\3\2\2\2\u010f\u010e\3\2\2\2\u0110)\3\2")
        buf.write("\2\2\u0111\u0112\7\b\2\2\u0112\u0113\7\66\2\2\u0113\u0114")
        buf.write("\7\n\2\2\u0114\u0115\7/\2\2\u0115\u0116\5,\27\2\u0116")
        buf.write("\u0117\7\60\2\2\u0117\u0118\5\4\3\2\u0118+\3\2\2\2\u0119")
        buf.write("\u011a\5.\30\2\u011a\u011b\5,\27\2\u011b\u011e\3\2\2\2")
        buf.write("\u011c\u011e\5.\30\2\u011d\u0119\3\2\2\2\u011d\u011c\3")
        buf.write("\2\2\2\u011e-\3\2\2\2\u011f\u0120\7\66\2\2\u0120\u0121")
        buf.write("\7-\2\2\u0121\u0122\5\60\31\2\u0122\u0125\7.\2\2\u0123")
        buf.write("\u0126\5\b\5\2\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\5")
        buf.write("\4\3\2\u0128/\3\2\2\2\u0129\u012c\5\62\32\2\u012a\u012c")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c")
        buf.write("\61\3\2\2\2\u012d\u012e\5\64\33\2\u012e\u012f\7\64\2\2")
        buf.write("\u012f\u0130\5\62\32\2\u0130\u0133\3\2\2\2\u0131\u0133")
        buf.write("\5\64\33\2\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("\63\3\2\2\2\u0134\u0135\5\66\34\2\u0135\u0136\5\b\5\2")
        buf.write("\u0136\65\3\2\2\2\u0137\u0138\7\66\2\2\u0138\u0139\7\64")
        buf.write("\2\2\u0139\u013c\5\66\34\2\u013a\u013c\7\66\2\2\u013b")
        buf.write("\u0137\3\2\2\2\u013b\u013a\3\2\2\2\u013c\67\3\2\2\2\u013d")
        buf.write("\u0140\5:\36\2\u013e\u0140\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u013e\3\2\2\2\u01409\3\2\2\2\u0141\u0142\5<\37")
        buf.write("\2\u0142\u0143\5:\36\2\u0143\u0146\3\2\2\2\u0144\u0146")
        buf.write("\5<\37\2\u0145\u0141\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write(";\3\2\2\2\u0147\u0151\5@!\2\u0148\u0151\5> \2\u0149\u0151")
        buf.write("\5D#\2\u014a\u0151\5J&\2\u014b\u0151\5V,\2\u014c\u0151")
        buf.write("\5^\60\2\u014d\u0151\5`\61\2\u014e\u0151\5b\62\2\u014f")
        buf.write("\u0151\5d\63\2\u0150\u0147\3\2\2\2\u0150\u0148\3\2\2\2")
        buf.write("\u0150\u0149\3\2\2\2\u0150\u014a\3\2\2\2\u0150\u014b\3")
        buf.write("\2\2\2\u0150\u014c\3\2\2\2\u0150\u014d\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151=\3\2\2\2\u0152\u0153")
        buf.write("\5\n\6\2\u0153\u0154\5\4\3\2\u0154?\3\2\2\2\u0155\u0156")
        buf.write("\5\f\7\2\u0156\u0157\5\4\3\2\u0157A\3\2\2\2\u0158\u0159")
        buf.write("\5F$\2\u0159\u015a\t\2\2\2\u015a\u015b\5\u008cG\2\u015b")
        buf.write("C\3\2\2\2\u015c\u015f\5B\"\2\u015d\u0160\7\65\2\2\u015e")
        buf.write("\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160E\3\2\2\2\u0161\u0162\b$\1\2\u0162\u0163\5H%\2\u0163")
        buf.write("\u016f\3\2\2\2\u0164\u016b\f\4\2\2\u0165\u0166\7\61\2")
        buf.write("\2\u0166\u0167\5\u008cG\2\u0167\u0168\7\62\2\2\u0168\u016c")
        buf.write("\3\2\2\2\u0169\u016a\7,\2\2\u016a\u016c\7\66\2\2\u016b")
        buf.write("\u0165\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016e\3\2\2\2")
        buf.write("\u016d\u0164\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170G\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0173\7\66\2\2\u0173I\3\2\2\2\u0174\u0175")
        buf.write("\7\3\2\2\u0175\u0176\7-\2\2\u0176\u0177\5\u008cG\2\u0177")
        buf.write("\u0178\7.\2\2\u0178\u0179\7/\2\2\u0179\u017a\5:\36\2\u017a")
        buf.write("\u017b\7\60\2\2\u017b\u017c\5L\'\2\u017c\u017d\5R*\2\u017d")
        buf.write("\u017e\5\4\3\2\u017eK\3\2\2\2\u017f\u0182\5N(\2\u0180")
        buf.write("\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182M\3\2\2\2\u0183\u0184\5P)\2\u0184\u0185\5N(\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0188\5P)\2\u0187\u0183\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188O\3\2\2\2\u0189\u018a\7\4\2\2\u018a")
        buf.write("\u018b\7\3\2\2\u018b\u018c\7-\2\2\u018c\u018d\5\u008c")
        buf.write("G\2\u018d\u018e\7.\2\2\u018e\u018f\7/\2\2\u018f\u0190")
        buf.write("\5:\36\2\u0190\u0191\7\60\2\2\u0191Q\3\2\2\2\u0192\u0195")
        buf.write("\5T+\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195S\3\2\2\2\u0196\u0197\7\4\2\2\u0197\u0198")
        buf.write("\7/\2\2\u0198\u0199\5:\36\2\u0199\u019a\7\60\2\2\u019a")
        buf.write("U\3\2\2\2\u019b\u019f\5X-\2\u019c\u019f\5Z.\2\u019d\u019f")
        buf.write("\5\\/\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7/\2\2")
        buf.write("\u01a1\u01a2\5:\36\2\u01a2\u01a3\7\60\2\2\u01a3\u01a4")
        buf.write("\5\4\3\2\u01a4W\3\2\2\2\u01a5\u01a6\7\5\2\2\u01a6\u01a7")
        buf.write("\5\u008cG\2\u01a7Y\3\2\2\2\u01a8\u01ab\7\5\2\2\u01a9\u01ac")
        buf.write("\5D#\2\u01aa\u01ac\5\n\6\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\7\65\2\2\u01ae")
        buf.write("\u01af\5\u008cG\2\u01af\u01b0\7\65\2\2\u01b0\u01b1\5B")
        buf.write("\"\2\u01b1[\3\2\2\2\u01b2\u01b3\7\5\2\2\u01b3\u01b4\7")
        buf.write("\66\2\2\u01b4\u01b5\7\64\2\2\u01b5\u01b6\7\66\2\2\u01b6")
        buf.write("\u01b7\7&\2\2\u01b7\u01b8\7\23\2\2\u01b8\u01b9\5\u008c")
        buf.write("G\2\u01b9]\3\2\2\2\u01ba\u01bb\7\22\2\2\u01bb\u01bc\5")
        buf.write("\4\3\2\u01bc_\3\2\2\2\u01bd\u01be\7\21\2\2\u01be\u01bf")
        buf.write("\5\4\3\2\u01bfa\3\2\2\2\u01c0\u01c1\5F$\2\u01c1\u01c2")
        buf.write("\7,\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c5\3\2\2\2\u01c4")
        buf.write("\u01c0\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c7\7\66\2\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\5")
        buf.write("\u0088E\2\u01c9\u01ca\7.\2\2\u01ca\u01cb\5\4\3\2\u01cb")
        buf.write("c\3\2\2\2\u01cc\u01cf\7\6\2\2\u01cd\u01d0\5\u008cG\2\u01ce")
        buf.write("\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d2\5\4\3\2\u01d2e\3\2\2")
        buf.write("\2\u01d3\u01dc\7\67\2\2\u01d4\u01dc\78\2\2\u01d5\u01dc")
        buf.write("\79\2\2\u01d6\u01dc\7\25\2\2\u01d7\u01dc\7\26\2\2\u01d8")
        buf.write("\u01dc\7\24\2\2\u01d9\u01dc\5~@\2\u01da\u01dc\5r:\2\u01db")
        buf.write("\u01d3\3\2\2\2\u01db\u01d4\3\2\2\2\u01db\u01d5\3\2\2\2")
        buf.write("\u01db\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2\u01db\u01d8\3")
        buf.write("\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dcg")
        buf.write("\3\2\2\2\u01dd\u01e0\5j\66\2\u01de\u01e0\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0i\3\2\2\2\u01e1")
        buf.write("\u01e2\5f\64\2\u01e2\u01e3\7\64\2\2\u01e3\u01e4\5j\66")
        buf.write("\2\u01e4\u01e7\3\2\2\2\u01e5\u01e7\5f\64\2\u01e6\u01e1")
        buf.write("\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7k\3\2\2\2\u01e8\u01f0")
        buf.write("\7\67\2\2\u01e9\u01f0\78\2\2\u01ea\u01f0\79\2\2\u01eb")
        buf.write("\u01f0\7\25\2\2\u01ec\u01f0\7\26\2\2\u01ed\u01f0\7\24")
        buf.write("\2\2\u01ee\u01f0\5~@\2\u01ef\u01e8\3\2\2\2\u01ef\u01e9")
        buf.write("\3\2\2\2\u01ef\u01ea\3\2\2\2\u01ef\u01eb\3\2\2\2\u01ef")
        buf.write("\u01ec\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2")
        buf.write("\u01f0m\3\2\2\2\u01f1\u01f4\5p9\2\u01f2\u01f4\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4o\3\2\2")
        buf.write("\2\u01f5\u01f6\5l\67\2\u01f6\u01f7\7\64\2\2\u01f7\u01f8")
        buf.write("\5p9\2\u01f8\u01fb\3\2\2\2\u01f9\u01fb\5l\67\2\u01fa\u01f5")
        buf.write("\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fbq\3\2\2\2\u01fc\u01fd")
        buf.write("\5\6\4\2\u01fd\u01fe\7/\2\2\u01fe\u01ff\5t;\2\u01ff\u0200")
        buf.write("\7\60\2\2\u0200s\3\2\2\2\u0201\u0202\5v<\2\u0202\u0203")
        buf.write("\7\64\2\2\u0203\u0204\5t;\2\u0204\u0207\3\2\2\2\u0205")
        buf.write("\u0207\5v<\2\u0206\u0201\3\2\2\2\u0206\u0205\3\2\2\2\u0207")
        buf.write("u\3\2\2\2\u0208\u020e\5p9\2\u0209\u020a\7/\2\2\u020a\u020b")
        buf.write("\5v<\2\u020b\u020c\7\60\2\2\u020c\u020e\3\2\2\2\u020d")
        buf.write("\u0208\3\2\2\2\u020d\u0209\3\2\2\2\u020ew\3\2\2\2\u020f")
        buf.write("\u0210\5z>\2\u0210\u0211\5x=\2\u0211\u0214\3\2\2\2\u0212")
        buf.write("\u0214\5z>\2\u0213\u020f\3\2\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("y\3\2\2\2\u0215\u0216\7\61\2\2\u0216\u0217\7\67\2\2\u0217")
        buf.write("\u0218\7\62\2\2\u0218{\3\2\2\2\u0219\u021a\t\3\2\2\u021a")
        buf.write("}\3\2\2\2\u021b\u021c\7\66\2\2\u021c\u021d\7/\2\2\u021d")
        buf.write("\u021e\5\u0080A\2\u021e\u021f\7\60\2\2\u021f\177\3\2\2")
        buf.write("\2\u0220\u0223\5\u0082B\2\u0221\u0223\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u0081\3\2\2\2\u0224")
        buf.write("\u0225\5\u0084C\2\u0225\u0226\7\64\2\2\u0226\u0227\5\u0082")
        buf.write("B\2\u0227\u022a\3\2\2\2\u0228\u022a\5\u0084C\2\u0229\u0224")
        buf.write("\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u0083\3\2\2\2\u022b")
        buf.write("\u022c\7\66\2\2\u022c\u022d\7\63\2\2\u022d\u0230\5\u008c")
        buf.write("G\2\u022e\u0230\5\34\17\2\u022f\u022b\3\2\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230\u0085\3\2\2\2\u0231\u0232\7\66\2\2\u0232")
        buf.write("\u0233\7-\2\2\u0233\u0234\5\u0088E\2\u0234\u0235\7.\2")
        buf.write("\2\u0235\u0087\3\2\2\2\u0236\u0239\5\u008aF\2\u0237\u0239")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0237\3\2\2\2\u0239")
        buf.write("\u0089\3\2\2\2\u023a\u023b\5\u008cG\2\u023b\u023c\7\64")
        buf.write("\2\2\u023c\u023d\5\u008aF\2\u023d\u0240\3\2\2\2\u023e")
        buf.write("\u0240\5\u008cG\2\u023f\u023a\3\2\2\2\u023f\u023e\3\2")
        buf.write("\2\2\u0240\u008b\3\2\2\2\u0241\u0242\bG\1\2\u0242\u0243")
        buf.write("\5\u008eH\2\u0243\u0249\3\2\2\2\u0244\u0245\f\4\2\2\u0245")
        buf.write("\u0246\7#\2\2\u0246\u0248\5\u008eH\2\u0247\u0244\3\2\2")
        buf.write("\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a")
        buf.write("\3\2\2\2\u024a\u008d\3\2\2\2\u024b\u0249\3\2\2\2\u024c")
        buf.write("\u024d\bH\1\2\u024d\u024e\5\u0090I\2\u024e\u0254\3\2\2")
        buf.write("\2\u024f\u0250\f\4\2\2\u0250\u0251\7\"\2\2\u0251\u0253")
        buf.write("\5\u0090I\2\u0252\u024f\3\2\2\2\u0253\u0256\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u008f\3\2\2\2")
        buf.write("\u0256\u0254\3\2\2\2\u0257\u0258\bI\1\2\u0258\u0259\5")
        buf.write("\u0092J\2\u0259\u025f\3\2\2\2\u025a\u025b\f\4\2\2\u025b")
        buf.write("\u025c\t\4\2\2\u025c\u025e\5\u0092J\2\u025d\u025a\3\2")
        buf.write("\2\2\u025e\u0261\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u0091\3\2\2\2\u0261\u025f\3\2\2\2\u0262")
        buf.write("\u0263\bJ\1\2\u0263\u0264\5\u0094K\2\u0264\u026a\3\2\2")
        buf.write("\2\u0265\u0266\f\4\2\2\u0266\u0267\t\5\2\2\u0267\u0269")
        buf.write("\5\u0094K\2\u0268\u0265\3\2\2\2\u0269\u026c\3\2\2\2\u026a")
        buf.write("\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u0093\3\2\2\2")
        buf.write("\u026c\u026a\3\2\2\2\u026d\u026e\bK\1\2\u026e\u026f\5")
        buf.write("\u0096L\2\u026f\u0275\3\2\2\2\u0270\u0271\f\4\2\2\u0271")
        buf.write("\u0272\t\6\2\2\u0272\u0274\5\u0096L\2\u0273\u0270\3\2")
        buf.write("\2\2\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2\u0275\u0276")
        buf.write("\3\2\2\2\u0276\u0095\3\2\2\2\u0277\u0275\3\2\2\2\u0278")
        buf.write("\u0279\t\7\2\2\u0279\u027c\5\u0096L\2\u027a\u027c\5\u0098")
        buf.write("M\2\u027b\u0278\3\2\2\2\u027b\u027a\3\2\2\2\u027c\u0097")
        buf.write("\3\2\2\2\u027d\u027e\bM\1\2\u027e\u027f\5\u009aN\2\u027f")
        buf.write("\u028e\3\2\2\2\u0280\u028a\f\4\2\2\u0281\u0282\7\61\2")
        buf.write("\2\u0282\u0283\5\u008cG\2\u0283\u0284\7\62\2\2\u0284\u028b")
        buf.write("\3\2\2\2\u0285\u0288\7,\2\2\u0286\u0289\7\66\2\2\u0287")
        buf.write("\u0289\5\u0086D\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2")
        buf.write("\2\2\u0289\u028b\3\2\2\2\u028a\u0281\3\2\2\2\u028a\u0285")
        buf.write("\3\2\2\2\u028b\u028d\3\2\2\2\u028c\u0280\3\2\2\2\u028d")
        buf.write("\u0290\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028f\3\2\2\2")
        buf.write("\u028f\u0099\3\2\2\2\u0290\u028e\3\2\2\2\u0291\u0292\7")
        buf.write("-\2\2\u0292\u0293\5\u008cG\2\u0293\u0294\7.\2\2\u0294")
        buf.write("\u0299\3\2\2\2\u0295\u0299\5f\64\2\u0296\u0299\7\66\2")
        buf.write("\2\u0297\u0299\5\u0086D\2\u0298\u0291\3\2\2\2\u0298\u0295")
        buf.write("\3\2\2\2\u0298\u0296\3\2\2\2\u0298\u0297\3\2\2\2\u0299")
        buf.write("\u009b\3\2\2\28\u00aa\u00b1\u00b5\u00bf\u00c6\u00d7\u00df")
        buf.write("\u00e7\u00f0\u00f7\u0108\u010f\u011d\u0125\u012b\u0132")
        buf.write("\u013b\u013f\u0145\u0150\u015f\u016b\u016f\u0181\u0187")
        buf.write("\u0194\u019e\u01ab\u01c4\u01cf\u01db\u01df\u01e6\u01ef")
        buf.write("\u01f3\u01fa\u0206\u020d\u0213\u0222\u0229\u022f\u0238")
        buf.write("\u023f\u0249\u0254\u025f\u026a\u0275\u027b\u0288\u028a")
        buf.write("\u028e\u0298")
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
    RULE_assignment_statement_no_semi = 32
    RULE_assignment_statement = 33
    RULE_assignment_lhs = 34
    RULE_assignment_lhs_element = 35
    RULE_if_statement = 36
    RULE_list_elseif_prime = 37
    RULE_list_elseif = 38
    RULE_elseif = 39
    RULE_else_statement_prime = 40
    RULE_else_statement = 41
    RULE_for_statement = 42
    RULE_basic_for = 43
    RULE_init_for = 44
    RULE_range_for = 45
    RULE_break_statement = 46
    RULE_continue_statement = 47
    RULE_call_statement = 48
    RULE_return_statement = 49
    RULE_literal = 50
    RULE_list_literal_prime = 51
    RULE_list_literal = 52
    RULE_literal_primitive = 53
    RULE_list_literal_primitive_prime = 54
    RULE_list_literal_primitive = 55
    RULE_array_literal = 56
    RULE_list_array_element = 57
    RULE_array_element = 58
    RULE_list_array_specific = 59
    RULE_array_specific = 60
    RULE_array_declare_type = 61
    RULE_struct_literal = 62
    RULE_list_struct_element_prime = 63
    RULE_list_struct_element = 64
    RULE_struct_element = 65
    RULE_function_call = 66
    RULE_list_expression_prime = 67
    RULE_list_expression = 68
    RULE_expression = 69
    RULE_expression1 = 70
    RULE_expression2 = 71
    RULE_expression3 = 72
    RULE_expression4 = 73
    RULE_expression5 = 74
    RULE_expression6 = 75
    RULE_expression7 = 76

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
                   "assignment_statement_no_semi", "assignment_statement", 
                   "assignment_lhs", "assignment_lhs_element", "if_statement", 
                   "list_elseif_prime", "list_elseif", "elseif", "else_statement_prime", 
                   "else_statement", "for_statement", "basic_for", "init_for", 
                   "range_for", "break_statement", "continue_statement", 
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
            self.state = 154
            self.list_declaration()
            self.state = 155
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
            self.state = 157
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
            self.state = 159
            self.list_array_specific()
            self.state = 160
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
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.array_type()
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
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
            self.state = 170
            self.match(MiniGoParser.VAR)
            self.state = 171
            self.match(MiniGoParser.ID)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 172
                self.all_types()
                pass

            elif la_ == 2:
                self.state = 175
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                    self.state = 173
                    self.all_types()
                    pass
                elif token in [MiniGoParser.ASSIGN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 177
                self.match(MiniGoParser.ASSIGN)
                self.state = 178
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
            self.state = 181
            self.match(MiniGoParser.CONST)
            self.state = 182
            self.match(MiniGoParser.ID)
            self.state = 183
            self.match(MiniGoParser.ASSIGN)
            self.state = 184
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
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.declaration()
                self.state = 189 
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.var_declaration_global()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.const_declaration_global()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
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
            self.state = 198
            self.var_declaration()
            self.state = 199
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
            self.state = 201
            self.const_declaration()
            self.state = 202
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
            self.state = 204
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 205
            self.list_method_element()
            self.state = 206
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.method_element()
                self.state = 209
                self.match(MiniGoParser.COMMA)
                self.state = 210
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
        self.enterRule(localctx, 24, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 216
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
        self.enterRule(localctx, 26, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MiniGoParser.FUNC)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LEFT_PAREN]:
                self.state = 219
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 223
            self.match(MiniGoParser.ID)
            self.state = 224
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 225
            self.list_func_arguments_prime()
            self.state = 226
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 227
                self.all_types()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 231
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 232
            self.list_statement()
            self.state = 233
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 234
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
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.func_arguments()
                self.state = 241
                self.match(MiniGoParser.COMMA)
                self.state = 242
                self.list_func_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
        self.enterRule(localctx, 32, self.RULE_func_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.list_ID()
            self.state = 248
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
        self.enterRule(localctx, 34, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.TYPE)
            self.state = 251
            self.match(MiniGoParser.ID)
            self.state = 252
            self.match(MiniGoParser.STRUCT)
            self.state = 253
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 254
            self.list_struct_argument()
            self.state = 255
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 256
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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.struct_argument()
                self.state = 259
                self.list_struct_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


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
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(MiniGoParser.ID)
                self.state = 265
                self.all_types()
                self.state = 266
                self.terminate()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
        self.enterRule(localctx, 40, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.TYPE)
            self.state = 272
            self.match(MiniGoParser.ID)
            self.state = 273
            self.match(MiniGoParser.INTERFACE)
            self.state = 274
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 275
            self.list_interface_method_declaration()
            self.state = 276
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 277
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
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.interface_method_declaration()
                self.state = 280
                self.list_interface_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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
            self.state = 285
            self.match(MiniGoParser.ID)
            self.state = 286
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 287
            self.list_interface_method_element_prime()
            self.state = 288
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID]:
                self.state = 289
                self.all_types()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
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
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
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
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.interface_method_element()
                self.state = 300
                self.match(MiniGoParser.COMMA)
                self.state = 301
                self.list_interface_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
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
            self.state = 306
            self.list_ID()
            self.state = 307
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
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.ID)
                self.state = 310
                self.match(MiniGoParser.COMMA)
                self.state = 311
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
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
        self.enterRule(localctx, 56, self.RULE_list_statement)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.statement()
                self.state = 320
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.const_declaration_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.var_declaration_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 332
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 333
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
            self.state = 336
            self.var_declaration()
            self.state = 337
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
            self.state = 339
            self.const_declaration()
            self.state = 340
            self.terminate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statement_no_semiContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement_no_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement_no_semi" ):
                return visitor.visitAssignment_statement_no_semi(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement_no_semi(self):

        localctx = MiniGoParser.Assignment_statement_no_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignment_statement_no_semi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.assignment_lhs(0)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_COLON) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 344
            self.expression(0)
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

        def assignment_statement_no_semi(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statement_no_semiContext,0)


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
        self.enterRule(localctx, 66, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.assignment_statement_no_semi()
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 347
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.assignment_lhs_element()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 355
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 356
                        self.expression(0)
                        self.state = 357
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 359
                        self.match(MiniGoParser.DOT)
                        self.state = 360
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_assignment_lhs_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 72, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.IF)
            self.state = 371
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 372
            self.expression(0)
            self.state = 373
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 374
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 375
            self.list_statement()
            self.state = 376
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 377
            self.list_elseif_prime()
            self.state = 378
            self.else_statement_prime()
            self.state = 379
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
        self.enterRule(localctx, 74, self.RULE_list_elseif_prime)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
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
        self.enterRule(localctx, 76, self.RULE_list_elseif)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.elseif()
                self.state = 386
                self.list_elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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
        self.enterRule(localctx, 78, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MiniGoParser.ELSE)
            self.state = 392
            self.match(MiniGoParser.IF)
            self.state = 393
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 394
            self.expression(0)
            self.state = 395
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 396
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 397
            self.list_statement()
            self.state = 398
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
        self.enterRule(localctx, 80, self.RULE_else_statement_prime)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
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
        self.enterRule(localctx, 82, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MiniGoParser.ELSE)
            self.state = 405
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 406
            self.list_statement()
            self.state = 407
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
        self.enterRule(localctx, 84, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 409
                self.basic_for()
                pass

            elif la_ == 2:
                self.state = 410
                self.init_for()
                pass

            elif la_ == 3:
                self.state = 411
                self.range_for()
                pass


            self.state = 414
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 415
            self.list_statement()
            self.state = 416
            self.match(MiniGoParser.RIGHT_CURLY)
            self.state = 417
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
        self.enterRule(localctx, 86, self.RULE_basic_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MiniGoParser.FOR)
            self.state = 420
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


        def assignment_statement_no_semi(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statement_no_semiContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


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
        self.enterRule(localctx, 88, self.RULE_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.FOR)
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 423
                self.assignment_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 424
                self.var_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 427
            self.match(MiniGoParser.SEMICOLON)
            self.state = 428
            self.expression(0)
            self.state = 429
            self.match(MiniGoParser.SEMICOLON)
            self.state = 430
            self.assignment_statement_no_semi()
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
        self.enterRule(localctx, 90, self.RULE_range_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.FOR)
            self.state = 433
            self.match(MiniGoParser.ID)
            self.state = 434
            self.match(MiniGoParser.COMMA)
            self.state = 435
            self.match(MiniGoParser.ID)
            self.state = 436
            self.match(MiniGoParser.ASSIGN_COLON)
            self.state = 437
            self.match(MiniGoParser.RANGE)
            self.state = 438
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
        self.enterRule(localctx, 92, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(MiniGoParser.BREAK)
            self.state = 441
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
        self.enterRule(localctx, 94, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.CONTINUE)
            self.state = 444
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
        self.enterRule(localctx, 96, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 446
                self.assignment_lhs(0)
                self.state = 447
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 452
            self.match(MiniGoParser.ID)
            self.state = 453
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 454
            self.list_expression_prime()
            self.state = 455
            self.match(MiniGoParser.RIGHT_PAREN)
            self.state = 456
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
        self.enterRule(localctx, 98, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.RETURN)
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 459
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 463
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
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 470
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 471
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 472
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
        self.enterRule(localctx, 102, self.RULE_list_literal_prime)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
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
        self.enterRule(localctx, 104, self.RULE_list_literal)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.literal()
                self.state = 480
                self.match(MiniGoParser.COMMA)
                self.state = 481
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
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
        self.enterRule(localctx, 106, self.RULE_literal_primitive)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 489
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 490
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 491
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 492
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
        self.enterRule(localctx, 108, self.RULE_list_literal_primitive_prime)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
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
        self.enterRule(localctx, 110, self.RULE_list_literal_primitive)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.literal_primitive()
                self.state = 500
                self.match(MiniGoParser.COMMA)
                self.state = 501
                self.list_literal_primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
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
        self.enterRule(localctx, 112, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.array_type()
            self.state = 507
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 508
            self.list_array_element()
            self.state = 509
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
        self.enterRule(localctx, 114, self.RULE_list_array_element)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.array_element()
                self.state = 512
                self.match(MiniGoParser.COMMA)
                self.state = 513
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
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
        self.enterRule(localctx, 116, self.RULE_array_element)
        try:
            self.state = 523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.list_literal_primitive()
                pass
            elif token in [MiniGoParser.LEFT_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(MiniGoParser.LEFT_CURLY)
                self.state = 520
                self.array_element()
                self.state = 521
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
        self.enterRule(localctx, 118, self.RULE_list_array_specific)
        try:
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.array_specific()
                self.state = 526
                self.list_array_specific()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
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
        self.enterRule(localctx, 120, self.RULE_array_specific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(MiniGoParser.LEFT_SQUARE)
            self.state = 532
            self.match(MiniGoParser.INT_LIT)
            self.state = 533
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
        self.enterRule(localctx, 122, self.RULE_array_declare_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
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
        self.enterRule(localctx, 124, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.ID)
            self.state = 538
            self.match(MiniGoParser.LEFT_CURLY)
            self.state = 539
            self.list_struct_element_prime()
            self.state = 540
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
        self.enterRule(localctx, 126, self.RULE_list_struct_element_prime)
        try:
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
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
        self.enterRule(localctx, 128, self.RULE_list_struct_element)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.struct_element()
                self.state = 547
                self.match(MiniGoParser.COMMA)
                self.state = 548
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
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
        self.enterRule(localctx, 130, self.RULE_struct_element)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.match(MiniGoParser.ID)
                self.state = 554
                self.match(MiniGoParser.COLON)
                self.state = 555
                self.expression(0)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
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
        self.enterRule(localctx, 132, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.ID)
            self.state = 560
            self.match(MiniGoParser.LEFT_PAREN)
            self.state = 561
            self.list_expression_prime()
            self.state = 562
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
        self.enterRule(localctx, 134, self.RULE_list_expression_prime)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
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
        self.enterRule(localctx, 136, self.RULE_list_expression)
        try:
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.expression(0)
                self.state = 569
                self.match(MiniGoParser.COMMA)
                self.state = 570
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 578
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 579
                    self.match(MiniGoParser.OR)
                    self.state = 580
                    self.expression1(0) 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 594
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 589
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 590
                    self.match(MiniGoParser.AND)
                    self.state = 591
                    self.expression2(0) 
                self.state = 596
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 605
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 600
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 601
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IS_EQUAL) | (1 << MiniGoParser.IS_DIFF) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LT_EQUAL) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GT_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 602
                    self.expression3(0) 
                self.state = 607
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        _startState = 144
        self.enterRecursionRule(localctx, 144, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 616
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 611
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 612
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 613
                    self.expression4(0) 
                self.state = 618
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 627
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 622
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 623
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 624
                    self.expression5() 
                self.state = 629
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 148, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 633
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 630
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 631
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LEFT_PAREN, MiniGoParser.LEFT_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 632
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
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 652
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 638
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 648
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LEFT_SQUARE]:
                        self.state = 639
                        self.match(MiniGoParser.LEFT_SQUARE)
                        self.state = 640
                        self.expression(0)
                        self.state = 641
                        self.match(MiniGoParser.RIGHT_SQUARE)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 643
                        self.match(MiniGoParser.DOT)
                        self.state = 646
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                        if la_ == 1:
                            self.state = 644
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 645
                            self.function_call()
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 654
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 152, self.RULE_expression7)
        try:
            self.state = 662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.match(MiniGoParser.LEFT_PAREN)
                self.state = 656
                self.expression(0)
                self.state = 657
                self.match(MiniGoParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 660
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 661
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
        self._predicates[34] = self.assignment_lhs_sempred
        self._predicates[69] = self.expression_sempred
        self._predicates[70] = self.expression1_sempred
        self._predicates[71] = self.expression2_sempred
        self._predicates[72] = self.expression3_sempred
        self._predicates[73] = self.expression4_sempred
        self._predicates[75] = self.expression6_sempred
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
         




