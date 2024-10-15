"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir
o volume. Certifique-se de que o número do canal e o nível do volume
permanecem dentro de faixas válidas.
"""


class Tv():
    def __init__(self, volume, canal):
        #  1 a 100
        self.volume = volume
        #  1 a 20
        self.canal = canal

    def muda_canal(self, canal=1):
        if 1 < canal < 20:
            self.canal = canal

    def mudar_volume(self, volume=1):
        if 1 < volume < 20:
            self.volume = volume
