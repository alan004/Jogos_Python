import jogos
def  jogar():
    import random
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")

    with open("palavras.txt", 'r') as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    arquivo.close()
    sorteada = random.randrange(0, len(palavras))
    palavra_secreta = palavras[sorteada].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Escolha uma letra: ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Você errou. Você ainda tem {} tentativas.".format(6-tentativas))

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou! Parabéns, palavra era {}!".format(palavra_secreta))
    else:
        print("Você perdeeu :(")
    print("Fim de jogo")
    quit()

if(__name__ == "__main__"):
    jogar()