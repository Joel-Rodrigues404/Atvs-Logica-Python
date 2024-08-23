# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.


sx = input("digite seu sexo: ")

if sx in 'Ff':
    print('feminino')
elif sx in 'Mm':
    print('masculino')
else:
    print('sexo invalido')
