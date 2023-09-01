""" 
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e 
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 
311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = abs(int(input("digite um numero qualquer de 1 a 1000: ")))

if 0 < num < 1000:
    # resto1 = num % 100
    # centenas = int((num - resto1)/100)
    # unidades = resto1 % 10
    # dezenas = int((resto1 - unidades)/10)
    centenas, dezenas, unidades = map(int, str(num))
    if centenas == 0 and dezenas == 0:
        print(f'{unidades} unidades')
        if unidades == 0:
            print('zero')
    elif centenas == 0:
        print(f'{dezenas} dezenas e {unidades}unidades')
    
    print(centenas, dezenas, unidades)
else:
    print("O numero deve estar entre 1 e mil")