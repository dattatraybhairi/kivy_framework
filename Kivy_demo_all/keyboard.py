import kivy
kivy.require("1.11.1")
from kivy.config import Config
Config.set("kivy", "keyboard_mode", 'dock')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


# Window.size = (1080 / 3, 2127 / 3)
Window.size = (480, 800)

class Calc(TextInput):
    def _keyboard_close(self):
        pass

    def setup_keyboard(self):
        kb = Window.request_keyboard(self._keyboard_close, self)
        if kb.widget:
            # kb.widget.layout = 'numeric.json'
            kb.widget.font_size = 38
            kb.widget.height = 350


class TestApp(App):
    def build(self):
        root = Calc()
        root.setup_keyboard()
        return root


if __name__ == '__main__':
    TestApp().run()