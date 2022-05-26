import pygame

color = (255, 0, 0)

level = [
    "##########",
    "#        #",
    "#        #",
    "#        #",
    "#      & #",
    "#        #",
    "#   *    #",
    "#        #",
    "#        #",
    "##########",
]


class Player:

    def __init__(self, x, y, width_player, height_player, color_player):
        self.x = x
        self.y = y
        self.width = width_player
        self.height = height_player
        self.color = color_player


player = Player(40, 40, 40, 40, color)

pygame.init()
screen_stat = {'width': 10, 'height': 10, 'tile': 40}
fps = 30
title = 'Sokoban game'

color = (255, 0, 0)
black = (0, 0, 0)
display = (screen_stat['width']*screen_stat['tile'], screen_stat['height']*screen_stat['tile'])
window = pygame.display.set_mode(display)

pygame.display.set_caption(title)

player_image = pygame.image.load('png/player.PNG')
person = pygame.transform.scale(player_image, (screen_stat['tile'], screen_stat['tile']))

wall_image = pygame.image.load('png/wall.png')
wall = pygame.transform.scale(wall_image, (screen_stat['tile'], screen_stat['tile']))

box_image = pygame.image.load('png/box.png')
box = pygame.transform.scale(box_image, (screen_stat['tile'],
                                         screen_stat['tile']))

clock = pygame.time.Clock()


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

            if event.key == pygame.K_s and player.y < screen_stat['width'] * screen_stat['tile'] - player.width:
                player.y += speed

            if event.key == pygame.K_d and player.x < screen_stat['height'] * screen_stat['tile'] - player.height:
                player.x += speed

            if event.key == pygame.K_a and player.x > 0:
                player.x -= speed

    window.fill((135, 206, 250))
    for x in range(len(level)):
        for y in range(len(level[x])):
            coord_x = x * screen_stat['tile']
            coord_y = y * screen_stat['tile']

            if level[y][x] == "#":
                window.blit(wall, (coord_x, coord_y))
            if level[y][x] == "*":
                window.blit(box, (coord_x, coord_y))
            if level[y][x] == "&":
                pass

    pygame.draw.rect(window, player.color, (player.x, player.y, player.width, player.height))

    pygame.display.update()
pygame.quit()







