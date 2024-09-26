"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador
poderá errar 6 vezes antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!
"""

palavra = 'PALAVRA'

erros = 0
rep_palavra = ['_' for x in palavra]
letras_usadas = []

print('A palavra é: ' + ' '.join(rep_palavra))

while ''.join(rep_palavra) != palavra:
    if erros == 6:
        print(f'-> Você errou pela {erros}ª vez. Jogo Acabado')
        break
    letra = input('Digite uma letra: ').upper()
    if letra in palavra:
        for i, x in enumerate(palavra):
            if letra == palavra[i]:
                rep_palavra[i] = x
    else:
        erros += 1
        print(f'-> Você errou pela {erros}ª vez. Tente de novo!')
    print('A palavra é: ' + ' '.join(rep_palavra))
