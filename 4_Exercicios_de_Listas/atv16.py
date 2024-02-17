"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""


def calcular_salario(vendas_brutas):
    return 200 + (0.09 * vendas_brutas)


def determinar_intervalo(salario):
    if salario < 1000:
        return (salario - 200) // 100
    else:
        return 8


contadores = [0] * 9

vendas = [3000, 2500, 4000, 1500, 6000]  # Exemplo de vendas brutas dos vendedores

for vendas_brutas in vendas:
    salario = calcular_salario(vendas_brutas)
    indice = int(determinar_intervalo(salario))
    if indice != -1:
        contadores[indice] += 1

print(contadores)

for i, contador in enumerate(contadores):
    if i < 8:
        print(f"${200 + i*100} - ${299 + i*100}: {contador} vendedores")
    else:
        print(f"$1000 em diante: {contador} vendedores")
