from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time

class CheckScreen(Screen):
    pass

class CameraClickScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))


GUI = Builder.load_string("""

GridLayout:
    cols: 1
    ScreenManager:
        id: screen_manager
        CameraClickScreen:
            name: "camera_click_screen"
            id: camera_click_screen
        CheckScreen:
            name: "check_screen"
            id: check_screen



<CameraClickScreen>:
    orientation: 'vertical'
    GridLayout:
        cols: 1
        Camera:
            id: camera
            #resolution: (640, 480)
            play: False
        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press:
                root.capture()
                # root refers to <CameraClickScreen>
                # app refers to TestCamera, app.root refers to the GridLayout: at the top
                app.root.ids['screen_manager'].transition.direction = 'left'
                app.root.ids['screen_manager'].current = 'check_screen'

<CheckScreen>:
    Button:
        text: "Next Screen"
        font_size: 50
""")

class TestCamera(App):

    def build(self):
        return GUI


TestCamera().run()