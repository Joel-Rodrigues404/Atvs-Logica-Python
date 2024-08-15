from typing import Any
from functools import singledispatchmethod


class Somar:
    def __init__(self, arg1: Any, arg2: Any) -> None:
        self.arg1 = arg1
        self.arg2 = arg2

    @singledispatchmethod
    def soma(self, verbose: bool = False) -> Any:
        raise NotImplementedError(
            f"Tipo {type(self.arg1)} e {type(self.arg2)} não suportado para a função"
        )

    @soma.register(int)
    def _soma_int(self, verbose: bool = False) -> Any:
        if verbose:
            print("Como são números, vamos somá-los")
        return f"{self.arg1 + self.arg2} é um inteiro ou float"

    @soma.register(str)
    def _soma_str(self, verbose: bool = False) -> Any:
        if verbose:
            print("Como são strings, vamos concatená-las")
        return f"{self.arg1 + self.arg2} é uma string"


somar = Somar(2, 3)
somar.soma()

somar_str = Somar("Hello, ", "world!")
somar_str.soma(verbose=True)
