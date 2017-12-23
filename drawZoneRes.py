from drawZone import DrawZone
from utilities import Point
from kivy.uix.button import Button
from kivy.core.window import Window
from buttonZone import ScrollZone

class Decalage():
    def __init__(self, onUpdate):
        self.speedx = 20
        self.speedy = 20
        self.speedzoom = 1.2
        self.onUpdate = onUpdate

        self.x = 0
        self.y = 0
        self.zoomcoef = 1

    def up(self):
        self.y += self.speedy
        self.onUpdate()
    def down(self):
        self.y -= self.speedy
        self.onUpdate()
    def left(self):
        self.x -= self.speedx
        self.onUpdate()
    def right(self):
        self.x += self.speedx
        self.onUpdate()
    def reset(self):
        self.x = 0
        self.y = 0
        self.zoomcoef = 0
        self.onUpdate()
    def dezoom(self, point):
        self.x-=(self.zoomcoef-1)*Window.size[0]
        self.y-=(self.zoomcoef-1)*Window.size[1]
        self.zoomcoef /= self.speedzoom
        self.onUpdate()
    def zoom(self, point):
        self.zoomcoef *= self.speedzoom
        self.x+=(self.zoomcoef-1)*Window.size[0]
        self.y+=(self.zoomcoef-1)*Window.size[1]
        self.onUpdate()
     

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
            self.decal.left()
        if (keycode[1] == "right"):
            self.decal.right()
        if (keycode[1] == "up"):
            self.decal.up()
        if (keycode[1] == "down"):
            self.decal.down()
        return True
     

class ScrollableDrawZone(DrawZone):
    def __init__(self, evr):
        super(ScrollableDrawZone, self).__init__(evr)
        self.evr.decal = Decalage(self.refreshDrawZone)
        self.keyboard = ScreenMoverKeyboard(self.evr.decal , self.refreshDrawZone)
        # self.add_widget(ScrollZone(self.evr))

    def on_touch_down(self, touch):
        if touch.button == 'left':
            return super().on_touch_down(touch)
        if touch.button == 'scrollup':
            self.evr.decal.zoom(Point(touch.x, touch.y))
        if touch.button == 'scrolldown':
            self.evr.decal.dezoom(Point(touch.x, touch.y))

    def on_touch_up(self, touch):
        return super().on_touch_up(self.evr.undecale(touch))

            

    def refreshDrawZone(self):
        self.canvas.clear()
        self.clear_widgets()
        toAdd = self.room.draw()
        if toAdd is not None:
            for elem in toAdd:
                self.add_widget(elem)
                print("je redessine l'element")


