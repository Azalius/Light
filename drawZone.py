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
                print(self.lastLine)
                points = [self.xline1, self.yline1, touch.x, touch.y]
                if self.lastLine is not None:
                    self.canvas.remove(self.lastLine)
                self.lastLine = Line(points=points, width=5)

    def on_touch_up(self, touch):
        points = [self.xline1, self.yline1, touch.x, touch.y]
        if (self.evr.isMur):
            mur = Mur(self.xline1, self.yline1, touch.x, touch.y)
            self.room.walls.append(mur)
        else:
            self.room.lights.append(Lumiere(touch.x, touch.y))
        with self.canvas:
            Color(0, 0, 1)
            self.canvas.remove(self.lastLine)
            Line(points=points, width=5, cap='none')
            print(self.evr.isMur)
