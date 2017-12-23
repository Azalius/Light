from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from allButons import SelecWhatDraw, Modif
from utilities import ButtonOverlay


class ButtonZone(GridLayout, ButtonOverlay):

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


class ScrollZone(GridLayout):
    def __init__(self, evr):
        super(ScrollZone, self).__init__()
        self.evr = evr
        self.cols = 3
        self.rows = 3
        self.size_hint = (.1, .1)
        buttonCenter = Button(text="C")
        buttonCenter.bind(on_click=self.evr.decal.reset)
        buttonRight = Button(text="R")
        buttonLeft = Button(text="G")
        buttonUp = Button(text="U")
        buttonDown = Button(text="D")
        self.add_widget(buttonUp)
        self.add_widget(Widget())
        self.add_widget(Widget())
        self.add_widget(buttonDown)
        self.add_widget(Widget())
        self.add_widget(Widget())
        self.add_widget(buttonCenter)
        self.add_widget(buttonLeft)
        self.add_widget(buttonRight)

        

