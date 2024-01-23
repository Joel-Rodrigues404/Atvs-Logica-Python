"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes 
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""

interv_1, interv_2, interv_3, interv_4 = 0, 0, 0, 0
while True:
    num = int(input("digite num: "))
    if num > 0:
        if num < 25:
            interv_1 += 1
        elif num > 26 or num < 50:
            interv_2 += 1
        elif num > 51 or num < 75:
            interv_3 += 1
        elif num > 76 or num < 100:
            interv_4 += 1
        else:
            continue
    elif num < 0:
        break

print(f'interv_1 {interv_1} interv_2 {interv_2} interv_3 {interv_3} interv_4 {interv_4}')