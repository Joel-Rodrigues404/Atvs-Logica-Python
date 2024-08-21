"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no 
formato DD de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]


def mes_por_extenco(data: str):
    new_data = data.split("/")
    mes_num = int(new_data.pop(1))
    mes_extenco = meses[mes_num - 1]
    return f"{new_data[0]} de {mes_extenco} de {new_data[1]}"


for x in range(1, 13):
    print(mes_por_extenco(data=f"12/{x}/2005"))
