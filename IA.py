from src.user import user

class launch_ia():
    def __init__(self):
        self.info = user()
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        return

    def main_ia(self):
        if (self.x1 == 0):
            self.info.move_ghost_up("Red")
            self.x1 = 1
        else:
            self.x1 = 0
            self.info.move_ghost_left("Red")

        if (self.x2 == 0):
            self.info.move_ghost_up("Blue")
            self.x2 = 1
        else:
            self.x2 = 0
            self.info.move_ghost_left("Blue")

        if (self.x3 == 0):
            self.info.move_ghost_up("Pink")
            self.x3 = 1
        else:
            self.x3 = 0
            self.info.move_ghost_left("Pink")

        if (self.x4 == 0):
            self.info.move_ghost_up("Orange")
            self.x4 = 1
        else:
            self.x4 = 0
            self.info.move_ghost_left("Orange")
        return