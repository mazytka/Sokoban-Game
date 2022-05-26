import pygame

pygame.init()

width = 10
height = 10
tile = 48
fps = 30
title = 'Sokoban game'

color = (255, 0, 0)
black = (0, 0, 0)

window = pygame.display.set_mode((width * tile, height * tile))
pygame.display.set_caption(title)

clock = pygame.time.Clock()


class Player:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


player = Player(width * tile // 2, height * tile // 2, 40, 40, color)
speed = player.width

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player.y > 0:
                player.y -= speed

            if event.key == pygame.K_s and player.y < width * tile - player.width:
                player.y += speed

            if event.key == pygame.K_d and player.x < height * tile - player.height:
                player.x += speed

            if event.key == pygame.K_a and player.x > 0:
                player.x -= speed

    window.fill((0, 0, 0))
    pygame.draw.rect(window, player.color, (player.x, player.y, player.width, player.height))

    pygame.display.update()
pygame.quit()







