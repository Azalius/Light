from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from allButons import *


class ButtonZone(GridLayout):

    def __init__(self, evr):
        super(ButtonZone, self).__init__()
        self.evr = evr
        self.rows = 3
        self.add_widget(SelecWhatDraw(evr))
        self.add_widget(Modif(evr))

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
