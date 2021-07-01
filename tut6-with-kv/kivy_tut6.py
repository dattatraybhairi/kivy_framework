from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class MyGridLayout(Widget):
    name = ObjectProperty(None)
    food = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        food = self.food.text
        color = self.color.text

        # self.add_widget(Label(text=f"{name}{pizza}{color}"))

        # clear the input text box
        self.name.text = ""
        self.food.text = ""
        self.color.text = ""

        print(f'hello {name}{food}{color}')


class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
