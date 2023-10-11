"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

c1 = 0
c2 = 0
c3 = 0 

num_eleitor = abs(int(input("digite o numero de eleitores: ")))

for x in range(num_eleitor):
    escolha = abs(int(input('escolha \nc1[1]\nc2[2]\nc3[3]\n: ')))
    if escolha == 1:
        c1 += 1
    elif escolha == 2:
        c2 += 1
    elif escolha == 3:
        c3 += 1

if c1 > c2 and c1 > c3:
    print('Ganhador cand1')
elif c2 > c1 and c2 > c3:
    print('Ganhador cand2')
elif c3 > c1 and c3 > c2:
    print('Ganhador cand3')
else:
    print('empate')


