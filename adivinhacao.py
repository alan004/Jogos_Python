import random
import jogos
pontos = 1000

def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Advinhação")
    print("*******************************")

    def seleciona_nivel():
        print("Selecione o nivel de dificuldade do jogo")
        print("(1) Fácil (2) Médio (3) Difícil (0) Sair")
        global tentativas
        global nivel
        nivel = int(input("Nivel:"))
        while (nivel != 1) or (nivel != 2) or (nivel != 3) or (nivel != 0):
            try:
                if (nivel == 1):
                    tentativas = 10
                elif (nivel == 2):
                    tentativas = 6
                elif (nivel == 3):
                    tentativas = 3
                elif (nivel == 0):
                    jogos.escolhe_jogo()
                else:
                    print("Nível inválido. Digite novamente.")
                    print("(1) Fácil (2) Médio (3) Difícil (0) Sair")
                    nivel = int(input("Nivel:"))
            finally:
                advinhar()
                print("Fim de jogo")
                seleciona_nivel()

    def advinhar():
        global pontos
        numero_secreto = random.randrange(1, 101)
        for rodada in range(1, tentativas + 1):
            print("Tentativa {} de {}".format(rodada, tentativas))
            chute = input("Digite o seu número:")
            chute_numero = int(chute)
            print("Voce digitou ", chute)
            global pontuacao
            if (chute_numero < 1 or chute_numero > 100):
                print("Digite um número entre 1 e 100")
                continue
            acertou = (chute_numero == numero_secreto)
            maior = chute_numero > numero_secreto
            menor = chute_numero < numero_secreto

            if (acertou):
                print("Parabéns, você acertou e fez {} pontos".format(pontos))
                break
            else:
                if (maior):
                    print("Você errou. O número é menor do que você chutou")
                    pontos -= 100
                elif (menor):
                    print("Você errou. O número é maior do que você chutou")
                    pontos -= 100



    seleciona_nivel()


if (__name__ == "__main__"):
    jogar()
