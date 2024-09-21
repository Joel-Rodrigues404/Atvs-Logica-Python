"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte: # noqa

    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u.
"""

texto = input("Digite uma frase: ")

espacos = texto.count(" ")
letras_a = texto.count("a")
letras_e = texto.count("e")
letras_i = texto.count("i")
letras_o = texto.count("o")
letras_u = texto.count("u")

print(f"""
    quantos espaços em branco existem na frase == {espacos}
    quantas vezes aparecem as vogais
    a == {letras_a},
    e == {letras_e},
    i == {letras_i},
    o == {letras_o},
    u == {letras_u},
""")
