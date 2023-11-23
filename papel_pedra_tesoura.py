

def resultado(c,j:str):
    if c == "pedra":
        if j == "pedra":
            return "EMPATE"
        elif j == "papel":
            return "o jogador venceu"
        elif j == "tesoura":
            return "O computador venceu"
        else:
            return "Opção inválida. As opções são pedra, papel ou tesoura"
    if c == "papel":
        if j == "papel":
            return "EMPATE"
        elif j == "tesoura":
            return "o jogador venceu"
        elif j == "pedra":
            return "O computador venceu"
        else:
            return "Opção inválida. As opções são pedra, papel ou tesoura"
    if c == "tesoura":
        if j == "tesoura":
            return "EMPATE"
        elif j == "pedra":
            return "o jogador venceu"
        elif j == "papel":
            return "O computador venceu"
        else:
            return "Opção inválida. As opções são pedra, papel ou tesoura"

import random
items = ["pedra", "papel", "tesoura"]
computador = (random.choice(items))
jogador = str(input("Qual é a sua jogada? "))
print(f"O jogador jogou {jogador}")
print(f"O computador jogou {computador}")
print(resultado(computador, jogador))