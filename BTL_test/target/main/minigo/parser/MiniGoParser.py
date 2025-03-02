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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u027b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3o\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3z\n\3\5\3|\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0090")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u009d")
        buf.write("\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a6\n\7\3\7\3\7")
        buf.write("\5\7\u00aa\n\7\3\b\3\b\3\b\3\b\5\b\u00b0\n\b\3\b\3\b\5")
        buf.write("\b\u00b4\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00bd\n\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00c6\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00ce\n\f\3\f\3\f\5\f\u00d2\n\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00dc\n\r\3\r\3\r")
        buf.write("\5\r\u00e0\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00f1\n\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0100\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u0108\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u0113\n\22\3\22\3\22\3\22\3\22\5\22\u0119")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u0129\n\24\7\24\u012b\n\24\f")
        buf.write("\24\16\24\u012e\13\24\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u013d\n\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u0145\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u015b\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u0166")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0183\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u018c\n\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u019a\n\35\3\36\3\36\3\36\3\36\5\36\u01a0\n\36\3\36\3")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u01ad\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u01bd\n\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\5$\u01cf\n$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\5$\u01df\n$\5$\u01e1\n$\3%\3%\3%\3%\3")
        buf.write("%\3%\5%\u01e9\n%\3&\3&\3&\3&\5&\u01ef\n&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01fd\n\'\3(\3(\3")
        buf.write("(\3(\3(\3(\7(\u0205\n(\f(\16(\u0208\13(\3)\3)\3)\3)\3")
        buf.write(")\3)\7)\u0210\n)\f)\16)\u0213\13)\3*\3*\3*\3*\3*\3*\7")
        buf.write("*\u021b\n*\f*\16*\u021e\13*\3+\3+\3+\3+\3+\3+\7+\u0226")
        buf.write("\n+\f+\16+\u0229\13+\3,\3,\3,\3,\3,\3,\7,\u0231\n,\f,")
        buf.write("\16,\u0234\13,\3-\3-\3-\5-\u0239\n-\3.\3.\3.\3.\3.\3.")
        buf.write("\3.\5.\u0242\n.\3.\3.\3.\3.\5.\u0248\n.\7.\u024a\n.\f")
        buf.write(".\16.\u024d\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\5/\u0260\n/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u0268\n\60\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u0270")
        buf.write("\n\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u0279\n")
        buf.write("\62\3\62\2\t&NPRTVZ\63\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\b")
        buf.write("\5\2\30\30\36\36!%\4\2\66\668;\3\2\32\37\3\2)*\3\2+-\4")
        buf.write("\2((**\2\u02b5\2d\3\2\2\2\4{\3\2\2\2\6}\3\2\2\2\b\u008f")
        buf.write("\3\2\2\2\n\u0091\3\2\2\2\f\u00a9\3\2\2\2\16\u00ab\3\2")
        buf.write("\2\2\20\u00bc\3\2\2\2\22\u00be\3\2\2\2\24\u00c5\3\2\2")
        buf.write("\2\26\u00c7\3\2\2\2\30\u00d5\3\2\2\2\32\u00e1\3\2\2\2")
        buf.write("\34\u00e7\3\2\2\2\36\u00ec\3\2\2\2 \u00ff\3\2\2\2\"\u0118")
        buf.write("\3\2\2\2$\u011a\3\2\2\2&\u011e\3\2\2\2(\u012f\3\2\2\2")
        buf.write("*\u0133\3\2\2\2,\u015a\3\2\2\2.\u015c\3\2\2\2\60\u0162")
        buf.write("\3\2\2\2\62\u016f\3\2\2\2\64\u017a\3\2\2\2\66\u0184\3")
        buf.write("\2\2\28\u0199\3\2\2\2:\u019b\3\2\2\2<\u01ac\3\2\2\2>\u01ae")
        buf.write("\3\2\2\2@\u01b1\3\2\2\2B\u01bc\3\2\2\2D\u01be\3\2\2\2")
        buf.write("F\u01e0\3\2\2\2H\u01e8\3\2\2\2J\u01ea\3\2\2\2L\u01fc\3")
        buf.write("\2\2\2N\u01fe\3\2\2\2P\u0209\3\2\2\2R\u0214\3\2\2\2T\u021f")
        buf.write("\3\2\2\2V\u022a\3\2\2\2X\u0238\3\2\2\2Z\u023a\3\2\2\2")
        buf.write("\\\u025f\3\2\2\2^\u0261\3\2\2\2`\u026b\3\2\2\2b\u0278")
        buf.write("\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3\3\2\2\2go\5> \2ho\5\26")
        buf.write("\f\2io\5\32\16\2jo\5\36\20\2ko\5\6\4\2lo\5\n\6\2mo\5\66")
        buf.write("\34\2ng\3\2\2\2nh\3\2\2\2ni\3\2\2\2nj\3\2\2\2nk\3\2\2")
        buf.write("\2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2pq\5\4\3\2q|\3\2\2\2r")
        buf.write("z\5> \2sz\5\26\f\2tz\5\32\16\2uz\5\36\20\2vz\5\6\4\2w")
        buf.write("z\5\n\6\2xz\5\66\34\2yr\3\2\2\2ys\3\2\2\2yt\3\2\2\2yu")
        buf.write("\3\2\2\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2\2z|\3\2\2\2{n\3\2")
        buf.write("\2\2{y\3\2\2\2|\5\3\2\2\2}~\7\b\2\2~\177\7\66\2\2\177")
        buf.write("\u0080\7\t\2\2\u0080\u0081\7\60\2\2\u0081\u0082\5\b\5")
        buf.write("\2\u0082\u0083\7\61\2\2\u0083\u0084\7\64\2\2\u0084\7\3")
        buf.write("\2\2\2\u0085\u0086\7\66\2\2\u0086\u0087\5H%\2\u0087\u0088")
        buf.write("\7\64\2\2\u0088\u0089\3\2\2\2\u0089\u008a\5\b\5\2\u008a")
        buf.write("\u0090\3\2\2\2\u008b\u008c\7\66\2\2\u008c\u008d\5H%\2")
        buf.write("\u008d\u008e\7\64\2\2\u008e\u0090\3\2\2\2\u008f\u0085")
        buf.write("\3\2\2\2\u008f\u008b\3\2\2\2\u0090\t\3\2\2\2\u0091\u0092")
        buf.write("\7\b\2\2\u0092\u0093\7\66\2\2\u0093\u0094\7\n\2\2\u0094")
        buf.write("\u0095\7\60\2\2\u0095\u0096\5\f\7\2\u0096\u0097\7\61\2")
        buf.write("\2\u0097\u0098\7\64\2\2\u0098\13\3\2\2\2\u0099\u009c\5")
        buf.write("\16\b\2\u009a\u009d\5H%\2\u009b\u009d\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\7\64\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\5\f\7")
        buf.write("\2\u00a1\u00aa\3\2\2\2\u00a2\u00a5\5\16\b\2\u00a3\u00a6")
        buf.write("\5H%\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7\64\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u0099\3\2\2\2\u00a9\u00a2\3\2\2\2")
        buf.write("\u00aa\r\3\2\2\2\u00ab\u00ac\7\66\2\2\u00ac\u00af\7.\2")
        buf.write("\2\u00ad\u00b0\5\20\t\2\u00ae\u00b0\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00b4\5H%\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7/\2\2")
        buf.write("\u00b6\17\3\2\2\2\u00b7\u00b8\5\22\n\2\u00b8\u00b9\7\65")
        buf.write("\2\2\u00b9\u00ba\5\20\t\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd")
        buf.write("\5\22\n\2\u00bc\u00b7\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\21\3\2\2\2\u00be\u00bf\5\24\13\2\u00bf\u00c0\5H%\2\u00c0")
        buf.write("\23\3\2\2\2\u00c1\u00c2\7\66\2\2\u00c2\u00c3\7\65\2\2")
        buf.write("\u00c3\u00c6\5\24\13\2\u00c4\u00c6\7\66\2\2\u00c5\u00c1")
        buf.write("\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\25\3\2\2\2\u00c7\u00c8")
        buf.write("\7\20\2\2\u00c8\u00d1\7\66\2\2\u00c9\u00cd\5H%\2\u00ca")
        buf.write("\u00cb\7 \2\2\u00cb\u00ce\5N(\2\u00cc\u00ce\3\2\2\2\u00cd")
        buf.write("\u00ca\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d2\3\2\2\2")
        buf.write("\u00cf\u00d0\7 \2\2\u00d0\u00d2\5N(\2\u00d1\u00c9\3\2")
        buf.write("\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\7\64\2\2\u00d4\27\3\2\2\2\u00d5\u00d6\7\20\2\2\u00d6")
        buf.write("\u00df\7\66\2\2\u00d7\u00db\5H%\2\u00d8\u00d9\7 \2\2\u00d9")
        buf.write("\u00dc\5N(\2\u00da\u00dc\3\2\2\2\u00db\u00d8\3\2\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\u00e0\3\2\2\2\u00dd\u00de\7 \2\2")
        buf.write("\u00de\u00e0\5N(\2\u00df\u00d7\3\2\2\2\u00df\u00dd\3\2")
        buf.write("\2\2\u00e0\31\3\2\2\2\u00e1\u00e2\7\17\2\2\u00e2\u00e3")
        buf.write("\7\66\2\2\u00e3\u00e4\7 \2\2\u00e4\u00e5\5N(\2\u00e5\u00e6")
        buf.write("\7\64\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\7\17\2\2\u00e8")
        buf.write("\u00e9\7\66\2\2\u00e9\u00ea\7 \2\2\u00ea\u00eb\5N(\2\u00eb")
        buf.write("\35\3\2\2\2\u00ec\u00ed\7\7\2\2\u00ed\u00f0\5:\36\2\u00ee")
        buf.write("\u00f1\5H%\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7\60\2")
        buf.write("\2\u00f3\u00f4\5\"\22\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6")
        buf.write("\7\64\2\2\u00f6\37\3\2\2\2\u00f7\u00f8\7\66\2\2\u00f8")
        buf.write("\u00f9\5H%\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7\65\2\2")
        buf.write("\u00fb\u00fc\5 \21\2\u00fc\u0100\3\2\2\2\u00fd\u00fe\7")
        buf.write("\66\2\2\u00fe\u0100\5H%\2\u00ff\u00f7\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u0100!\3\2\2\2\u0101\u0113\5$\23\2\u0102\u0113")
        buf.write("\5*\26\2\u0103\u0107\7\6\2\2\u0104\u0108\5`\61\2\u0105")
        buf.write("\u0108\5N(\2\u0106\u0108\3\2\2\2\u0107\u0104\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108\u0113\3\2\2\2")
        buf.write("\u0109\u0113\5\30\r\2\u010a\u0113\5\34\17\2\u010b\u0113")
        buf.write("\5.\30\2\u010c\u0113\5\60\31\2\u010d\u0113\5\62\32\2\u010e")
        buf.write("\u0113\5`\61\2\u010f\u0113\5^\60\2\u0110\u0113\7\22\2")
        buf.write("\2\u0111\u0113\7\21\2\2\u0112\u0101\3\2\2\2\u0112\u0102")
        buf.write("\3\2\2\2\u0112\u0103\3\2\2\2\u0112\u0109\3\2\2\2\u0112")
        buf.write("\u010a\3\2\2\2\u0112\u010b\3\2\2\2\u0112\u010c\3\2\2\2")
        buf.write("\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0112\u010f\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0115\7\64\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0119\5\"\22\2\u0117\u0119\3\2\2\2\u0118\u0112\3\2\2")
        buf.write("\2\u0118\u0117\3\2\2\2\u0119#\3\2\2\2\u011a\u011b\5&\24")
        buf.write("\2\u011b\u011c\t\2\2\2\u011c\u011d\5N(\2\u011d%\3\2\2")
        buf.write("\2\u011e\u011f\b\24\1\2\u011f\u0120\7\66\2\2\u0120\u012c")
        buf.write("\3\2\2\2\u0121\u0128\f\4\2\2\u0122\u0123\7\27\2\2\u0123")
        buf.write("\u0129\7\66\2\2\u0124\u0125\7\62\2\2\u0125\u0126\5N(\2")
        buf.write("\u0126\u0127\7\63\2\2\u0127\u0129\3\2\2\2\u0128\u0122")
        buf.write("\3\2\2\2\u0128\u0124\3\2\2\2\u0129\u012b\3\2\2\2\u012a")
        buf.write("\u0121\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\'\3\2\2\2\u012e\u012c\3\2\2")
        buf.write("\2\u012f\u0130\7\66\2\2\u0130\u0131\t\2\2\2\u0131\u0132")
        buf.write("\5N(\2\u0132)\3\2\2\2\u0133\u0134\7\3\2\2\u0134\u0135")
        buf.write("\7.\2\2\u0135\u0136\5N(\2\u0136\u0137\7/\2\2\u0137\u0138")
        buf.write("\7\60\2\2\u0138\u0139\5\"\22\2\u0139\u013c\7\61\2\2\u013a")
        buf.write("\u013d\5,\27\2\u013b\u013d\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d\u0144\3\2\2\2\u013e\u013f\7")
        buf.write("\4\2\2\u013f\u0140\7\60\2\2\u0140\u0141\5\"\22\2\u0141")
        buf.write("\u0142\7\61\2\2\u0142\u0145\3\2\2\2\u0143\u0145\3\2\2")
        buf.write("\2\u0144\u013e\3\2\2\2\u0144\u0143\3\2\2\2\u0145+\3\2")
        buf.write("\2\2\u0146\u0147\7\4\2\2\u0147\u0148\7\3\2\2\u0148\u0149")
        buf.write("\7.\2\2\u0149\u014a\5N(\2\u014a\u014b\7/\2\2\u014b\u014c")
        buf.write("\7\60\2\2\u014c\u014d\5\"\22\2\u014d\u014e\7\61\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\5,\27\2\u0150\u015b\3\2\2\2")
        buf.write("\u0151\u0152\7\4\2\2\u0152\u0153\7\3\2\2\u0153\u0154\7")
        buf.write(".\2\2\u0154\u0155\5N(\2\u0155\u0156\7/\2\2\u0156\u0157")
        buf.write("\7\60\2\2\u0157\u0158\5\"\22\2\u0158\u0159\7\61\2\2\u0159")
        buf.write("\u015b\3\2\2\2\u015a\u0146\3\2\2\2\u015a\u0151\3\2\2\2")
        buf.write("\u015b-\3\2\2\2\u015c\u015d\7\5\2\2\u015d\u015e\5N(\2")
        buf.write("\u015e\u015f\7\60\2\2\u015f\u0160\5\"\22\2\u0160\u0161")
        buf.write("\7\61\2\2\u0161/\3\2\2\2\u0162\u0165\7\5\2\2\u0163\u0166")
        buf.write("\5(\25\2\u0164\u0166\5\64\33\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\7\64\2")
        buf.write("\2\u0168\u0169\5N(\2\u0169\u016a\7\64\2\2\u016a\u016b")
        buf.write("\5(\25\2\u016b\u016c\7\60\2\2\u016c\u016d\5\"\22\2\u016d")
        buf.write("\u016e\7\61\2\2\u016e\61\3\2\2\2\u016f\u0170\7\5\2\2\u0170")
        buf.write("\u0171\7\66\2\2\u0171\u0172\7\65\2\2\u0172\u0173\7\66")
        buf.write("\2\2\u0173\u0174\7\30\2\2\u0174\u0175\7\23\2\2\u0175\u0176")
        buf.write("\5N(\2\u0176\u0177\7\60\2\2\u0177\u0178\5\"\22\2\u0178")
        buf.write("\u0179\7\61\2\2\u0179\63\3\2\2\2\u017a\u017b\7\20\2\2")
        buf.write("\u017b\u0182\7\66\2\2\u017c\u017d\5H%\2\u017d\u017e\7")
        buf.write(" \2\2\u017e\u017f\5N(\2\u017f\u0183\3\2\2\2\u0180\u0181")
        buf.write("\7 \2\2\u0181\u0183\5N(\2\u0182\u017c\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0183\65\3\2\2\2\u0184\u0185\7\7\2\2\u0185\u0186")
        buf.write("\7.\2\2\u0186\u0187\58\35\2\u0187\u0188\7/\2\2\u0188\u018b")
        buf.write("\5:\36\2\u0189\u018c\5H%\2\u018a\u018c\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("\u018e\7\60\2\2\u018e\u018f\5\"\22\2\u018f\u0190\7\61")
        buf.write("\2\2\u0190\u0191\7\64\2\2\u0191\67\3\2\2\2\u0192\u0193")
        buf.write("\7\66\2\2\u0193\u0194\7\66\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("\u0196\7\65\2\2\u0196\u019a\58\35\2\u0197\u0198\7\66\2")
        buf.write("\2\u0198\u019a\7\66\2\2\u0199\u0192\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a9\3\2\2\2\u019b\u019c\7\66\2\2\u019c\u019f")
        buf.write("\7.\2\2\u019d\u01a0\5<\37\2\u019e\u01a0\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a2\7/\2\2\u01a2;\3\2\2\2\u01a3\u01a4\5\24\13")
        buf.write("\2\u01a4\u01a5\5H%\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\7")
        buf.write("\65\2\2\u01a7\u01a8\5<\37\2\u01a8\u01ad\3\2\2\2\u01a9")
        buf.write("\u01aa\5\24\13\2\u01aa\u01ab\5H%\2\u01ab\u01ad\3\2\2\2")
        buf.write("\u01ac\u01a3\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ad=\3\2\2")
        buf.write("\2\u01ae\u01af\5@!\2\u01af\u01b0\5D#\2\u01b0?\3\2\2\2")
        buf.write("\u01b1\u01b2\5B\"\2\u01b2\u01b3\5H%\2\u01b3A\3\2\2\2\u01b4")
        buf.write("\u01b5\7\62\2\2\u01b5\u01b6\t\3\2\2\u01b6\u01b7\7\63\2")
        buf.write("\2\u01b7\u01b8\3\2\2\2\u01b8\u01bd\5B\"\2\u01b9\u01ba")
        buf.write("\7\62\2\2\u01ba\u01bb\t\3\2\2\u01bb\u01bd\7\63\2\2\u01bc")
        buf.write("\u01b4\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bdC\3\2\2\2\u01be")
        buf.write("\u01bf\7\60\2\2\u01bf\u01c0\5F$\2\u01c0\u01c1\7\61\2\2")
        buf.write("\u01c1E\3\2\2\2\u01c2\u01cf\7\25\2\2\u01c3\u01cf\7\26")
        buf.write("\2\2\u01c4\u01cf\7\24\2\2\u01c5\u01cf\7\67\2\2\u01c6\u01cf")
        buf.write("\78\2\2\u01c7\u01cf\79\2\2\u01c8\u01cf\7:\2\2\u01c9\u01cf")
        buf.write("\7;\2\2\u01ca\u01cf\7<\2\2\u01cb\u01cf\5J&\2\u01cc\u01cf")
        buf.write("\5D#\2\u01cd\u01cf\7\66\2\2\u01ce\u01c2\3\2\2\2\u01ce")
        buf.write("\u01c3\3\2\2\2\u01ce\u01c4\3\2\2\2\u01ce\u01c5\3\2\2\2")
        buf.write("\u01ce\u01c6\3\2\2\2\u01ce\u01c7\3\2\2\2\u01ce\u01c8\3")
        buf.write("\2\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca\3\2\2\2\u01ce\u01cb")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d1\7\65\2\2\u01d1\u01e1\5F$\2")
        buf.write("\u01d2\u01df\7\25\2\2\u01d3\u01df\7\26\2\2\u01d4\u01df")
        buf.write("\7\24\2\2\u01d5\u01df\7\67\2\2\u01d6\u01df\78\2\2\u01d7")
        buf.write("\u01df\79\2\2\u01d8\u01df\7:\2\2\u01d9\u01df\7;\2\2\u01da")
        buf.write("\u01df\7<\2\2\u01db\u01df\5J&\2\u01dc\u01df\5D#\2\u01dd")
        buf.write("\u01df\7\66\2\2\u01de\u01d2\3\2\2\2\u01de\u01d3\3\2\2")
        buf.write("\2\u01de\u01d4\3\2\2\2\u01de\u01d5\3\2\2\2\u01de\u01d6")
        buf.write("\3\2\2\2\u01de\u01d7\3\2\2\2\u01de\u01d8\3\2\2\2\u01de")
        buf.write("\u01d9\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e1\3")
        buf.write("\2\2\2\u01e0\u01ce\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1G")
        buf.write("\3\2\2\2\u01e2\u01e9\7\66\2\2\u01e3\u01e9\7\f\2\2\u01e4")
        buf.write("\u01e9\7\r\2\2\u01e5\u01e9\7\16\2\2\u01e6\u01e9\7\13\2")
        buf.write("\2\u01e7\u01e9\5@!\2\u01e8\u01e2\3\2\2\2\u01e8\u01e3\3")
        buf.write("\2\2\2\u01e8\u01e4\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9I\3\2\2\2\u01ea\u01eb")
        buf.write("\7\66\2\2\u01eb\u01ee\7\60\2\2\u01ec\u01ef\5L\'\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2")
        buf.write("\u01ef\u01f0\3\2\2\2\u01f0\u01f1\7\61\2\2\u01f1K\3\2\2")
        buf.write("\2\u01f2\u01f3\7\66\2\2\u01f3\u01f4\7\31\2\2\u01f4\u01f5")
        buf.write("\5N(\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\7\65\2\2\u01f7")
        buf.write("\u01f8\5L\'\2\u01f8\u01fd\3\2\2\2\u01f9\u01fa\7\66\2\2")
        buf.write("\u01fa\u01fb\7\31\2\2\u01fb\u01fd\5N(\2\u01fc\u01f2\3")
        buf.write("\2\2\2\u01fc\u01f9\3\2\2\2\u01fdM\3\2\2\2\u01fe\u01ff")
        buf.write("\b(\1\2\u01ff\u0200\5P)\2\u0200\u0206\3\2\2\2\u0201\u0202")
        buf.write("\f\4\2\2\u0202\u0203\7\'\2\2\u0203\u0205\5P)\2\u0204\u0201")
        buf.write("\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207O\3\2\2\2\u0208\u0206\3\2\2\2\u0209")
        buf.write("\u020a\b)\1\2\u020a\u020b\5R*\2\u020b\u0211\3\2\2\2\u020c")
        buf.write("\u020d\f\4\2\2\u020d\u020e\7&\2\2\u020e\u0210\5R*\2\u020f")
        buf.write("\u020c\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212Q\3\2\2\2\u0213\u0211\3\2\2")
        buf.write("\2\u0214\u0215\b*\1\2\u0215\u0216\5T+\2\u0216\u021c\3")
        buf.write("\2\2\2\u0217\u0218\f\4\2\2\u0218\u0219\t\4\2\2\u0219\u021b")
        buf.write("\5T+\2\u021a\u0217\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021dS\3\2\2\2\u021e\u021c")
        buf.write("\3\2\2\2\u021f\u0220\b+\1\2\u0220\u0221\5V,\2\u0221\u0227")
        buf.write("\3\2\2\2\u0222\u0223\f\4\2\2\u0223\u0224\t\5\2\2\u0224")
        buf.write("\u0226\5V,\2\u0225\u0222\3\2\2\2\u0226\u0229\3\2\2\2\u0227")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228U\3\2\2\2\u0229")
        buf.write("\u0227\3\2\2\2\u022a\u022b\b,\1\2\u022b\u022c\5X-\2\u022c")
        buf.write("\u0232\3\2\2\2\u022d\u022e\f\4\2\2\u022e\u022f\t\6\2\2")
        buf.write("\u022f\u0231\5X-\2\u0230\u022d\3\2\2\2\u0231\u0234\3\2")
        buf.write("\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233W\3")
        buf.write("\2\2\2\u0234\u0232\3\2\2\2\u0235\u0236\t\7\2\2\u0236\u0239")
        buf.write("\5X-\2\u0237\u0239\5Z.\2\u0238\u0235\3\2\2\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239Y\3\2\2\2\u023a\u023b\b.\1\2\u023b\u023c")
        buf.write("\5\\/\2\u023c\u024b\3\2\2\2\u023d\u0247\f\4\2\2\u023e")
        buf.write("\u0241\7\27\2\2\u023f\u0242\7\66\2\2\u0240\u0242\5`\61")
        buf.write("\2\u0241\u023f\3\2\2\2\u0241\u0240\3\2\2\2\u0242\u0248")
        buf.write("\3\2\2\2\u0243\u0244\7\62\2\2\u0244\u0245\5N(\2\u0245")
        buf.write("\u0246\7\63\2\2\u0246\u0248\3\2\2\2\u0247\u023e\3\2\2")
        buf.write("\2\u0247\u0243\3\2\2\2\u0248\u024a\3\2\2\2\u0249\u023d")
        buf.write("\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c[\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u0260\7\66\2\2\u024f\u0260\78\2\2\u0250\u0260\79\2\2")
        buf.write("\u0251\u0260\7:\2\2\u0252\u0260\7;\2\2\u0253\u0260\7\67")
        buf.write("\2\2\u0254\u0255\7.\2\2\u0255\u0256\5N(\2\u0256\u0257")
        buf.write("\7/\2\2\u0257\u0260\3\2\2\2\u0258\u0260\5`\61\2\u0259")
        buf.write("\u0260\7<\2\2\u025a\u0260\5J&\2\u025b\u0260\5> \2\u025c")
        buf.write("\u0260\7\25\2\2\u025d\u0260\7\26\2\2\u025e\u0260\7\24")
        buf.write("\2\2\u025f\u024e\3\2\2\2\u025f\u024f\3\2\2\2\u025f\u0250")
        buf.write("\3\2\2\2\u025f\u0251\3\2\2\2\u025f\u0252\3\2\2\2\u025f")
        buf.write("\u0253\3\2\2\2\u025f\u0254\3\2\2\2\u025f\u0258\3\2\2\2")
        buf.write("\u025f\u0259\3\2\2\2\u025f\u025a\3\2\2\2\u025f\u025b\3")
        buf.write("\2\2\2\u025f\u025c\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u025e")
        buf.write("\3\2\2\2\u0260]\3\2\2\2\u0261\u0262\5&\24\2\u0262\u0263")
        buf.write("\7\27\2\2\u0263\u0264\7\66\2\2\u0264\u0267\7.\2\2\u0265")
        buf.write("\u0268\5b\62\2\u0266\u0268\3\2\2\2\u0267\u0265\3\2\2\2")
        buf.write("\u0267\u0266\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a\7")
        buf.write("/\2\2\u026a_\3\2\2\2\u026b\u026c\7\66\2\2\u026c\u026f")
        buf.write("\7.\2\2\u026d\u0270\5b\62\2\u026e\u0270\3\2\2\2\u026f")
        buf.write("\u026d\3\2\2\2\u026f\u026e\3\2\2\2\u0270\u0271\3\2\2\2")
        buf.write("\u0271\u0272\7/\2\2\u0272a\3\2\2\2\u0273\u0274\5N(\2\u0274")
        buf.write("\u0275\7\65\2\2\u0275\u0276\5b\62\2\u0276\u0279\3\2\2")
        buf.write("\2\u0277\u0279\5N(\2\u0278\u0273\3\2\2\2\u0278\u0277\3")
        buf.write("\2\2\2\u0279c\3\2\2\2\65ny{\u008f\u009c\u00a5\u00a9\u00af")
        buf.write("\u00b3\u00bc\u00c5\u00cd\u00d1\u00db\u00df\u00f0\u00ff")
        buf.write("\u0107\u0112\u0118\u0128\u012c\u013c\u0144\u015a\u0165")
        buf.write("\u0182\u018b\u0199\u019f\u01ac\u01bc\u01ce\u01de\u01e0")
        buf.write("\u01e8\u01ee\u01fc\u0206\u0211\u021c\u0227\u0232\u0238")
        buf.write("\u0241\u0247\u024b\u025f\u0267\u026f\u0278")
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
                     "'false'", "'.'", "':='", "':'", "'<'", "'<='", "'>'", 
                     "'>='", "'=='", "'!='", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "'&&'", "'||'", "'!'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", "COLON", 
                      "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "AND", "OR", "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "SEMICOLON", "COMMA", "ID", "FLOAT_LIT", 
                      "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", "STRING_LIT", 
                      "BOOLEAN_LIT", "NEWLINE", "WS", "COMMENTS", "COMMENTS_LINE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declaration = 1
    RULE_struct_type = 2
    RULE_data_struct = 3
    RULE_interface_type = 4
    RULE_data_inter = 5
    RULE_initialize_inter = 6
    RULE_list_interface = 7
    RULE_data_inter_thamso_list = 8
    RULE_data_inter_thamso = 9
    RULE_global_variable = 10
    RULE_local_variable = 11
    RULE_global_constant = 12
    RULE_local_constant = 13
    RULE_function = 14
    RULE_data_func = 15
    RULE_body_func = 16
    RULE_assignment_func = 17
    RULE_dot = 18
    RULE_assignment_for = 19
    RULE_if_else = 20
    RULE_else_if = 21
    RULE_for_basic = 22
    RULE_for_icu = 23
    RULE_for_range = 24
    RULE_var_for = 25
    RULE_struct_func = 26
    RULE_method = 27
    RULE_func_call_str = 28
    RULE_func_call_thamso_str = 29
    RULE_array_literal = 30
    RULE_type_array = 31
    RULE_list_type_arr = 32
    RULE_list_expr = 33
    RULE_data_list_expr = 34
    RULE_type_data = 35
    RULE_struct_literal = 36
    RULE_list_elements = 37
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_expr3 = 41
    RULE_expr4 = 42
    RULE_expr5 = 43
    RULE_expr6 = 44
    RULE_expr7 = 45
    RULE_call_statement = 46
    RULE_func_call = 47
    RULE_func_call_thamso = 48

    ruleNames =  [ "program", "list_declaration", "struct_type", "data_struct", 
                   "interface_type", "data_inter", "initialize_inter", "list_interface", 
                   "data_inter_thamso_list", "data_inter_thamso", "global_variable", 
                   "local_variable", "global_constant", "local_constant", 
                   "function", "data_func", "body_func", "assignment_func", 
                   "dot", "assignment_for", "if_else", "else_if", "for_basic", 
                   "for_icu", "for_range", "var_for", "struct_func", "method", 
                   "func_call_str", "func_call_thamso_str", "array_literal", 
                   "type_array", "list_type_arr", "list_expr", "data_list_expr", 
                   "type_data", "struct_literal", "list_elements", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "call_statement", "func_call", "func_call_thamso" ]

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
    DOT=21
    COLONASSIGN=22
    COLON=23
    LT=24
    LE=25
    GT=26
    GE=27
    EQ=28
    NE=29
    ASSIGN=30
    ADD_ASSIGN=31
    SUB_ASSIGN=32
    MUL_ASSIGN=33
    DIV_ASSIGN=34
    MOD_ASSIGN=35
    AND=36
    OR=37
    NOT=38
    ADD=39
    SUB=40
    MUL=41
    DIV=42
    MOD=43
    LPAREN=44
    RPAREN=45
    LBRACE=46
    RBRACE=47
    LBRACKET=48
    RBRACKET=49
    SEMICOLON=50
    COMMA=51
    ID=52
    FLOAT_LIT=53
    INT_DEC=54
    INT_BIN=55
    INT_OCT=56
    INT_HEX=57
    STRING_LIT=58
    BOOLEAN_LIT=59
    NEWLINE=60
    WS=61
    COMMENTS=62
    COMMENTS_LINE=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

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
            self.state = 98
            self.list_declaration()
            self.state = 99
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

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def global_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Global_variableContext,0)


        def global_constant(self):
            return self.getTypedRuleContext(MiniGoParser.Global_constantContext,0)


        def function(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def struct_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_funcContext,0)


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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 101
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 102
                    self.global_variable()
                    pass

                elif la_ == 3:
                    self.state = 103
                    self.global_constant()
                    pass

                elif la_ == 4:
                    self.state = 104
                    self.function()
                    pass

                elif la_ == 5:
                    self.state = 105
                    self.struct_type()
                    pass

                elif la_ == 6:
                    self.state = 106
                    self.interface_type()
                    pass

                elif la_ == 7:
                    self.state = 107
                    self.struct_func()
                    pass


                self.state = 110
                self.list_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 112
                    self.array_literal()
                    pass

                elif la_ == 2:
                    self.state = 113
                    self.global_variable()
                    pass

                elif la_ == 3:
                    self.state = 114
                    self.global_constant()
                    pass

                elif la_ == 4:
                    self.state = 115
                    self.function()
                    pass

                elif la_ == 5:
                    self.state = 116
                    self.struct_type()
                    pass

                elif la_ == 6:
                    self.state = 117
                    self.interface_type()
                    pass

                elif la_ == 7:
                    self.state = 118
                    self.struct_func()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniGoParser.TYPE)
            self.state = 124
            self.match(MiniGoParser.ID)
            self.state = 125
            self.match(MiniGoParser.STRUCT)
            self.state = 126
            self.match(MiniGoParser.LBRACE)
            self.state = 127
            self.data_struct()
            self.state = 128
            self.match(MiniGoParser.RBRACE)

            self.state = 129
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_struct" ):
                return visitor.visitData_struct(self)
            else:
                return visitor.visitChildren(self)




    def data_struct(self):

        localctx = MiniGoParser.Data_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_struct)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(MiniGoParser.ID)
                self.state = 132
                self.type_data()

                self.state = 133
                self.match(MiniGoParser.SEMICOLON)
                self.state = 135
                self.data_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MiniGoParser.ID)
                self.state = 138
                self.type_data()

                self.state = 139
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Data_interContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MiniGoParser.TYPE)
            self.state = 144
            self.match(MiniGoParser.ID)
            self.state = 145
            self.match(MiniGoParser.INTERFACE)
            self.state = 146
            self.match(MiniGoParser.LBRACE)
            self.state = 147
            self.data_inter()
            self.state = 148
            self.match(MiniGoParser.RBRACE)

            self.state = 149
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Data_interContext,0)


        def initialize_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Initialize_interContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter" ):
                return visitor.visitData_inter(self)
            else:
                return visitor.visitChildren(self)




    def data_inter(self):

        localctx = MiniGoParser.Data_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_inter)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.initialize_inter()
                self.state = 154
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                    self.state = 152
                    self.type_data()
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 156
                self.match(MiniGoParser.SEMICOLON)
                self.state = 158
                self.data_inter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.initialize_inter()
                self.state = 163
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                    self.state = 161
                    self.type_data()
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 165
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initialize_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_interfaceContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialize_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialize_inter" ):
                return visitor.visitInitialize_inter(self)
            else:
                return visitor.visitChildren(self)




    def initialize_inter(self):

        localctx = MiniGoParser.Initialize_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initialize_inter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniGoParser.ID)
            self.state = 170
            self.match(MiniGoParser.LPAREN)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 171
                self.list_interface()
                pass

            elif la_ == 2:
                pass


            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 175
                self.type_data()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter_thamso_list(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamso_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface" ):
                return visitor.visitList_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_interface(self):

        localctx = MiniGoParser.List_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_interface)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.data_inter_thamso_list()
                self.state = 182
                self.match(MiniGoParser.COMMA)
                self.state = 183
                self.list_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.data_inter_thamso_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_inter_thamso_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter_thamso_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter_thamso_list" ):
                return visitor.visitData_inter_thamso_list(self)
            else:
                return visitor.visitChildren(self)




    def data_inter_thamso_list(self):

        localctx = MiniGoParser.Data_inter_thamso_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_inter_thamso_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.data_inter_thamso()
            self.state = 189
            self.type_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_inter_thamsoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_inter_thamso

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_inter_thamso" ):
                return visitor.visitData_inter_thamso(self)
            else:
                return visitor.visitChildren(self)




    def data_inter_thamso(self):

        localctx = MiniGoParser.Data_inter_thamsoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data_inter_thamso)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(MiniGoParser.ID)
                self.state = 192
                self.match(MiniGoParser.COMMA)
                self.state = 193
                self.data_inter_thamso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_variableContext(ParserRuleContext):
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

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_global_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_variable" ):
                return visitor.visitGlobal_variable(self)
            else:
                return visitor.visitChildren(self)




    def global_variable(self):

        localctx = MiniGoParser.Global_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_global_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MiniGoParser.VAR)
            self.state = 198
            self.match(MiniGoParser.ID)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 199
                self.type_data()
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 200
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 201
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 205
                self.match(MiniGoParser.ASSIGN)

                self.state = 206
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_local_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_variable" ):
                return visitor.visitLocal_variable(self)
            else:
                return visitor.visitChildren(self)




    def local_variable(self):

        localctx = MiniGoParser.Local_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_local_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.VAR)
            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 213
                self.type_data()
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 214
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 215
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 219
                self.match(MiniGoParser.ASSIGN)

                self.state = 220
                self.expr(0)
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


    class Global_constantContext(ParserRuleContext):
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_global_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_constant" ):
                return visitor.visitGlobal_constant(self)
            else:
                return visitor.visitChildren(self)




    def global_constant(self):

        localctx = MiniGoParser.Global_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_global_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MiniGoParser.CONST)
            self.state = 224
            self.match(MiniGoParser.ID)
            self.state = 225
            self.match(MiniGoParser.ASSIGN)

            self.state = 226
            self.expr(0)
            self.state = 227
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_constantContext(ParserRuleContext):
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_local_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_constant" ):
                return visitor.visitLocal_constant(self)
            else:
                return visitor.visitChildren(self)




    def local_constant(self):

        localctx = MiniGoParser.Local_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_local_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.CONST)
            self.state = 230
            self.match(MiniGoParser.ID)
            self.state = 231
            self.match(MiniGoParser.ASSIGN)

            self.state = 232
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def func_call_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_strContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MiniGoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.FUNC)
            self.state = 235
            self.func_call_str()
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 236
                self.type_data()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 240
            self.match(MiniGoParser.LBRACE)
            self.state = 241
            self.body_func()
            self.state = 242
            self.match(MiniGoParser.RBRACE)
            self.state = 243
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_func(self):
            return self.getTypedRuleContext(MiniGoParser.Data_funcContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_func" ):
                return visitor.visitData_func(self)
            else:
                return visitor.visitChildren(self)




    def data_func(self):

        localctx = MiniGoParser.Data_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_data_func)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(MiniGoParser.ID)
                self.state = 246
                self.type_data()
                self.state = 248
                self.match(MiniGoParser.COMMA)
                self.state = 249
                self.data_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(MiniGoParser.ID)
                self.state = 252
                self.type_data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def assignment_func(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_funcContext,0)


        def if_else(self):
            return self.getTypedRuleContext(MiniGoParser.If_elseContext,0)


        def local_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Local_variableContext,0)


        def local_constant(self):
            return self.getTypedRuleContext(MiniGoParser.Local_constantContext,0)


        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_icu(self):
            return self.getTypedRuleContext(MiniGoParser.For_icuContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_body_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_func" ):
                return visitor.visitBody_func(self)
            else:
                return visitor.visitChildren(self)




    def body_func(self):

        localctx = MiniGoParser.Body_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body_func)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 255
                    self.assignment_func()
                    pass

                elif la_ == 2:
                    self.state = 256
                    self.if_else()
                    pass

                elif la_ == 3:
                    self.state = 257
                    self.match(MiniGoParser.RETURN)
                    self.state = 261
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 258
                        self.func_call()
                        pass

                    elif la_ == 2:
                        self.state = 259
                        self.expr(0)
                        pass

                    elif la_ == 3:
                        pass


                    pass

                elif la_ == 4:
                    self.state = 263
                    self.local_variable()
                    pass

                elif la_ == 5:
                    self.state = 264
                    self.local_constant()
                    pass

                elif la_ == 6:
                    self.state = 265
                    self.for_basic()
                    pass

                elif la_ == 7:
                    self.state = 266
                    self.for_icu()
                    pass

                elif la_ == 8:
                    self.state = 267
                    self.for_range()
                    pass

                elif la_ == 9:
                    self.state = 268
                    self.func_call()
                    pass

                elif la_ == 10:
                    self.state = 269
                    self.call_statement()
                    pass

                elif la_ == 11:
                    self.state = 270
                    self.match(MiniGoParser.BREAK)
                    pass

                elif la_ == 12:
                    self.state = 271
                    self.match(MiniGoParser.CONTINUE)
                    pass


                self.state = 274
                self.match(MiniGoParser.SEMICOLON)
                self.state = 276
                self.body_func()
                pass
            elif token in [MiniGoParser.RBRACE]:
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


    class Assignment_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

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
            return MiniGoParser.RULE_assignment_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_func" ):
                return visitor.visitAssignment_func(self)
            else:
                return visitor.visitChildren(self)




    def assignment_func(self):

        localctx = MiniGoParser.Assignment_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.dot(0)

            self.state = 281
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLONASSIGN) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 282
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot" ):
                return visitor.visitDot(self)
            else:
                return visitor.visitChildren(self)



    def dot(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.DotContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_dot, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.DotContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dot)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 294
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 288
                        self.match(MiniGoParser.DOT)
                        self.state = 289
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 290
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 291
                        self.expr(0)
                        self.state = 292
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

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
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MiniGoParser.ID)

            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COLONASSIGN) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 303
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACE)
            else:
                return self.getToken(MiniGoParser.LBRACE, i)

        def body_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Body_funcContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Body_funcContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACE)
            else:
                return self.getToken(MiniGoParser.RBRACE, i)

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_else" ):
                return visitor.visitIf_else(self)
            else:
                return visitor.visitChildren(self)




    def if_else(self):

        localctx = MiniGoParser.If_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.IF)
            self.state = 306
            self.match(MiniGoParser.LPAREN)
            self.state = 307
            self.expr(0)
            self.state = 308
            self.match(MiniGoParser.RPAREN)
            self.state = 309
            self.match(MiniGoParser.LBRACE)
            self.state = 310
            self.body_func()
            self.state = 311
            self.match(MiniGoParser.RBRACE)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 312
                self.else_if()
                pass

            elif la_ == 2:
                pass


            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 316
                self.match(MiniGoParser.ELSE)
                self.state = 317
                self.match(MiniGoParser.LBRACE)
                self.state = 318
                self.body_func()
                self.state = 319
                self.match(MiniGoParser.RBRACE)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
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


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_if)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(MiniGoParser.ELSE)
                self.state = 325
                self.match(MiniGoParser.IF)
                self.state = 326
                self.match(MiniGoParser.LPAREN)
                self.state = 327
                self.expr(0)
                self.state = 328
                self.match(MiniGoParser.RPAREN)
                self.state = 329
                self.match(MiniGoParser.LBRACE)
                self.state = 330
                self.body_func()
                self.state = 331
                self.match(MiniGoParser.RBRACE)
                self.state = 333
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(MiniGoParser.ELSE)
                self.state = 336
                self.match(MiniGoParser.IF)
                self.state = 337
                self.match(MiniGoParser.LPAREN)
                self.state = 338
                self.expr(0)
                self.state = 339
                self.match(MiniGoParser.RPAREN)
                self.state = 340
                self.match(MiniGoParser.LBRACE)
                self.state = 341
                self.body_func()
                self.state = 342
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MiniGoParser.FOR)
            self.state = 347
            self.expr(0)
            self.state = 348
            self.match(MiniGoParser.LBRACE)
            self.state = 349
            self.body_func()
            self.state = 350
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_icuContext(ParserRuleContext):
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignment_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,i)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def var_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_icu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_icu" ):
                return visitor.visitFor_icu(self)
            else:
                return visitor.visitChildren(self)




    def for_icu(self):

        localctx = MiniGoParser.For_icuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_icu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MiniGoParser.FOR)
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 353
                self.assignment_for()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 354
                self.var_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 357
            self.match(MiniGoParser.SEMICOLON)
            self.state = 358
            self.expr(0)
            self.state = 359
            self.match(MiniGoParser.SEMICOLON)
            self.state = 360
            self.assignment_for()
            self.state = 361
            self.match(MiniGoParser.LBRACE)
            self.state = 362
            self.body_func()
            self.state = 363
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
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

        def COLONASSIGN(self):
            return self.getToken(MiniGoParser.COLONASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.FOR)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.match(MiniGoParser.COMMA)
            self.state = 368
            self.match(MiniGoParser.ID)
            self.state = 369
            self.match(MiniGoParser.COLONASSIGN)
            self.state = 370
            self.match(MiniGoParser.RANGE)
            self.state = 371
            self.expr(0)
            self.state = 372
            self.match(MiniGoParser.LBRACE)
            self.state = 373
            self.body_func()
            self.state = 374
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_for" ):
                return visitor.visitVar_for(self)
            else:
                return visitor.visitChildren(self)




    def var_for(self):

        localctx = MiniGoParser.Var_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_var_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MiniGoParser.VAR)
            self.state = 377
            self.match(MiniGoParser.ID)
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 378
                self.type_data()

                self.state = 379
                self.match(MiniGoParser.ASSIGN)

                self.state = 380
                self.expr(0)
                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 382
                self.match(MiniGoParser.ASSIGN)

                self.state = 383
                self.expr(0)
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


    class Struct_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_strContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def body_func(self):
            return self.getTypedRuleContext(MiniGoParser.Body_funcContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_func" ):
                return visitor.visitStruct_func(self)
            else:
                return visitor.visitChildren(self)




    def struct_func(self):

        localctx = MiniGoParser.Struct_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_struct_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MiniGoParser.FUNC)
            self.state = 387
            self.match(MiniGoParser.LPAREN)
            self.state = 388
            self.method()
            self.state = 389
            self.match(MiniGoParser.RPAREN)
            self.state = 390
            self.func_call_str()
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 391
                self.type_data()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 395
            self.match(MiniGoParser.LBRACE)
            self.state = 396
            self.body_func()
            self.state = 397
            self.match(MiniGoParser.RBRACE)
            self.state = 398
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(MiniGoParser.ID)
                self.state = 401
                self.match(MiniGoParser.ID)
                self.state = 403
                self.match(MiniGoParser.COMMA)
                self.state = 404
                self.method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(MiniGoParser.ID)
                self.state = 406
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_strContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamso_strContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_str

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_str" ):
                return visitor.visitFunc_call_str(self)
            else:
                return visitor.visitChildren(self)




    def func_call_str(self):

        localctx = MiniGoParser.Func_call_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_call_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.ID)
            self.state = 410
            self.match(MiniGoParser.LPAREN)
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 411
                self.func_call_thamso_str()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 415
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_thamso_strContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def func_call_thamso_str(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamso_strContext,0)


        def data_inter_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Data_inter_thamsoContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_thamso_str

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_thamso_str" ):
                return visitor.visitFunc_call_thamso_str(self)
            else:
                return visitor.visitChildren(self)




    def func_call_thamso_str(self):

        localctx = MiniGoParser.Func_call_thamso_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_call_thamso_str)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.data_inter_thamso()
                self.state = 418
                self.type_data()
                self.state = 420
                self.match(MiniGoParser.COMMA)
                self.state = 421
                self.func_call_thamso_str()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.data_inter_thamso()
                self.state = 424
                self.type_data()
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

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.type_array()
            self.state = 429
            self.list_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def type_data(self):
            return self.getTypedRuleContext(MiniGoParser.Type_dataContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.list_type_arr()

            self.state = 432
            self.type_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_type_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_type_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type_arr" ):
                return visitor.visitList_type_arr(self)
            else:
                return visitor.visitChildren(self)




    def list_type_arr(self):

        localctx = MiniGoParser.List_type_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_list_type_arr)
        self._la = 0 # Token type
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(MiniGoParser.LBRACKET)
                self.state = 435
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_DEC) | (1 << MiniGoParser.INT_BIN) | (1 << MiniGoParser.INT_OCT) | (1 << MiniGoParser.INT_HEX))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.match(MiniGoParser.RBRACKET)
                self.state = 438
                self.list_type_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(MiniGoParser.LBRACKET)
                self.state = 440
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_DEC) | (1 << MiniGoParser.INT_BIN) | (1 << MiniGoParser.INT_OCT) | (1 << MiniGoParser.INT_HEX))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 441
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Data_list_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_list_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.LBRACE)
            self.state = 445
            self.data_list_expr()
            self.state = 446
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_list_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Data_list_exprContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_list_expr" ):
                return visitor.visitData_list_expr(self)
            else:
                return visitor.visitChildren(self)




    def data_list_expr(self):

        localctx = MiniGoParser.Data_list_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_data_list_expr)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 448
                    self.match(MiniGoParser.TRUE)
                    pass

                elif la_ == 2:
                    self.state = 449
                    self.match(MiniGoParser.FALSE)
                    pass

                elif la_ == 3:
                    self.state = 450
                    self.match(MiniGoParser.NIL)
                    pass

                elif la_ == 4:
                    self.state = 451
                    self.match(MiniGoParser.FLOAT_LIT)
                    pass

                elif la_ == 5:
                    self.state = 452
                    self.match(MiniGoParser.INT_DEC)
                    pass

                elif la_ == 6:
                    self.state = 453
                    self.match(MiniGoParser.INT_BIN)
                    pass

                elif la_ == 7:
                    self.state = 454
                    self.match(MiniGoParser.INT_OCT)
                    pass

                elif la_ == 8:
                    self.state = 455
                    self.match(MiniGoParser.INT_HEX)
                    pass

                elif la_ == 9:
                    self.state = 456
                    self.match(MiniGoParser.STRING_LIT)
                    pass

                elif la_ == 10:
                    self.state = 457
                    self.struct_literal()
                    pass

                elif la_ == 11:
                    self.state = 458
                    self.list_expr()
                    pass

                elif la_ == 12:
                    self.state = 459
                    self.match(MiniGoParser.ID)
                    pass


                self.state = 462
                self.match(MiniGoParser.COMMA)
                self.state = 463
                self.data_list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 464
                    self.match(MiniGoParser.TRUE)
                    pass

                elif la_ == 2:
                    self.state = 465
                    self.match(MiniGoParser.FALSE)
                    pass

                elif la_ == 3:
                    self.state = 466
                    self.match(MiniGoParser.NIL)
                    pass

                elif la_ == 4:
                    self.state = 467
                    self.match(MiniGoParser.FLOAT_LIT)
                    pass

                elif la_ == 5:
                    self.state = 468
                    self.match(MiniGoParser.INT_DEC)
                    pass

                elif la_ == 6:
                    self.state = 469
                    self.match(MiniGoParser.INT_BIN)
                    pass

                elif la_ == 7:
                    self.state = 470
                    self.match(MiniGoParser.INT_OCT)
                    pass

                elif la_ == 8:
                    self.state = 471
                    self.match(MiniGoParser.INT_HEX)
                    pass

                elif la_ == 9:
                    self.state = 472
                    self.match(MiniGoParser.STRING_LIT)
                    pass

                elif la_ == 10:
                    self.state = 473
                    self.struct_literal()
                    pass

                elif la_ == 11:
                    self.state = 474
                    self.list_expr()
                    pass

                elif la_ == 12:
                    self.state = 475
                    self.match(MiniGoParser.ID)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_data" ):
                return visitor.visitType_data(self)
            else:
                return visitor.visitChildren(self)




    def type_data(self):

        localctx = MiniGoParser.Type_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_type_data)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 483
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 484
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 485
                self.type_array()
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


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.ID)
            self.state = 489
            self.match(MiniGoParser.LBRACE)
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 490
                self.list_elements()
                pass
            elif token in [MiniGoParser.RBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 494
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elements(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementsContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements" ):
                return visitor.visitList_elements(self)
            else:
                return visitor.visitChildren(self)




    def list_elements(self):

        localctx = MiniGoParser.List_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_elements)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.match(MiniGoParser.ID)
                self.state = 497
                self.match(MiniGoParser.COLON)
                self.state = 498
                self.expr(0)
                self.state = 500
                self.match(MiniGoParser.COMMA)
                self.state = 501
                self.list_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(MiniGoParser.ID)
                self.state = 504
                self.match(MiniGoParser.COLON)
                self.state = 505
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 516
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 511
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 512
                    self.match(MiniGoParser.OR)
                    self.state = 513
                    self.expr1(0) 
                self.state = 518
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 527
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 522
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 523
                    self.match(MiniGoParser.AND)
                    self.state = 524
                    self.expr2(0) 
                self.state = 529
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NE(self):
            return self.getToken(MiniGoParser.NE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 533
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 534
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE) | (1 << MiniGoParser.EQ) | (1 << MiniGoParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 535
                    self.expr3(0) 
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 544
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 545
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 546
                    self.expr4(0) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 555
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 556
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 557
                    self.expr5() 
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT, MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 564
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 585
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 571
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 581
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 572
                        self.match(MiniGoParser.DOT)
                        self.state = 575
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                        if la_ == 1:
                            self.state = 573
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 574
                            self.func_call()
                            pass


                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 577
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 578
                        self.expr(0)
                        self.state = 579
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 587
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_DEC(self):
            return self.getToken(MiniGoParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(MiniGoParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(MiniGoParser.INT_OCT, 0)

        def INT_HEX(self):
            return self.getToken(MiniGoParser.INT_HEX, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr7)
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 589
                self.match(MiniGoParser.INT_DEC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 590
                self.match(MiniGoParser.INT_BIN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 591
                self.match(MiniGoParser.INT_OCT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 592
                self.match(MiniGoParser.INT_HEX)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 593
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 594
                self.match(MiniGoParser.LPAREN)
                self.state = 595
                self.expr(0)
                self.state = 596
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 598
                self.func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 599
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 600
                self.struct_literal()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 601
                self.array_literal()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 602
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 603
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 604
                self.match(MiniGoParser.NIL)
                pass


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

        def dot(self):
            return self.getTypedRuleContext(MiniGoParser.DotContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.dot(0)
            self.state = 608
            self.match(MiniGoParser.DOT)
            self.state = 609
            self.match(MiniGoParser.ID)
            self.state = 610
            self.match(MiniGoParser.LPAREN)
            self.state = 613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.state = 611
                self.func_call_thamso()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 615
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(MiniGoParser.ID)
            self.state = 618
            self.match(MiniGoParser.LPAREN)
            self.state = 621
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.INT_DEC, MiniGoParser.INT_BIN, MiniGoParser.INT_OCT, MiniGoParser.INT_HEX, MiniGoParser.STRING_LIT]:
                self.state = 619
                self.func_call_thamso()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 623
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_thamsoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def func_call_thamso(self):
            return self.getTypedRuleContext(MiniGoParser.Func_call_thamsoContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call_thamso

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_thamso" ):
                return visitor.visitFunc_call_thamso(self)
            else:
                return visitor.visitChildren(self)




    def func_call_thamso(self):

        localctx = MiniGoParser.Func_call_thamsoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_func_call_thamso)
        try:
            self.state = 630
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self.expr(0)
                self.state = 626
                self.match(MiniGoParser.COMMA)
                self.state = 627
                self.func_call_thamso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                self.expr(0)
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
        self._predicates[18] = self.dot_sempred
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr1_sempred
        self._predicates[40] = self.expr2_sempred
        self._predicates[41] = self.expr3_sempred
        self._predicates[42] = self.expr4_sempred
        self._predicates[44] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def dot_sempred(self, localctx:DotContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




