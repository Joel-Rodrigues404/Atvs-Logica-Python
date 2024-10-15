"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do
correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
saque; No construtor, saldo é opcional, com valor default zero e os demais
atributos são obrigatórios.
"""


class ContaCorrente():
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.__numero_conta = self._sanitiza_numero_conta(numero_conta)
        self.nome_correntista = nome_correntista
        self.__saldo = self._sanitiza_saldo(saldo)

    def __str__(self):
        return f'A conta tem saldo de {self.saldo}R$'

    def __gt__(self, other):
        pass

    def _sanitiza_numero_conta(self, valor):
        if type(valor) is not int:
            raise ValueError(
                "O numero da conta deve ser um numero!")
        else:
            if valor < 0:
                raise ValueError("O numero da conta deve ser positivo!!")
            return valor

    def _sanitiza_saldo(self, valor):
        if type(valor) is not int:
            raise ValueError(
                "O saldo deve ser um numero!")
        else:
            if valor < 0:
                raise ValueError("O saldo deve ser positivo!!")
            return valor

    @property
    def numero_conta(self):
        return self.__numero_conta

    @numero_conta.setter
    def numero_conta(self, valor):
        if type(valor) is int:
            self.__numero_conta = valor
        else:
            raise ValueError(
                "O valor para numero da conta deve ser um numero!")

    @property
    def saldo(self):
        return self.__saldo

    def alterar_nome(self, novo_nome):
        if type(novo_nome) is str:
            self.nome_correntista = novo_nome
        else:
            print("O valor deve ser uma string!")

    def deposito(self, valor):
        if type(valor) is int or type(valor) is float:
            self.__saldo += valor
        else:
            print("O valor deve ser um inteiro ou de ponto flutuante!!")

    def saque(self, valor):
        if type(valor) is int or type(valor) is float:
            saldo = self.__saldo - valor
            if saldo < 0:
                raise ValueError("Voçe não tem todo esse dinheiro pra sacar!!")
            self.__saldo -= valor
        else:
            print("O valor deve ser um inteiro ou de ponto flutuante!!")


conta1 = ContaCorrente(numero_conta="1234",
                       nome_correntista="Joel", saldo=-1)
print(conta1)
