from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
    # initialize Infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        row_force_default = True,
        row_default_height = 120,
        col_force_default = True,
        col_default_width = 100
        # define the required colomns
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height =120,
            col_force_default=True,
            col_default_width=100
        )
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Name"))
        # add text input box
        self.name = TextInput(multiline=True
                              )
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="food"))
        # add text input box
        self.pizza = TextInput(multiline=False
                               )
        self.top_grid.add_widget(self.pizza)

        # add widgets
        self.top_grid.add_widget(Label(text="color"
                                       ))
        # add text input box
        self.color = TextInput(multiline=False
                               )
        self.top_grid.add_widget(self.color)

        # Adding to the Ui
        self.add_widget(self.top_grid)

        self.submit = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200

                             )
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text=f"{name}{pizza}{color}"))

        # clear the input text box
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

        print(f'hello {name}{pizza}{color}')


class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
