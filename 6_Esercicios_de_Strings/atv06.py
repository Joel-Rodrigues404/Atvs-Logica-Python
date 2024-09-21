"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês
por extenso.

    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973.
"""

data_de_nascimento = input(
    "digite sua data de nascimento no formato (dd/mm/aaaa): ")
dia = data_de_nascimento[0:2]
mes = int(data_de_nascimento[data_de_nascimento.find(
    '/') + 1:data_de_nascimento.find('/') + 3])
ano = data_de_nascimento[-4:]

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abriu",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezenbro"
]

print(f'Você nasceu em {dia} de {meses[mes - 1]} de {ano}.')
