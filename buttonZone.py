from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder


class BtnLumiere(Button):
    pass


class BtnMur(Button):
    pass


class ButtonZone(Widget):

    def modeMur(self, instance):
        # self.evr.isMur = True
        print("caca")

    def modeLumiere(self, instance):
        # self.evr.isMur = False
        print("coucou")

    def __init__(self, evr):
        super(ButtonZone, self).__init__()
        Builder.load_file('./kv/buttons.kv')
        self.evr = evr
        with self.canvas:
            layout = GridLayout(rows=2)
            mur = BtnMur()
            mur.bind(on_press=self.modeMur)
            lum = BtnLumiere()
            lum.bind(on_press=self.modeLumiere)
            layout.add_widget(mur)
            layout.add_widget(lum)
