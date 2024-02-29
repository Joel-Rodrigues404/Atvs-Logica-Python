"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato Dia de mesPorExtenso de Ano. Opcionalmente, valide a data e retorne NULL
caso a data seja inválida.
"""

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}


def tranforma_data(d, m, a):
    if d > 31 or d < 1:
        raise ValueError('O valor para o dia deve estar entre 1 e 31')
    if m > 12 or m < 1:
        raise ValueError('O valor para o mes deve ser entre 1 e 12')
    elif m == 2 and d > 29:
        raise ValueError('Fevereiro so tem 29 dias tente novamente')

    return print(f'{d} de {meses[m]} de {a}')


tranforma_data(2, 2, 2022)
