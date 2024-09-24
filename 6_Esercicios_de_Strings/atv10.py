"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso. 

        9        9
99 > noventa e nove
        8        8
88 > oitenta e oito
"""

print(17 % 10, 17 // 10)  # 7
numero = abs(int(input("Digite um numero entre 0 e 99: ")))

unidade = numero % 10  # resto(o que sobra)
dezena = numero // 10  # pega o quociente(o que da certo dividir)

unidades = [
    "Um",
    "Dois",
    "Tres",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
]

dezenas_de_dez = [
    "Onze",
    "Doze",
    "Treze",
    "Quartorze",
    "Quinze",
    "Dezeseis",
    "Dezesete",
    "Dezoito",
    "Dezenove",
]

dezenas = [
    "Dez",
    "Vinte",
    "Trinta",
    "Quarenta",
    "Cinquenta",
    "Sesenta",
    "Setenta",
    "Oitenta",
    "Noventa",
]

if numero == 10:
    print(dezenas[0])
elif numero < 10:
    print(unidades[numero - 1])
elif 10 < numero < 20:
    print(dezenas_de_dez[numero - 11])
else:
    print(f'{dezenas[dezena - 1]} e {unidades[unidade - 1]}')
