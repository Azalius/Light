from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class BtnSelec(Button):
    pass


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
        mur.bind(on_press=self.evr.modeMur)
        lum = BtnLumiere()
        lum.bind(on_press=self.evr.modeLumiere)
        selec = BtnSelec()
        selec.bind(on_press=self.evr.changeSelecMode)
        self.add_widget(mur)
        self.add_widget(lum)
        self.add_widget(selec)

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
