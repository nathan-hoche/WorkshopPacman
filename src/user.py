size_window = [760, 840]
split_tile_map = None
player_pos = [1, 1]
block_size = 40

ghost_pos_red = [360 + 10, 320 + 10]
ghost_pos_pink = [360 + 10, 360 + 10]
ghost_pos_blue = [360 + 10, 400 + 10]
ghost_pos_orange = [320 + 10, 360 + 10]

ghost_pos_red_map = [9, 8]
ghost_pos_pink_map = [9, 9]
ghost_pos_blue_map = [9, 10]
ghost_pos_orange_map = [8, 9]

already_move = [0, 0, 0, 0]

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
        global split_tile_map
        return split_tile_map

    def move_ghost_up(self, ghost_type):
        global split_tile_map
        global already_move

        if (already_move[0] == 1):
            return

        if (ghost_type == "Red" and already_move[0] == 0):
            global ghost_pos_red
            global ghost_pos_red_map
            val = int(split_tile_map[ghost_pos_red_map[0] - 1][ghost_pos_red_map[1]])
            

            if (val == 0 or val == 2):
                ghost_pos_red[0] -= 40
                ghost_pos_red_map[0] -= 1
                already_move[0] = 1
        elif (ghost_type == "Pink" and already_move[1] == 0):
            global ghost_pos_pink
            global ghost_pos_pink_map
            val = int(split_tile_map[ghost_pos_pink_map[0] - 1][ghost_pos_pink_map[1]])
            

            if (val == 0 or val == 2):
                ghost_pos_pink_map[0] -= 1
                ghost_pos_pink[0] -= 40
                already_move[1] = 1
        elif (ghost_type == "Blue" and already_move[2] == 0):
            global ghost_pos_blue
            global ghost_pos_blue_map
            val = int(split_tile_map[ghost_pos_blue_map[0] - 1][ghost_pos_blue_map[1]])
            

            if (val == 0 or val == 2):
                ghost_pos_blue_map[0] -= 1
                ghost_pos_blue[0] -= 40
                already_move[2] = 1
        elif (ghost_type == "Orange" and already_move[3] == 0):
            global ghost_pos_orange
            global ghost_pos_orange_map
            val = int(split_tile_map[ghost_pos_orange_map[0] - 1][ghost_pos_orange_map[1]])
            

            if (val == 0 or val == 2):
                ghost_pos_orange_map[0] -= 1
                ghost_pos_orange[0] -= 40
                already_move[3] = 1

    def move_ghost_down(self, ghost_type):
        global split_tile_map
        global already_move

        if (already_move[1] == 1):
            return

        if (ghost_type == "Red" and already_move[0] == 0):
            global ghost_pos_red
            global ghost_pos_red_map
            val = int(split_tile_map[ghost_pos_red_map[0] + 1][ghost_pos_red_map[1]])

            if (val == 0 or val == 2):
                ghost_pos_red[0] += 40
                ghost_pos_red_map[0] += 1
                already_move[0] = 1
        elif (ghost_type == "Pink" and already_move[1] == 0):
            global ghost_pos_pink
            global ghost_pos_pink_map
            val = int(split_tile_map[ghost_pos_pink_map[0] + 1][ghost_pos_pink_map[1]])

            if (val == 0 or val == 2):
                ghost_pos_pink_map[0] += 1
                ghost_pos_pink[0] += 40
                already_move[1] = 1
        elif (ghost_type == "Blue" and already_move[2] == 0):
            global ghost_pos_blue
            global ghost_pos_blue_map
            val = int(split_tile_map[ghost_pos_blue_map[0] + 1][ghost_pos_blue_map[1]])

            if (val == 0 or val == 2):
                ghost_pos_blue_map[0] += 1
                ghost_pos_blue[0] += 40
                already_move[2] = 1
        elif (ghost_type == "Orange" and already_move[3] == 0):
            global ghost_pos_orange
            global ghost_pos_orange_map
            val = int(split_tile_map[ghost_pos_orange_map[0] + 1][ghost_pos_orange_map[1]])

            if (val == 0 or val == 2):
                ghost_pos_orange_map[0] += 1
                ghost_pos_orange[0] += 40
                already_move[3] = 1

    def move_ghost_left(self, ghost_type):
        global split_tile_map
        global already_move

        if (ghost_type == "Red" and already_move[0] == 0):
            global ghost_pos_red
            global ghost_pos_red_map
            val = int(split_tile_map[ghost_pos_red_map[0]][ghost_pos_red_map[1] - 1])

            if (val == 0 or val == 2):
                ghost_pos_red[1] -= 40
                ghost_pos_red_map[1] -= 1
                already_move[0] = 1
        elif (ghost_type == "Pink" and already_move[1] == 0):
            global ghost_pos_pink
            global ghost_pos_pink_map
            val = int(split_tile_map[ghost_pos_pink_map[0]][ghost_pos_pink_map[1] - 1])

            if (val == 0 or val == 2):
                ghost_pos_pink_map[1] -= 1
                ghost_pos_pink[1] -= 40
                already_move[1] = 1
        elif (ghost_type == "Blue" and already_move[2] == 0):
            global ghost_pos_blue
            global ghost_pos_blue_map
            val = int(split_tile_map[ghost_pos_blue_map[0]][ghost_pos_blue_map[1] - 1])

            if (val == 0 or val == 2):
                ghost_pos_blue_map[1] -= 1
                ghost_pos_blue[1] -= 40
                already_move[2] = 1
        elif (ghost_type == "Orange" and already_move[3] == 0):
            global ghost_pos_orange
            global ghost_pos_orange_map
            val = int(split_tile_map[ghost_pos_orange_map[0]][ghost_pos_orange_map[1] - 1])

            if (val == 0 or val == 2):
                ghost_pos_orange_map[1] -= 1
                ghost_pos_orange[1] -= 40
                already_move[3] = 1

    def move_ghost_right(self, ghost_type):
        global split_tile_map
        global already_move

        if (already_move[3] == 1):
            return

        if (ghost_type == "Red" and already_move[0] == 0):
            global ghost_pos_red
            global ghost_pos_red_map
            val = int(split_tile_map[ghost_pos_red_map[0]][ghost_pos_red_map[1] + 1])

            if (val == 0 or val == 2):
                ghost_pos_red[1] += 40
                ghost_pos_red_map[1] += 1
                already_move[0] = 1
        elif (ghost_type == "Pink" and already_move[1] == 0):
            global ghost_pos_pink
            global ghost_pos_pink_map
            val = int(split_tile_map[ghost_pos_pink_map[0]][ghost_pos_pink_map[1] + 1])

            if (val == 0 or val == 2):
                ghost_pos_pink_map[1] += 1
                ghost_pos_pink[1] += 40
                already_move[1] = 1
        elif (ghost_type == "Blue" and already_move[2] == 0):
            global ghost_pos_blue
            global ghost_pos_blue_map
            val = int(split_tile_map[ghost_pos_blue_map[0]][ghost_pos_blue_map[1] + 1])

            if (val == 0 or val == 2):
                ghost_pos_blue_map[1] += 1
                ghost_pos_blue[1] += 40
                already_move[2] = 1
        elif (ghost_type == "Orange" and already_move[3] == 0):
            global ghost_pos_orange
            global ghost_pos_orange_map
            val = int(split_tile_map[ghost_pos_orange_map[0]][ghost_pos_orange_map[1] + 1])

            if (val == 0 or val == 2):
                ghost_pos_orange_map[1] += 1
                ghost_pos_orange[1] += 40
                already_move[3] = 1

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

    def get_ia_ghost_Map(self, ghost_type):
        global already_move
        already_move = [0, 0, 0, 0]
        if (ghost_type == "Red"):
            global ghost_pos_red_map
            return ghost_pos_red_map
        elif (ghost_type == "Pink"):
            global ghost_pos_pink_map
            return ghost_pos_pink_map
        elif (ghost_type == "Blue"):
            global ghost_pos_blue_map
            return ghost_pos_blue_map
        else:
            global ghost_pos_orange_map
            return ghost_pos_orange_map

    def set_map(self, map_1):
        global split_tile_map
        split_tile_map = map_1

    def set_player_pos(self, pos):
        global player_pos
        player_pos = pos