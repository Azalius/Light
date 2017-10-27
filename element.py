from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from math import sqrt


class Selectionable(Widget):
    def __init__(self):
        super(Selectionable, self).__init__()
        self.selecColor = [.8, .5, .5]

    def manif(self):
        self.color = self.selecColor

    def demanif(self):
        self.color = self.defColor

    def changecolor(self, instance, value):
        print(str(value))


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

    def remove(self, elem):
        if self.lights.count(elem) != 0:
            self.lights.remove(elem)
        if self.walls.count(elem) != 0:
            self.walls.remove(elem)


class Lumiere(Selectionable, ButtonBehavior):

    def __init__(self, posx, posy):
        super(Lumiere, self).__init__()
        self.posx = posx
        self.posy = posy
        self.selecColor = [.8, .5, .5]
        self.defColor = [.6, .1, .2]
        self.color = self.defColor
        self.intensite = 100
        self.larg = 20

    def drawe(self):
        with self.canvas:
            Color(self.color[0], self.color[1], self.color[2])
            center = (self.posx - self.larg / 2, self.posy - self.larg / 2)
            self.e = Ellipse(pos=center, size=(self.larg, self.larg))
        return self

    def collide_point(self, x, y):
        if sqrt(((x-self.posx)**2)+((y-self.posy)**2)) < self.larg:
            return True
        return False


class Mur(Selectionable, ButtonBehavior):

    def __init__(self, ax, ay, bx, by):
        super(Mur, self).__init__()
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.width = 150
        self.collidewidth = 20
        self.defColor = [.6, .1, .2]
        self.color = self.defColor

    def drawe(self):
        with self.canvas:
            Color(self.color[0], self.color[1], self.color[2])
            Line(points=[self.ax, self.ay, self.bx, self.by])
        return self

    def collide_point(self, x, y):
        if ((x >= self.ax and x >= self.bx) or(x <= self.ax and x <= self.bx)):
            return False
        if ((y >= self.ay and y >= self.by) or(y <= self.ay and y <= self.by)):
            return False
        wallVector = [self.bx-self.ax, self.by-self.ay]
        perpVector = [- wallVector[1], wallVector[0]]
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
