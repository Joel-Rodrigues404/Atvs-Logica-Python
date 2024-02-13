"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

list_num = list()

while True:
    c = int(input("digite numeros (-1 para encerrar): "))
    if c == -1:
        break
    list_num.append(c)

print(f'valores lidos {len(list_num)}')
[print(list_num[x], end='-') for x in range(len(list_num))]
print(list_num[::-1])
print(f'soma {sum(list_num)}')
media = sum(list_num) / len(list_num)
print(f'Media {media}')
acima_da_media = list()
acima_de_7 = list()
for x in list_num:
    if x > media:
        acima_da_media.append(x)
    if x > 7:
        acima_de_7.append(x)

print(f'Quantidade acima da media {len(acima_da_media)}')
print(f'Numeros acima de 7 {len(acima_de_7)}')
print('mensagem')
