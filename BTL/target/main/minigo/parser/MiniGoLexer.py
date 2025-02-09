# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0212\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c\13\65\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u0162\n\66\3\66\6\66\u0165\n\66\r")
        buf.write("\66\16\66\u0166\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u016f")
        buf.write("\n\67\3\67\6\67\u0172\n\67\r\67\16\67\u0173\3\67\3\67")
        buf.write("\38\38\38\38\58\u017c\n8\38\68\u017f\n8\r8\168\u0180\3")
        buf.write("8\38\39\39\3:\3:\3:\7:\u018a\n:\f:\16:\u018d\13:\5:\u018f")
        buf.write("\n:\3;\7;\u0192\n;\f;\16;\u0195\13;\5;\u0197\n;\3<\3<")
        buf.write("\5<\u019b\n<\3<\6<\u019e\n<\r<\16<\u019f\5<\u01a2\n<\3")
        buf.write("=\3=\3=\7=\u01a7\n=\f=\16=\u01aa\13=\5=\u01ac\n=\3>\6")
        buf.write(">\u01af\n>\r>\16>\u01b0\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@")
        buf.write("\3A\3A\5A\u01bf\nA\3B\3B\7B\u01c3\nB\fB\16B\u01c6\13B")
        buf.write("\3B\3B\3B\3C\3C\5C\u01cd\nC\3D\3D\3E\6E\u01d2\nE\rE\16")
        buf.write("E\u01d3\3E\3E\3F\5F\u01d9\nF\3F\3F\3F\3F\3G\3G\3G\3G\3")
        buf.write("G\7G\u01e4\nG\fG\16G\u01e7\13G\3G\3G\3G\3G\3G\3H\3H\3")
        buf.write("H\3H\7H\u01f2\nH\fH\16H\u01f5\13H\3H\3H\3I\3I\3I\3J\3")
        buf.write("J\7J\u01fe\nJ\fJ\16J\u0201\13J\3J\5J\u0204\nJ\3J\3J\3")
        buf.write("K\3K\7K\u020a\nK\fK\16K\u020d\13K\3K\3K\3K\3K\3\u01e5")
        buf.write("\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2")
        buf.write("q\2s\2u\2w\2y\67{8}\2\177\2\u0081\2\u00839\u0085:\u0087")
        buf.write(";\u0089<\u008b=\u008d>\u008f?\u0091@\u0093A\u0095B\3\2")
        buf.write("\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62\63\3\2\629\5\2\62")
        buf.write(";CHch\3\2\62;\3\2\63;\4\2GGgg\4\2--//\7\2$$^^ppttvv\6")
        buf.write("\2\f\f\17\17$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\4\3")
        buf.write("\f\f\17\17\2\u0225\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a")
        buf.write("\3\2\2\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13\u00aa\3\2")
        buf.write("\2\2\r\u00af\3\2\2\2\17\u00b4\3\2\2\2\21\u00bb\3\2\2\2")
        buf.write("\23\u00c5\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0\3\2\2\2\31")
        buf.write("\u00d6\3\2\2\2\33\u00de\3\2\2\2\35\u00e4\3\2\2\2\37\u00e8")
        buf.write("\3\2\2\2!\u00f1\3\2\2\2#\u00f7\3\2\2\2%\u00fd\3\2\2\2")
        buf.write("\'\u0101\3\2\2\2)\u0106\3\2\2\2+\u010c\3\2\2\2-\u010e")
        buf.write("\3\2\2\2/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2")
        buf.write("\2\2\65\u0116\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011e\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2I\u0130")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0144\3")
        buf.write("\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c")
        buf.write("\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2")
        buf.write("g\u0154\3\2\2\2i\u0156\3\2\2\2k\u0161\3\2\2\2m\u016e\3")
        buf.write("\2\2\2o\u017b\3\2\2\2q\u0184\3\2\2\2s\u018e\3\2\2\2u\u0196")
        buf.write("\3\2\2\2w\u01a1\3\2\2\2y\u01ab\3\2\2\2{\u01ae\3\2\2\2")
        buf.write("}\u01b6\3\2\2\2\177\u01b9\3\2\2\2\u0081\u01be\3\2\2\2")
        buf.write("\u0083\u01c0\3\2\2\2\u0085\u01cc\3\2\2\2\u0087\u01ce\3")
        buf.write("\2\2\2\u0089\u01d1\3\2\2\2\u008b\u01d8\3\2\2\2\u008d\u01de")
        buf.write("\3\2\2\2\u008f\u01ed\3\2\2\2\u0091\u01f8\3\2\2\2\u0093")
        buf.write("\u01fb\3\2\2\2\u0095\u0207\3\2\2\2\u0097\u0098\7k\2\2")
        buf.write("\u0098\u0099\7h\2\2\u0099\4\3\2\2\2\u009a\u009b\7g\2\2")
        buf.write("\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e\7g")
        buf.write("\2\2\u009e\6\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7")
        buf.write("q\2\2\u00a1\u00a2\7t\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7")
        buf.write("t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\f\3\2\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7{\2\2\u00b1\u00b2\7r\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7e\2\2\u00b9\u00ba\7v\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7g\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\26\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\32\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\36\3\2\2\2\u00e8\u00e9")
        buf.write("\7e\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7w\2\2\u00ef\u00f0\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2")
        buf.write("\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7m\2\2\u00f6\"\3\2\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7i\2\2\u00fb\u00fc\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7n\2\2\u0100&\3")
        buf.write("\2\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7g\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7u\2\2\u010a\u010b\7g\2\2\u010b*\3\2\2\2\u010c\u010d")
        buf.write("\7-\2\2\u010d,\3\2\2\2\u010e\u010f\7/\2\2\u010f.\3\2\2")
        buf.write("\2\u0110\u0111\7,\2\2\u0111\60\3\2\2\2\u0112\u0113\7\61")
        buf.write("\2\2\u0113\62\3\2\2\2\u0114\u0115\7\'\2\2\u0115\64\3\2")
        buf.write("\2\2\u0116\u0117\7?\2\2\u0117\u0118\7?\2\2\u0118\66\3")
        buf.write("\2\2\2\u0119\u011a\7#\2\2\u011a\u011b\7?\2\2\u011b8\3")
        buf.write("\2\2\2\u011c\u011d\7>\2\2\u011d:\3\2\2\2\u011e\u011f\7")
        buf.write(">\2\2\u011f\u0120\7?\2\2\u0120<\3\2\2\2\u0121\u0122\7")
        buf.write("@\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7")
        buf.write("?\2\2\u0125@\3\2\2\2\u0126\u0127\7(\2\2\u0127\u0128\7")
        buf.write("(\2\2\u0128B\3\2\2\2\u0129\u012a\7~\2\2\u012a\u012b\7")
        buf.write("~\2\2\u012bD\3\2\2\2\u012c\u012d\7#\2\2\u012dF\3\2\2\2")
        buf.write("\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130\u0131\7<\2\2")
        buf.write("\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133\u0134\7-\2\2")
        buf.write("\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136\u0137\7/\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139\u013a\7,\2\2")
        buf.write("\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c\u013d\7\61\2")
        buf.write("\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f\u0140\7\'\2")
        buf.write("\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142\u0143\7\60")
        buf.write("\2\2\u0143V\3\2\2\2\u0144\u0145\7*\2\2\u0145X\3\2\2\2")
        buf.write("\u0146\u0147\7+\2\2\u0147Z\3\2\2\2\u0148\u0149\7}\2\2")
        buf.write("\u0149\\\3\2\2\2\u014a\u014b\7\177\2\2\u014b^\3\2\2\2")
        buf.write("\u014c\u014d\7]\2\2\u014d`\3\2\2\2\u014e\u014f\7_\2\2")
        buf.write("\u014fb\3\2\2\2\u0150\u0151\7<\2\2\u0151d\3\2\2\2\u0152")
        buf.write("\u0153\7.\2\2\u0153f\3\2\2\2\u0154\u0155\7=\2\2\u0155")
        buf.write("h\3\2\2\2\u0156\u015a\t\2\2\2\u0157\u0159\t\3\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015bj\3\2\2\2\u015c\u015a\3\2\2")
        buf.write("\2\u015d\u015e\7\62\2\2\u015e\u0162\7d\2\2\u015f\u0160")
        buf.write("\7\62\2\2\u0160\u0162\7D\2\2\u0161\u015d\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0165\t\4\2\2")
        buf.write("\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3")
        buf.write("\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169")
        buf.write("\b\66\2\2\u0169l\3\2\2\2\u016a\u016b\7\62\2\2\u016b\u016f")
        buf.write("\7q\2\2\u016c\u016d\7\62\2\2\u016d\u016f\7Q\2\2\u016e")
        buf.write("\u016a\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u0172\t\5\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0176\b\67\2\2\u0176n\3\2\2\2\u0177\u0178")
        buf.write("\7\62\2\2\u0178\u017c\7z\2\2\u0179\u017a\7\62\2\2\u017a")
        buf.write("\u017c\7Z\2\2\u017b\u0177\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017c\u017e\3\2\2\2\u017d\u017f\t\6\2\2\u017e\u017d\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\b8\2\2\u0183")
        buf.write("p\3\2\2\2\u0184\u0185\t\7\2\2\u0185r\3\2\2\2\u0186\u018f")
        buf.write("\7\62\2\2\u0187\u018b\t\b\2\2\u0188\u018a\5q9\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3")
        buf.write("\2\2\2\u018e\u0186\3\2\2\2\u018e\u0187\3\2\2\2\u018ft")
        buf.write("\3\2\2\2\u0190\u0192\5q9\2\u0191\u0190\3\2\2\2\u0192\u0195")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0193\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197v\3\2\2\2\u0198\u019a\t\t\2")
        buf.write("\2\u0199\u019b\t\n\2\2\u019a\u0199\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\5q9\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u0198\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2x\3\2\2\2\u01a3\u01ac\7\62\2")
        buf.write("\2\u01a4\u01a8\t\b\2\2\u01a5\u01a7\5q9\2\u01a6\u01a5\3")
        buf.write("\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab")
        buf.write("\u01a3\3\2\2\2\u01ab\u01a4\3\2\2\2\u01acz\3\2\2\2\u01ad")
        buf.write("\u01af\5q9\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2\u01b3\5U+\2\u01b3\u01b4\5u;\2\u01b4\u01b5\5w<\2")
        buf.write("\u01b5|\3\2\2\2\u01b6\u01b7\7^\2\2\u01b7\u01b8\t\13\2")
        buf.write("\2\u01b8~\3\2\2\2\u01b9\u01ba\7^\2\2\u01ba\u01bb\n\13")
        buf.write("\2\2\u01bb\u0080\3\2\2\2\u01bc\u01bf\n\f\2\2\u01bd\u01bf")
        buf.write("\5}?\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u0082")
        buf.write("\3\2\2\2\u01c0\u01c4\7$\2\2\u01c1\u01c3\5\u0081A\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c5\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3")
        buf.write("\2\2\2\u01c7\u01c8\7$\2\2\u01c8\u01c9\bB\3\2\u01c9\u0084")
        buf.write("\3\2\2\2\u01ca\u01cd\5\'\24\2\u01cb\u01cd\5)\25\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u0086\3\2\2\2")
        buf.write("\u01ce\u01cf\5%\23\2\u01cf\u0088\3\2\2\2\u01d0\u01d2\t")
        buf.write("\r\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d6\bE\4\2\u01d6\u008a\3\2\2\2\u01d7\u01d9\7\17\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\3")
        buf.write("\2\2\2\u01da\u01db\7\f\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd")
        buf.write("\bF\5\2\u01dd\u008c\3\2\2\2\u01de\u01df\7\61\2\2\u01df")
        buf.write("\u01e0\7,\2\2\u01e0\u01e5\3\2\2\2\u01e1\u01e4\5\u008d")
        buf.write("G\2\u01e2\u01e4\13\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u01e9\7,\2\2\u01e9\u01ea\7\61\2\2\u01ea\u01eb\3")
        buf.write("\2\2\2\u01eb\u01ec\bG\4\2\u01ec\u008e\3\2\2\2\u01ed\u01ee")
        buf.write("\7\61\2\2\u01ee\u01ef\7\61\2\2\u01ef\u01f3\3\2\2\2\u01f0")
        buf.write("\u01f2\n\16\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f5\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\bH\4\2\u01f7")
        buf.write("\u0090\3\2\2\2\u01f8\u01f9\13\2\2\2\u01f9\u01fa\bI\6\2")
        buf.write("\u01fa\u0092\3\2\2\2\u01fb\u01ff\7$\2\2\u01fc\u01fe\5")
        buf.write("\u0081A\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0203\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0202\u0204\t\17\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\bJ\7\2\u0206")
        buf.write("\u0094\3\2\2\2\u0207\u020b\7$\2\2\u0208\u020a\5\u0081")
        buf.write("A\2\u0209\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u020f\5\177@\2\u020f\u0210\7$\2\2")
        buf.write("\u0210\u0211\bK\b\2\u0211\u0096\3\2\2\2\37\2\u015a\u0161")
        buf.write("\u0166\u016e\u0173\u017b\u0180\u018b\u018e\u0193\u0196")
        buf.write("\u019a\u019f\u01a1\u01a8\u01ab\u01b0\u01be\u01c4\u01cc")
        buf.write("\u01d3\u01d8\u01e3\u01e5\u01f3\u01ff\u0203\u020b\t\t\67")
        buf.write("\2\3B\2\b\2\2\3F\3\3I\4\3J\5\3K\6")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    IS_EQUAL = 26
    IS_DIFF = 27
    LT = 28
    LT_EQUAL = 29
    GT = 30
    GT_EQUAL = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    ASSIGN_COLON = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    LEFT_PAREN = 43
    RIGHT_PAREN = 44
    LEFT_CURLY = 45
    RIGHT_CURLY = 46
    LEFT_SQUARE = 47
    RIGHT_SQUARE = 48
    COLON = 49
    COMMA = 50
    SEMICOLON = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    BOOL_LIT = 56
    NIL_LIT = 57
    WS = 58
    NEWLINE = 59
    COMMENT_BLOCK = 60
    COMMENT_LINE = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "IS_EQUAL", "IS_DIFF", "LT", "LT_EQUAL", "GT", 
            "GT_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN_COLON", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", 
            "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY", "RIGHT_CURLY", "LEFT_SQUARE", 
            "RIGHT_SQUARE", "COLON", "COMMA", "SEMICOLON", "ID", "INT_LIT", 
            "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", "WS", "NEWLINE", 
            "COMMENT_BLOCK", "COMMENT_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "IS_EQUAL", "IS_DIFF", 
                  "LT", "LT_EQUAL", "GT", "GT_EQUAL", "AND", "OR", "NOT", 
                  "ASSIGN", "ASSIGN_COLON", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LEFT_PAREN", 
                  "RIGHT_PAREN", "LEFT_CURLY", "RIGHT_CURLY", "LEFT_SQUARE", 
                  "RIGHT_SQUARE", "COLON", "COMMA", "SEMICOLON", "ID", "BIN_INT_LIT", 
                  "OCT_INT_LIT", "HEX_INT_LIT", "DIGIT", "DIGITS", "OPT_FRAC", 
                  "OPT_EXP", "INT_LIT", "FLOAT_LIT", "ESC_SEQ", "ILLEGAL_ESC_SEQ", 
                  "STRING_CHAR", "STRING_LIT", "BOOL_LIT", "NIL_LIT", "WS", 
                  "NEWLINE", "COMMENT_BLOCK", "COMMENT_LINE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    lastTokenType = 0

    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            self.lastTokenType = result.type
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            self.lastTokenType = result.type
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            self.lastTokenType = result.type
            raise ErrorToken(result.text); 
        else:
            result = super().emit();
            self.lastTokenType = result.type
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[64] = self.STRING_LIT_action 
            actions[68] = self.NEWLINE_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]

     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if self.lastTokenType == self.RIGHT_SQUARE or self.lastTokenType == self.RIGHT_PAREN or self.lastTokenType == self.RIGHT_CURLY or self.lastTokenType == self.ID or self.lastTokenType == self.INT_LIT or self.lastTokenType == self.FLOAT_LIT or self.lastTokenType == self.TRUE or self.lastTokenType == self.FALSE or self.lastTokenType == self.STRING_LIT or self.lastTokenType == self.INT or self.lastTokenType == self.FLOAT or self.lastTokenType == self.BOOLEAN or self.lastTokenType == self.STRING or self.lastTokenType == self.RETURN or self.lastTokenType == self.CONTINUE or self.lastTokenType == self.BREAK:
                    self.text = ";"
                    self.type = self.SEMICOLON
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if self.text[-1] == '\n':
                    if self.text[-2] == '\r':
                        self.text = self.text[1:-2]
                    else:
                        self.text = self.text[1:-1]
                elif self.text[-1] == '\r':
                    self.text = self.text[1: -1]
                else:
                    self.text = self.text[1:]
                raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text[1:-1])

     


