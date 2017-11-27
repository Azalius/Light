from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from element import Room, Mur, Lumiere
from copy import deepcopy
from utilities import Point


class DrawZone(FloatLayout):

    def __init__(self, evr):
        super(DrawZone, self).__init__()
        self.drawingColor=[1, 1, 0]
        self.isDrawing = False
        self.evr = evr
        self.room = Room()
        self.lastLine = None
        self.lastTouch = None
        self.firstTouch = None

    def dessine(self):
        shouldRefresh = (self.evr.isLightDemo and not self.evr.hasDispLights)
        shouldRefresh = shouldRefresh or not self.evr.isLightDemo
        if(not self.isDrawing and self.room is not None and shouldRefresh):
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
            if self.evr.isLightDemo and not self.evr.hasDispLights:
                for lum in self.room.lights:
                    print("je dessine une lumiere")
                    lum.draweLight(self.room)
                    self.evr.hasDispLights = True
            if self.evr.hasDispLights and not self.evr.isLightDemo:
                self.canvas.clear()
                self.clear_widgets()
                self.evr.hasDispLights = False
        if self.evr.deleteElemSelected is True:
            if self.evr.elemSelected is not None:
                self.remove_widget(self.evr.elemSelected)
                self.room.remove(self.evr.elemSelected)
                self.evr.elemSelected = None
                print("Je retire l'element")
            self.evr.deleteElemSelected = False

    def selecElem(self, continu, touch):
        if self.lastLine is not None:
            self.lastLine.demanif()
        for elem in self.children:
            if elem.collide_point(*touch.pos):
                self.evr.deselecElem()
                self.evr.elemSelected = elem
                elem.manif()
                continu = True
                break
        if continu is False:
            self.evr.deselecElem()
        return continu

    def drawSth(self, touch):
        if self.evr.shouldDrawWall():
            for mur in self.room.walls:
                touch = mur.adjustedToMatchExtremity(touch)
            self.firstTouch = Point(touch.x, touch.y)
        
        elif self.evr.shouldDrawLight():
            light = Lumiere(touch.x, touch.y)
            self.room.lights.append(light)
        return touch

    def on_touch_down(self, touch):
        continu = False
        if self.evr.shouldSelec():
            continu = self.selecElem(continu, touch)
        else:
            touch = self.drawSth(touch) 

    def on_touch_move(self, touch):
        if self.evr.shouldDrawWall():
            self.isDrawing = True
            if self.evr.isMur:
                with self.canvas:
                    Color(self.drawingColor[0], self.drawingColor[1], self.drawingColor[2])
                    points = [self.firstTouch.x, self.firstTouch.y, touch.x, touch.y]
                    if self.lastLine is not None:
                        self.canvas.remove(self.lastLine)
                    if self.firstTouch is not None and touch.x is not None:
                        self.lastLine = Line(points=points, width=5)
        if self.evr.shouldSelec():
            if self.evr.elemSelected is not None:
                if self.lastTouch is not None:
                    decalx = touch.x-self.lastTouch.x
                    decaly = touch.y-self.lastTouch.y
                    self.evr.elemSelected.isInterestedInMove(touch, decalx, decaly)
                self.lastTouch = deepcopy(touch)



    def on_touch_up(self, touch):
        self.lastTouch = None
        if self.evr.shouldDrawWall():
            for mur in self.room.walls:
                touch = mur.adjustedToMatchExtremity(touch)
            self.isDrawing = False
            if (self.evr.isMur):
                if (self.firstTouch is not None and touch.x is not None):
                    mur = Mur(self.firstTouch.x, self.firstTouch.y, touch.x, touch.y)
                    self.room.walls.append(mur)
            else:
                self.room.lights.append(Lumiere(touch.x, touch.y))
            if self.lastLine is not None:
                self.canvas.remove(self.lastLine)
            self.lastLine = None
            self.firstTouch = None
        self.dessine()
