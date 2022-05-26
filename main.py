import pygame

pygame.init()

width = 800
height = 640
fps = 30
title = 'Sokoban game'

color = (255, 0, 0)
black = (0, 0, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = pygame.time.Clock()


class Player:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


player = Player(400, 400, 40, 40, color)
speed = player.width

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.y -= speed

            if event.key == pygame.K_s:
                player.y += speed

            if event.key == pygame.K_d:
                player.x += speed

            if event.key == pygame.K_a:
                player.x -= speed

    window.fill((0, 0, 0))
    pygame.draw.rect(window, player.color, (player.x, player.y, player.width, player.height))

    pygame.display.update()
pygame.quit()







