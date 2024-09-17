import matplotlib.pyplot as plt
import networkx as nx
from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.edges = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                self.edges.append((current_node.value, value))
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                self.edges.append((current_node.value, value))
            else:
                self._insert(current_node.right, value)
        else:
            print("Value already exists in the tree")

    def plot_tree(self):
        G = nx.DiGraph()
        G.add_edges_from(self.edges)
        pos = self._hierarchy_pos(self.root)
        labels = {node: node for node in G.nodes()}
        plt.figure(figsize=(10, 8))
        nx.draw(
            G,
            pos=pos,
            labels=labels,
            with_labels=True,
            node_size=2000,
            node_color="skyblue",
            font_size=12,
            font_weight="bold",
            arrows=False,
        )
        plt.savefig("arquivos/binary_tree.png")  # Salva o gráfico em um arquivo

    def _hierarchy_pos(self, root, pos=None, x=0, y=0, level=1, width=2):
        if pos is None:
            pos = {}
        pos[root.value] = (x, y)
        if root.left:
            pos = self._hierarchy_pos(
                root.left,
                pos=pos,
                x=x - width / level,
                y=y - 1,
                level=level + 1,
                width=width,
            )
        if root.right:
            pos = self._hierarchy_pos(
                root.right,
                pos=pos,
                x=x + width / level,
                y=y - 1,
                level=level + 1,
                width=width,
            )
        return pos


# Exemplo de uso
tree = BinaryTree()
# values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
values = [randint(1, 100) for x in range(30)]
print(values)

for value in values:
    tree.insert(value)

tree.plot_tree()
