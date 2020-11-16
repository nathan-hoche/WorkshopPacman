size_window = [760, 840]
tile_map = None
player_pos = [0, 0]
block_size = 40

ghost_pos_red = [400, 400]
ghost_pos_pink = [440, 400]
ghost_pos_blue = [480, 400]
ghost_pos_orange = [440, 440]

class user():
    def __init__(self):
        return

    def get_size_screen(self):
        global size_window
        return size_window

    def get_pos_player(self):
        global player_pos
        return player_pos

    def get_map(self):
        global tile_map
        return tile_map

    def move_ghost_up(self, ghost_type):
        if (ghost_type == "red"):
            global ghost_pos_red
            ghost_pos_red[1] += 40
        elif (ghost_type == "pink"):
            global ghost_pos_pink
            ghost_pos_pink[1] += 40
        elif (ghost_type == "blue"):
            global ghost_pos_blue
            ghost_pos_blue[1] += 40
        else:
            global ghost_pos_orange
            ghost_pos_orange[1] += 40

    def move_ghost_down(self, ghost_type):
        if (ghost_type == "red"):
            global ghost_pos_red
            ghost_pos_red[1] -= 40
        elif (ghost_type == "pink"):
            global ghost_pos_pink
            ghost_pos_pink[1] -= 40
        elif (ghost_type == "blue"):
            global ghost_pos_blue
            ghost_pos_blue[1] -= 40
        else:
            global ghost_pos_orange
            ghost_pos_orange[1] -= 40

    def move_ghost_left(self, ghost_type):
        if (ghost_type == "red"):
            global ghost_pos_red
            ghost_pos_red[0] -= 40
        elif (ghost_type == "pink"):
            global ghost_pos_pink
            ghost_pos_pink[0] -= 40
        elif (ghost_type == "blue"):
            global ghost_pos_blue
            ghost_pos_blue[0] -= 40
        else:
            global ghost_pos_orange
            ghost_pos_orange[0] -= 40

    def move_ghost_right(self, ghost_type):
        if (ghost_type == "red"):
            global ghost_pos_red
            ghost_pos_red[0] += 40
        elif (ghost_type == "pink"):
            global ghost_pos_pink
            ghost_pos_pink[0] += 40
        elif (ghost_type == "blue"):
            global ghost_pos_blue
            ghost_pos_blue[0] += 40
        else:
            global ghost_pos_orange
            ghost_pos_orange[0] += 40

class program_init_user():
    def __init__(self):
        return

    def get_ia_ghost_pos(self, ghost_type):
        if (ghost_type == "Red"):
            global ghost_pos_red
            return ghost_pos_red
        elif (ghost_type == "Pink"):
            global ghost_pos_pink
            return ghost_pos_pink
        elif (ghost_type == "Blue"):
            global ghost_pos_blue
            return ghost_pos_blue
        else:
            global ghost_pos_orange
            return ghost_pos_orange

    def set_map(self, map_1):
        global tile_map
        tile_map = map_1

    def set_player_pos(self, pos):
        global player_pos
        player_pos = pos