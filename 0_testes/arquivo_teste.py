class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        self._raio = valor

    @property
    def area(self):
        return 3.1416 * (self._raio ** 2)


# Uso
c = Circulo(5)
print(c.raio)  # Acessa o raio como um atributo
print(c.area)  # Calcula a área com base no raio

c.raio = 10    # Modifica o raio com validação

print(c.raio)  # Acessa o raio como um atributo
print(c.area)  # Calcula a área com base no raio
