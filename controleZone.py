from kivy.uix.gridlayout import GridLayout
from allButons import RunBtn


class ControleZone(GridLayout):

    def __init__(self, evr):
        super(ControleZone, self).__init__()
        self.evr = evr
        self.rows = 2
        self.add_widget(RunBtn(self.evr))

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
