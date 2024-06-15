"""
Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular, endereço e saldo. Adicione métodos para realizar depósitos e saques. Obs.: utilize herança e encapsulamento nessa questão.
"""


class ContaBancaria:
    def __init__(
        self, numero_conta: int, nome_titular: str, endereco: str, saldo: float = 0.0
    ) -> None:
        self.__numero_conta = numero_conta
        self.__nome_titular = nome_titular
        self.__endereco = endereco
        self.__saldo = saldo

    def deposito(self, valor) -> None:
        # Existe saldo negativo
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R$ {valor} realizado com sucesso")
        else:
            print("Valor de deposito invalido")

    def saque(self, valor) -> None:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso")
        else:
            print("saque invalido")

    def get_numero_conta(self) -> int:
        return self.__numero_conta

    def get_nome_titular(self) -> str:
        return self.__nome_titular

    def get_endereco(self) -> str:
        return self.__endereco

    def get_saldo(self) -> float:
        return self.__saldo


conta1 = ContaBancaria(123456, "João", "Rua A, 123")
print(f"Saldo inicial da conta {conta1.get_numero_conta()}: R${conta1.get_saldo()}")

conta1.deposito(100)
print(f"Novo saldo após depósito: R${conta1.get_saldo()}")

conta1.saque(50)
print(f"Novo saldo após saque: R${conta1.get_saldo()}")
