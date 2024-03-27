"""
Implemente uma classe chamada “Triangulo” que possua atributos para armazenar os lados do triangulo. Adicione métodos para calcular se os lados formam um triangulo, calcular o maior lado e o perímetro.
"""


class Triangulo:
    def __init__(self, lado1: float, lado2: float, lado3: float) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def forma_triangulo(self) -> bool:
        condicoes = [
            self.lado1 + self.lado2 > self.lado3,
            self.lado1 + self.lado3 > self.lado2,
            self.lado2 + self.lado3 > self.lado1,
        ]
        resultado = True if all(condicoes) else False
        return resultado

    def maior_lado(self) -> None:
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("todos são iguais")
        elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"Maior e o 1° lado com {self.lado1}")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f"Maior e o 2° lado com {self.lado2}")
        else:
            print(f"Maior e o 3° lado com {self.lado3}")

    def perimetro(self) -> None:
        if self.forma_triangulo():
            soma = self.lado1 + self.lado2 + self.lado3
            print(f"Perimetro e {soma}")
        else:
            print("Triagulo invalido")


t = Triangulo(12, 5, 5)
t.maior_lado()
print(t.forma_triangulo())
t.perimetro()
