"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes
e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido
        e mostra a quantidade de litros que foi colocada no veículo
        abastecerPorLitro( ) – método onde é informado a quantidade em litros
        de combustível e mostra o valor a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível
        restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a
    quantidade de combustível total na bomba.
"""

# TODO atividade 10 classes


class Carro():
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
        self.tanque_litros = 0


class Combustivel():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class BombaCombustível():
    def __init__(self):
        self.tipo_combustivel = ['comun', 'aditivado']
        self.combustivels_sendo_usado = self.tipo_combustivel[0]
        # self.valor_litro = 6.07
        self.valor_litro = 4
        self.quantidade_combustivel = 0
        self.quantidade_combustivel_na_bomba = 60000  # litros

    def abastecer_por_valor(self, valor):
        # 4 -- 1
        # v -- x
        qtd_combs = valor / self.valor_litro

        self.quantidade_combustivel_na_bomba -= qtd_combs
        return qtd_combs

    def abastecer_por_litro(self, litros):
        qtds_combs = litros * self.valor_litro

        self.quantidade_combustivel_na_bomba -= qtds_combs
        return qtds_combs

    def altera_valor(self, valor):
        self.valor_litro = valor

    def altera_combustivel(self):
        for i, x in enumerate(self.tipo_combustivel):
            print(f'tipos de combustiveis {i} - {x}')
        combustivel = int(input(
            "digite o numero do combustivel que voçe quer usar: "))
        self.combustivels_sendo_usado = self.tipo_combustivel[combustivel]

    def altera_quantidade_combustivel(self, qtd_nova):
        self.quantidade_combustivel_na_bomba = qtd_nova

    def __str__(self):
        return f'A bomba_de_combustivel tem {self.quantidade_combustivel_na_bomba}L, valor litro = {self.valor_litro}'  # noqa E261


tesla = Carro(nome='tesla', marca='Tesla')
bomba_de_combustivel = BombaCombustível()
bomba_de_combustivel.altera_combustivel()
print(bomba_de_combustivel)
