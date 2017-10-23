from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class BtnLumiere(Button):
    pass


class BtnMur(Button):
    pass


class ButtonZone(GridLayout):

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

    def modeMur(self):
        # self.evr.isMur = True
        print("caca")

    def modeLumiere(self):
        # self.evr.isMur = False
        print("coucou")

    def __init__(self, evr):
        super(ButtonZone, self).__init__()
        Builder.load_file('./kv/buttons.kv')
        self.cols = 2
        self.evr = evr
        mur = BtnMur()
        lum = BtnLumiere()
        self.add_widget(mur)
        self.add_widget(lum)
