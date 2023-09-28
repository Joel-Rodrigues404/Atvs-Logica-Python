""" 
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

day = abs((int(input("digite o numero de um dia da semana entre [1/7]: "))))

dias = {
    1:"Domingo",
    2:"Segunda",
    3:"Terça",
    4:"Quarta",
    5:"Quinta",
    6:"Sexta",
    7:"Sabado"
}
if day not in [1,2,3,4,5,6,7]:
    print("valor invalido digite um valor de 1 a 7")
else:
    for dia_num, dias_str in dias.items():
        if day == dia_num:
            print(dias_str)