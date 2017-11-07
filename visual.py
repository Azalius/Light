from utilities import Point, angle
from math import cos, sin, pi, atan
from kivy.graphics import Line, Canvas, Color
from copy import deepcopy


class lightBeam(Canvas):

    def __init__(self, room, startpoint, direction, energy, color, energyMin, lineLong):
        self.energyMax = energy
        self.lineLong = lineLong
        self.energy = energy
        self.direction = direction
        self.color = deepcopy(color)
        transp = 1
        x0 = startpoint.x
        y0 = startpoint.y
        j = 0
        while self.energy > energyMin:
            xline = x0 + self.lineLong * cos(self.direction)
            yline = y0 + self.lineLong * sin(self.direction)
            oldPt = Point(x0, y0)
            newPt = Point(xline, yline)
            for mur in room.walls:
                if mur.are2PointOnDifferentsSide(oldPt, newPt):
                    self.bounce(mur)
            self.energy = self.energy * self.attenuation()**self.lineLong
            transp = self.energy / self.energyMax
            Color(self.color[0], self.color[1], self.color[2], transp)
            Line(points=[x0, y0, xline, yline], width=1)
            x0 = xline
            y0 = yline
            j = j+1


    def attenuation(self):
        return .97

    def bounce(self, wall):
        perpVector = wall.getPerpVector()
        lumVector = [cos(self.direction), sin(self.direction)]
        angl = angle(lumVector, wall.getVector())
        self.direction = self.direction + 2*angl

class Light(Canvas):

    def disp(self, transMin=0.0001, lineLong=2):
        i = 0
        Color(self.color[0], self.color[1], self.color[2], 1)
        while i < self.nblignes:
            angle = 2*pi*i/self.nblignes
            lightBeam(self.room, self.pos, angle, self.energyPerBeam, self.color, transMin, lineLong)
            i = i + 1



    def __init__(self, posx, posy, power=5, room=None, color=[1, 1, 1]):
        self.lines = []
        self.room = room
        self.pos = Point(posx, posy)
        self.nblignes = power**2
        self.color = color
        self.energyPerBeam = 10
