import adivinhacao
import forca
import cobrinha

def escolhe_jogo():
    boas_vindas()
    jogo = int(input("Opção escolhida:"))
    abrir_jogo(jogo)


def boas_vindas():
    print("*******************************")
    print("*******Escolha seu jogo********")
    print("*******************************")
    print("(1) Adivinhacao (2) Forca (3) Cobrinha (0) Sair")


def abrir_jogo(jogo):
    if (jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 3):
        print("Jogando o jogo da cobrinha")
        cobrinha.jogar()
    elif (jogo == 0):
        quit()
    else:
        print("Escolha uma opção válida")
        escolhe_jogo()


if(__name__ == "__main__"):
    escolhe_jogo()