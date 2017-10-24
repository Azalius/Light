from kivy.app import App
from drawZone import DrawZone
from buttonZone import ButtonZone
from kivy.uix.boxlayout import BoxLayout


class Environement():
    def __init__(self, **kwargs):
        self.isMur = True
        self.kwa = kwargs


class EcranModification(BoxLayout):

    def __init__(self, **kwargs):
        self.evr = Environement(**kwargs)
        super(EcranModification, self).__init__(**kwargs)
        simu = DrawZone(evr=self.evr)
        simu.size_hint = (.7, 1)
        controle = ButtonZone(evr=self.evr)
        controle.size_hint = (.3, 1)
        self.add_widget(simu)
        self.add_widget(controle)


class MyPaintApp(App):
    def build(self):
        self.title = "App"
        return EcranModification()


if __name__ == '__main__':
    MyPaintApp().run()

wait = input("PRESS ENTER TO CONTINUE.")
