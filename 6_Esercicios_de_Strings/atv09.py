"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um
número de CPF no formato xxx.xxx.xxx-xx e indique se é um
número válido ou inválido através
da validação dos dígitos verificadores edos caracteres de formatação.
"""
# https://www.dio.me/articles/como-fazer-uma-validacao-de-cpf-com-python
cpf = input("Digite seu cpf: ")

if cpf.count(".") != 3 or cpf.count("-") != 1 or len(cpf) != 14:
    print("CPF invalido!!!")
else:
