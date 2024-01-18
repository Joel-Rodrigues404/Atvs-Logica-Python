"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, 
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos 
duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor 
‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para 
registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores 
de entrada todas as vezes que desejar
"""

def conversor_horas(h, m):
    if h > 24 or h < 1:
        raise ValueError('As horas devem estar entre 1 e 24')
    if m > 60 or m < 1:
        raise ValueError('Os minutos devem estar entre 1 e 60')
    if h > 12:
        h = h - 12
    return h, m

def saida(h,m):
    print(f'{h}:{m}')

h,m = conversor_horas(23, 12)

saida(h,m)