from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.clock import Clock


class SelecWhatDraw(GridLayout):

    def changeSelecMode(self, instance):
        self.evr.changeSelecMode()
        if self.evr.selec is True:
            instance.background_color = self.evr.colorButtonSelected
        else:
            instance.background_color = (1, 1, 1, 1)

    def modeMur(self, instance):
        self.evr.modeMur(instance)
        instance.background_color = self.evr.colorButtonSelected
        self.lum.background_color = (1, 1, 1, 1)

    def modeLumiere(self, instance):
        self.evr.modeLumiere(instance)
        instance.background_color = self.evr.colorButtonSelected
        self.mur.background_color = (1, 1, 1, 1)

    def __init__(self, evr):
        super(SelecWhatDraw, self).__init__()
        Builder.load_file('./kv/buttons.kv')
        self.rows = 2
        self.evr = evr
        elemDraw = GridLayout(cols=2)
        self.mur = BtnMur()
        self.mur.bind(on_press=self.modeMur)
        self.lum = BtnLumiere()
        self.lum.bind(on_press=self.modeLumiere)
        self.selec = BtnSelec()
        self.selec.bind(on_press=self.changeSelecMode)
        elemDraw.add_widget(self.mur)
        elemDraw.add_widget(self.lum)
        self.add_widget(self.selec)
        self.add_widget(elemDraw)
        self.modeMur(self.mur)
        self.isInfoDisplayed = False


class Modif(GridLayout):
    def __init__(self, evr):
        super(Modif, self).__init__()
        self.evr = evr
        self.isInfoDisplayed = False
        Clock.schedule_interval(self.dispMenu, 1/10)

    def dispMenu(self, sth):
        if self.evr.elemSelected is not None and self.isInfoDisplayed is False:
            self.rows = 2
            self.deleteBtn = DeleteBtn()
            self.deleteBtn.bind(on_press=self.evr.deleteElemSelec)
            self.add_widget(self.deleteBtn)
            self.isInfoDisplayed = True
        if self.evr.elemSelected is None and self.isInfoDisplayed is True:
            self.clear_widgets()
            self.isInfoDisplayed = False


class DeleteBtn(Button):
    pass


class BtnSelec(Button):
    pass


class BtnLumiere(Button):
    pass


class BtnMur(Button):
    pass
