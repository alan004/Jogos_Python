import adivinhacao
import forca

def escolhe_jogo():
    boas_vindas()
    jogo = int(input("Opção escolhida:"))
    abrir_jogo(jogo)


def boas_vindas():
    print("*******************************")
    print("*******Escolha seu jogo********")
    print("*******************************")
    print("(1) Adivinhacao (2) Forca (0) Sair")


def abrir_jogo(jogo):
    if (jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 0):
        quit()
    else:
        print("Escolha uma opção válida")
        escolhe_jogo()


if(__name__ == "__main__"):
    escolhe_jogo()