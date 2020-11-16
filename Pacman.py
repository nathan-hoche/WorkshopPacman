import tkinter as tk
from tkinter import Canvas
import os
from src.user import program_init_user
import time
from IA import launch_ia

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size_window_x = 760
size_window_y = 840

fd = open("maps/map_1.txt", "r")
tile_map = fd.read()
split_tile_map = tile_map.split('\n')

pacgome = list(split_tile_map)

IA_params = program_init_user()
IA_params.set_map(split_tile_map)

IA_ghost = launch_ia()

class mapping():
    def __init__(self):
        self.pcgome_list = []

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
    
    def draw_pacgome(self, canvas):
        posx = 0
        posy = 0
        is_stop = 0
        if (len(self.pcgome_list) != 0):
            for sprite in self.pcgome_list:
                canvas.delete(sprite)
            self.pcgome_list = []
        for block in pacgome:
            for char in block:
                if (char == '0'):
                    self.pcgome_list.append(canvas.create_rectangle(posx + 16, posy + 16, posx + 20, posy + 20, fill='yellow'))
                    is_stop = 1
                posx += 40
            posy += 40
            posx = 0
        if (is_stop != 1):
            print("Pacman win!")
            gui.quit()

class Player():
    def __init__(self, canvas):
        self.sprite = None
        self.frame = 0
        self.pacman = None
        self.posPacman = [40, 40]
        self.posPacmanMap = [1, 1]
        self.keyActu = 'Left'
        self.canvas = canvas
        self.keypress = time.monotonic_ns()
        self.ghost_move = time.monotonic_ns()

    def animate(self, event):
        global IA_params
        global split_tile_map
        global pacgome
        Key = event.keysym

        if (time.monotonic_ns() - self.keypress >= 150000000):
            if Key == 'Up':
                val2 = int(split_tile_map[self.posPacmanMap[0] - 1][self.posPacmanMap[1]])

                if (val2 == 0 or val2 == 2):
                    self.posPacman[0] -= 40
                    self.posPacmanMap[0] -= 1
                    self.keyActu = 'Up'
            elif Key == 'Down':
                val2 = int(split_tile_map[self.posPacmanMap[0] + 1][self.posPacmanMap[1]])
                
                if (val2 == 0 or val2 == 2):
                    self.posPacman[0] += 40
                    self.posPacmanMap[0] += 1
                    self.keyActu = 'Down'
            elif Key == 'Left':
                val2 = int(split_tile_map[self.posPacmanMap[0]][self.posPacmanMap[1] - 1])
                
                if (val2 == 0 or val2 == 2):
                    self.posPacman[1] -= 40
                    self.posPacmanMap[1] -= 1
                    self.keyActu = 'Left'
            elif Key == 'Right':
                val2 = int(split_tile_map[self.posPacmanMap[0]][self.posPacmanMap[1] + 1])
                
                if (val2 == 0 or val2 == 2):
                    self.posPacman[1] += 40
                    self.posPacmanMap[1] += 1
                    self.keyActu = 'Right'
            tmp = list(pacgome[self.posPacmanMap[0]])
            tmp[self.posPacmanMap[1]] = "2"
            pacgome[self.posPacmanMap[0]] = tmp
            self.keypress = time.monotonic_ns()

        IA_params.set_player_pos(self.posPacman)

    def update_pacman(self):
        if self.sprite != None:
            self.canvas.delete(self.sprite)

        self.pacman = tk.PhotoImage(file = "images/gif/pacman{}.gif".format(self.keyActu), format="gif -index {}".format(self.frame))
        self.sprite = self.canvas.create_image(self.posPacman[1], self.posPacman[0], anchor=tk.NW, image=self.pacman)
        self.frame += 1
        
        if self.frame == 3:
            self.frame = 0

        if (time.monotonic_ns() - self.ghost_move >= 400000000):
            if (IA_params.get_ia_ghost_Map("Red") == self.posPacmanMap or
            IA_params.get_ia_ghost_Map("Blue") == self.posPacmanMap or
            IA_params.get_ia_ghost_Map("Pink") == self.posPacmanMap or
            IA_params.get_ia_ghost_Map("Orange") == self.posPacmanMap):
                gui.quit()
            self.ghost_move = time.monotonic_ns()
            

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
        self.sprite = canvas.create_image(self.pos_ghost[1], self.pos_ghost[0], anchor=tk.NW, image=self.pacman)
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
    obj_map.draw_pacgome(canvas)
    player.update_pacman()
    Red_Ghost.update_ghost(canvas)
    Pink_Ghost.update_ghost(canvas)
    Blue_Ghost.update_ghost(canvas)
    Orange_Ghost.update_ghost(canvas)
    IA_ghost.main_ia()
    gui.after(75, game_loop)

gui.after_idle(game_loop)
gui.mainloop()