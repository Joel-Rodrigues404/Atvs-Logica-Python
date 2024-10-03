"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
    a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
    e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
    informe as medidades de um local. Depois, deve criar um objeto com as
    medidas e calcular a quantidade de pisos e de rodapés necessárias para o
    local.
"""


class Retangulo():
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self._algo = 1

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def largura(self):
        return self.__largura

    @comprimento.setter
    def comprimento(self, valor):
        self.__comprimento = valor

    @largura.setter
    def largura(self, valor):
        self.__largura = valor

    def area(self):
        return self.__largura * self.__comprimento

    def perimetro(self):
        return (self.__largura * 2) + (self.__comprimento * 2)

    def __str__(self):
        return f'O retangulo tem: largura = {self.__largura}, comprimento = {self.__comprimento}, area = {self.area()}, perimetro = {self.perimetro()}'  # noqa E261


rect = Retangulo(10, 20)
print(rect)

# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
# informe as medidades de um local. Depois, deve criar um objeto com as
# medidas e calcular a quantidade de pisos e de rodapés necessárias para o
# local.

largura = abs(float(input("Digite a largura: ")))
comprimento = abs(float(input("Digite o comprimento: ")))

area_pisos = abs(float(input("Digite a area dos pisos em m²: ")))
altura_rodape = abs(float(input("Digite a altura do rodapé em cm²: ")))

quarto = Retangulo(comprimento, largura)

print(f'Voçe vai precisa de {quarto.area() / area_pisos} pisos para o chão')
print(f'Voçe vai precisa de {quarto.perimetro() / (altura_rodape / 100)} pisos para o rodapé')  # noqa E261
print(quarto)
