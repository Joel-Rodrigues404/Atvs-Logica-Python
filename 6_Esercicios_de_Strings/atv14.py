"""
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando
outros símbolos em lugar das letras, como números por exemplo. A própria
palavra
leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito
usada para confundir os iniciantes e afirmar-se como parte de um grupo.
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um
programa que peça uma texto e transforme-o para a grafia leet speak.
"""
import random

letras_para_simbolos = {
    " ": [" ", " "],
    "A": ["4", "/\\", "@", "/-\\", "^", "ä", "ª", "aye"],
    "B": ["8", "6", "|3", "ß", "P>", "|:"],
    "C": ["[", "¢", "<", "("],
    "D": ["|))", "o|", "[)", "I>", "|>", "?"],
    "E": ["3", "&", "£", "ë", "[-", "€", "ê", "|=-"],
    "F": ["|=", "ph", "|#"],
    "G": ["6", "&", "(_+", "9", "C-", "gee", "("],
    "H": ["#", "/-/", "[-]", "{=}", "<~>", "|-|", "]~[", "}{", "]-[", "?", "8", "}-{", "]["],  # noqa E261
    "I": ["1", "!", "|", "&", "eye", "3y3", "ï", "][", "[]"],
    "J": ["j", ";", "_/", "</", "(/"],
    "K": ["X", "|<", "|{", "]{", "}<", "|("],
    "L": ["1", "7", "1_", "|", "|_", "#", "¬", "£"],
    "M": ["//.", "^^", "|v|", "[V]", "{V}", "|\\/|", "/\\/\\", "(u)", "[]V[]", "(V)", "/|\\", "IVI"],  # noqa E261
    "N": ["//", "^/", "|\\|", "/\\/", "[\\]", "<\\>", "{\\}", "[]\\[]", "n", "/V", "₪"],  # noqa E261
    "O": ["0", "()", "?p", "*", "ö"],
    "P": ["|^", "|*", "|o", "|^(o)", "|>", "|\"", "9", "[]D", "|̊", "|7"],
    "Q": ["q", "9", "(_,)", "o,"],
    "R": ["|2", "P\\", "|?", "|^", "lz", "[z", "12", "Я"],
    "S": ["5", "$", "z", "§", "ehs"],
    "T": ["7", "+", "-|-", "1", "']['", '"|"'],
    "U": ["(_)", "|_|", "v", "ü"],
    "V": ["\\/", ],
    "W": ["\\/\\/", "vv", "'//", "\\^/", "(n)", "\\V/", "\\//", "\\X/", "\\|/"],  # noqa E261
    "X": ["><", "Ж", "ecks", ")("],
    "Y": ["Y", "j", "`/", "¥"],
    "Z": ["2", "z", "~\\_", "~/_", "%"]
}


palavra = input("Digite uma palavra ou frase: ").upper()
nova_palavra = ''
for x in palavra:
    nova_palavra += random.choice(letras_para_simbolos[x])
print(nova_palavra)
