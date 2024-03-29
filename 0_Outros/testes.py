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
def soma(a: Union[int, str], b: Union[int, str], verbose=False):
    raise NotImplementedError(
        f"Type {type(a) and type(b)} Not suported for a function"
    )  # noqa E501


@soma.register(int)
def s(a, b, verbose=False):
    if verbose:
        print("Como são numeros vamos somalos")
    return f"{a + b}  integer"


@soma.register(str)
def s(a, b, verbose=False):  # noqa F811
    if verbose:
        print("Como são strings vamos concatenalas")
    return f"{a + b} string"


# print(soma("3", "3"))  # saida 33 string
# print(soma(3, 3))  # 6  integer
# print(soma(2.2, 2.3, verbose=True))  # type: ignore[arg-type]


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
