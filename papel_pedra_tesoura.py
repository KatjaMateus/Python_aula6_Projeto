
import random
items = ["pedra", "papel", "tesoura"]
def resultado(c,j:str):
    if j == c:
        return 'EMPATE'
    else:
        if c == "pedra" and j == "papel" or c == "papel" and j == "tesoura" or c == "tesoura" and j == "pedra":
            return "o jogador venceu"
        elif c == "pedra" and j == "tesoura" or c == "papel" and j == "pedra" or c == "tesoura" and j == "papel":
            return "O computador venceu"


computador = (random.choice(items))
print("""OPÇÕES:
        pedra
        papel
        tesoura""")
while True:
    jogador = str(input("Qual é a sua jogada? "))
    if jogador not in items:
        print("Opção inválida")
    else:
        break
print(f"O jogador jogou {jogador}")
print(f"O computador jogou {computador}")
print(resultado(computador, jogador))
