from drawZone import DrawZone
from kivy.core.window import Window

class Decalage():
    def __init__(self):
        self.x = 0
        self.y = 0


class ScreenMoverKeyboard():
    def __init__(self, decal, onEvent):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self.decal = decal
        self.onEvent = onEvent

        self.decaly = 20
        self.decalx = 20

        if self._keyboard.widget:
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        if (keycode[1] == "left"):
            self.decal.x = self.decal.x - self.decalx
            self.onEvent()
        if (keycode[1] == "right"):
            self.decal.x = self.decal.x + self.decalx
            self.onEvent()
        if (keycode[1] == "up"):
            self.decal.y = self.decal.y + self.decaly
            self.onEvent()
        if (keycode[1] == "down"):
            self.decal.y = self.decal.y - self.decaly
            self.onEvent() 
        return True


class ScrollableDrawZone(DrawZone):
    def __init__(self, evr):
        super(ScrollableDrawZone, self).__init__(evr)
        self.evr.decal = Decalage()
        self.keyboard = ScreenMoverKeyboard(self.evr.decal, self.refreshDrawZone)

    def refreshDrawZone(self):
        self.canvas.clear()
        self.clear_widgets()
        toAdd = self.room.draw()
        if toAdd is not None:
            for elem in toAdd:
                self.add_widget(elem)
                print("je redessine l'element")


