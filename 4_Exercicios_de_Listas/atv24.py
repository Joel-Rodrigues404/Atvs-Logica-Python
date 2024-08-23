"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""

from random import randint

lances_dado = [[] for _ in range(6)]

for x in range(1, 101):
    lance_dado = randint(1, 6)
    lances_dado[lance_dado - 1].append(lance_dado)

print(lances_dado)
for i, x in enumerate(lances_dado):
    print(f"O numero {i + 1} caiu {len(x)} vezes")
