#!/usr/bin/env python
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager as scr_mngr
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import subprocess, os


class Tab(FloatLayout, MDTabsBase):
    pass


class MyLayout(BoxLayout, MDApp):
    dialog = None


    def check_data_login(self):

        # self.ids['spinner'].active = False
        # self.change_screen("screen2")
        # toast("Logged in Successfully !")

        # self.ids['spinner'].active = True
        password = self.ids['password'].text
        username = self.ids['username'].text

        print("username: ",username)
        print("password: ",password)
        # if not username and not password:
        #     toast("Username and password are required")
        # elif not username:
        #     toast("Username is required ")
        # elif not password:
        #     toast("Password is required")
        # else:
        #     if username == "admin" and password == "admin":
        #         self.ids['spinner'].active = False
        #         self.change_screen("screen2")
        #     else:
        #         self.ids['spinner'].active = False
        #         toast("Wrong username or password")


    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

    def logout(self):
        self.dialog.dismiss()
        self.change_screen("screen1")

    def calc(self, instance):
        pass
        # print(self.ids['qrlabel'].text)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Logout ?",
                text="Are you sure you want to logout now?.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=lambda _: self.dismiss()
                    ),
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_release=lambda _: self.logout()
                    ),
                ],
            )
        self.dialog.open()

    def dismiss(self):
        self.dialog.dismiss()

    def sleep(self):
        p = os.popen('sudo -E sh -c \'echo 1 > /sys/class/backlight/rpi_backlight/bl_power\'')


class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (800, 480)
    DemoApp().run()
