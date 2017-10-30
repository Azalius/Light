from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from math import sqrt
from utilities import Point


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

    def decaler(self, x, y):
        pass

    def isInterestedInMove(self, touch, x, y):
        self.decaler(x, y)
        return True

    def drawe(self):
        pass


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
            self.canvas.clear()
            Color(self.color[0], self.color[1], self.color[2])
            center = (self.posx - self.larg / 2, self.posy - self.larg / 2)
            self.e = Ellipse(pos=center, size=(self.larg, self.larg))
        return self

    def collide_point(self, x, y):
        if sqrt(((x-self.posx)**2)+((y-self.posy)**2)) < self.larg:
            return True
        return False

    def decaler(self, x, y):
        self.posx += x
        self.posy += y


class Mur(Selectionable, ButtonBehavior):

    def __init__(self, ax, ay, bx, by):
        super(Mur, self).__init__()
        self.a = Point(ax, ay)
        self.b = Point(bx, by)
        self.width = 150
        self.pointsWidth = 20
        self.collidewidth = 35
        self.defColor = [.6, .1, .2]
        self.color = self.defColor
        self.isSelected = False

    def drawe(self):
        with self.canvas:
            self.canvas.clear()
            Color(self.color[0], self.color[1], self.color[2])
            Line(points=[self.a.x, self.a.y, self.b.x, self.b.y])
            if self.isSelected:
                center = (self.a.x - self.pointsWidth / 2, self.a.y - self.pointsWidth / 2)
                Ellipse(pos=center, size=(self.pointsWidth, self.pointsWidth))
                center = (self.b.x - self.pointsWidth / 2, self.b.y - self.pointsWidth / 2)
                Ellipse(pos=center, size=(self.pointsWidth, self.pointsWidth))
        return self

    def getNearestPointOnLine(self, point):
        wallVector = [self.b.x-self.a.x, self.b.y-self.a.y]
        perpVector = [- wallVector[1], wallVector[0]]
        # ax+b equation of line perp. to the wall that goes trough the touch
        ap = perpVector[1]/perpVector[0]
        bp = -ap*point.x+point.y
        # print("perp equation : " + str(ap) + "x+" + str(bp))
        # ax+b equation of the wall
        aw = (self.b.y-self.a.y)/(self.b.x-self.a.x)
        bw = -aw*self.a.x+self.a.y
        # print("equation : " + str(aw) + "x+" + str(bw))
        # xx where the 2 points intersect in any equatin
        xx = (bp-bw)/(aw-ap)
        return Point(xx, ap*xx+bp)

    def collide_point(self, x, y):
        if ((x >= self.a.x and x >= self.b.x) or(x <= self.a.x and x <= self.b.x)):
            return False
        if ((y >= self.a.y and y >= self.b.y) or(y <= self.a.y and y <= self.b.y)):
            return False
        minPoint = self.getNearestPointOnLine(Point(x, y))
        dist = minPoint.dist(Point(x, y))
        if dist < self.collidewidth:
            return True
        return False

    def decaler(self, x, y):
        self.a.x += x
        self.b.x += x
        self.a.y += y
        self.b.y += y

    def isInterestedInMove(self, touch, x, y):
        distanceA = self.a.dist(Point(touch.x, touch.y))
        distanceB = self.b.dist(Point(touch.x, touch.y))
        if (distanceA < self.pointsWidth and distanceA <= distanceB):
            self.a.x += x
            self.a.y += y
        elif (distanceB < self.pointsWidth and distanceA > distanceB):
            self.b.x += x
            self.b.y += y
        else:
            self.decaler(x, y)
        return True

    def adjustedToMatchExtremity(self, touch):
        distA = self.a.dist(Point(touch.x, touch.y))
        if distA < self.collidewidth:
            touch.x = self.a.x
            touch.y = self.a.y
            return touch
        distB = self.b.dist(Point(touch.x, touch.y))
        if distB < self.collidewidth:
            touch.x = self.b.x
            touch.y = self.b.y
            return touch
        nearest = self.getNearestPointOnLine(Point(touch.x, touch.y))
        distance = Point(touch.x, touch.y).dist(nearest)
        if distance < self.collidewidth:
            touch.x = nearest.x
            touch.y = nearest.y
        return touch

    def manif(self):
        self.color = self.selecColor
        self.isSelected = True

    def demanif(self):
        self.color = self.defColor
        self.isSelected = False
