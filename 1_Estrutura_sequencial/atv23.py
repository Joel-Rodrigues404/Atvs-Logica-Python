"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_mb = abs(int(input("Digite o tamanho do arquivo em MB: ")))
velocidade_mbps = abs(int(input("Digite a velocidade da internet em Mbps: ")))

tempo = tamanho_mb / velocidade_mbps

print(f'para fazer o dawnload de {tamanho_mb}mb com um link de {velocidade_mbps}mbps serão nesseçarios {tempo}s')
