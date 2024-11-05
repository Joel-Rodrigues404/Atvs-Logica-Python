""" 
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades: # noqa E501

    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de 
    combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""


class Carro():
    def __init__(self, consumo=0, quantidade_no_tanque=0):
        self.consumo = consumo
        self.quantidade_no_tanque = quantidade_no_tanque

    def andar(self, kms):
        print(f'O carro andou {kms}km')
        self.quantidade_no_tanque -= kms / self.consumo

    def obter_gasolina(self):
        return self.quantidade_no_tanque

    def adicionar_gasolina(self, qtd_litros):
        self.quantidade_no_tanque += qtd_litros


# 15 quilômetros por litro de combustível.
meuFusca = Carro(consumo=15, quantidade_no_tanque=20)
meuFusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível.
meuFusca.andar(100)            # anda 100 quilômetros.
# Imprime o combustível que resta no tanque.
meuFusca.obter_gasolina()
