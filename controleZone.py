from kivy.uix.gridlayout import GridLayout
from allButons import RunBtn
from utilities import ButtonOverlay


class ControleZone(GridLayout, ButtonOverlay):

    def __init__(self, evr):
        super(ControleZone, self).__init__()
        self.evr = evr
        self.rows = 2
        self.add_widget(RunBtn(self.evr))
