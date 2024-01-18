"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o 
segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número 
do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

num_maior = 0
altura_maior = 0

for x in range(10):
    num = abs(int(input('numero da chamada: ')))
    altura = abs(int(input('altura do aluno: ')))

    if altura > altura_maior:
        num_maior = num
        altura_maior = altura

print(f'A maior altura e do aluno de numero {num_maior} com {altura_maior}')