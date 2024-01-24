"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = list()
for x in range(10):
    nota1 = abs(float(input('digite a nota 1: ')))
    nota2 = abs(float(input('digite a nota 2: ')))
    nota3 = abs(float(input('digite a nota 3: ')))
    nota4 = abs(float(input('digite a nota 4: ')))

    media = (nota1 + nota2 + nota3 + nota4)/4
    medias.append(media)


m7 = 0
for x in medias:
    if x >= 7:
        m7 += 1

print(f'todas as medias {medias} medias maiores ou igual a 7 {m7}')