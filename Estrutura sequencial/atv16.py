# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num_int1 = int(input('digite um numero inteiro : '))
num_int2 = int(input('digite um numero inteiro : '))
num_float = float(input('digite um numero real : '))

mult = (2 * num_int1) * (num_int2/2)
soma = (3 * num_int1) + (num_float)
potenc = num_float**3

print(f'resposta A ({mult})')
print(f'resposta B ({soma})')
print(f'resposta C ({potenc})')

