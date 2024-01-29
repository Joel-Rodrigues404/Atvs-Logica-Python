"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""


idades = []
alturas = []
maior13 = 0

for x in range(2):
    idade = abs(int(input("digite a idade: ")))
    idades.append(idade)
    if idade >= 13:
        maior13 +=1
    alturas.append(abs(int(input("digite a Altura: "))))

media_alturas = (sum(alturas))/len(alturas)

for idade, altura in zip(idades, alturas):
    if idade >= 13 and altura <= media_alturas:
        maior13 += 1