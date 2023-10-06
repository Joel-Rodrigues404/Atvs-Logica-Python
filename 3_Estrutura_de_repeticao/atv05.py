"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

while True:
    try:
        city_A = abs(int(input("digite a numero de habitantes da cidade A: ")))
        city_B = abs(int(input("digite a numero de habitantes da cidade B: ")))

        if city_A >= city_B:
            print('A população da cidade A ja e maior que da cidade B')
        else:
            cont = 0
            while city_A < city_B:
                city_A += city_A*(3/100)
                city_B += city_B*(1.5/100)
                cont += 1

        print(f'{city_B}, {city_A}, {cont}')
    except ValueError:
        print('entrada invalida')
