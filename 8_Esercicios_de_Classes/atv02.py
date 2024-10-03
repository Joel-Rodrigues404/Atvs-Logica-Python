"""
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado():
    def __init__(self, tamanho_lado):
        self._tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_valor):
        self._tamanho_lado = novo_valor

    def mostrar_lado(self):
        return print(self._tamanho_lado)

    def area(self):
        return self._tamanho_lado ** 2


quadrado = Quadrado(5)
quadrado.mostrar_lado()
print(quadrado.area())
quadrado.mudar_valor_lado(novo_valor=10)
quadrado.mostrar_lado()
print(quadrado.area())
