""" 
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no 
salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario_atual = abs(float(input("digite o valor do salario atual: ")))

if salario_atual < 280:
    percent = 20
    percent_calc = salario_atual * (percent/100)
    salario_novo = salario_atual + percent_calc
    aumento = salario_novo - salario_atual

elif 280 <= salario_atual < 700:
    percent = 15 
    percent_calc = salario_atual * (percent/100)
    salario_novo = salario_atual + percent_calc
    aumento = salario_novo - salario_atual

elif 700 <= salario_atual < 1500:
    percent = 10
    percent_calc = salario_atual * (percent/100)
    salario_novo = salario_atual + percent_calc
    aumento = salario_novo - salario_atual

elif salario_atual >= 1500:
    percent = 5
    percent_calc = salario_atual * (percent/100)
    salario_novo = salario_atual + percent_calc
    aumento = salario_novo - salario_atual

else:
    print(f'Algo deu errado')

print(f'O seu salario era de {salario_atual} então foi aplicado um aumento de {percent}% adicionando {aumento} ficando assim {salario_novo}')

