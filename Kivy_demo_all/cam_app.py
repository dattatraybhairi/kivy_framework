import self as self
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import cv2

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
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
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        self.camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        # image = cv2.imread(self.camera) #THIS IS SHOWING ERROR, need to use same image in opencv
                                             # inside other_function() function


class TestCamera(App):

   def build(self):
       return CameraClick()
TestCamera().run()