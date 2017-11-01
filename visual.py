from utilities import Point
from math import cos, sin, pi, exp
from kivy.graphics import Line, Canvas, Color


class Light(Canvas):

    def attenuation(self, dist):
        return exp(-5*dist)

    def disp(self, lineLongMax=100, definition=50):
        self.linelong = lineLongMax
        self.defe = definition
        i = 0
        Color(self.color[0], self.color[1], self.color[2], 1)
        while i < self.nblignes:
            j = 0
            angle = 2*pi*i/self.nblignes
            longe = self.linelong/self.defe
            x0 = self.pos.x
            y0 = self.pos.y
            while j < self.defe:
                xline = x0 + longe * cos(angle)
                yline = y0 + longe * sin(angle)
                transp = self.attenuation(float(j)/float(self.defe))
                Color(self.color[0], self.color[1], self.color[2], transp)
                Line(points=[x0, y0, xline, yline], width=1)
                x0 = xline
                y0 = yline
                j = j+1
            i = i+1

    def __init__(self, posx, posy, power=200, room=None, color=[1, 1, 1]):
        self.lines = []
        self.room = room
        self.pos = Point(posx, posy)
        self.nblignes = power
        self.color = color
