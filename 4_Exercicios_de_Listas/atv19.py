"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador         Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""


def percentual_jogador(num_votos, total_votos):
    """
    num_votos == x
    total == 100
    total*x == num_votos * 100
    x == (num_votos * 100) / total
    """
    percent = (num_votos * 100) / total_votos
    return percent


numeros_jogadores = [x for x in range(1, 24)]
votos = [[] for _ in range(23)]

num = 1
cont = 0

while num != 0:
    num = abs(int(input("digite um numero entre 1 e 23: ")))

    if num not in numeros_jogadores:
        # raise ValueError("O numero deve estar entre 1 e 23!!")
        print("O numero deve estar entre 1 e 23!!")
        continue

    votos[num - 1].append(num)
    cont += 1

print(votos, cont)

string = []

for x in range(1, 24):
    percentual = percentual_jogador(len(votos[x - 1]), cont)

    if x == 1:
        total_string = f"Votos totais == {cont}\n"
    else:
        total_string = ""

    estatisticas_jogadores_string = f"""Jogador N° {x}
Numero de votos do Jogador == {len(votos[x - 1])}
Percentual em relação ao tota de votos == {percentual:.2f}%
"""
    string.append(total_string)
    string.append(estatisticas_jogadores_string)
    string.append("\n")

maior = -1
index_maior = 0
for i, x in enumerate(votos):
    if len(x) > maior:
        maior = len(x)
        index_maior = i + 1

jogador_mais_votado = f"O melhor jogador foi o número {index_maior}, com {len(votos[index_maior - 1])} votos, correspondendo a {percentual_jogador(len(votos[index_maior - 1]), cont)}% do total de votos."

string.append(jogador_mais_votado)

with open("arquivos/atv19_listas.txt", "a", encoding="utf-8") as arquivo:
    for x in string:
        arquivo.write(str(x))
    arquivo.write("\n")
