import Forca
import Advinhacao
import Templates


def escolhe_jogo():
    Templates.imprime_cabecalho_menu("Bem vindo aos jogos em Python!", "Escolha o seu jogo")

    print("[1] Adivinhacao")
    print("[2] Forca", end="\n\n")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        Advinhacao.jogar_adivinhacao()
    elif jogo == 2:
        Forca.jogar_forca()


if __name__ == "__main__":
    escolhe_jogo()
