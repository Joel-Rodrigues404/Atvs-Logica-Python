# variaveis = [(1, 2, 3), (4, 5, 6)]
#
# print(','.join(*variaveis))

#
# def prox_rest(valor):
#     print(valor // 2)
#     print(valor % 2)
#
#
# prox_rest(176)

# import ast
#
# string = 'teste'
# print(ast.dump(ast.parse(f'x = 1; y = 2, {string}', mode='single'), indent=4))


num = abs(int(input("digite um numero: ")))
num2 = abs(int(input("digite outro numero: ")))
num3 = abs(int(input("digite outro peste: ")))

lista = [num, num2, num3]

print(f'maior = {max(lista)}, menor = {min(lista)}')
