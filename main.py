import pygame
import time
import random
import sys

pygame.init()

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Snake game')


snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont('Verdana', 24)
score_style = pygame.font.SysFont('Verdana', 18)


def your_score(score):
    value = score_style.render("Your Score: " + str(score), True, BLACK_COLOR)
    screen.blit(value, [0, 0])


def our_snake(snake_bl, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK_COLOR, [x[0], x[1], snake_bl, snake_bl])


def message(msg, color):
    txt = font_style.render(msg, True, color)
    txt_rect = txt.get_rect()
    txt_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(txt, txt_rect)


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(WHITE_COLOR)
            message("You Lost! Press Q-Quit or C-Play Again", RED_COLOR)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= (WIDTH - snake_block) or x1 < 0 or y1 >= (HEIGHT - snake_block) or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(WHITE_COLOR)
        pygame.draw.rect(screen, BLUE_COLOR, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

            length_of_snake += 1
        clock.tick(snake_speed)

    pygame.display.update()


game_loop()
