"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

tipo:
    +-----+
    |     |
    |     |
    +-----+
"""


def desenha_moldura(linha: int, coluna: int):
    linha = max(1, min(linha, 20))
    coluna = max(1, min(coluna, 20))
    linha = linha * 3
    line = "-"
    espaco = " "
    print(f"+{line * linha}+")
    print(f"|{espaco * linha}|\n" * coluna, end="")
    print(f"+{line * linha}+")


desenha_moldura(5, 5)
