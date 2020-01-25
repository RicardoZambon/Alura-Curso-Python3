import random
import Templates


def jogar_adivinhacao():
    imprime_cabecalho()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("[1] Fácil / [2] Médio / [3] Difícil")
    nivel = int(input("::: "))

    print("")
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(f"Você possui {total_de_tentativas} tentativas, boa sorte!", end="\n\n")

    for rodada in range(1, total_de_tentativas + 1):
        # print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute = int(input("Digite um número entre 1 e 100: "))
        # print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if total_de_tentativas - rodada > 0:
                print(f"Não acertou, ainda faltam {total_de_tentativas - rodada} tentativas. O seu chute foi ", end="")
                if chute > numero_secreto:
                    print("maior", end="")
                elif chute < numero_secreto:
                    print("menor", end="")
                print(" do que o número secreto.")
            else:
                print(f"Acabaram suas tentativas, o número secreto era {numero_secreto}.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("")

    print("Fim do jogo")


def imprime_cabecalho():
    Templates.imprime_cabecalho_menu("Jogos em Python", "Adivinhação de números")


if __name__ == "__main__":
    jogar_adivinhacao()
