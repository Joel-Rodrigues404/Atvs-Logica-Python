"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a
    cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
    ela deve crescer 0,5 cm.
"""


class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if anos > 0:
            if self.idade <= 17:
                aumento_altura = 17 - self.idade
                self.altura += (0.005 * aumento_altura)
            self.idade += anos

    def engordar(self, quilos):
        if quilos > 0:
            self.peso += quilos

    def emagrecer(self, quilos):
        if quilos > 0:
            self.peso -= quilos

    def crescer(self, altura):
        if altura > 0:
            self.altura += altura

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos, {self.peso}kg, {self.altura}m'


pessoa1 = Pessoa('joel', 12, 50, 1.70)
print(pessoa1)
pessoa1.envelhecer(10)
