
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ExampleApp>:
    orientation: "vertical"
    Button:
        text: ""
        on_press: gif.anim_delay = 0.10
        on_press: gif._coreimage.anim_reset(True)

        Image:
            id: gif
            source: 'nfc.gif'
            center: self.parent.center
            size: 500, 500
            allow_stretch: True
            anim_delay: -1
            anim_loop: 1
""")

class ExampleApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ExampleApp().run()