""" 
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no 
mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

val_h = abs(float(input("digite o valor da sua hora de trabalho: ")))
horas = abs(float(input("digite o o numero de horas que trabalha por mês: ")))
sal_brut = val_h * horas

impost_rend_dict = {
    900: 0,
    1500: 5,
    2500: 10,
    float("inf"): 20,
}

desc_imp_rend = None
for faixa, percent in impost_rend_dict.items():
    if sal_brut <= faixa:
        if percent == 0:
            desc_imp_rend = 0
            break
        else:
            desc_imp_rend = sal_brut * (percent / 100)
            break

desc_inss = sal_brut * (10 / 100)
desc_fgts = sal_brut * (11 / 100)
total_desc = desc_imp_rend + desc_inss
sal_liq = sal_brut - total_desc

print(f"""
    Salário Bruto: ({horas} * {val_h})        : R$ {sal_brut}
    (-) IR (5%)                     : R$   {desc_imp_rend}
    (-) INSS ( 10%)                 : R$  {desc_inss}
    FGTS (11%)                      : R$  {desc_fgts}
    Total de descontos              : R$  {total_desc}
    Salário Liquido                 : R$  {sal_liq}
""")
