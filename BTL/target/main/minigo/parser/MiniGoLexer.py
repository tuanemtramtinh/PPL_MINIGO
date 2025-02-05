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
        buf.write("\u0208\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\66\16\66\u0166\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u0171\n\67\3\67\6\67\u0174\n\67\r\67\16\67\u0175")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\58\u0180\n8\38\68\u0183")
        buf.write("\n8\r8\168\u0184\38\38\38\38\39\39\3:\3:\3:\7:\u0190\n")
        buf.write(":\f:\16:\u0193\13:\5:\u0195\n:\3;\3;\7;\u0199\n;\f;\16")
        buf.write(";\u019c\13;\5;\u019e\n;\3<\3<\5<\u01a2\n<\3<\5<\u01a5")
        buf.write("\n<\3=\3=\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\5A\u01b5")
        buf.write("\nA\3B\3B\7B\u01b9\nB\fB\16B\u01bc\13B\3B\3B\3B\3C\3C")
        buf.write("\5C\u01c3\nC\3D\3D\3E\6E\u01c8\nE\rE\16E\u01c9\3E\3E\3")
        buf.write("F\5F\u01cf\nF\3F\3F\3F\3F\3G\3G\3G\3G\3G\7G\u01da\nG\f")
        buf.write("G\16G\u01dd\13G\3G\3G\3G\3G\3G\3H\3H\3H\3H\7H\u01e8\n")
        buf.write("H\fH\16H\u01eb\13H\3H\3H\3I\3I\3I\3J\3J\7J\u01f4\nJ\f")
        buf.write("J\16J\u01f7\13J\3J\5J\u01fa\nJ\3J\3J\3K\3K\7K\u0200\n")
        buf.write("K\fK\16K\u0203\13K\3K\3K\3K\3K\3\u01db\2L\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2y\67")
        buf.write("{8}\2\177\2\u0081\2\u00839\u0085:\u0087;\u0089<\u008b")
        buf.write("=\u008d>\u008f?\u0091@\u0093A\u0095B\3\2\20\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62\63\3\2\629\5\2\62;CHch\3\2\62")
        buf.write(";\3\2\63;\4\2GGgg\4\2--//\7\2$$^^ppttvv\6\2\f\f\17\17")
        buf.write("$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2")
        buf.write("\u0217\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a\3\2\2\2\7\u009f")
        buf.write("\3\2\2\2\t\u00a3\3\2\2\2\13\u00aa\3\2\2\2\r\u00af\3\2")
        buf.write("\2\2\17\u00b4\3\2\2\2\21\u00bb\3\2\2\2\23\u00c5\3\2\2")
        buf.write("\2\25\u00cc\3\2\2\2\27\u00d0\3\2\2\2\31\u00d6\3\2\2\2")
        buf.write("\33\u00de\3\2\2\2\35\u00e4\3\2\2\2\37\u00e8\3\2\2\2!\u00f1")
        buf.write("\3\2\2\2#\u00f7\3\2\2\2%\u00fd\3\2\2\2\'\u0101\3\2\2\2")
        buf.write(")\u0106\3\2\2\2+\u010c\3\2\2\2-\u010e\3\2\2\2/\u0110\3")
        buf.write("\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2")
        buf.write("\2\2\67\u0119\3\2\2\29\u011c\3\2\2\2;\u011e\3\2\2\2=\u0121")
        buf.write("\3\2\2\2?\u0123\3\2\2\2A\u0126\3\2\2\2C\u0129\3\2\2\2")
        buf.write("E\u012c\3\2\2\2G\u012e\3\2\2\2I\u0130\3\2\2\2K\u0133\3")
        buf.write("\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2Q\u013c\3\2\2\2S\u013f")
        buf.write("\3\2\2\2U\u0142\3\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2")
        buf.write("[\u0148\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u014e\3")
        buf.write("\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2g\u0154\3\2\2\2i\u0156")
        buf.write("\3\2\2\2k\u0161\3\2\2\2m\u0170\3\2\2\2o\u017f\3\2\2\2")
        buf.write("q\u018a\3\2\2\2s\u0194\3\2\2\2u\u019d\3\2\2\2w\u01a4\3")
        buf.write("\2\2\2y\u01a6\3\2\2\2{\u01a8\3\2\2\2}\u01ac\3\2\2\2\177")
        buf.write("\u01af\3\2\2\2\u0081\u01b4\3\2\2\2\u0083\u01b6\3\2\2\2")
        buf.write("\u0085\u01c2\3\2\2\2\u0087\u01c4\3\2\2\2\u0089\u01c7\3")
        buf.write("\2\2\2\u008b\u01ce\3\2\2\2\u008d\u01d4\3\2\2\2\u008f\u01e3")
        buf.write("\3\2\2\2\u0091\u01ee\3\2\2\2\u0093\u01f1\3\2\2\2\u0095")
        buf.write("\u01fd\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099")
        buf.write("\4\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c\7n\2\2\u009c")
        buf.write("\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\6\3\2\2\2\u009f")
        buf.write("\u00a0\7h\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7t\2\2\u00a2")
        buf.write("\b\3\2\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7g\2\2\u00a5")
        buf.write("\u00a6\7v\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8\7t\2\2\u00a8")
        buf.write("\u00a9\7p\2\2\u00a9\n\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab")
        buf.write("\u00ac\7w\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7e\2\2\u00ae")
        buf.write("\f\3\2\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7{\2\2\u00b1")
        buf.write("\u00b2\7r\2\2\u00b2\u00b3\7g\2\2\u00b3\16\3\2\2\2\u00b4")
        buf.write("\u00b5\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7t\2\2\u00b7")
        buf.write("\u00b8\7w\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\20\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd")
        buf.write("\u00be\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7e\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\24\3\2\2\2\u00cc")
        buf.write("\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf")
        buf.write("\26\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7q\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7v\2\2\u00d5")
        buf.write("\30\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7c\2\2\u00dc\u00dd\7p\2\2\u00dd\32\3\2\2\2\u00de")
        buf.write("\u00df\7e\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7p\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2\u00e3\7v\2\2\u00e3\34\3\2\2\2\u00e4")
        buf.write("\u00e5\7x\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7t\2\2\u00e7")
        buf.write("\36\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7q\2\2\u00ea")
        buf.write("\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7k\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write(" \3\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7m\2\2\u00f6")
        buf.write("\"\3\2\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7c\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("$\3\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7k\2\2\u00ff")
        buf.write("\u0100\7n\2\2\u0100&\3\2\2\2\u0101\u0102\7v\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7w\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("(\3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108\7c\2\2\u0108")
        buf.write("\u0109\7n\2\2\u0109\u010a\7u\2\2\u010a\u010b\7g\2\2\u010b")
        buf.write("*\3\2\2\2\u010c\u010d\7-\2\2\u010d,\3\2\2\2\u010e\u010f")
        buf.write("\7/\2\2\u010f.\3\2\2\2\u0110\u0111\7,\2\2\u0111\60\3\2")
        buf.write("\2\2\u0112\u0113\7\61\2\2\u0113\62\3\2\2\2\u0114\u0115")
        buf.write("\7\'\2\2\u0115\64\3\2\2\2\u0116\u0117\7?\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118\66\3\2\2\2\u0119\u011a\7#\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b8\3\2\2\2\u011c\u011d\7>\2\2\u011d:\3\2\2")
        buf.write("\2\u011e\u011f\7>\2\2\u011f\u0120\7?\2\2\u0120<\3\2\2")
        buf.write("\2\u0121\u0122\7@\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2")
        buf.write("\2\u0124\u0125\7?\2\2\u0125@\3\2\2\2\u0126\u0127\7(\2")
        buf.write("\2\u0127\u0128\7(\2\2\u0128B\3\2\2\2\u0129\u012a\7~\2")
        buf.write("\2\u012a\u012b\7~\2\2\u012bD\3\2\2\2\u012c\u012d\7#\2")
        buf.write("\2\u012dF\3\2\2\2\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130")
        buf.write("\u0131\7<\2\2\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133")
        buf.write("\u0134\7-\2\2\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7/\2\2\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7,\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c")
        buf.write("\u013d\7\61\2\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7\'\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7\60\2\2\u0143V\3\2\2\2\u0144\u0145\7*\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u0147\7+\2\2\u0147Z\3\2\2\2\u0148\u0149")
        buf.write("\7}\2\2\u0149\\\3\2\2\2\u014a\u014b\7\177\2\2\u014b^\3")
        buf.write("\2\2\2\u014c\u014d\7]\2\2\u014d`\3\2\2\2\u014e\u014f\7")
        buf.write("_\2\2\u014fb\3\2\2\2\u0150\u0151\7<\2\2\u0151d\3\2\2\2")
        buf.write("\u0152\u0153\7.\2\2\u0153f\3\2\2\2\u0154\u0155\7=\2\2")
        buf.write("\u0155h\3\2\2\2\u0156\u015a\t\2\2\2\u0157\u0159\t\3\2")
        buf.write("\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015bj\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015d\u015e\7\62\2\2\u015e\u0162\7d\2\2\u015f")
        buf.write("\u0160\7\62\2\2\u0160\u0162\7D\2\2\u0161\u015d\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0165\t")
        buf.write("\4\2\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0169\b\66\2\2\u0169\u016a\3\2\2\2\u016a\u016b\b\66\3")
        buf.write("\2\u016bl\3\2\2\2\u016c\u016d\7\62\2\2\u016d\u0171\7q")
        buf.write("\2\2\u016e\u016f\7\62\2\2\u016f\u0171\7Q\2\2\u0170\u016c")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u0174\t\5\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\b\67\4\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017a\b\67\3\2\u017an\3\2\2\2\u017b\u017c\7\62\2\2\u017c")
        buf.write("\u0180\7z\2\2\u017d\u017e\7\62\2\2\u017e\u0180\7Z\2\2")
        buf.write("\u017f\u017b\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\3")
        buf.write("\2\2\2\u0181\u0183\t\6\2\2\u0182\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0187\b8\5\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\b8\3\2\u0189p\3\2\2\2\u018a\u018b\t\7\2\2")
        buf.write("\u018br\3\2\2\2\u018c\u0195\7\62\2\2\u018d\u0191\t\b\2")
        buf.write("\2\u018e\u0190\5q9\2\u018f\u018e\3\2\2\2\u0190\u0193\3")
        buf.write("\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u018c\3\2\2\2\u0194")
        buf.write("\u018d\3\2\2\2\u0195t\3\2\2\2\u0196\u019a\7\60\2\2\u0197")
        buf.write("\u0199\5q9\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019d\u0196\3\2\2\2\u019d\u019e\3")
        buf.write("\2\2\2\u019ev\3\2\2\2\u019f\u01a1\t\t\2\2\u01a0\u01a2")
        buf.write("\t\n\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a5\5s:\2\u01a4\u019f\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5x\3\2\2\2\u01a6\u01a7\5s:\2\u01a7")
        buf.write("z\3\2\2\2\u01a8\u01a9\5s:\2\u01a9\u01aa\5u;\2\u01aa\u01ab")
        buf.write("\5w<\2\u01ab|\3\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae\t")
        buf.write("\13\2\2\u01ae~\3\2\2\2\u01af\u01b0\7^\2\2\u01b0\u01b1")
        buf.write("\n\13\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b5\n\f\2\2\u01b3")
        buf.write("\u01b5\5}?\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u0082\3\2\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b9\5\u0081")
        buf.write("A\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bd\u01be\7$\2\2\u01be\u01bf\bB\6\2\u01bf")
        buf.write("\u0084\3\2\2\2\u01c0\u01c3\5\'\24\2\u01c1\u01c3\5)\25")
        buf.write("\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\u0086")
        buf.write("\3\2\2\2\u01c4\u01c5\5%\23\2\u01c5\u0088\3\2\2\2\u01c6")
        buf.write("\u01c8\t\r\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3")
        buf.write("\2\2\2\u01cb\u01cc\bE\7\2\u01cc\u008a\3\2\2\2\u01cd\u01cf")
        buf.write("\7\17\2\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d1\7\f\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d3\bF\b\2\u01d3\u008c\3\2\2\2\u01d4\u01d5\7")
        buf.write("\61\2\2\u01d5\u01d6\7,\2\2\u01d6\u01db\3\2\2\2\u01d7\u01da")
        buf.write("\5\u008dG\2\u01d8\u01da\13\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01de\u01df\7,\2\2\u01df\u01e0\7\61\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01e2\bG\7\2\u01e2\u008e\3\2\2\2\u01e3")
        buf.write("\u01e4\7\61\2\2\u01e4\u01e5\7\61\2\2\u01e5\u01e9\3\2\2")
        buf.write("\2\u01e6\u01e8\n\16\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01ec\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ed\bH\7\2")
        buf.write("\u01ed\u0090\3\2\2\2\u01ee\u01ef\13\2\2\2\u01ef\u01f0")
        buf.write("\bI\t\2\u01f0\u0092\3\2\2\2\u01f1\u01f5\7$\2\2\u01f2\u01f4")
        buf.write("\5\u0081A\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f9\3\2\2\2")
        buf.write("\u01f7\u01f5\3\2\2\2\u01f8\u01fa\t\17\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\bJ\n\2\u01fc")
        buf.write("\u0094\3\2\2\2\u01fd\u0201\7$\2\2\u01fe\u0200\5\u0081")
        buf.write("A\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204\u0205\5\177@\2\u0205\u0206\7$\2\2")
        buf.write("\u0206\u0207\bK\13\2\u0207\u0096\3\2\2\2\33\2\u015a\u0161")
        buf.write("\u0166\u0170\u0175\u017f\u0184\u0191\u0194\u019a\u019d")
        buf.write("\u01a1\u01a4\u01b4\u01ba\u01c2\u01c9\u01ce\u01d9\u01db")
        buf.write("\u01e9\u01f5\u01f9\u0201\f\3\66\2\t\67\2\3\67\3\38\4\3")
        buf.write("B\5\b\2\2\3F\6\3I\7\3J\b\3K\t")
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
            actions[52] = self.BIN_INT_LIT_action 
            actions[53] = self.OCT_INT_LIT_action 
            actions[54] = self.HEX_INT_LIT_action 
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


    def BIN_INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = str(int(self.text, 0))

     

    def OCT_INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = str(int(self.text, 0))

     

    def HEX_INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = str(int(self.text, 0))

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = self.text[1:-1]

     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                if self.lastTokenType == self.RIGHT_SQUARE or self.lastTokenType == self.RIGHT_PAREN or self.lastTokenType == self.RIGHT_CURLY or self.lastTokenType == self.ID or self.lastTokenType == self.INT_LIT or self.lastTokenType == self.FLOAT_LIT or self.lastTokenType == self.TRUE or self.lastTokenType == self.FALSE or self.lastTokenType == self.STRING_LIT or self.lastTokenType == self.INT or self.lastTokenType == self.FLOAT or self.lastTokenType == self.BOOLEAN or self.lastTokenType == self.STRING or self.lastTokenType == self.RETURN or self.lastTokenType == self.CONTINUE or self.lastTokenType == self.BREAK:
                    self.text = ";"
                    self.type = self.SEMICOLON
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

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
        if actionIndex == 7:

                raise IllegalEscape(self.text[1:-1])

     


