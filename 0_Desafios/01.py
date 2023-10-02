""" 
Uma escola presisa ler e imprimir as medias de seus 12 alunos nas 20 notas tiradas  por cada aluno um no ano letivo
faça um algoritimo que esqreva o nome e a media de cada aluno e a media geral da turma.
"""


cont_aluno = 0
nomes = ''
notas_turma = 0
cont_notas = 0

while cont_aluno < 2:
    nome = input("diginte nome: ")
    nome += '-'
    nomes += nome
    while cont_notas < 2:
        nota = abs(float(input("digite as 20 notas do aluno: ")))
        notas_turma += nota
        cont_notas += 1
    cont_notas = 0
    cont_aluno += 1

print(f'notas > {notas_turma}\n nomes > {nomes.split("-")}')
media_turma = notas_turma / cont_aluno
print(media_turma)