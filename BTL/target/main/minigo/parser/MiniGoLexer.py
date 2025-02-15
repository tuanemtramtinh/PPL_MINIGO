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
        buf.write("\u0210\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\5\2\u009a\n\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\7\67")
        buf.write("\u015f\n\67\f\67\16\67\u0162\13\67\38\38\38\38\58\u0168")
        buf.write("\n8\38\68\u016b\n8\r8\168\u016c\38\38\39\39\39\39\59\u0175")
        buf.write("\n9\39\69\u0178\n9\r9\169\u0179\39\39\3:\3:\3:\3:\5:\u0182")
        buf.write("\n:\3:\6:\u0185\n:\r:\16:\u0186\3:\3:\3;\3;\3<\3<\3<\7")
        buf.write("<\u0190\n<\f<\16<\u0193\13<\5<\u0195\n<\3=\7=\u0198\n")
        buf.write("=\f=\16=\u019b\13=\5=\u019d\n=\3>\3>\5>\u01a1\n>\3>\6")
        buf.write(">\u01a4\n>\r>\16>\u01a5\5>\u01a8\n>\3?\3?\3?\7?\u01ad")
        buf.write("\n?\f?\16?\u01b0\13?\5?\u01b2\n?\3@\6@\u01b5\n@\r@\16")
        buf.write("@\u01b6\3@\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\5C\u01c5\n")
        buf.write("C\3D\3D\7D\u01c9\nD\fD\16D\u01cc\13D\3D\3D\3E\6E\u01d1")
        buf.write("\nE\rE\16E\u01d2\3E\3E\3F\5F\u01d8\nF\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3G\3G\7G\u01e3\nG\fG\16G\u01e6\13G\3G\3G\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\7H\u01f1\nH\fH\16H\u01f4\13H\3H\3H\3I\3")
        buf.write("I\3I\3J\3J\7J\u01fd\nJ\fJ\16J\u0200\13J\3J\5J\u0203\n")
        buf.write("J\3J\3J\3K\3K\7K\u0209\nK\fK\16K\u020c\13K\3K\3K\3K\3")
        buf.write("\u01e4\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o\2q\2s\2u\2w\2y\2{\2}9\177:\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087;\u0089<\u008b=\u008d>\u008f?\u0091@\u0093A\u0095")
        buf.write("B\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62\63\3\2\629\5")
        buf.write("\2\62;CHch\3\2\62;\3\2\63;\4\2GGgg\4\2--//\7\2$$^^ppt")
        buf.write("tvv\6\2\f\f\17\17$$^^\5\2\13\13\16\17\"\"\4\2\f\f\17\17")
        buf.write("\4\3\f\f\17\17\2\u0223\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0099\3\2\2\2\5\u009b")
        buf.write("\3\2\2\2\7\u009d\3\2\2\2\t\u00a0\3\2\2\2\13\u00a5\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00b0\3\2\2\2\21\u00b5\3\2\2\2")
        buf.write("\23\u00ba\3\2\2\2\25\u00c1\3\2\2\2\27\u00cb\3\2\2\2\31")
        buf.write("\u00d2\3\2\2\2\33\u00d6\3\2\2\2\35\u00dc\3\2\2\2\37\u00e4")
        buf.write("\3\2\2\2!\u00ea\3\2\2\2#\u00ee\3\2\2\2%\u00f7\3\2\2\2")
        buf.write("\'\u00fd\3\2\2\2)\u0103\3\2\2\2+\u0107\3\2\2\2-\u010c")
        buf.write("\3\2\2\2/\u0112\3\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011f\3\2\2\2=\u0122\3\2\2\2?\u0124\3\2\2\2A\u0127\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012f\3\2\2\2I\u0132")
        buf.write("\3\2\2\2K\u0134\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0145\3")
        buf.write("\2\2\2Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014c\3\2\2\2_\u014e")
        buf.write("\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e\u0154\3\2\2\2")
        buf.write("g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u015c\3")
        buf.write("\2\2\2o\u0167\3\2\2\2q\u0174\3\2\2\2s\u0181\3\2\2\2u\u018a")
        buf.write("\3\2\2\2w\u0194\3\2\2\2y\u019c\3\2\2\2{\u01a7\3\2\2\2")
        buf.write("}\u01b1\3\2\2\2\177\u01b4\3\2\2\2\u0081\u01bc\3\2\2\2")
        buf.write("\u0083\u01bf\3\2\2\2\u0085\u01c4\3\2\2\2\u0087\u01c6\3")
        buf.write("\2\2\2\u0089\u01d0\3\2\2\2\u008b\u01d7\3\2\2\2\u008d\u01dd")
        buf.write("\3\2\2\2\u008f\u01ec\3\2\2\2\u0091\u01f7\3\2\2\2\u0093")
        buf.write("\u01fa\3\2\2\2\u0095\u0206\3\2\2\2\u0097\u009a\5+\26\2")
        buf.write("\u0098\u009a\5-\27\2\u0099\u0097\3\2\2\2\u0099\u0098\3")
        buf.write("\2\2\2\u009a\4\3\2\2\2\u009b\u009c\5)\25\2\u009c\6\3\2")
        buf.write("\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f\b\3\2")
        buf.write("\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\n\3\2\2\2\u00a5\u00a6")
        buf.write("\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7e\2\2\u00b4\20")
        buf.write("\3\2\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7{\2\2\u00b7\u00b8")
        buf.write("\7r\2\2\u00b8\u00b9\7g\2\2\u00b9\22\3\2\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7w\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\24")
        buf.write("\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\30\3\2\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\32")
        buf.write("\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7p\2\2\u00e3\36\3\2\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7v\2\2\u00e9 \3\2\2\2\u00ea\u00eb")
        buf.write("\7x\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed\"")
        buf.write("\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6$\3")
        buf.write("\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc&\3")
        buf.write("\2\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7i\2\2\u0101\u0102\7g\2\2\u0102(\3")
        buf.write("\2\2\2\u0103\u0104\7p\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106*\3\2\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2\u010b,\3")
        buf.write("\2\2\2\u010c\u010d\7h\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111.\3")
        buf.write("\2\2\2\u0112\u0113\7-\2\2\u0113\60\3\2\2\2\u0114\u0115")
        buf.write("\7/\2\2\u0115\62\3\2\2\2\u0116\u0117\7,\2\2\u0117\64\3")
        buf.write("\2\2\2\u0118\u0119\7\61\2\2\u0119\66\3\2\2\2\u011a\u011b")
        buf.write("\7\'\2\2\u011b8\3\2\2\2\u011c\u011d\7?\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e:\3\2\2\2\u011f\u0120\7#\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121<\3\2\2\2\u0122\u0123\7>\2\2\u0123>\3\2\2")
        buf.write("\2\u0124\u0125\7>\2\2\u0125\u0126\7?\2\2\u0126@\3\2\2")
        buf.write("\2\u0127\u0128\7@\2\2\u0128B\3\2\2\2\u0129\u012a\7@\2")
        buf.write("\2\u012a\u012b\7?\2\2\u012bD\3\2\2\2\u012c\u012d\7(\2")
        buf.write("\2\u012d\u012e\7(\2\2\u012eF\3\2\2\2\u012f\u0130\7~\2")
        buf.write("\2\u0130\u0131\7~\2\2\u0131H\3\2\2\2\u0132\u0133\7#\2")
        buf.write("\2\u0133J\3\2\2\2\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136")
        buf.write("\u0137\7<\2\2\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139")
        buf.write("\u013a\7-\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c")
        buf.write("\u013d\7/\2\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f")
        buf.write("\u0140\7,\2\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7\61\2\2\u0143\u0144\7?\2\2\u0144V\3\2\2\2\u0145")
        buf.write("\u0146\7\'\2\2\u0146\u0147\7?\2\2\u0147X\3\2\2\2\u0148")
        buf.write("\u0149\7\60\2\2\u0149Z\3\2\2\2\u014a\u014b\7*\2\2\u014b")
        buf.write("\\\3\2\2\2\u014c\u014d\7+\2\2\u014d^\3\2\2\2\u014e\u014f")
        buf.write("\7}\2\2\u014f`\3\2\2\2\u0150\u0151\7\177\2\2\u0151b\3")
        buf.write("\2\2\2\u0152\u0153\7]\2\2\u0153d\3\2\2\2\u0154\u0155\7")
        buf.write("_\2\2\u0155f\3\2\2\2\u0156\u0157\7<\2\2\u0157h\3\2\2\2")
        buf.write("\u0158\u0159\7.\2\2\u0159j\3\2\2\2\u015a\u015b\7=\2\2")
        buf.write("\u015bl\3\2\2\2\u015c\u0160\t\2\2\2\u015d\u015f\t\3\2")
        buf.write("\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161n\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0164\7\62\2\2\u0164\u0168\7d\2\2\u0165")
        buf.write("\u0166\7\62\2\2\u0166\u0168\7D\2\2\u0167\u0163\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u016b\t")
        buf.write("\4\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\b8\2\2\u016fp\3\2\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0175\7q\2\2\u0172\u0173\7\62\2\2\u0173\u0175\7Q\2\2")
        buf.write("\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0177\3")
        buf.write("\2\2\2\u0176\u0178\t\5\2\2\u0177\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017c\b9\2\2\u017cr\3\2\2\2\u017d")
        buf.write("\u017e\7\62\2\2\u017e\u0182\7z\2\2\u017f\u0180\7\62\2")
        buf.write("\2\u0180\u0182\7Z\2\2\u0181\u017d\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0185\t\6\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\b")
        buf.write(":\2\2\u0189t\3\2\2\2\u018a\u018b\t\7\2\2\u018bv\3\2\2")
        buf.write("\2\u018c\u0195\7\62\2\2\u018d\u0191\t\b\2\2\u018e\u0190")
        buf.write("\5u;\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0194\u018c\3\2\2\2\u0194\u018d\3\2\2\2")
        buf.write("\u0195x\3\2\2\2\u0196\u0198\5u;\2\u0197\u0196\3\2\2\2")
        buf.write("\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u0199")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019dz\3\2\2\2\u019e\u01a0")
        buf.write("\t\t\2\2\u019f\u01a1\t\n\2\2\u01a0\u019f\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u01a4\5u;\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u019e\3")
        buf.write("\2\2\2\u01a7\u01a8\3\2\2\2\u01a8|\3\2\2\2\u01a9\u01b2")
        buf.write("\7\62\2\2\u01aa\u01ae\t\b\2\2\u01ab\u01ad\5u;\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3")
        buf.write("\2\2\2\u01b1\u01a9\3\2\2\2\u01b1\u01aa\3\2\2\2\u01b2~")
        buf.write("\3\2\2\2\u01b3\u01b5\5u;\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01b9\5Y-\2\u01b9\u01ba\5y=\2\u01ba")
        buf.write("\u01bb\5{>\2\u01bb\u0080\3\2\2\2\u01bc\u01bd\7^\2\2\u01bd")
        buf.write("\u01be\t\13\2\2\u01be\u0082\3\2\2\2\u01bf\u01c0\7^\2\2")
        buf.write("\u01c0\u01c1\n\13\2\2\u01c1\u0084\3\2\2\2\u01c2\u01c5")
        buf.write("\n\f\2\2\u01c3\u01c5\5\u0081A\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5\u0086\3\2\2\2\u01c6\u01ca\7$\2\2")
        buf.write("\u01c7\u01c9\5\u0085C\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\7$\2\2")
        buf.write("\u01ce\u0088\3\2\2\2\u01cf\u01d1\t\r\2\2\u01d0\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\bE\3\2\u01d5")
        buf.write("\u008a\3\2\2\2\u01d6\u01d8\7\17\2\2\u01d7\u01d6\3\2\2")
        buf.write("\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\7\f\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bF\4\2\u01dc")
        buf.write("\u008c\3\2\2\2\u01dd\u01de\7\61\2\2\u01de\u01df\7,\2\2")
        buf.write("\u01df\u01e4\3\2\2\2\u01e0\u01e3\5\u008dG\2\u01e1\u01e3")
        buf.write("\13\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7")
        buf.write(",\2\2\u01e8\u01e9\7\61\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\bG\3\2\u01eb\u008e\3\2\2\2\u01ec\u01ed\7\61\2\2\u01ed")
        buf.write("\u01ee\7\61\2\2\u01ee\u01f2\3\2\2\2\u01ef\u01f1\n\16\2")
        buf.write("\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f6\bH\3\2\u01f6\u0090\3\2\2\2")
        buf.write("\u01f7\u01f8\13\2\2\2\u01f8\u01f9\bI\5\2\u01f9\u0092\3")
        buf.write("\2\2\2\u01fa\u01fe\7$\2\2\u01fb\u01fd\5\u0085C\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01fe\u01ff\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3")
        buf.write("\2\2\2\u0201\u0203\t\17\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0205\bJ\6\2\u0205\u0094\3\2\2\2")
        buf.write("\u0206\u020a\7$\2\2\u0207\u0209\5\u0085C\2\u0208\u0207")
        buf.write("\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020d\u020e\5\u0083B\2\u020e\u020f\bK\7\2\u020f\u0096")
        buf.write("\3\2\2\2\37\2\u0099\u0160\u0167\u016c\u0174\u0179\u0181")
        buf.write("\u0186\u0191\u0194\u0199\u019c\u01a0\u01a5\u01a7\u01ae")
        buf.write("\u01b1\u01b6\u01c4\u01ca\u01d2\u01d7\u01e2\u01e4\u01f2")
        buf.write("\u01fe\u0202\u020a\b\t9\2\b\2\2\3F\2\3I\3\3J\4\3K\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    NIL_LIT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    IS_EQUAL = 28
    IS_DIFF = 29
    LT = 30
    LT_EQUAL = 31
    GT = 32
    GT_EQUAL = 33
    AND = 34
    OR = 35
    NOT = 36
    ASSIGN = 37
    ASSIGN_COLON = 38
    ADD_ASSIGN = 39
    SUB_ASSIGN = 40
    MUL_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    DOT = 44
    LEFT_PAREN = 45
    RIGHT_PAREN = 46
    LEFT_CURLY = 47
    RIGHT_CURLY = 48
    LEFT_SQUARE = 49
    RIGHT_SQUARE = 50
    COLON = 51
    COMMA = 52
    SEMICOLON = 53
    ID = 54
    INT_LIT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
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
            "BOOL_LIT", "NIL_LIT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
            "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "IS_EQUAL", "IS_DIFF", 
            "LT", "LT_EQUAL", "GT", "GT_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ASSIGN_COLON", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "DOT", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY", 
            "RIGHT_CURLY", "LEFT_SQUARE", "RIGHT_SQUARE", "COLON", "COMMA", 
            "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", 
            "NEWLINE", "COMMENT_BLOCK", "COMMENT_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOL_LIT", "NIL_LIT", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "IS_EQUAL", "IS_DIFF", "LT", "LT_EQUAL", 
                  "GT", "GT_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN_COLON", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY", 
                  "RIGHT_CURLY", "LEFT_SQUARE", "RIGHT_SQUARE", "COLON", 
                  "COMMA", "SEMICOLON", "ID", "BIN_INT_LIT", "OCT_INT_LIT", 
                  "HEX_INT_LIT", "DIGIT", "DIGITS", "OPT_FRAC", "OPT_EXP", 
                  "INT_LIT", "FLOAT_LIT", "ESC_SEQ", "ILLEGAL_ESC_SEQ", 
                  "STRING_CHAR", "STRING_LIT", "WS", "NEWLINE", "COMMENT_BLOCK", 
                  "COMMENT_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.lastTokenType == self.RIGHT_SQUARE or self.lastTokenType == self.RIGHT_PAREN or self.lastTokenType == self.RIGHT_CURLY or self.lastTokenType == self.ID or self.lastTokenType == self.INT_LIT or self.lastTokenType == self.FLOAT_LIT or self.lastTokenType == self.BOOL_LIT or self.lastTokenType == self.STRING_LIT or self.lastTokenType == self.INT or self.lastTokenType == self.FLOAT or self.lastTokenType == self.BOOLEAN or self.lastTokenType == self.STRING or self.lastTokenType == self.RETURN or self.lastTokenType == self.CONTINUE or self.lastTokenType == self.BREAK or self.lastTokenType == self.NIL_LIT:
                    self.text = ";"
                    self.type = self.SEMICOLON
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if self.text[-1] == '\n':
                    if self.text[-2] == '\r':
                        self.text = self.text[:-2]
                    else:
                        self.text = self.text[:-1]
                elif self.text[-1] == '\r':
                    self.text = self.text[: -1]
                else:
                    self.text = self.text[:]
                raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[:])

     


