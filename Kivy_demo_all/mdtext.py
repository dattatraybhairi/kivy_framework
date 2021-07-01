from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDScreen:

    MDTextField:
        mode: "rectangle"
        hint_text: 'Field with left and right icons'
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .5

'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()