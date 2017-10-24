from kivy.graphics import Color, Line
from visual import Light
from kivy.uix.behaviors import ButtonBehavior


class Room():

    def __init__(self):
        self.lights = []
        self.walls = []

    def draw(self):
        for mur in self.walls:
            mur.draw()

        for lum in self.lights:
            lum.draw()


class Lumiere(Light):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.color = Color(1, 1, 1)
        self.intensite = 100

    def draw(self):
        super(Lumiere, self).__init__(self.posx, self.posy, self.intensite)


class Mur(Line, ButtonBehavior):

    def __init__(self, ax, ay, bx, by, **kwargs):
        super(Mur, self).__init__(**kwargs)
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.width = 5
        self.color = Color(.8, .6, .8)

    def draw(self):
        point = [self.ax, self.ay, self.bx, self.by]
        super(Mur, self).__init__(points=point, width=self.width, cap='none')

    def on_press(self):
        print("coucou")
        # return super(Mur, self).on_touch_down(touch)
