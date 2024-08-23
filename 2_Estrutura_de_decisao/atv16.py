"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

var_a = float(input("Digite o valor de A: "))
if var_a == 0:
    raise ValueError("O valor de A deve ser diferente de zero")
var_b = float(input("Digite o valor de B: "))
var_c = float(input("Digite o valor de C: "))

if var_b >= 0:
    sinal1 = "+"
else:
    sinal1 = ""

if var_c >= 0:
    sinal2 = "+"
else:
    sinal2 = ""

delta = (var_b**2) - (4 * var_a * var_c)
neg = var_b - (2 * var_b)


def calc_x1(delta):
    var_b_ivert = var_b - (2 * var_b)
    x1 = (var_b_ivert + (delta**0.5)) / 2 * var_a
    return x1


def calc_x2(delta):
    var_b_ivert = var_b - (2 * var_b)
    x2 = (var_b_ivert - (delta**0.5)) / 2 * var_a
    return x2


if delta < 0:
    raise ValueError(
        f"Delta foi igual a {delta} então as raizes não pertencem ao cojunto dos numeros reais"
    )
elif delta == 0:
    print(f"Delta foi igual a {delta} então so tera uma raiz real")
    x1 = calc_x1(delta)
    x2 = calc_x2(delta)

elif delta > 0:
    print(f"Delta foi igual a {delta} então terão 2 raizes reais")
    x1 = calc_x1(delta)
    x2 = calc_x2(delta)
else:
    print("algo deu errado")

print(f"equaçao: {var_a}x²{sinal1}{var_b}x{sinal2}{var_c} = 0")
print(f"Tem as raizes X1 = {x1} e X2 = {x2}")
