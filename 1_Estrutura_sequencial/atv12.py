"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado = abs(float(input('digite o valor do lado do quadrado: ')))

area_do_quadrado = lado ** 2

dobro_da_area = area_do_quadrado * 2

print(f'o dobro da area do quadrado de area {area_do_quadrado} e igual a {dobro_da_area:.1f}')
