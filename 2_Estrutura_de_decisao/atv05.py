# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média 
# alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nome = input("digite o nome do aluno: ")

n1 = abs(float(input("digite a nota 1: ")))
n2 = abs(float(input("digite a nota 2: ")))

media = (n1 + n2) / 2

if media >= 7:
    print(f'O aluno {nome} esta aprovado')
elif media < 7:
    print(f'O aluno {nome} esta reprovado')
elif media == 10:
    print(f'O aluno {nome} foi aprovado com distinçao')
