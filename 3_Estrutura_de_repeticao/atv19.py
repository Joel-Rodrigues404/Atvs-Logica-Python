"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

maior = float("-inf")
menor = float("inf")
soma = 0
while True:
    n = abs(int(input("digite um numero entre 0 e 1000 [0 para parar]: ")))
    if n > 1000:
        break
    soma += n
    if n == 0:
        break
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print(f"Maior {maior} menor {menor} soma {soma}")
