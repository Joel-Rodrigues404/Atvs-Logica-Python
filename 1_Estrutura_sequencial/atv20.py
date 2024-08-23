# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de
# Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

from time import sleep

salario = abs(float(input("digite seu salario aqui em R$: ")))

print("calculando...")
sleep(2)

ir = salario * (11 / 100)
inss = salario * (8 / 100)
sindicato = salario * (5 / 100)
descontos = ir + inss + sindicato
salario_liquido = salario - descontos

print(f'''
 + Salário Bruto : {salario}R$
 - IR (11%) : {ir}R$
 - INSS (8%) : {inss}R$
 - Sindicato ( 5%) : {sindicato}R$
 = Salário Liquido : {salario_liquido}R$
''')
