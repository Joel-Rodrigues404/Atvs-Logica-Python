"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item 
(preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

cachorro_quente = 1.20
bauru_simple = 1.30
bauru_ovo = 1,50
hamburger = 1.20
cheeseburger = 1.30
refri = 1
total = 0
while True:
    pedido = abs(int(input(f"""digite o codigo do pedido que deseja: 
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00 \n: """)))

    quantidade = abs(int(input("digite a quantidade: ")))

    if pedido == 100:
        valor = quantidade * cachorro_quente
        total += valor
    elif pedido == 101:
        valor = quantidade * bauru_simple
        total += valor
    elif pedido == 102:
        valor = quantidade * bauru_ovo
        total += valor
    elif pedido == 103:
        valor = quantidade * hamburger
        total += valor
    elif pedido == 104:
        valor = quantidade * cheeseburger
        total += valor
    elif pedido == 105:
        valor = quantidade * refri
        total += valor
    else:
        print("erro")
        break
    escolha = abs(int(input("Deseja pedir mais [1] sim [2] não: ")))
    if escolha == 1:
        continue
    elif escolha == 2:
        break

print(f"O total do seu pedido deu {total}")