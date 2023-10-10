"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa 
para que ele mostre os números um ao lado do outro.
"""

cont = 1

while True:
    escolha = abs(int(input("digite [1/2]: ")))
    cont = 1
    if escolha == 1:
        while cont <= 20:
            print(cont)
            cont += 1
    elif escolha == 2:
        while cont <= 20:
            if cont == 20:
                print(cont)
            else:
                print(cont, end=' ')
            cont += 1
    else:
        print(f'Entrada invalida')