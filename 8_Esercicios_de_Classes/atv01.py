"""
Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
"""


class Bola():
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor


bola = Bola("vermelho", 3, "madeira")
print(bola.cor)
bola.cor = "amarelo"
print(bola.cor)
