from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from visual import Light
from element import Room, Mur, Lumiere


class DrawZone(Widget):

    def __init__(self, evr):
        super(DrawZone, self).__init__()
        self.evr = evr
        self.room = Room()
        self.lastLine = None
        self.xline1 = 0
        self.yline1 = 0

    def on_touch_down(self, touch):
        if self.evr.isMur:
            with self.canvas:
                Light(touch.x, touch.y, 100)
                self.xline1 = touch.x
                self.yline1 = touch.y

    def on_touch_move(self, touch):
        if self.evr.isMur:
            with self.canvas:
                Color(1, 1, 0)
                points = [self.xline1, self.yline1, touch.x, touch.y]
                if self.lastLine is not None:
                    self.canvas.remove(self.lastLine)
                if self.xline1 is not None and touch.x is not None:
                    self.lastLine = Line(points=points, width=5)

    def on_touch_up(self, touch):
        with self.canvas:
            points = [self.xline1, self.yline1, touch.x, touch.y]
            if (self.evr.isMur):
                if (self.xline1 is not None and touch.x is not None):
                    mur = Mur(self.xline1, self.yline1, touch.x, touch.y)
                    self.room.walls.append(mur)
                    Line(points=points, width=5, cap='none')
            else:
                self.room.lights.append(Lumiere(touch.x, touch.y))
            Color(0, 0, 1)
            if self.lastLine is not None:
                self.canvas.remove(self.lastLine)
            self.lastLine = None
            self.xline1 = None
            self.yline1 = None
            print(self.evr.isMur)
