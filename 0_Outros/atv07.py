"""
Faça um algoritmo que imprima valores dentro dos seguintes
intervalos:
a) (0,5 pt) 0 até 80
b) (0,5 pt) 78 até 108, nos intervalos de 4 em 4
c) (0,5 pt) 20 até -20, nos intervalos de 4 em 4
d) (1 pt) imprima a tabuada de 0 até 9, com soma, subtração, multiplicação e
divisão
"""

# a)
print(*[x for x in range(0, 81)], sep=", ")
# b)
print("\n")
print(*[x for x in range(78, 109, 4)], sep=", ")
# c)
print("\n")
print(*[x for x in range(20, -21, -4)], sep=", ")
# d) oq quer dizer tabuada de 0 a 9
print("\n")

for x in range(0, 10):
    for y in range(0, 10):
        print(f"{x} + {y} = {x + y}")

for x in range(0, 10):
    for y in range(0, 10):
        print(f"{x} - {y} = {x - y}")

for x in range(0, 10):
    for y in range(0, 10):
        print(f"{x} x {y} = {x * y}")

for x in range(0, 10):
    for y in range(1, 10):
        print(f"{x} / {y} = {x / y}")
