"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, 
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
a = True
while a:
    valor_divida = abs(float(input("digite o valor da divida: ")))
    parcelas = abs(int(input("Escolha a quantidade de parcelas entre 1, 3, 6, 9, 12: ")))
    if parcelas == 1:
        juros = 0
    elif parcelas == 3:
        juros = valor_divida * 1/10
    elif parcelas == 6:
        juros = valor_divida * 15/100
    elif parcelas == 9:
        juros = valor_divida * 2/10
    elif parcelas == 12:
        juros = valor_divida * 25/100
    else:
        raise ValueError('Insira as parcelas corretamente!')

    valor_parcela = (valor_divida + juros)/parcelas
    
    print(f'{valor_divida + juros}R$    {juros} juros   {parcelas} parcelas    {valor_parcela:2f}')
    escolha = abs(int(input('deseja continuar [1] sim [2] nao')))
    if escolha == 1:
        continue
    elif escolha == 2:
        a = False
    else:
        raise ValueError("digite a corretamente")
    

