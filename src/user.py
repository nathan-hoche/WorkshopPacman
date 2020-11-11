size_window_x = 760
size_window_y = 840
ia_bar_pos = 15
ball_pos = [0, 0]
ball_speed = [0, 0]

class user():
    def __init__(self):
        return

    def get_size_screen_x(self):
        global size_window_x
        return size_window_x

    def get_size_screen_y(self):
        global size_window_y
        return size_window_y

    def get_pos_player(self):
        global ball_pos
        return ball_pos

    def get_map(self):
        global ball_pos
        return ball_pos

    def move_ghost_up(self, ghost_type):
        if (ghost_type == "red"):
            return
        elif (ghost_type == "pink"):
            return
        elif (ghost_type == "blue"):
            return
        else:
            return

    def move_ghost_down(self, ghost_type):
        if (ghost_type == "red"):
            return
        elif (ghost_type == "pink"):
            return
        elif (ghost_type == "blue"):
            return
        else:
            return

    def move_ghost_left(self, ghost_type):
        if (ghost_type == "red"):
            return
        elif (ghost_type == "pink"):
            return
        elif (ghost_type == "blue"):
            return
        else:
            return

    def move_ghost_right(self, ghost_type):
        if (ghost_type == "red"):
            return
        elif (ghost_type == "pink"):
            return
        elif (ghost_type == "blue"):
            return
        else:
            return

class program_init_user():
    def __init__(self):
        return

    def get_ia_bar_pos(self):
        global ia_bar_pos
        return ia_bar_pos

    def set_ball_pos(self, pos):
        global ball_pos
        ball_pos = pos

    def set_ball_speed(self, pos):
        global ball_speed
        ball_speed = pos