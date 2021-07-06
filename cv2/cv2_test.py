try:
    import kivy
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.image import Image
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy_garden.zbarcam import ZBarCam
except:
    import subprocess

    subprocess.check_call(["python", '-m', 'pip', 'install', 'kivy'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'kivy_garden'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'pyzbar'])


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.box = BoxLayout()
        self.box.orientation = 'vertical'
        self.box.spacing = 20
        self.box.padding = 20
        self.logo = Image(source='logo.png')
        self.box.add_widget(self.logo)
        self.btn_add_pick = Button(font_size=30, text='Add Pick')
        self.box.add_widget(self.btn_add_qr)
        self.btn_remove_pick = Button(font_size=30, text='Delet Pick')
        self.box.add_widget(self.btn_remove_pick)
        self.add_widget(self.box)


class CameraScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.box = BoxLayout(orientation='vertical')
        self.cam = ZBarCam()
        self.cam.play = False
        self.btn_close = Button(font_size=30, size_hint_y=None, text='Get')
        self.box.add_widget(self.cam)
        self.box.add_widget(self.btn_close)
        self.add_widget(self.box)


class WindowManager(ScreenManager):
    def __init__(self, **kv):
        super().__init__(**kv)
        ms = MainScreen(name="main")
        ms.btn_add_pick.bind(on_press=self.switch_to_camera)
        ms.btn_remove_pick.bind(on_press=self.switch_to_camera)
        self.add_widget(ms)
        cs = CameraScreen(name="camera")
        cs.btn_close.bind(on_press=self.switch_to_main)
        self.add_widget(cs)

    def switch_to_camera(self, instance):
        self.current = 'camera'
        self.transition.direction = 'down'

    def switch_to_main(self, instance):
        self.current = 'main'
        self.transition.direction = 'up'


class WoodWQApp(App):
    def build(self):
        wm = WindowManager()
        wm.current = 'main'
        return wm


if __name__ == "__main__":
    WoodWQApp().run()