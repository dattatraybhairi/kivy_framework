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

        # define the required colomns
        self.cols = 2

        # add widgets
        self.add_widget(Label(text="Name"))
        # add text input box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        # add widgets
        self.add_widget(Label(text="food"))
        # add text input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # add widgets
        self.add_widget(Label(text="color"))
        # add text input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.submit = Button(text="Submit", font_size=32)
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

    def press(self,instance):
        name= self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text= f"{name}{pizza}{color}"))

        #clear the input text box
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


        print(f'hello {name}{pizza}{color}')

class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
