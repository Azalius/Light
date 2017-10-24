from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class BtnLumiere(Button):
    pass


class BtnMur(Button):
    pass


class ButtonZone(GridLayout):

    def __init__(self, evr):
        super(ButtonZone, self).__init__()
        Builder.load_file('./kv/buttons.kv')
        self.rows = 2
        self.evr = evr
        mur = BtnMur()
        mur.bind(on_press=self.modeMur)
        lum = BtnLumiere()
        lum.bind(on_press=self.modeLumiere)
        self.add_widget(mur)
        self.add_widget(lum)

    def on_touch_down(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_down', touch)):
                return True

    def on_touch_up(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_up', touch)):
                return True

    def on_touch_move(self, touch):
        for child in self.children[:]:
            if(child.dispatch('on_touch_move', touch)):
                return True

    def modeMur(self, coucou):
        self.evr.isMur = True

    def modeLumiere(self, coucou):
        self.evr.isMur = False
