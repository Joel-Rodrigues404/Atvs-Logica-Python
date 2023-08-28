idade_anos = abs(int(input('quantos anos: ')))
idade_meses = abs(int(input('e quantos meses: ')))
idade_dias = abs(int(input('e quantos dias')))

anos_dias = idade_anos * 365
meses_dias = idade_meses * 30

print(f'sua idade em dias ehh {anos_dias + meses_dias + idade_dias}')