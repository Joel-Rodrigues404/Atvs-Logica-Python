"""
Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula, a turma, a série, a disciplina e as notas de n alunos. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).
"""


class Aluno:
    def __init__(
        self, nome: str, matricula: int, turma: str, serie: int, disciplina: str
    ) -> None:
        self.nome = nome
        self.__matricula = matricula
        self.turma = turma
        self.serie = serie
        self.disciplina = disciplina
        self.notas: list = []

    def adicionar_nota(self, nota) -> None:
        self.notas.append(nota)

    def calcular_media(self) -> float | str:
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return "nenhuma nota adicionada"

    def verificar_situacao(self) -> str | None:
        media = self.calcular_media()
        if isinstance(media, str):
            return None
        if media >= 6:
            return f"aprovado com media {media}"
        elif media < 6:
            return f"Reprovado com media {media}"
        return None

    def get_matricula(self) -> int:
        return self.__matricula


aluno1 = Aluno("João", 2022001, "A", 9, "Matemática")

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(6)

print(f"Situação do aluno {aluno1.nome}: {aluno1.verificar_situacao()}")
