from kivy.graphics import Color


class Room():

    def __init__(self):
        self.lights = []
        self.walls = []


class Lumiere():

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.color = Color(1, 1, 1)
        self.intensite = 100


class Mur():

    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
