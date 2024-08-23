total_eleitores = abs(int(input('Total de eleitores: ')))
Vbrancos = abs(int(input('numero de votos brancos: ')))
Vnulos = abs(int(input('numero de votos nulos: ')))

p1 = Vbrancos * 100
p2 = Vnulos * 100
Vvalidos = (total_eleitores) - (Vbrancos + Vnulos)
p3 = Vvalidos * 100
porcentagem_VB = p1 / total_eleitores
porcentagem_VN = p2 / total_eleitores
porcentagem_VV = p3 / total_eleitores
print(f'total de eleitores > {total_eleitores} / percentual de votos brancos > {porcentagem_VB}%')
print(f'total de eleitores > {total_eleitores} / percentual de votos nulos > {porcentagem_VN}%')
print(f'total de eleitores > {total_eleitores} / percentual de votos validos > {porcentagem_VV}%')
