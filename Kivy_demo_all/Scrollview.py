from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv_text = '''

<MyScreenManager>:
    HomeScreen:

<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1,.1
            orientation: "horizontal"
            Button:
                text:"1"
            Button:
                text:"2"
            Button:
                text:"3"
        ScrollView:
            GridLayout:
                #orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height  #<<<<<<<<<<<<<<<<<<<<
                row_default_height: 60
                cols:1

                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
                Button:
'''

class MyScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        return HomeScreen()

def main():
    Builder.load_string(kv_text)
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()