import random
import pygame
from pygame.constants import QUIT

pygame.init()

FPS = pygame.time.Clock()
HEIGHT = 600
WIDTH = 800
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]
plain = True

while plain:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            plain = False
    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_speed = random.choice(([1, -1], [-1, -1]))
    if player_rect.top <= 0:
        player_speed = random.choice(([-1, 1], [1, 1]))
    if player_rect.right >= WIDTH:
        player_speed = random.choice(([-1, -1], [-1, 1]))
    if player_rect.left <= 0:
        player_speed = random.choice(([1, 1], [1, -1]))

    player_rect = player_rect.move(player_speed)
    main_display.blit(player, player_rect)
    pygame.display.flip()