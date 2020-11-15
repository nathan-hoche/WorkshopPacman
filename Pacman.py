import tkinter as tk
from tkinter import Canvas
import os
from src.user import program_init_user
import time

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
                canvas.create_rectangle(posx, posy, posx + 40, posy + 40, fill='white')
            posx += 40
            if (posx >= 800):
                posy += 40
                posx = 0

class Player():
    def __init__(self, canvas):
        self.sprite = None
        self.frame = 0
        self.pacman = None
        self.posPacman = [0, 0]
        self.keyActu = 'Left'
        self.canvas = canvas
        self.keypress = time.monotonic_ns()

    def animate(self, event):
        global IA_params
        Key = event.keysym

        if (time.monotonic_ns() - self.keypress >= 200000000):
            if Key == 'Up':
                self.posPacman[1] -= 40
                self.keyActu = 'Up'
            elif Key == 'Down':
                self.posPacman[1] += 40
                self.keyActu = 'Down'
            elif Key == 'Left':
                self.posPacman[0] -= 40
                self.keyActu = 'Left'
            elif Key == 'Right':
                self.posPacman[0] += 40
                self.keyActu = 'Right'
            self.keypress = time.monotonic_ns()

        IA_params.set_player_pos(self.posPacman)

    def update_pacman(self):
        if self.sprite != None:
            self.canvas.delete(self.sprite)
        self.pacman = tk.PhotoImage(file = "images/gif/pacman{}.gif".format(self.keyActu), format="gif -index {}".format(self.frame))
        self.sprite = self.canvas.create_image(self.posPacman[0], self.posPacman[1], anchor=tk.NW, image=self.pacman)
        self.frame += 1
        if self.frame == 3:
            self.frame = 0

class Ghost():
    def __init__(self, color):
        self.color = color
        self.sprite = None
        self.frame = 0
        self.pos_ghost = [0, 0]

    def update_ghost(self, canvas):
        global IA_params

        self.pos_ghost = IA_params.get_ia_ghost_pos(self.color)
        
        if self.sprite != None:
            canvas.delete(self.sprite)
        
        self.pacman = tk.PhotoImage(file = "images/gif/ghost{}.gif".format(self.color), format="gif -index {}".format(self.frame))
        self.sprite = canvas.create_image(self.pos_ghost[0], self.pos_ghost[1], anchor=tk.NW, image=self.pacman)
        self.frame += 1
        if self.frame == 2:
            self.frame = 0

gui = tk.Tk()
gui.geometry(str(size_window_x) + "x" + str(size_window_y))
gui.resizable(width = False, height = False)
gui.title("Workshop Pacman")
gui['background'] = "#FFFFFF"

if "nt" == os.name:
    gui.wm_iconbitmap(bitmap = "@images/logo.ico")
else:
    gui.wm_iconbitmap(bitmap = "@images/logo.xbm")

canvas = Canvas(gui, width = size_window_x, height = size_window_y, bd = 0, bg = "black")
canvas.pack(padx = 0, pady = 0)
canvas.focus_set()

obj_map = mapping()
obj_map.draw_map(canvas)

player = Player(canvas)
Red_Ghost = Ghost("Red")
Pink_Ghost = Ghost("Pink")
Blue_Ghost = Ghost("Blue")
Orange_Ghost = Ghost("Orange")

canvas.bind('<Key>', player.animate)

def game_loop():
    player.update_pacman()
    Red_Ghost.update_ghost(canvas)
    Pink_Ghost.update_ghost(canvas)
    Blue_Ghost.update_ghost(canvas)
    Orange_Ghost.update_ghost(canvas)
    
    gui.after(75, game_loop)

gui.after_idle(game_loop)
gui.mainloop()
