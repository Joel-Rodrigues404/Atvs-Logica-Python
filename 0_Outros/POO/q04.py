"""
Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de compras, aplicar descontos e calcular o valor total da compra. Obs.: utilize polimorfismo e herança nesta questão.
"""


class Produto:
    def __init__(self, produto: str, valor: float) -> None:
        self.__produto = produto
        self.__valor = valor

    def calcular_preco(self) -> float:
        return self.__valor

    def get_produto(self) -> str:
        return f"{self.__produto}"

    def get_valor(self) -> float:
        return self.__valor

    def __str__(self) -> str:
        return f"{self.__produto}"


class ProdutoComDesconto(Produto):
    def __init__(self, produto: str, valor: float, desconto: float) -> None:
        super().__init__(produto, valor)
        self.__desconto = desconto

    def get_desconto(self) -> float:
        return self.__desconto

    def calcular_preco(self) -> float:
        preco_com_desconto = super().calcular_preco() * (1 - self.__desconto / 100)
        return preco_com_desconto

    def __str__(self) -> str:
        return f"{self.__produto}"


class LojaVirtual:
    def __init__(self) -> None:
        self.__produtos: list = []
        self.__carrinho: list = []
        self.total = 0

    def cadastrar_produto(self, produto: Produto | ProdutoComDesconto) -> None:
        if isinstance(produto, (Produto, ProdutoComDesconto)):
            self.__produtos.append(produto)
        else:
            print("Não e um produto")

    def adicionar_no_carrinho_compras(
        self, produto: Produto | ProdutoComDesconto
    ) -> None:
        if isinstance(produto, (Produto, ProdutoComDesconto)):
            self.__carrinho.append(produto)
        else:
            print("Não e um produto")

    def valor_total_compra(self) -> int | float:
        self.total = 0
        # Itens do carrinho são instacias de objetos que contem valor
        for x in self.__carrinho:
            self.total += x.calcular_preco()
        return self.total

    def get_produtos(self) -> list[str]:
        aux = []
        for produto in self.__produtos:
            aux.append(produto.get_produto())
        return aux

    def get_carrinho(self) -> list[str]:
        aux = []
        for produto in self.__carrinho:
            aux.append(produto.get_produto())
        return aux

    def __str__(self) -> str:
        return f"Produtos: {', '.join(self.get_produtos())}"


# CRIA PRODUTOS
produto01 = Produto("produto01", 10)
produto02 = ProdutoComDesconto("produto02", 10, 10)

# CRIA LOJA VIRTUAL
loja_virtual = LojaVirtual()

# CADASTRA PRODUTOS NA LOJA
loja_virtual.cadastrar_produto(produto01)
loja_virtual.cadastrar_produto(produto02)

# ADICIONA PRODUTOS AO CARRINHO
loja_virtual.adicionar_no_carrinho_compras(produto01)
loja_virtual.adicionar_no_carrinho_compras(produto02)

# MOSTRA PRODUTOS CADASTRADOS NA LOJA
print(loja_virtual.get_produtos())

# MOSTRA PRODUTOS ADICIONADOS AO CARRINHO
print(loja_virtual.get_carrinho())

# MOSTRA O VALOR TOTAL DOS ITEMS DO CARRINHO
print(loja_virtual.valor_total_compra())
