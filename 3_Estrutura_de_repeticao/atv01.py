""" 
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
vpedindo até que o usuário informe um valor válido.
"""

nota = input("ditite a nota do aluno entre 0 e 10: ")

while not nota.isnumeric():
    nota = input("ditite a nota do aluno entre 0 e 10: ")

print(f"A nota e {nota}")
