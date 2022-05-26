import pygame

level1 = [
    " #  #  # #",
    "  #   #   ",
    "  #     # ",
    "     ##   ",
    "    #     ",
    "          ",
    "    #     ",
    "          ",
    "   &   #  ",
    "          ",
]


class Player:

    def __init__(self, x, y, width_player, height_player, ):
        self.x = x
        self.y = y
        self.width = width_player
        self.height = height_player

    def move(self):

        lst = lvl1.get_coord_wall()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.y > 0:
                self.y -= speed
                if (self.x, self.y) in lst:
                    self.y += speed
            if event.key == pygame.K_s and self.y < screen_stat['width'] * screen_stat['tile'] - self.width:
                self.y += speed
                if (self.x, self.y) in lst:
                    self.y -= speed
            if event.key == pygame.K_d and self.x < screen_stat['height'] * screen_stat['tile'] - self.height:
                self.x += speed
                if (self.x, self.y) in lst:
                    self.x -= speed
            if event.key == pygame.K_a and self.x > 0:
                self.x -= speed
                if (self.x, self.y) in lst:
                    self.x += speed


class GenerateLevel:

    def __init__(self, level, coord_x=0, coord_y=0):
        self.level = level
        self.coord_x = coord_x
        self.coord_y = coord_y

    def get_lvl(self):

        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * screen_stat['tile']
                self.coord_y = y * screen_stat['tile']

                if self.level[y][x] == "#":
                    window.blit(wall, (self.coord_x, self.coord_y))

                if self.level[y][x] == "*":
                    window.blit(box, (self.coord_x, self.coord_y))

                if self.level[y][x] == "&":
                    window.blit(person, (player.x, player.y))

    def get_coord_wall(self):
        lst = []
        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * screen_stat['tile']
                self.coord_y = y * screen_stat['tile']
                if self.level[y][x] == "#":
                    lst.append((self.coord_x, self.coord_y))
        return lst

    def get_coord_player(self):
        lst = []
        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * 40
                self.coord_y = y * 40
                if self.level[y][x] == "&":
                    lst.append((self.coord_x, self.coord_y))
        return lst


lvl1 = GenerateLevel(level1)

player = Player(lvl1.get_coord_player()[0][0], lvl1.get_coord_player()[0][1], 40, 40)

pygame.init()
screen_stat = {'width': 10, 'height': 10, 'tile': 40}
fps = 30
title = 'Sokoban game'


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

        player.move()

    window.fill((135, 206, 250))

    lvl1.get_lvl()

    pygame.display.update()
pygame.quit()
