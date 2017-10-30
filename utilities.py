from math import sqrt

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

    def deselecElem(self):
        if self.elemSelected is not None and self.deleteElemSelec is False:
            self.elemSelected.demanif()
            self.elemSelected = None

    def deleteElemSelec(self, sth):
        self.deleteElemSelected = True

    def changeSelecMode(self):
        if self.selec is True:
            self.selec = False
        else:
            self.selec = True

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
