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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01e9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\7\65\u014f\n\65\f\65\16")
        buf.write("\65\u0152\13\65\3\66\7\66\u0155\n\66\f\66\16\66\u0158")
        buf.write("\13\66\3\66\3\66\3\66\7\66\u015d\n\66\f\66\16\66\u0160")
        buf.write("\13\66\3\66\3\66\5\66\u0164\n\66\3\66\7\66\u0167\n\66")
        buf.write("\f\66\16\66\u016a\13\66\3\66\5\66\u016d\n\66\3\67\3\67")
        buf.write("\3\67\6\67\u0172\n\67\r\67\16\67\u0173\5\67\u0176\n\67")
        buf.write("\38\38\38\68\u017b\n8\r8\168\u017c\39\39\39\69\u0182\n")
        buf.write("9\r9\169\u0183\3:\3:\3:\6:\u0189\n:\r:\16:\u018a\3;\3")
        buf.write(";\7;\u018f\n;\f;\16;\u0192\13;\3;\3;\3<\3<\5<\u0198\n")
        buf.write("<\3=\3=\3=\3>\3>\3>\3?\3?\5?\u01a2\n?\3@\5@\u01a5\n@\3")
        buf.write("@\6@\u01a8\n@\r@\16@\u01a9\3@\3@\3A\6A\u01af\nA\rA\16")
        buf.write("A\u01b0\3A\3A\3B\3B\3B\3B\3B\7B\u01ba\nB\fB\16B\u01bd")
        buf.write("\13B\3B\3B\3B\3B\3B\3C\3C\3C\3C\7C\u01c8\nC\fC\16C\u01cb")
        buf.write("\13C\3C\3C\3D\3D\3D\3E\3E\7E\u01d4\nE\fE\16E\u01d7\13")
        buf.write("E\3E\3E\3E\5E\u01dc\nE\3E\3E\3F\3F\7F\u01e2\nF\fF\16F")
        buf.write("\u01e5\13F\3F\3F\3F\3\u01bb\2G\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{\2}=\177>\u0081")
        buf.write("?\u0083@\u0085A\u0087B\u0089C\u008bD\3\2\24\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62\62\3\2\62;\4\2GGgg\4\2--//\3\2")
        buf.write("\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62")
        buf.write(";CHch\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\5\2\13\13\16\17")
        buf.write("\"\"\4\2\f\f\17\17\3\3\f\f\2\u01fc\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0090\3\2\2")
        buf.write("\2\7\u0095\3\2\2\2\t\u0099\3\2\2\2\13\u00a0\3\2\2\2\r")
        buf.write("\u00a5\3\2\2\2\17\u00aa\3\2\2\2\21\u00b1\3\2\2\2\23\u00bb")
        buf.write("\3\2\2\2\25\u00c2\3\2\2\2\27\u00c6\3\2\2\2\31\u00cc\3")
        buf.write("\2\2\2\33\u00d4\3\2\2\2\35\u00da\3\2\2\2\37\u00de\3\2")
        buf.write("\2\2!\u00e7\3\2\2\2#\u00ed\3\2\2\2%\u00f3\3\2\2\2\'\u00f7")
        buf.write("\3\2\2\2)\u00fc\3\2\2\2+\u0102\3\2\2\2-\u0104\3\2\2\2")
        buf.write("/\u0107\3\2\2\2\61\u0109\3\2\2\2\63\u010b\3\2\2\2\65\u010e")
        buf.write("\3\2\2\2\67\u0110\3\2\2\29\u0113\3\2\2\2;\u0116\3\2\2")
        buf.write("\2=\u0119\3\2\2\2?\u011b\3\2\2\2A\u011e\3\2\2\2C\u0121")
        buf.write("\3\2\2\2E\u0124\3\2\2\2G\u0127\3\2\2\2I\u012a\3\2\2\2")
        buf.write("K\u012d\3\2\2\2M\u0130\3\2\2\2O\u0132\3\2\2\2Q\u0134\3")
        buf.write("\2\2\2S\u0136\3\2\2\2U\u0138\3\2\2\2W\u013a\3\2\2\2Y\u013c")
        buf.write("\3\2\2\2[\u013e\3\2\2\2]\u0140\3\2\2\2_\u0142\3\2\2\2")
        buf.write("a\u0144\3\2\2\2c\u0146\3\2\2\2e\u0148\3\2\2\2g\u014a\3")
        buf.write("\2\2\2i\u014c\3\2\2\2k\u0156\3\2\2\2m\u0175\3\2\2\2o\u0177")
        buf.write("\3\2\2\2q\u017e\3\2\2\2s\u0185\3\2\2\2u\u018c\3\2\2\2")
        buf.write("w\u0197\3\2\2\2y\u0199\3\2\2\2{\u019c\3\2\2\2}\u01a1\3")
        buf.write("\2\2\2\177\u01a7\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b4")
        buf.write("\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01ce\3\2\2\2\u0089")
        buf.write("\u01d1\3\2\2\2\u008b\u01df\3\2\2\2\u008d\u008e\7k\2\2")
        buf.write("\u008e\u008f\7h\2\2\u008f\4\3\2\2\2\u0090\u0091\7g\2\2")
        buf.write("\u0091\u0092\7n\2\2\u0092\u0093\7u\2\2\u0093\u0094\7g")
        buf.write("\2\2\u0094\6\3\2\2\2\u0095\u0096\7h\2\2\u0096\u0097\7")
        buf.write("q\2\2\u0097\u0098\7t\2\2\u0098\b\3\2\2\2\u0099\u009a\7")
        buf.write("t\2\2\u009a\u009b\7g\2\2\u009b\u009c\7v\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7t\2\2\u009e\u009f\7p\2\2\u009f\n")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7e\2\2\u00a4\f\3\2\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7{\2\2\u00a7\u00a8\7r\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\16\3\2\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac")
        buf.write("\7v\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7e\2\2\u00af\u00b0\7v\2\2\u00b0\20\3\2\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba\7g\2\2\u00ba\22")
        buf.write("\3\2\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7v\2\2\u00c5\26\3\2\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7v\2\2\u00cb\30\3\2\2\2\u00cc\u00cd")
        buf.write("\7d\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7n\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\32\3\2\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\34\3\2\2\2\u00da\u00db\7x\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7t\2\2\u00dd\36\3\2\2\2\u00de\u00df")
        buf.write("\7e\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7w\2\2\u00e5\u00e6\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8")
        buf.write("\7d\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7c\2\2\u00eb\u00ec\7m\2\2\u00ec\"\3\2\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7i\2\2\u00f1\u00f2\7g\2\2\u00f2$\3\2\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7n\2\2\u00f6&\3")
        buf.write("\2\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb(\3\2\2\2\u00fc\u00fd")
        buf.write("\7h\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100\u0101\7g\2\2\u0101*\3\2\2\2\u0102\u0103")
        buf.write("\7\60\2\2\u0103,\3\2\2\2\u0104\u0105\7<\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106.\3\2\2\2\u0107\u0108\7<\2\2\u0108\60\3\2")
        buf.write("\2\2\u0109\u010a\7>\2\2\u010a\62\3\2\2\2\u010b\u010c\7")
        buf.write(">\2\2\u010c\u010d\7?\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7@\2\2\u010f\66\3\2\2\2\u0110\u0111\7@\2\2\u0111\u0112")
        buf.write("\7?\2\2\u01128\3\2\2\2\u0113\u0114\7?\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115:\3\2\2\2\u0116\u0117\7#\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118<\3\2\2\2\u0119\u011a\7?\2\2\u011a>\3\2\2")
        buf.write("\2\u011b\u011c\7-\2\2\u011c\u011d\7?\2\2\u011d@\3\2\2")
        buf.write("\2\u011e\u011f\7/\2\2\u011f\u0120\7?\2\2\u0120B\3\2\2")
        buf.write("\2\u0121\u0122\7,\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2")
        buf.write("\2\u0124\u0125\7\61\2\2\u0125\u0126\7?\2\2\u0126F\3\2")
        buf.write("\2\2\u0127\u0128\7\'\2\2\u0128\u0129\7?\2\2\u0129H\3\2")
        buf.write("\2\2\u012a\u012b\7(\2\2\u012b\u012c\7(\2\2\u012cJ\3\2")
        buf.write("\2\2\u012d\u012e\7~\2\2\u012e\u012f\7~\2\2\u012fL\3\2")
        buf.write("\2\2\u0130\u0131\7#\2\2\u0131N\3\2\2\2\u0132\u0133\7-")
        buf.write("\2\2\u0133P\3\2\2\2\u0134\u0135\7/\2\2\u0135R\3\2\2\2")
        buf.write("\u0136\u0137\7,\2\2\u0137T\3\2\2\2\u0138\u0139\7\61\2")
        buf.write("\2\u0139V\3\2\2\2\u013a\u013b\7\'\2\2\u013bX\3\2\2\2\u013c")
        buf.write("\u013d\7*\2\2\u013dZ\3\2\2\2\u013e\u013f\7+\2\2\u013f")
        buf.write("\\\3\2\2\2\u0140\u0141\7}\2\2\u0141^\3\2\2\2\u0142\u0143")
        buf.write("\7\177\2\2\u0143`\3\2\2\2\u0144\u0145\7]\2\2\u0145b\3")
        buf.write("\2\2\2\u0146\u0147\7_\2\2\u0147d\3\2\2\2\u0148\u0149\7")
        buf.write("=\2\2\u0149f\3\2\2\2\u014a\u014b\7.\2\2\u014bh\3\2\2\2")
        buf.write("\u014c\u0150\t\2\2\2\u014d\u014f\t\3\2\2\u014e\u014d\3")
        buf.write("\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151j\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155")
        buf.write("\t\4\2\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0159\u015a\5m\67\2\u015a\u015e\5")
        buf.write("+\26\2\u015b\u015d\t\5\2\2\u015c\u015b\3\2\2\2\u015d\u0160")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u016c\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0163\t\6\2\2")
        buf.write("\u0162\u0164\t\7\2\2\u0163\u0162\3\2\2\2\u0163\u0164\3")
        buf.write("\2\2\2\u0164\u0168\3\2\2\2\u0165\u0167\t\4\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016b\u016d\5m\67\2\u016c\u0161\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016dl\3\2\2\2\u016e\u0176\t\5\2\2\u016f\u0171")
        buf.write("\t\b\2\2\u0170\u0172\t\5\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u016e\3\2\2\2\u0175\u016f\3")
        buf.write("\2\2\2\u0176n\3\2\2\2\u0177\u0178\t\4\2\2\u0178\u017a")
        buf.write("\t\t\2\2\u0179\u017b\t\n\2\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017dp\3\2\2\2\u017e\u017f\t\4\2\2\u017f\u0181\t\13\2")
        buf.write("\2\u0180\u0182\t\f\2\2\u0181\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("r\3\2\2\2\u0185\u0186\t\4\2\2\u0186\u0188\t\r\2\2\u0187")
        buf.write("\u0189\t\16\2\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2")
        buf.write("\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018bt\3\2")
        buf.write("\2\2\u018c\u0190\7$\2\2\u018d\u018f\5w<\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0193\u0194\7$\2\2\u0194v\3\2\2\2\u0195\u0198\5y=\2\u0196")
        buf.write("\u0198\n\17\2\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2")
        buf.write("\2\u0198x\3\2\2\2\u0199\u019a\7^\2\2\u019a\u019b\t\20")
        buf.write("\2\2\u019bz\3\2\2\2\u019c\u019d\7^\2\2\u019d\u019e\n\20")
        buf.write("\2\2\u019e|\3\2\2\2\u019f\u01a2\5\'\24\2\u01a0\u01a2\5")
        buf.write(")\25\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2~")
        buf.write("\3\2\2\2\u01a3\u01a5\7\17\2\2\u01a4\u01a3\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\7\f\2\2")
        buf.write("\u01a7\u01a4\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3")
        buf.write("\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac")
        buf.write("\b@\2\2\u01ac\u0080\3\2\2\2\u01ad\u01af\t\21\2\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\b")
        buf.write("A\3\2\u01b3\u0082\3\2\2\2\u01b4\u01b5\7\61\2\2\u01b5\u01b6")
        buf.write("\7,\2\2\u01b6\u01bb\3\2\2\2\u01b7\u01ba\5\u0083B\2\u01b8")
        buf.write("\u01ba\13\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2")
        buf.write("\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01bf\7,\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c2\bB\3\2\u01c2\u0084\3\2\2\2\u01c3\u01c4\7")
        buf.write("\61\2\2\u01c4\u01c5\7\61\2\2\u01c5\u01c9\3\2\2\2\u01c6")
        buf.write("\u01c8\n\22\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2")
        buf.write("\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\bC\3\2\u01cd")
        buf.write("\u0086\3\2\2\2\u01ce\u01cf\13\2\2\2\u01cf\u01d0\bD\4\2")
        buf.write("\u01d0\u0088\3\2\2\2\u01d1\u01d5\7$\2\2\u01d2\u01d4\5")
        buf.write("w<\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01db\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\7\17\2\2\u01d9\u01dc\7\f\2")
        buf.write("\2\u01da\u01dc\t\23\2\2\u01db\u01d8\3\2\2\2\u01db\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bE\5\2\u01de")
        buf.write("\u008a\3\2\2\2\u01df\u01e3\7$\2\2\u01e0\u01e2\5w<\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e7\5{>\2\u01e7\u01e8\bF\6\2\u01e8\u008c")
        buf.write("\3\2\2\2\32\2\u0150\u0156\u015e\u0163\u0168\u016c\u0173")
        buf.write("\u0175\u017c\u0183\u018a\u0190\u0197\u01a1\u01a4\u01a9")
        buf.write("\u01b0\u01b9\u01bb\u01c9\u01d5\u01db\u01e3\7\3@\2\b\2")
        buf.write("\2\3D\3\3E\4\3F\5")
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
    DOT = 21
    COLONASSIGN = 22
    COLON = 23
    LT = 24
    LE = 25
    GT = 26
    GE = 27
    EQ = 28
    NE = 29
    ASSIGN = 30
    ADD_ASSIGN = 31
    SUB_ASSIGN = 32
    MUL_ASSIGN = 33
    DIV_ASSIGN = 34
    MOD_ASSIGN = 35
    AND = 36
    OR = 37
    NOT = 38
    ADD = 39
    SUB = 40
    MUL = 41
    DIV = 42
    MOD = 43
    LPAREN = 44
    RPAREN = 45
    LBRACE = 46
    RBRACE = 47
    LBRACKET = 48
    RBRACKET = 49
    SEMICOLON = 50
    COMMA = 51
    ID = 52
    FLOAT_LIT = 53
    INT_DEC = 54
    INT_BIN = 55
    INT_OCT = 56
    INT_HEX = 57
    STRING_LIT = 58
    BOOLEAN_LIT = 59
    NEWLINE = 60
    WS = 61
    COMMENTS = 62
    COMMENTS_LINE = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'.'", "':='", "':'", "'<'", "'<='", "'>'", 
            "'>='", "'=='", "'!='", "'='", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", 
            "COLON", "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", 
            "OR", "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", 
            "ID", "FLOAT_LIT", "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", 
            "STRING_LIT", "BOOLEAN_LIT", "NEWLINE", "WS", "COMMENTS", "COMMENTS_LINE", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "DOT", "COLONASSIGN", "COLON", "LT", "LE", "GT", "GE", 
                  "EQ", "NE", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", "NOT", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", 
                  "ID", "FLOAT_LIT", "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", 
                  "STRING_LIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "BOOLEAN_LIT", 
                  "NEWLINE", "WS", "COMMENTS", "COMMENTS_LINE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    prevtoken = None
    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            self.prevtoken = result;
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            self.prevtoken = result;
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            self.prevtoken = result;
            raise ErrorToken(result.text); 
        else:
            result = super().emit()
            self.prevtoken = result
            return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.NEWLINE_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.prevtoken is not None and self.prevtoken.type in {
                    self.ID, self.RPAREN, self.RBRACKET, self.RBRACE,
                    self.INT_DEC, self.INT_BIN, self.INT_OCT, self.INT_HEX,
                    self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT,
                    self.RETURN, self.CONTINUE, self.BREAK,
                    self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.NIL
                }:
                    self.text = ";"
                    self.type = self.SEMICOLON
                    
                else:
                    self.skip()
                    

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[0:-1])
                else:
                    raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[0:])

     


