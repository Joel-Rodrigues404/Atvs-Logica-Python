# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input(f'digite uma letra: ')


if letra.isalpha():
    if letra in 'aAeEIiOoUu':
        print(f'A letra e uma {letra} e uma vogal')
    else:
        print(f'A letra e uma {letra} consoante')
else:
    print(f'Digite uma letra')