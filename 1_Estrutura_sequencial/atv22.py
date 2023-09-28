# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
# arredonde os valores para cima, isto é, considere latas cheias.


area_para_pintar = abs(float(input("Digite a area para ser pintada em m²")))

#Lata de tinta
lata_tinta_cap = 18.0
lata_tinta_preco = 80.0
#Galão de tinta
galao_tinta_cap = 3.6
galao_tinta_preco = 25.0



