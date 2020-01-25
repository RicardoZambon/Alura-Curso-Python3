# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


def imprime_cabecalho_menu(linha1, linha2):
    # os.system('cls' if os.name == 'nt' else 'clear')

    clear()

    linha1 = linha1[0:30]
    linha2 = linha2[0:30]

    print(f"{'*' * 40}")
    print(f"**** {' ' * calcula_espacos(linha1, 30, False)}{linha1}{' ' * calcula_espacos(linha1, 30, True)} ****")
    print(f"**** {' ' * calcula_espacos(linha2, 30, False)}{linha2}{' ' * calcula_espacos(linha2, 30, False)} ****")
    print(f"{'*' * 40}", end="\n\n")


def calcula_espacos(texto, tamanho, inclui_resto):
    espaco = tamanho - len(texto)
    metade = int(espaco // 2)
    if inclui_resto:
        metade += (espaco % 2)
    return metade


# define our clear function
def clear():
    if name == 'nt': # for windows
        _ = system('cls')
    else: # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


# if __name__ == "__main__":
#     imprime_cabecalho_menu("Bem vindo aos jogos em Python!", "Escolha o seu jogo")
