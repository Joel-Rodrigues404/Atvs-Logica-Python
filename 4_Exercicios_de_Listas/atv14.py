"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

respostas_positivas = []
print('responda as perguntas a seguir [1] = sim [2] = não')
p1 = abs(int(input("Telefonou Para a vitima: ")))
p2 = abs(int(input("Esteve no local do crime: ")))
p3 = abs(int(input("Mora perto da vítima: ")))
p4 = abs(int(input("Devia para a vítima: ")))
p5 = abs(int(input("á trabalhou com a vítima: ")))

if p1 == 1:
    respostas_positivas.append('sim')
if p2 == 1:
    respostas_positivas.append('sim')
if p3 == 1:
    respostas_positivas.append('sim')
if p4 == 1:
    respostas_positivas.append('sim')
if p5 == 1:
    respostas_positivas.append('sim')

if len(respostas_positivas) == 2:
    print('Suspeito')
elif len(respostas_positivas) >= 3 and len(respostas_positivas) <= 4:
    print('Cumplice')
else:
    print('Assasino')
