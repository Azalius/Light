from math import sqrt, acos


def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def length(v):
    return sqrt(dotproduct(v, v))


def angle(v1, v2):
    return acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


class ButtonOverlay():

    def on_touch_down(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_down', touch)):
                self.evr.deselecElem()
                return True

    def on_touch_up(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_up', touch)):
                return True

    def on_touch_move(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_move', touch)):
                return True


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, point):
        return sqrt((self.x-point.x)**2+(self.y-point.y)**2)


class Environement():
    def __init__(self, **kwargs):
        self.isMur = True
        self.selec = False
        self.elemSelected = None
        self.deleteElemSelected = False
        self.colorButtonSelected = (.2, 1, 1, 1)
        self.isLightDemo = False
        self.hasDispLights = False

    def changeRunMode(self, oth):
        self.isLightDemo = not self.isLightDemo

    def deselecElem(self):
        if self.elemSelected is not None and self.deleteElemSelected is False:
            self.elemSelected.demanif()
            self.elemSelected = None

    def deleteElemSelec(self, sth):
        self.deleteElemSelected = True

    def changeSelecMode(self):
        self.selec = not self.selec

    def modeMur(self):
        self.selec = False
        self.isMur = True

    def modeLumiere(self):
        self.selec = False
        self.isMur = False

    def shouldDrawWall(self):
        return self.isMur and not self.selec

    def shouldDrawLight(self):
        return not self.isMur and not self.selec

    def shouldSelec(self):
        return self.selec
