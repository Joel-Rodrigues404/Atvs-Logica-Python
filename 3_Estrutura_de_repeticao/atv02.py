"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = input("digite seu nome: ")
senha = input("digite sua senha: ")

while senha == nome or nome == senha:
    print("Erro a senha n pode ser igual ao nome nem nome igual a senha")
    nome = input("digite seu nome: ")
    senha = input("digite sua senha: ")
