"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi
(Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome,
    Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma
    informação que devemos levar em consideração, o Humor do nosso tamagushi,
    este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um
    campo calculado, então não devemos criar um atributo para armazenar esta
    informação por que ela pode ser calculada a qualquer momento.
"""


class myexeption(Exception):
    def __init__(self, mensagem):
        super.__init__(mensagem)
        self.mensagem = mensagem


class BichinhoVirtual():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.humor = self.calcula_humor()

    def __str__(self):
        return f'nome: {self.nome}\npeso: {self.fome}\nsaude: {self.saude}\nidade: {self.idade}\nhumor: {self.humor}'  # noqa E261

    def calcula_humor(self):
        nfome = 100 - self.fome
        return (nfome + self.saude) / 2

    def alterar_nome(self, valor):
        self.nome = valor

    def alterar_fome(self, valor):
        self.fome = valor

    def alterar_saude(self, valor):
        self.saude = valor

    def alterar_idade(self, valor):
        self.idade = valor

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        return self.humor


bixo = BichinhoVirtual(nome='clautersonislaw')
print(bixo)
