import pygame
import random
from pygame.locals import *

def grade_jogo():
    x = random.randint(0,390)
    y = random.randint(0,290)
    return (x//10 * 10, y//10 * 10)

def comer(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def jogar():
    pygame.init()

    # definição de tela
    tela_tamanho = [400, 300]
    tela_largura = tela_tamanho[0]
    tela_altura = tela_tamanho[1]
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    pygame.display.set_caption("Cobrinha")
    fps = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # definição dos elementos
    cobra = [(250, 250), (260, 250), (270, 250)]
    cobrinha = pygame.Surface((10, 10))
    cobrinha.fill((255, 255, 255))
    fruta = pygame.Surface((10, 10))
    fruta.fill(("blue"))
    fruta_pos = grade_jogo()

    # variáveis do controle
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    direcao = LEFT
    pontuacao = 0


    while True:
        fps.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            # entradas do usuário
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    direcao = UP
                if event.key == K_DOWN:
                    direcao = DOWN
                if event.key == K_LEFT:
                    direcao = LEFT
                if event.key == K_RIGHT:
                    direcao = RIGHT

        # confere se comeu a fruta e adiciona pontos
        if comer(cobra[0], fruta_pos):
            fruta_pos = grade_jogo()
            cobra.append((0, 0))
            pontuacao += 100

        # aumenta a cobra
        for i in range(len(cobra) - 1, 0, -1):
            cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

        # direção em que o tupple aumenta
        if direcao == UP:
            cobra[0] = (cobra[0][0], cobra[0][1] - 10)
        if direcao == DOWN:
            cobra[0] = (cobra[0][0], cobra[0][1] + 10)
        if direcao == RIGHT:
            cobra[0] = (cobra[0][0] + 10, cobra[0][1])
        if direcao == LEFT:
            cobra[0] = (cobra[0][0] - 10, cobra[0][1])

        #batida da cobra e gameover
        if cobra[0] in cobra[1:] or cobra[0][0] < 0 or cobra[0][0] >= tela.get_width() or cobra[0][1] < 0 or cobra[0][1] >= tela.get_height():
            game_over(pontuacao, tela, font)
            break

        # exibe tela e fruta
        tela.fill((0, 0, 0))
        tela.blit(fruta, fruta_pos)

        # exibe a cobra
        for i in cobra:
            tela.blit(cobrinha, i)
        pygame.display.update()

def game_over(pontuacao, tela, font):
    mensagem_game_over = font.render("Game Over", True, (255, 255, 255))
    mensagem_pontuacao = font.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    tela.blit(mensagem_game_over, (tela.get_width() // 2 - mensagem_game_over.get_width() // 2, tela.get_height() // 2 - mensagem_game_over.get_width() // 2))
    tela.blit(mensagem_pontuacao, (tela.get_width() // 2 - mensagem_pontuacao.get_width() // 2,
                                 tela.get_height() // 2 - mensagem_pontuacao.get_height() // 2 + 50))
    pygame.display.flip()
    pygame.time.wait(4000)
    print("Game Over")


if(__name__ == "__main__"):
    jogar()
