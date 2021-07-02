from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from kivy.core.window import Window

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
        loc = "IMG_{}.png".format(timestr)
        print("Captured")
        TestCamera().stop()
        image = cv2.imread(loc)  # THIS IS SHOWING ERROR, need to use same image in opencv
        decodedObjects = pyzbar.decode(image)
        for obj in decodedObjects:
            print("Type:", obj.type)
            print("Data: ", obj.data, "\n")




class TestCamera(App):

    def build(self):
        return CameraClick()

if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (800, 480)
    TestCamera().run()
