from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('test.kv')

    def presser(self):
        self.root.ids.my_label.text = f'hello'



MainApp().run()
