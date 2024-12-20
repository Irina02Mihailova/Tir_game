import pygame
import random

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
target_img = pygame.image.load("img/15593439.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
#цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Переменная для подсчета очков
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    # Отображение очков
    score_text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Отображение в верхнем левом углу
    pygame.display.update()

pygame.quit()