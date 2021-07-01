#!/usr/bin/env python
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager as scr_mngr
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class Tab(FloatLayout, MDTabsBase):
    pass


class MyLayout(BoxLayout):
    name = ObjectProperty(None)

    def check_data_login(self):

        self.ids['spinner'].active = True
        username = self.ids.username.text
        password = self.ids['password'].text
        print(username)
        print(password)
        if not username and not password:
            toast("Username and password are required")
        elif not username:
            toast("Username is required ")
        elif not password:
            toast("Password is required")
        else:
            if username == "admin" and password == "admin":
                self.ids['spinner'].active = False
                self.change_screen("screen2")
            else:
                self.ids['spinner'].active = False
                toast("Wrong username or password")

    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

    def calc(self, instance):
        print(self.ids['qrlabel'].text)


class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (680, 680)
    DemoApp().run()