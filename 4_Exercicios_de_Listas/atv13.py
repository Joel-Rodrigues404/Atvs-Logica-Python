"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
lista_temp = list()

for x in meses:
    temp = float(input(f"digite a temperatura media do mes {x}: "))
    lista_temp.append(temp)


media_temp_anual = (sum(lista_temp)) / len(lista_temp)


for mes, temp in zip(meses, lista_temp):
    if temp > media_temp_anual:
        print(f"{mes} com temperatura {temp}")
