salario_func = abs(float(input('Digite o salario mensal do funcionario: ')))

print(f'reajuste salarial')
tipo = abs(int(input(f"""
Digite para
[1] acreçimo de salario
[2] decreçimo de salario
> """)))
if tipo == 1:
    reajuste = abs(int(input('Digite o percentual de reajuste do salario: ')))
    n1 = reajuste * salario_func
    n2 = n1/100
    print(n2)
    salario_ajustado = salario_func + n2
elif tipo == 2:
    reajuste = abs(int(input('Digite o percentual de reajuste do salario: ')))
    n1 = reajuste * salario_func
    n2 = n1/100
    print(n2)
    salario_ajustado = salario_func - n2
else:
    print(f'Digite somente 1 ou 2 para a escolha')

print(f'O novo salario do funcionario com o reajuste de {reajuste}% ficou de {salario_ajustado}R$')