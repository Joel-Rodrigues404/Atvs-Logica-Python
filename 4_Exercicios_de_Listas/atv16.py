"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe
$200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em
uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores)
que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
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

trabalhadores = abs(int(input("trabalhadores: ")))
sal_semanal = 200
salarios = []

for x in range(trabalhadores):
    vendas_brutas = abs(int(input("Digite o valor das vendas brutas: ")))
    comicao = vendas_brutas * (9 / 100)
    salario = sal_semanal + comicao if comicao > 0 else sal_semanal
    salarios.append(salario)

valores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in salarios:
    if x in set(range(200, 300)):
        valores[0] = valores[0] + 1
    if x in set(range(300, 400)):
        valores[1] = valores[1] + 1
    if x in set(range(400, 500)):
        valores[2] = valores[2] + 1
    if x in set(range(500, 600)):
        valores[3] = valores[3] + 1
    if x in set(range(600, 700)):
        valores[4] = valores[4] + 1
    if x in set(range(700, 800)):
        valores[5] = valores[5] + 1
    if x in set(range(800, 900)):
        valores[6] = valores[6] + 1
    if x in set(range(900, 1000)):
        valores[7] = valores[7] + 1
    if x > 1000:
        valores[8] = valores[8] + 1


print(
    f"""
$200 - $299 == {valores[0]}
$300 - $399 == {valores[1]}
$400 - $499 == {valores[2]}
$500 - $599 == {valores[3]}
$600 - $699 == {valores[4]}
$700 - $799 == {valores[5]}
$800 - $899 == {valores[6]}
$900 - $999 == {valores[7]}
$1000 em diante == {valores[8]}
"""
)

salario_busca = abs(float(input("digite o salario a qual quer buscar: ")))
print(salarios.index(salario_busca))
