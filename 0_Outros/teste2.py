from typing import Union, Any, overload
from functools import singledispatch, singledispatchmethod

# type: ignore[misc] comment


# class Somar:
#     def __init__(self) -> None:
#         pass

#     @singledispatch
#     def soma(self, arg1: int | float | str, arg2: int | float | str, verbose=False):
#         raise NotImplementedError(
#             f"Type {type(arg1)}  {type(arg2)} Not suported for a function"  # noqa E501
#         )

#     @soma.register
#     def _(self, arg1: int | float, arg2: int | float, verbose=False):  # noqa E501
#         if verbose:
#             print("como são numeros vamos somalos")
#         return f"{arg1 + arg2} integer or float"

#     @soma.register
#     def _(self, arg1: str, arg2: str, verbose=False):
#         if verbose:
#             print("como são strings vamos concatenalas")
#         return f"{arg1 + arg2} integer or float"


# somar = Somar()
# print(somar.soma(3, 3, True))
# print(somar.soma("3", "3", True))
# print(somar.soma("3", 3, True))


class Somar:
    def __init__(self) -> None:
        pass

    @overload
    def soma(self, num1: int | float, num2: int | float):
        return "temos 2 inteiros"

    @overload
    def soma(self, num1: str, num2: str):
        return "temos 2 str"

    def soma(self, num1, num2):
        return f"{num1 + num2}"


soma = Somar()
print(soma.soma("2", "2"))
