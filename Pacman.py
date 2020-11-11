import tkinter as tk
from tkinter import Canvas
import os
from src.user import program_init_user

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size_window_x = 760
size_window_y = 840

fd = open("maps/map_1.txt", "r")
tile_map = fd.read()

IA_params = program_init_user()
IA_params.set_map(tile_map)

class mapping():
    def _init_(self):
        return

    def draw_map(self, canvas):
        posx = 0
        posy = 0
        for block in tile_map:
            if (block == '1'):
                canvas.create_rectangle(posx, posy, posx + 40, posy + 40, fill='black')
            posx += 40
            if (posx >= 800):
                posy += 40
                posx = 0

class Player():
    def __init__(self):
        self.posx = 7
        self.posy = 7
        self.change_pos = 20
        self.rect = [self.posx, self.posy, 13, 13]

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
            self.rect = [self.posx, self.red_posy, 14, 14]
        elif (color == "pink"):
            self.rect = [self.posx, self.pink_posy, 14, 14]
        elif (color == "blue"):
            self.rect = [self.posx, self.blue_posy, 14, 14]
        else:
            self.rect = [self.posx, self.orange_posy, 14, 14]

gui = tk.Tk()
gui.geometry(str(size_window_x) + "x" + str(size_window_y))
gui.resizable(width = False, height = False)
gui.title("Workshop Pacman")
gui['background'] = "#FFFFFF"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@images/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@images/logo.xbm")

#sprite_sheet = tk.PhotoImage(file = "images/pacman.png")

canvas = Canvas(gui, width = size_window_x, height = size_window_y, bd = 0, bg = "white")
canvas.pack(padx = 0, pady = 0)
canvas.focus_set()

obj_map = mapping()
obj_map.draw_map(canvas)

player = Player()
Red_Ghost = Ghost()
Pink_Ghost = Ghost()
Blue_Ghost = Ghost()
Orange_Ghost = Ghost()

def game_loop():

    gui.after(75, game_loop)

gui.after_idle(game_loop)
gui.mainloop()
