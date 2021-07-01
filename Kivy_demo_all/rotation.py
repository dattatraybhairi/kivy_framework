from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color


class MainScreen(FloatLayout, Label):

    """MAIN WINDOW CLASS"""

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.988, 0.725, 0.074, 1, mode='rgba')
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_rect)

        self.titlos = Label(text="",
                            bold=True,
                            text_size=(None,None),
                            font_size="20sp",
                            pos_hint={'center_x': 0.5, 'center_y': .85},
                            size_hint_y=None,
                            size = self.size,
                            height=self.texture_size[1],
                            halign="center",
                            valign = "middle",
                            color=(0.055, 0.235, 0.541, 1))

        self.add_widget(self.titlos)
        self.bind(size=self.update_orientation)

    def update_rect(self, *args):
        """FUNCTION TO UPDATE THE RECATANGLE OF CANVAS TO FIT THE WHOLE SCREEN OF MAINSCREEN ALWAYS"""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_orientation(self, *args):
        """FUNCTION TO UPDATE THE SCREEN CONTENTS WHEN THE WINDOW SIZE CHANGES"""
        if self.parent.size[1] > self.parent.size[0]:
            self.titlos.text = "This is\nPortrait\nOrientation"
        else:
            self.titlos.text = "This is Landscape Orientation"

        # This is just for checking. Not essential to the program.
        print("Width:", self.parent.size[0], ", Height:", self.parent.size[1])



class main(App):
    """BUILDING THE APP"""
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    main().run()