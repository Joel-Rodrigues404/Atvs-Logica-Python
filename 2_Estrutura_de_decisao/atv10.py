""" Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
 ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o 
 caso. """

estuda = str(input("voçe estuda [S/N]: "))

if estuda in 'Ss':
    turno = str(input("digite o turno que voçe estuda [M / V / N]: "))
    if turno in "Mm":
        print("bom dia")
    elif turno in 'Vv':
        print("boa tarde")
    elif turno in "Nn":
        print("boa noite")
    else:
        print('valor invalido')
        print('validos são [M / V / N]')

elif estuda in 'Nn':
    print("So pra que estuda")
else:
    print("digite S ou N")
