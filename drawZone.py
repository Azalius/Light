from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line
from element import Room, Mur, Lumiere
from kivy.clock import Clock


class DrawZone(RelativeLayout):

    def __init__(self, evr):
        super(DrawZone, self).__init__()
        self.isDrawing = False
        self.evr = evr
        self.room = Room()
        self.lastLine = None
        self.xline1 = 0
        self.yline1 = 0
        Clock.schedule_interval(self.dessine, 1/10)

    def dessine(self, coucou):
        if(not self.isDrawing and self.room is not None):
            # with self.canvas:
                # self.canvas.clear()
            toAdd = self.room.draw()
            if toAdd is not None:
                for elem in toAdd:
                    add = True
                    for widg in self.children[:]:
                        if (elem == widg):
                            add = False
                    if (add is True):
                        self.add_widget(elem)
                        print("je dessine l'element")
        if self.evr.deleteElemSelected is True:
            if self.evr.elemSelected is not None:
                self.remove_widget(self.evr.elemSelected)
                self.room.remove(self.evr.elemSelected)
                self.evr.elemSelected = None
                print("Je retire l'element")
            self.evr.deleteElemSelected = False

    def on_touch_down(self, touch):
        continu = False
        if self.evr.shouldSelec():
            for elem in self.children:
                if elem.collide_point(*touch.pos):
                    self.evr.elemSelected = elem
                    elem.manif()
                    continu = True
                    break
            if continu is False:
                self.evr.elemSelected = None
        else:
            if self.evr.shouldDrawWall():
                with self.canvas:
                    self.xline1 = touch.x
                    self.yline1 = touch.y

            elif self.evr.shouldDrawLight():
                light = Lumiere(touch.x, touch.y)
                self.room.lights.append(light)

    def on_touch_move(self, touch):
        if self.evr.shouldDrawWall():
            self.isDrawing = True
            if self.evr.isMur:
                with self.canvas:
                    Color(1, 1, 0)
                    points = [self.xline1, self.yline1, touch.x, touch.y]
                    if self.lastLine is not None:
                        self.canvas.remove(self.lastLine)
                    if self.xline1 is not None and touch.x is not None:
                        self.lastLine = Line(points=points, width=5)

    def on_touch_up(self, touch):
        if self.evr.shouldDrawWall():
            self.isDrawing = False
            if (self.evr.isMur):
                if (self.xline1 is not None and touch.x is not None):
                    mur = Mur(self.xline1, self.yline1, touch.x, touch.y)
                    self.room.walls.append(mur)
            else:
                self.room.lights.append(Lumiere(touch.x, touch.y))
            if self.lastLine is not None:
                self.canvas.remove(self.lastLine)
            self.lastLine = None
            self.xline1 = None
            self.yline1 = None
