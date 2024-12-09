from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import random
from pygame.examples.scrap_clipboard import screen

pygame.init()

#размер экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#заголовок
pygame.display.set_caption("Игра Тир")
#иконка
icon = pygame.image.load("img/1.jpg")
pygame.display.set_icon(icon)
#цель
target_img = pygame.image.load("img/2.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

runnig = True
while runnig:
    pass

pygame.quit()