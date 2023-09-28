""" 
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é 
ou não bissexto.
"""


ano = abs(int(input("digite o ano: ")))

if ano % 4 != 0:
    print(f'O ano {ano} não e bissesto')
else:
    print(f'O ano {ano} e bissesto')