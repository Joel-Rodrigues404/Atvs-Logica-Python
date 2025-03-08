"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e
bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo
do estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
É possível criar um macaco canibal?
"""


class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def ver_bucho(self):
        # return ', '.join(self.bucho)
        return self.bucho

    def digerir(self, comida):
        self.bucho.remove(comida)

    def __str__(self):
        return f'O macaco com nome {self.nome} esto com {self.ver_bucho()} no bucho!'  # noqa E261


luffy = Macaco(nome='luffy')
garp = Macaco(nome='Garp')
luffy.comer("banana")
luffy.comer("maça")
luffy.comer("algo")
luffy.comer(garp)
print(luffy)
