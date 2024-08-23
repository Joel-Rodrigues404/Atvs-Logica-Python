"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

ganhoHora = abs(float(input('digite quanto voçe ganha por hora de trabalho: ')))
horas_trabalhadas = abs(int(input('digite quantas horas voçe trabalha por mes: ')))

print(f'seu salario deste mes e igual a {ganhoHora * horas_trabalhadas:.2f}R$')
