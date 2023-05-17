import jogos
import random

def  jogar():
    try:
        boas_vindas()
        palavra_secreta = gera_palavra_secreta()
        letras_acertadas = gera_template_dicas(palavra_secreta)
        print(letras_acertadas)
        loop_tentativas(palavra_secreta,letras_acertadas)
    finally:
        jogos.escolhe_jogo()


def boas_vindas():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")


def gera_palavra_secreta():
    with open("adivinhacao_palavras.txt", 'r') as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    arquivo.close()
    sorteada = random.randrange(0, len(palavras))
    palavra_secreta = palavras[sorteada].upper()
    return palavra_secreta


def gera_template_dicas(palavra):
    return ["_" for letra in palavra]


def recebe_chute():
    chute = input("Escolha uma letra: ")
    return chute.strip().upper()


def imprime_letras_acertadas(chute,palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def loop_tentativas(palavra_secreta, letras_acertadas):
    enforcou = False
    acertou = False
    tentativas = 7
    while (not enforcou and not acertou):
        chute = recebe_chute()
        if (chute in palavra_secreta):
            imprime_letras_acertadas(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas -= 1
            desenha_forca(tentativas)
            if(tentativas > 0):
                print("Você errou e ainda tem {} tentativas de 7".format(tentativas))
            else:
                break
        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        mensagem_ganhou(palavra_secreta)
    else:
        mensagem_perdeu(palavra_secreta)


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")
    erros = tentativas
    erros += 1
    if(erros == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_ganhou(palavra_secreta):
    print("Você acertou! Parabéns, palavra era {}!".format(palavra_secreta))
    print("        .-=========-.")
    print("        |'-=======-'|")
    print("        _|   .=.   |_")
    print("       ((|  {{1}}  |))")
    print("        \|   /|\   |/")
    print("         \__ '`' __/")
    print("           _`) (`_")
    print("         _/_______\_")
    print("         |_________|")


def mensagem_perdeu(palavra_secreta):
    print("Você perdeu. A palavra era {}".format(palavra_secreta))
    print("                       ______")
    print("                    .-\"      \"-.")
    print("                   /            \\")
    print("       _          |              |          _")
    print("      ( \\         |,  .-.  .-.  ,|         / )")
    print("       > \"=._     | )(__/  \\__)( |     _.=\" <")
    print("      (_/\"=._\"=._ |/     /\\     \\| _.=\"_.=\"\\_)")
    print("             \"=._ (_     ^^     _)\"_.=\"")
    print("                 \"=\\__|IIIIII|__/=\"")
    print("                _.=\"| \\IIIIII/ |\"=._")
    print("      _     _.=\"_.=\"\\          /\"=._\"=._     _")
    print("     ( \\_.=\"_.=\"     `--------`     \"=._\"=._/ )")
    print("      > _.=\"                            \"=._ <")
    print("     (_/                                    \\_)")


if(__name__ == "__main__"):
    jogar()