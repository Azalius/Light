from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from math import sqrt


class Room():

    def __init__(self):
        self.lights = []
        self.walls = []

    def draw(self):
        aret = []
        for mur in self.walls:
            aret.append(mur.drawe())
        for lum in self.lights:
            aret.append(lum.drawe())
        return aret


class Lumiere(Widget, ButtonBehavior):

    def __init__(self, posx, posy):
        super(Lumiere, self).__init__()
        self.posx = posx
        self.posy = posy
        self.color = Color(1, 1, 1)
        self.intensite = 100
        self.larg = 20

    def drawe(self):
        with self.canvas:
            Color(.6, .1, .2)
            center = (self.posx - self.larg / 2, self.posy - self.larg / 2)
            Ellipse(pos=center, size=(self.larg, self.larg))
        return self

    def manif(self):
        print("manif lum appele")

    def collide_point(self, x, y):
        if sqrt(((x-self.posx)**2)+((y-self.posy)**2)) < self.larg:
            return True
        return False


class Mur(Widget, ButtonBehavior):

    def __init__(self, ax, ay, bx, by):
        super(Mur, self).__init__()
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.width = 150
        self.collidewidth = 20
        self.wallVector = [self.bx-self.ax, self.by-self.ay]

    def manif(self):
        print("manif mur appele")

    def drawe(self):
        with self.canvas:
            Color(.6, .1, .2)
            Line(points=[self.ax, self.ay, self.bx, self.by])
        return self

    def collide_point(self, x, y):
        if ((x >= self.ax and x >= self.bx) or(x <= self.ax and x <= self.bx)):
            return False
        if ((y >= self.ay and y >= self.by) or(y <= self.ay and y <= self.by)):
            return False
        perpVector = [- self.wallVector[1], self.wallVector[0]]
        # ax+b equation of line perp. to the wall that goes trough the touch
        ap = perpVector[1]/perpVector[0]
        bp = -ap*x+y
        # print("perp equation : " + str(ap) + "x+" + str(bp))
        # ax+b equation of the wall
        aw = (self.by-self.ay)/(self.bx-self.ax)
        bw = -aw*self.ax+self.ay
        # print("equation : " + str(aw) + "x+" + str(bw))
        # xx where the 2 points intersect in any equatin
        xx = (bp-bw)/(aw-ap)
        # min dist between the touch and the line
        dist = sqrt((xx-x) ** 2 + (ap*xx+bp-y) ** 2)
        if dist < self.collidewidth:
            return True
        return False
