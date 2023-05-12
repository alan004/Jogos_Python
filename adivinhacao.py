import random

print("Bem vindo ao jogo de Advinhação")
numero_secreto = random.randrange(1, 101)
tentativas = 0
def seleciona_nivel():
    global tentativas
    print("Selecione o nivel de dificuldade do jogo")
    print("(1) Fácil (2) Médio (3) Difícil")
    global nivel
    nivel = int(input("Nivel:"))
    while (nivel != 1) or (nivel != 2) or (nivel != 3):
        try:
            if (nivel == 1):
                tentativas = 15
                advinhar()
            elif (nivel == 2):
                tentativas = 10
                advinhar()
            elif (nivel == 3):
                tentativas= 3
                advinhar()
            else:
                print("Nível inválido. Digite novamente.")
                print("(1) Fácil (2) Médio (3) Difícil")
                nivel = int(input("Nivel:"))
        finally:
            advinhar()


def advinhar():
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = input ("Digite o seu número:")
        chute_numero = int(chute)
        print("Voce digitou ", chute)

        if (chute_numero < 1 or chute_numero > 100):
            print("Digiete um número entre 1 e 100")
            continue

        acertou = chute_numero == numero_secreto
        maior = chute_numero > numero_secreto


        if (acertou):
            print("Parabéns, você acertou!")
            break
        elif(maior):
            print("Você errou. O número é menor do que você chutou")
        else:
            print("Você errou. O número é maior do que você chutou")


seleciona_nivel()





