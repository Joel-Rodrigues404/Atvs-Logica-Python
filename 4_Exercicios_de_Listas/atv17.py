"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

distancia_saltos = []
nome = input("digite seu nome: ")
for x in range(1, 6):
    distancia = abs(float(input(f"digite a distancia do salto {x}: ")))
    distancia_saltos.append(distancia)
media = sum(distancia_saltos) / 5

distancia_saltos = [str(x) for x in distancia_saltos]

print(
    f"""   
    Primeiro Salto: {distancia_saltos[0]}
    Segundo Salto: {distancia_saltos[1]}
    Terceiro Salto: {distancia_saltos[2]}
    Quarto Salto: {distancia_saltos[3]}
    Quinto Salto: {distancia_saltos[4]}
"""
)

separador = " - "

resultado = separador.join(distancia_saltos)

print(
    f"""   
    Resultado final:
    Atleta: {nome}
    Saltos: {resultado}
    Média dos saltos: {media}
"""
)
