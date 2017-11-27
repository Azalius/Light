from kivy.app import App
from drawZone import DrawZone
from buttonZone import ButtonZone
from kivy.uix.boxlayout import BoxLayout
from utilities import Environement
from controleZone import ControleZone


class EcranModification(BoxLayout):

    def __init__(self, **kwargs):
        self.evr = Environement(**kwargs)
        super(EcranModification, self).__init__(**kwargs)
        controle = ControleZone(evr=self.evr)
        controle.size_hint = (.15, 1)
        simu = DrawZone(evr=self.evr)
        simu.size_hint = (.7, 1)
        modif = ButtonZone(evr=self.evr)
        modif.size_hint = (.15, 1)
        self.add_widget(controle, index=0)
        self.add_widget(simu, index=2)
        self.add_widget(modif, index=1)


class MyPaintApp(App):
    def build(self):
        self.title = "App"
        return EcranModification()


if __name__ == '__main__':
    MyPaintApp().run()

