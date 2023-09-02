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
    resto1 = num % 100
    centenas = int((num - resto1)/100)
    unidades = resto1 % 10
    dezenas = int((resto1 - unidades)/10)
    # centenas, dezenas, unidades = map(int, str(num))

    resultado = []

    if centenas > 0:
        resultado.append(f'{centenas} centena{"s" if centenas > 1 else "":}{", " if dezenas > 0 else " ":}')
    if dezenas > 0:
        resultado.append(f'{dezenas} dezena{"s" if dezenas > 1 else "":} {"e " if unidades > 0 else " ":}')
    if unidades > 0:
        resultado.append(f'{unidades} unidade{"s" if unidades > 1 else ""}.')
    
    print("".join(resultado))
    
    
else:
    print("O numero deve estar entre 1 e mil")