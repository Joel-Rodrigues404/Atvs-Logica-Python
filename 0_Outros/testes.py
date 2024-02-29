# def cont_regre(num):
#     print(num)

#     if num == 0:
#         return

#     num -= 1
#     return cont_regre(num)


# class Pilha:
#     def __init__(self, lista):
#         self.lista = lista

#     def mostra_lista(self):
#         print(self.lista)


# lista = [_ for _ in range(1, 11)]
# lista_obj = Pilha(lista=lista)

# mypy: disable-error-code="no-redef"
import functools
from typing import overload, Union, Tuple  # noqa E402


@functools.singledispatch
def soma(a, b):
    pass


@soma.register(int)
def s(a, b):
    return f"{a + b}  integer"


@soma.register(str)
def s(a, b):  # noqa F811
    return f"{a + b} string"


print(soma("3", "3"))  # saida 33 string
print(soma(3, 3))  # 6  integer


class Processor:
    @overload
    def process(self, response: None) -> None: ...

    @overload
    def process(self, response: int) -> Tuple[int, str]: ...

    @overload
    def process(self, response: bytes) -> str: ...

    def process(
        self, response: Union[None, int, bytes]
    ) -> Union[None, Tuple[int, str], str]:
        if response is None:
            return None
        elif isinstance(response, int):
            return response, "Integer"
        elif isinstance(response, bytes):
            return response.decode("utf-8")
        else:
            raise TypeError("Invalid type for response")


# Testando a classe com exemplos
processor = Processor()
print(processor.process(None))  # Saída: None
print(processor.process(10))  # Saída: (10, 'Integer')
print(processor.process(b"hello"))  # Saída: 'hello'
