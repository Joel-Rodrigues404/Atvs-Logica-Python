"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa
terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou
ou perdeu o jogo.
"""
import random

with open('arquivos/atv13_strings.txt', 'r', encoding='utf-8') as palavras_txt:
    palavras = palavras_txt.readlines()

palavra_aleatoria = random.choice(palavras).lower()
palavra_aleatoria = list(palavra_aleatoria)
palavra_aleatoria.remove('\n')
tamanho_palavra = len(palavra_aleatoria)

palavra_aleatoria_embaralhada = []


aux = palavra_aleatoria.copy()
for x in range(tamanho_palavra):
    letra = random.choice(aux)
    palavra_aleatoria_embaralhada.append(letra)
    aux.remove(letra)

print(palavra_aleatoria)
print(''.join(palavra_aleatoria_embaralhada))

erros = 0
while erros != 6:
    chute_palavra = input("Digite qual a palavra embaralhada: ")
    if chute_palavra == ''.join(palavra_aleatoria):
        print("Voçe ganhou!!")
        break
    else:
        print("Voçe errou! tente novamente!")
    erros += 1
