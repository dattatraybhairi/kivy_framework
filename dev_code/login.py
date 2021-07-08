#!/usr/bin/env python
import socket
import subprocess

from kivy.animation import Animation
from kivy.uix.vkeyboard import VKeyboard
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivy_garden import zbarcam
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

from self import self

login_key = False


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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.login_key = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def check_data_login(self):
        self.ids["zbarcam"].xcamera.play = False
        self.ids["RFID"].text = ""
        self.ids['spinner'].active = True
        username = self.ids['username'].text
        password = self.ids['password'].text
        print(username)
        print(password)
        self.change_screen("screen2")
        self.login_key = True
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
        if self.login_key == True:
            print(self.ids['qrlabel'].text)
            if self.ids['qrlabel'].text != "":
                self.scanned = str(self.ids['qrlabel'].text)
                text = self.scanned.split("b")
                self.ids["RFID"].text = str(text[1]).replace("'", "")
                self.change_screen("screen3")
                self.ids["zbarcam"].xcamera.play = False
            else:
                self.change_screen("screen6")
                self.ids["zbarcam"].xcamera.play = True

    def scan(self):
        self.change_screen("screen6")
        self.ids["zbarcam"].xcamera.play = True

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
        # print(len(self.rows))
        self.ids['spinner2'].active = True
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0, "center_y": 0},
            size_hint=(1, 1),
            # use_pagination=True,
            # check=True,
            rows_num=1000,
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

        self.ids.container.add_widget(self.data_tables)
        self.ids['spinner2'].active = False

    def close_data_table(self, *args):
        self.ids.container.remove_widget(self.data_tables)

    def insert_db(self):

        query = f"insert into taginfo values ({self.ids['spinner2'].text})"
        self.db.c.execute(query)
        rows = self.db.c.fetchall()

    def file_manager_open(self):
        self.file_manager.show('/home/scientist/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def connect_wifi(self):
        self.ids['spinnerwifi'].active = True
        SSID = self.ids["ssid"].text
        PASS = self.ids["passkey"].text
        self.config_lines = [
            'ctrl_interface=DIR=var/run/wpa_supplicant Group=netdev',
            'update_config=1',
            'country=IN',
            '\n',
            'network={',
            '\tssid="{}"'.format(SSID),
            '\tpsk="{}"'.format(PASS),
            '\tkey_mgmt=WPA-PSK',
            '}'
        ]

        self.config = '\n'.join(self.config_lines)
        print(self.config)

        # with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
        #     wifi.write(self.config)
        print("Wifi config added")
        self.ids['spinnerwifi'].active = False
        subprocess.call(["sudo", "systemctl", "daemon-reload"])
        subprocess.call(["sudo", "systemctl", "restart", "dhcpcd"])
        # subprocess.call(["sudo", "dhclient", "wlan0"])
        # print("changed Network")
        self.ids['wifi_connect'].text = "Connected"
        myip = socket.gethostbyname(socket.gethostname())
        self.ids['ip'].text = myip



class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (800, 480)
    Window.borderless = True

    DemoApp().run()
    # MyLayout().run()
