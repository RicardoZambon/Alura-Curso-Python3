import random


def jogar_forca():

    imprime_mensagem_abertura()

    segredo = carrega_palavra_secreta()
    palavra_secreta = segredo[0]
    letras_acertadas = segredo[1]

    enforcou = False
    acertou = False
    tentativas = 7

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()

        acertou_chute = marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        if not acertou_chute:
            tentativas -= 1
            desenha_forca(7 - tentativas)
            # print(f"Não há a letra {chute} na palavra, você ainda tem {tentativas} tentativas.")

        letras_faltando = letras_acertadas.count("_")
        if letras_faltando > 0:
            print(f"Ainda faltam acertar {letras_faltando} letras.")

        acertou = "_" not in letras_acertadas
        enforcou = tentativas <= 0
        print(f"{letras_acertadas}")

    if acertou:
        imprime_mensagem_vencedor()
    elif enforcou:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo no jogo de Adivinhação")
    print("********************************")


def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo.read().split("\n") if not palavra.strip() == ""]
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta, ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Qual letra? ").upper().strip()
    print("")
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao_letra = palavra_secreta.find(chute)
    if posicao_letra < 0:
        return False
    else:
        while posicao_letra >= 0:
            letras_acertadas[posicao_letra] = chute
            posicao_letra = palavra_secreta.find(chute, posicao_letra + 1)
    return True


def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar_forca()
