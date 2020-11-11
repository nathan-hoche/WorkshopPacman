import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size_window_x = 760
size_window_y = 840

running = True
fd = open("maps/map_1.txt", "r")
tile_map = fd.read()

pygame.init()
screen = pygame.display.set_mode([size_window_x, size_window_y])
sprite_sheet = pygame.image.load("images/pacman.png").convert()

class mapping():
    def _init_(self):
        return

    def draw_map(self, screen):
        posx = 0
        posy = 0
        for block in tile_map:
            if (block == '1'):
                pygame.draw.rect(screen, BLACK, (posx, posy, 40, 40))
            posx += 40
            if (posx >= 800):
                posy += 40
                posx = 0

class Player():
    def __init__(self):
        self.sprit = pygame.sprite.Sprite()
        self.posx = 7
        self.posy = 7
        self.change_pos = 20
        self.rect = sprite_sheet.get_rect()
        #slef.rect. self.posx, self.posy, 13, 13)

    def animation(self):
        global sprite_sheet
        self.rect.x += self.change_pos
        if (self.rect.x >= (2 * self.change_pos)):
            self.rect.x = self.posx
        sprite_sheet.rect()


class Ghost():
    def __init__(self):
        self.posx = 127
        self.red_posy = 87
        self.pink_posy = 107
        self.blue_posy = 127
        self.orange_posy = 147
        self.change_pos = 20
        self.rect = None

    def animation(self):
        self.rect.x += self.change_pos
        if (self.rect.x >= (2 * self.change_pos)):
            self.rect.x = self.posx

    def init_ghost(self, color):
        if (color == "red"):
            self.rect = pygame.rect(self.posx, self.red_posy, 14, 14)
        elif (color == "pink"):
            self.rect = pygame.rect(self.posx, self.pink_posy, 14, 14)
        elif (color == "blue"):
            self.rect = pygame.rect(self.posx, self.blue_posy, 14, 14)
        else:
            self.rect = pygame.rect(self.posx, self.orange_posy, 14, 14)

#def set_sound():
    #pygame.mixer.music.load("music/willy-la-chanson-de-pac-man-audio.mp3")
    #pygame.mixer.music.play(loops = -1)
    #win_sound = pygame.mixer.Sound("music/win.ogg")
    #lose_sound = pygame.mixer.Sound("music/lose.ogg")


obj_map = mapping()
player = Player()
Ghost = Ghost()
#set_sound()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    obj_map.draw_map(screen)

    #all_sprites = pygame.sprite.Group()
    #all_sprites.add(player)
    
    pygame.display.flip()

pygame.quit()