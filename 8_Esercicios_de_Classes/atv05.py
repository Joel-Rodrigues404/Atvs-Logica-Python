"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do
correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
saque; No construtor, saldo é opcional, com valor default zero e os demais
atributos são obrigatórios. 
"""


class ContaCorrente():
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.__numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.__saldo = saldo

    def __str__(self):
        return f'A conta tem saldo de {self.saldo}R$'

    def __gt__(self, other):
        pass

    @property
    def numero_conta(self):
        return self.__numero_conta

    @numero_conta.setter
    def numero_conta(self, valor):
        if type(valor) is int:
            self.__numero_conta = valor

    @property
    def saldo(self):
        return self.__saldo

    # @saldo.setter
    # def numero_conta(self, valor):
    #     if type(valor) is int:
    #         self.__saldo = valor

    def alterar_nome(self, novo_nome):
        if type(novo_nome) is int:
            self.nome_correntista = novo_nome

    def deposito(self):
        pass

    def saque(self):
        pass


conta1 = ContaCorrente(numero_conta=1234, nome_correntista="Joel", saldo="10")
print(conta1)
