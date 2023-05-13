import adivinhacao
import forca

def escolhe_jogo():
    print("*******************************")
    print("*******Escolha seu jogo********")
    print("*******************************")

    print("(1) Adivinhacao (2) Forca")
    jogo = int(input("Opção escolhida:"))

    if(jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()