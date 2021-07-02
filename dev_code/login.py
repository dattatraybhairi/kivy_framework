#!/usr/bin/env python
import time
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from kivy.core.window import Window
import MySQLdb
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import os

class DbCon:

    def __init__(self):
        self.db = MySQLdb.connect(user="vacus", passwd="vacus321", db="vacus")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM taginfo")
        self.row = self.c.fetchall()
        # print(self.row)

        return self.row


class Tab(FloatLayout, MDTabsBase):
    pass


class MyLayout(BoxLayout, MDApp):
    dialog = None
    wifi = None
    cam_error = None
    # theme_cls = ThemeManager()
    def check_data_login(self):
        self.ids["RFID"].text = ""
        self.ids['spinner'].active = True
        username = self.ids['username'].text
        password = self.ids['password'].text
        print(username)
        print(password)
        self.change_screen("screen2")
        # if not username and not password:
        #     toast("Username and password are required")
        # elif not username:
        #     toast("Username is required ")
        # elif not password:
        #     toast("Password is required")
        # else:
        #     if username == "a" and password == "a":
        #         self.ids['spinner'].active = False
        #         self.change_screen("screen2")
        #     else:
        #         self.ids['spinner'].active = False
        #         toast("Wrong username or password")

    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

    def calc(self, instance):
        print(self.ids['qrlabel'].text)

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
        p = os.popen('sudo -E sh -c \'echo 0 > /sys/class/backlight/rpi_backlight/bl_power\'')

    def logout(self):
        self.dialog.dismiss()
        self.change_screen("screen1")

    def open_data_table(self):
        self.db = DbCon()
        self.rows = self.db.get_rows()
        print(len(self.rows))
        self.ids['spinner2'].active = True
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0, "center_y": 0},
            size_hint=(1, 1),
            # use_pagination=True,
            # check=True,
            rows_num=100,
            column_data=[
                # page1
                ("No.", dp(15)),  # 0
                ("Physical", dp(25)),  # 1
                ("Data Center", dp(25)),  # 2
                ("Description", dp(25)),  # 3
                ("Device Model", dp(25)),  # 4
                ("Floor", dp(10)),  # 5
                ("Manufacturer", dp(25)),  # 6
                ("Asset Unit Usage ", dp(25)),  # 7
                ("Room", dp(10)),  # 8
                ("Serial Number", dp(25)),  # 9
                ("RackNo", dp(15)),  # 10
                ("Column", dp(15)),  # 11
                ("Supplier", dp(25)),  # 12
                ("Address", dp(25)),  # 13
                ("MAC Address1", dp(25)),  # 14
                ("MAC Address2", dp(25)),  # 15
                # #page2 15
                ("Equipment Category", dp(25)),  # 16
                ("Weight(KG)", dp(25)),  # 17
                ("Inventory Code", dp(25)),  # 18
                ("Life Cycle", dp(25)),  # 19
                ("Power(W)", dp(25)),  # 20
                ("Last Maintenance Staff", dp(25)),  # 21
                ("Maintenance Cycle", dp(25)),  # 22
                ("Current(A)", dp(25)),  # 23
                ("Next Maintenance Staff", dp(25)),  # 24
                ("Principal", dp(25)),  # 25
                ("Voltage(V)", dp(25)),  # 26
                ("Last Updated Time", dp(25)),  # 27
                ("Maintenance Contact", dp(25)),  # 28
                ("First Use Time", dp(25)),  # 29
                ("Next Update Time", dp(25)),  # 30

                #

            ],
            row_data=[
                (row[0],
                 row[1],
                 row[2],
                 row[3],
                 row[4],
                 row[5],
                 row[6],
                 row[7],
                 row[8],
                 row[9],
                 row[10],
                 row[11],
                 row[12],
                 row[13],
                 row[14],
                 row[15],
                 row[16],
                 #
                 row[17],
                 row[18],
                 row[19],
                 row[20],
                 row[21],

                 row[22],
                 row[23],
                 row[24],
                 row[25],
                 row[26],
                 row[27],
                 row[28],
                 row[29],
                 row[30],
                 # row[31],

                 ) for row in self.rows
            ],
        )

        for row in self.rows:
            print(len(row))
        # self.data_tables.ids.container.add_widget(
        #     MDRaisedButton(
        #         text="CLOSE",
        #         pos_hint={"right": 1},
        #         on_release=self.close_data_table,
        #     )
        # )

        # self.ids.btn.disabled = True
        self.ids.container.add_widget(self.data_tables)
        self.ids['spinner2'].active = False

    def close_data_table(self, *args):
        # self.ids.btn.disabled = False
        self.ids.container.remove_widget(self.data_tables)

    def capture(self):
        self.camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png("IMG_{}.png".format(timestr))
        loc = "IMG_{}.png".format(timestr)
        print("Captured")
        image = cv2.imread(loc)  # THIS IS SHOWING ERROR, need to use same image in opencv
        decodedObjects = pyzbar.decode(image)
        if decodedObjects:
            for obj in decodedObjects:
                print("Type:", obj.type)
                print("Data: ", obj.data, "\n")
                self.ids["RFID"].text = obj.data
        else:
            # cam_error
            if not self.cam_error:
                self.cam_error = MDDialog(
                    title="Read Error ?",
                    text="Make Sure Image is Clearly Visible?.",
                    buttons=[
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release=lambda _: self.close_cam_error()
                        ),
                    ],
                )
            self.cam_error.open()




    def close_cam_error(self):
        self.cam_error.dismiss()
        self.change_screen("screen3")

class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (800, 480)
    DemoApp().run()
