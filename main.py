from kivy.app import App
from drawZone import DrawZone
from buttonZone import ButtonZone
from kivy.uix.gridlayout import GridLayout


class Environement():
    def __init__(self):
        self.isMur = True


class EcranModification(GridLayout):

    def __init__(self, **kwargs):
        self.evr = Environement()
        super(EcranModification, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(DrawZone(evr=self.evr))
        self.add_widget(ButtonZone(evr=self.evr))


class MyPaintApp(App):
    def build(self):
        self.title = "App"
        return EcranModification()


if __name__ == '__main__':
    MyPaintApp().run()

wait = input("PRESS ENTER TO CONTINUE.")
