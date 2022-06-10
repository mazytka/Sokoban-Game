import pygame

level1 = [
    " #  #  # #",
    "     #    ",
    "    ###   ",
    "          ",
    "  *###  * ",
    " *      & ",
    "    ####  ",
    "   ##     ",
    "        # ",
    "   ###    ",
]



class MoveBox():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        box_lst = []
        lst = lvl1.get_coord_wall()
        lst1 = lvl1.get_coord_box()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.y > 0:
                self.y -= speed
                if (self.x, self.y) in lst:
                    self.y += speed
            elif event.key == pygame.K_s and self.y < screen_stat['width'] * screen_stat['tile'] - player.width:
                self.y += speed
                if (self.x, self.y) in lst:
                    self.y -= speed

                if (self.x, self.y) in lst1:
                    box_lst.append((self.x, self.y))
                    print(box_lst)


            elif event.key == pygame.K_d and self.x < screen_stat['height'] * screen_stat['tile'] - player.height:
                self.x += speed
                if (self.x, self.y) in lst:
                    self.x -= speed
            elif event.key == pygame.K_a and self.x > 0:
                self.x -= speed
                if (self.x, self.y) in lst:
                    self.x += speed


class Player(pygame.sprite.Sprite, MoveBox):

    def __init__(self, x, y, width_player, height_player):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width_player
        self.height = height_player
        self.image = pygame.transform.scale(pygame.image.load('png/player.PNG'), (40, 40))


class Box(pygame.sprite.Sprite, MoveBox):

    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        self.image = pygame.transform.scale(pygame.image.load('png/box.png'), (40, 40))

    def revove(self):
        print(self.lst)

class Wall(pygame.surface.Surface):

    def __init__(self):

        pygame.surface.Surface.__init__(self, (40, 40))
        self.image = pygame.transform.scale(pygame.image.load('png/wall.png'), (40, 40))


class GenerateLevel:

    def __init__(self, level, coord_x=0, coord_y=0):
        self.level = level
        self.coord_x = coord_x
        self.coord_y = coord_y

    def get_lvl(self):

        self.box = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * screen_stat['tile']
                self.coord_y = y * screen_stat['tile']

                if self.level[y][x] == "#":
                    window.blit(wall.image, (self.coord_x, self.coord_y))

                if self.level[y][x] == "*":
                    window.blit(box.image, (self.coord_x, self.coord_y))
                    self.box.add(box)

                if self.level[y][x] == "&":
                    window.blit(player.image, (player.x, player.y))

    def get_coord_wall(self):
        lst = []
        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * 40
                self.coord_y = y * 40
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

    def get_coord_box(self):
        lst = []
        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                self.coord_x = x * 40
                self.coord_y = y * 40
                if self.level[y][x] == "*":
                    lst.append((self.coord_x, self.coord_y))
        return lst

    def collision(self):
        player = self.player.sprite
        player.rect.x += speed
        for sprite in self.box.sprites():
            if sprite.rect.colliderect(player.rect):
                print('gre')


lvl1 = GenerateLevel(level1)

player = Player(lvl1.get_coord_player()[0][0], lvl1.get_coord_player()[0][1], 40, 40)
box = Box(lvl1.get_coord_box())
print(lvl1.get_coord_box()[0][0], lvl1.get_coord_box()[0][1])
wall = Wall()
pygame.init()
screen_stat = {'width': 10, 'height': 10, 'tile': 40}
fps = 30
title = 'Sokoban game'

black = (0, 0, 0)
display = (screen_stat['width'] * screen_stat['tile'], screen_stat['height'] * screen_stat['tile'])
window = pygame.display.set_mode(display)

pygame.display.set_caption(title)







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
