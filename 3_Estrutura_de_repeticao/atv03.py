"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("digite seu nome: ")
while len(nome) <= 3:
    print('nome deve ter mais de 3 letras:')
    nome = input("digite seu nome: ")

idade = int(input(f"{nome} digite sua idade: "))
while 0 > idade or 150 < idade:
    print('Idade deve estar entre 0 e 150')
    idade = int(input(f"{nome} digite sua idade: "))

salario = abs(float(input(f"{nome} digite seu salario: ")))
while salario <= 0:
    print('O salario deve ser maior que zero')
    salario = abs(float(input(f"{nome} digite seu salario: ")))

sx = input(f"{nome} digite seu sexo resposta deve estar entre [F, M]: ")
while sx not in "FfMm":
    print('A escolha deve estar entre [f,m]')
    sx = input(f"{nome} digite seu sexo resposta deve estar entre [F, M]: ")

est_civ = input(f'{nome} digite seu estado civil resposta deve estar entre [S, C, V, D]: ')
while sx not in "SsCcVvDd":
    print('A escolha deve estar entre [Ss, Cc, Vv, Dd]')
    sx = input(f"{nome} digite seu sexo resposta deve estar entre [Ss, Cc, Vv, Dd]: ")

print(f"""
nome :{nome}
idade: {idade}
salario: {salario}
sexo: {sx}
estado civil: {est_civ}
""")
