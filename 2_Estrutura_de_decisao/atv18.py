""" 
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

data_str = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data_str.split("/"))

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

bissesto = False
if ano % 4 == 0:
    dias_por_mes[2] = 29

if mes < 1 or mes > 12:
    data_valida = False
elif dia < 1 or dia > dias_por_mes[mes]:
    data_valida = False
else:
    data_valida = True

if data_valida:
    print(f"A data {data_str} e valida")
else:
    print(f"A data {data_str} não e valida")
