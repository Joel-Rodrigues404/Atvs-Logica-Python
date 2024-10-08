"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

"""

nota1 = abs(float(input("digite nota 1: ")))
nota2 = abs(float(input("digite nota 2: ")))

media = (nota1 + nota2) / 2

if 0 < media < 4:
    conceito = "E"
elif 4 <= media < 6:
    conceito = "D"
elif 6 <= media < 7.5:
    conceito = "C"
elif 7.5 <= media < 9:
    conceito = "B"
elif media >= 9:
    conceito = "A"
else:
    print('Digite valores de 0 a 10')

if conceito in "ABCabc":
    status = "APROVADO"
elif conceito in "DEde":
    status = "REPROVADO"
else:
    print('Algo Errado')

print(f'Com as notas {nota1}, {nota2}, tem-se a media {media} que corresponde a letra {conceito} então o aluno foi {status}')
