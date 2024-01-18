"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do 
percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

s_ini = 1000
perc = 1.5/100

novo_sal = 0
aumento = 0
ano_atual = abs(int(input("Digite o ano atual: ")))
ano_atual = 2023

for x in range(1996, ano_atual + 1):
    aumento = s_ini * perc
    novo_sal = s_ini + aumento
    perc = perc * 2

print(novo_sal)