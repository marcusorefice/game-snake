from random import randint
import pygame
from pygame.locals import *
# from pygame.event import QUIT, KEYDOWN, K_RIGHT, K_UP, K_LEFT, K_DOWN


#Alinha para aparecer a maçã no mesmo grid da cobra
def on_grid_random():
    x = randint(0, 490)
    y = randint(0, 490)
    return (x//10 * 10, y//10 *10)

#Verificar colisão
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Iniciar o pygame e definir o tamanho da tela
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

#Posição da cobra
snake = [(200, 200), (210, 200), (220, 200)]
#Tamanho da cobra
snake_skin = pygame.Surface((10, 10))
#Cor da cobra (branca)
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
#Tamanho da maçã
apple = pygame.Surface((10, 10))
#Cor da maçã
apple.fill((255, 0, 0))

#Lado que a cobra começa
my_direction = LEFT

clock = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    #Velocidade da cobra
    clock.tick(20)
    for event in pygame.event.get():
        #Fechar o jogo
        if event.type == QUIT:
            pygame.QUIT()

        #Direção da cobra pelo teclado
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    
    

    #Se houver colisão da cobra com a maçã, a maçã aparece em outro lugar e aumenta o tamanho da cobra
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1

    #Se vai colidir com as bordas
    if snake[0][0] == 500 or snake[0][1] == 500 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    #Se vai colidir com ela mesmo
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake [0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Mudar direção da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
   
    #Limpar a tela    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    #Desenhar linhas na vertical e horizontal
    for x in range(0, 500, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 500))
    for y in range(0, 500, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (500, y))

    #Adicionar score no jogo
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500 -120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

#Adicionar Game Over na tela
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (500 / 2, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
