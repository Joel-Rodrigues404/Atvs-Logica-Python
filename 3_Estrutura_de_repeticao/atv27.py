"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e 
a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

num_turm = abs(int(input("Digite o numero de turmas: ")))

soma = 0
for x in range(num_turm):
    aluno_por_turma = abs(int(input(f"digite o numero de alunos da turma {x}: ")))
    soma += aluno_por_turma

media = soma / num_turm

print(f'A media de alunos por turma eh {media}')