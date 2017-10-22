from kivy.app import App
from drawZone import DrawZone
from buttonZone import ButtonZone
from kivy.uix.gridlayout import GridLayout


class Environement():
    def __init__(self):
        self.isMur = True


class MyPaintApp(App):
    def build(self):
        self.title = "App"
        self.evr = Environement()
        parent = GridLayout(cols=2)
        self.zoneDessin = DrawZone(self.evr)
        self.button = ButtonZone(self.evr)
        parent.add_widget(self.button)
        parent.add_widget(self.zoneDessin)
        return parent


if __name__ == '__main__':
    MyPaintApp().run()

wait = input("PRESS ENTER TO CONTINUE.")
