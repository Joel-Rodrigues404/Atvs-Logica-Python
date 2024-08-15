"""
Implemente um algoritmo que imprima os valores da sequência de
Fibonacci até o valor de posição 1000, e apresente a razão do valor atual com o
elemento da sequência anterior. A sequência de Fibonacci é dada pelos valores iniciais
1,1 e segue cada elemento pela soma dos dois últimos elementos.
"""

cont = 1
aux = 1
num = 1
while cont <= 15:
    print(num, end=", ")
    aux = num - aux
    num += aux
    cont += 1
