import random
import jogos

def jogar():
    try:
        boas_vindas()
        tentativas = seleciona_nivel()
        pontos = 1000

        advinhar(pontos, tentativas)
    finally:
        jogos.escolhe_jogo()


def chute_usuario():
    chute = input("Digite o seu número:")
    return int(chute)


def advinhar(pontos, tentativas):
    numero_secreto = random.randrange(1, 101)
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = chute_usuario()
        print("Voce digitou ", chute)
        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100")
            continue

        acertou = (chute == numero_secreto)
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print("Parabéns, você acertou e fez {} pontos".format(pontos))
            break
        else:
            pontos -= 100
            if (maior):
                print("Você errou. O número é menor do que você chutou")
            elif (menor):
                print("Você errou. O número é maior do que você chutou")


def boas_vindas():
    print("*******************************")
    print("Bem vindo ao jogo de Advinhação")
    print("*******************************")


def seleciona_nivel():
    print("Selecione o nivel de dificuldade do jogo")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Nivel:"))
    while (nivel != 1) or (nivel != 2) or (nivel != 3):
        if (nivel == 1):
            tentativas = 10
            return tentativas
        elif (nivel == 2):
            tentativas = 6
            return tentativas
        elif (nivel == 3):
            tentativas = 3
            return tentativas
        else:
            print("Nível inválido. Digite novamente.")
            print("(1) Fácil (2) Médio (3) Difícil")
            nivel = int(input("Nivel:"))


if (__name__ == "__main__"):
    jogar()
