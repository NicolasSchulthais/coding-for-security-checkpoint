import random


def nome_opcao(num):
    opcoes = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
    return opcoes[num - 1]


def jogar(jogador, computador):
    regras = {
        (1, 3): "Pedra quebra Tesoura",
        (1, 4): "Pedra esmaga Lagarto",
        (2, 1): "Papel cobre Pedra",
        (2, 5): "Papel refuta Spock",
        (3, 2): "Tesoura corta Papel",
        (3, 4): "Tesoura decapita Lagarto",
        (4, 2): "Lagarto come Papel",
        (4, 5): "Lagarto envenena Spock",
        (5, 1): "Spock vaporiza Pedra",
        (5, 3): "Spock derrete Tesoura"
    }

    if jogador == computador:
        return "Empate!", ""

    if (jogador, computador) in regras:
        return "Você venceu!", regras[(jogador, computador)]

    if (computador, jogador) in regras:
        return "Computador venceu!", regras[(computador, jogador)]


print("[1] Pedra\n[2] Papel\n[3] Tesoura\n[4] Lagarto\n[5] Spock")

while True:
    jogador = int(input("Escolha (1 a 5): "))
    if 1 <= jogador <= 5:
        break
    print("Valor inválido! Digite um número entre 1 e 5.")
    
computador = random.randint(1, 5)

print("\nVocê:", nome_opcao(jogador))
print("Computador:", nome_opcao(computador))

resultado, frase = jogar(jogador, computador)

if frase != "":
    print(frase, "—", resultado)
else:
    print(resultado)