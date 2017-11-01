from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.spinner import Spinner
from kivy.uix.colorpicker import ColorPicker


class SelecWhatDraw(GridLayout):

    def changeSelecMode(self, instance):
        self.evr.changeSelecMode()
        if self.evr.selec is True:
            instance.background_color = self.evr.colorButtonSelected
        else:
            instance.background_color = (1, 1, 1, 1)

    def selecElem(self, spinner, text):
        if text == 'Mur':
            self.evr.modeMur()
        elif text == 'Lumiere':
            self.evr.modeLumiere()

    def __init__(self, evr):
        super(SelecWhatDraw, self).__init__()
        Builder.load_file('./kv/buttons.kv')
        self.rows = 2
        self.evr = evr
        self.selec = BtnSelec()
        elemDraw = Spinner(
            text='Mur',
            values=('Mur', 'Lumiere'))
        elemDraw.bind(text=self.selecElem)
        self.selec.bind(on_press=self.changeSelecMode)
        self.add_widget(self.selec)
        self.add_widget(elemDraw)
        self.evr.modeMur()
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
            self.clr_picker = ColorPicker()
            self.clr_picker.bind(color=self.evr.elemSelected.changecolor)
            self.add_widget(self.clr_picker)

        if self.evr.elemSelected is None and self.isInfoDisplayed is True:
            self.clear_widgets()
            self.isInfoDisplayed = False


class RunBtn(Button):
    def __init__(self, evr):
        super(RunBtn, self).__init__()
        self.evr = evr
        self.text = "Run"
        self.bind(on_press=self.evr.changeRunMode)


class DeleteBtn(Button):
    pass


class BtnSelec(Button):
    pass


class BtnLumiere(Button):
    pass


class BtnMur(Button):
    pass
