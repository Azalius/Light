from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from math import sqrt
from utilities import Point
from visual import Light


class Selectionable(Widget):
    def __init__(self, evr):
        super(Selectionable, self).__init__()
        self.selecColor = [.8, .5, .5]
        self.isSelected = False
        self.size_hint = (None, None)
        self.evr = evr

    def manif(self):
        self.color = self.selecColor

    def demanif(self):
        self.color = self.defColor

    def changecolor(self, instance, value):
        pass

    def decaler(self, x, y):
        pass

    def isInterestedInMove(self, touch, x, y):
        if self.collide_point(touch.x, touch.y):
            self.decaler(x, y)
            return True
        return False

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

    def __init__(self, posx, posy, evr):
        super(Lumiere, self).__init__(evr)
        self.posx = posx
        self.posy = posy
        self.selecColor = [.8, .5, .5]
        self.defColor = [.6, .1, .2]
        self.color = self.defColor
        self.lines = Light(self.posx, self.posy)
        self.larg = 20

    def drawe(self):
        with self.canvas:
            self.canvas.clear()
            point = self.evr.decale(Point(self.posx, self.posy))
            Color(self.color[0], self.color[1], self.color[2])
            center = (point.x - self.larg / 2, point.y - self.larg / 2)
            self.e = Ellipse(pos=center, size=(self.larg, self.larg))
        return self

    def draweLight(self, room):
        with self.canvas:
            self.lines = Light(self.posx, self.posy, room=room)
            self.lines.disp()

    def collide_point(self, x, y):
        if sqrt(((x-self.posx)**2)+((y-self.posy)**2)) < self.larg:
            return True
        return False

    def decaler(self, x, y):
        self.posx += x
        self.posy += y

    def demanif(self):
        self.color = self.defColor
        self.isSelected = False


class Mur(Selectionable, ButtonBehavior):

    def __init__(self, ax, ay, bx, by, evr):
        super(Mur, self).__init__(evr)
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
            a = self.evr.decale(Point(self.a.x, self.a.y))
            b = self.evr.decale(Point(self.b.x, self.b.y))
            Line(points=[a.x, a.y, b.x, b.y])
            if self.isSelected:
                center = (a.x - self.pointsWidth / 2, a.y - self.pointsWidth / 2)
                Ellipse(pos=center, size=(self.pointsWidth, self.pointsWidth))
                center = (b.x - self.pointsWidth / 2, b.y - self.pointsWidth / 2)
                Ellipse(pos=center, size=(self.pointsWidth, self.pointsWidth))
        return self

    def getaxplusbEquation(self):
        if self.b.x != self.a.x:
            aw = (self.b.y-self.a.y)/(self.b.x-self.a.x)
        else:
            aw = 999999
        bw = -aw*self.a.x+self.a.y
        return[aw, bw]

    def getVector(self):
        vec = [self.b.x-self.a.x, self.b.y-self.a.y]
        longVec = sqrt((vec[0]**2)+(vec[1]**2))
        vec[0] = vec[0]/longVec
        vec[1] = vec[1]/longVec
        return vec

    def getPerpVector(self):
        wallVector = self.getVector()
        return [-wallVector[1], wallVector[0]]

    def getNearestPointOnLine(self, point):
        perpVector = self.getPerpVector()
        if perpVector[0] == 0:
            perpVector[0] = 0.001
        ap = perpVector[1]/perpVector[0]
        bp = -ap*point.x+point.y
        wallEq = self.getaxplusbEquation()
        xx = (bp-wallEq[1])/(wallEq[0]-ap)
        return Point(xx, ap*xx+bp)

    def are2PointOnDifferentsSide(self, pt1, pt2):
        if not self.isAlignedWith(pt1) or not self.isAlignedWith(pt2):
            return False
        eq = self.getaxplusbEquation()
        y1 = eq[0]*pt1.x+eq[1]
        y2 = eq[0]*pt2.x+eq[1]
        if (y1 > pt1.y and y2 > pt2.y):
            return False
        if (y1 < pt1.y and y2 < pt2.y):
            return False
        return True

    def isAlignedWith(self, pt):
        if ((pt.x >= self.a.x and pt.x >= self.b.x) or(pt.x <= self.a.x and pt.x <= self.b.x)):
            return True
        if ((pt.y >= self.a.y and pt.y >= self.b.y) or(pt.y <= self.a.y and pt. y <= self.b.y)):
            return True
        return False

    def collide_point(self, x, y):
        if self.isAlignedWith(Point(x, y)):
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
