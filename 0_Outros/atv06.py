"""
Dado duas variáveis user1 e user2, que podem apresentar os seguintes
valores, “pedra”, “papel” e “tesoura”. Faça um algoritmo que imprima dizendo quem
venceu, perdeu ou empatou. (Pedra vence tesoura, tesoura vence papel e papel vence
pedra)
"""

from random import randint

# pedra = 1
# papel = 2
# tesoura = 3

"""
casos de derrota
user1 | user2
papel | pedra 2 1
pedra | papel 1 2
tesoura | pedra 3 1
"""

conversao = ["pedra", "papel", "tesoura"]

user1 = abs(int(input("Digite\n1- Pedra\n2- Tesoura\n3- papel\n> ")))
user2 = randint(1, 3)

print(f"user1 >> {conversao[user1 - 1]}")
print(f"user2 >> {conversao[user2 - 1]}")

if user1 == user2:
    print("Empatou")

elif any(
    [user1 == 2 and user2 == 1, user1 == 1 and user2 == 2, user1 == 3 and user2 == 1]
):
    print("Perdeu")

else:
    print("Venceu")
