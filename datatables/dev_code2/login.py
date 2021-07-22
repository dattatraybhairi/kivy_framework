#!/usr/bin/env python
import socket
import asyncio

from kivy.config import Config

from kivy.properties import StringProperty

from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager

import MySQLdb
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem, TwoLineIconListItem, OneLineAvatarIconListItem, IRightBodyTouch, \
    TwoLineAvatarIconListItem, ThreeLineAvatarIconListItem
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import os

login_key = False
Config.set('kivy', 'keyboard_mode', 'dock')
loop = asyncio.get_event_loop()


class DbCon:

    def __init__(self):
        self.db = MySQLdb.connect(user="vacus", passwd="vacus321", db="vacus")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM taginfo")
        self.row = self.c.fetchall()
        print(self.row)
        self.c.close()
        self.db.close()
        return self.row


class Tab(FloatLayout, MDTabsBase):
    pass


class ListItemWithCheckbox(TwoLineIconListItem):
    '''Custom list item.'''
    #
    icon = StringProperty("checkbox-marked-circle")


class MyLayout(BoxLayout, MDApp):
    dialog = None
    fileError = None
    wifi = None
    cam_error = None

    # theme_cls = ThemeManager()
    def __init__(self, **kwargs):
        # self.key.setup_keyboard()
        super().__init__(**kwargs)
        self.manager_open = False
        self.login_key = False
        self.database_key = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            # preview=True,
            # ext=[".py", "kv"],
        )

    def disable_cam(self):
        self.ids["zbarcam"].xcamera.play = False

    def check_data_login(self):
        self.ids["zbarcam"].xcamera.play = False

        self.ids["RFID"].text = ""
        # self.ids['spinner'].active = True
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
        print(self.ids['qrlabel'].text)
        if self.login_key:
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
                        text="CANCEL", text_color=self.theme_cls.primary_color,
                        on_release=lambda _: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_release=lambda _: self.logout()
                    ),
                ],
            )
        self.dialog.open()

    def sleep(self):
        p = os.popen('sudo -E sh -c \'echo 0 > /sys/class/backlight/rpi_backlight/bl_power\'')

    def logout(self):
        self.dialog.dismiss()
        self.change_screen("screen1")
        # self.ids.container.

    def open_data_table(self):
        if not self.database_key:
            self.db = DbCon()
            self.rows = self.db.get_rows()
            self.database_key = True
            count = 0
            for i in self.rows:
                count = count + 1
                self.ids.container.add_widget(
                    ListItemWithCheckbox(text=f"{count}",
                                         on_release=self.click,
                                         secondary_text=f"{i[1]},{i[2]},{i[3]},{i[4]},{i[6]} ",
                                         )
                )
        else:
            # ListItemWithCheckbox.clear_widgets(self.ids.container)
            print("Already Loaded")

    def cleardatabase(self):
        self.database_key = False
        ListItemWithCheckbox.clear_widgets(self.ids.container)

    def click(self, ListItemWithCheckbox):
        print(str(ListItemWithCheckbox.text))
        print(self.rows[int(ListItemWithCheckbox.text) - 1])
        self.ids.RFID1.text = self.rows[int(ListItemWithCheckbox.text) - 1][1]
        self.ids.AssetSN2.text = self.rows[int(ListItemWithCheckbox.text) - 1][2]
        self.ids.DataCenter2.text = str(self.rows[int(ListItemWithCheckbox.text) - 1][3])
        self.ids.Description2.text = self.rows[int(ListItemWithCheckbox.text) - 1][4]
        self.ids.DeviceModel2.text = self.rows[int(ListItemWithCheckbox.text) - 1][5]
        self.ids.Floor2.text = self.rows[int(ListItemWithCheckbox.text) - 1][6]
        self.ids.Manufacturer2.text = self.rows[int(ListItemWithCheckbox.text) - 1][7]
        self.ids.AssetUnitUsage2.text = self.rows[int(ListItemWithCheckbox.text) - 1][8]
        self.ids.Room2.text = self.rows[int(ListItemWithCheckbox.text) - 1][9]
        self.ids.SerialNumber2.text = self.rows[int(ListItemWithCheckbox.text) - 1][10]
        self.ids.RackNo2.text = self.rows[int(ListItemWithCheckbox.text) - 1][11]
        self.ids.Column2.text = self.rows[int(ListItemWithCheckbox.text) - 1][12]
        self.ids.Supplier2.text = self.rows[int(ListItemWithCheckbox.text) - 1][13]
        self.ids.Address2.text = self.rows[int(ListItemWithCheckbox.text) - 1][14]
        self.ids.MacAddress12.text = self.rows[int(ListItemWithCheckbox.text) - 1][15]
        self.ids.MacAddress22.text = self.rows[int(ListItemWithCheckbox.text) - 1][16]
        self.change_screen("screen9")

    def file_manager_open(self):
        self.file_manager.show('/home/scientist/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        self.ids["file_location"].text = path
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
        # subprocess.call(["sudo", "systemctl", "daemon-reload"])
        # subprocess.call(["sudo", "systemctl", "restart", "dhcpcd"])
        # subprocess.call(["sudo", "dhclient", "wlan0"])
        # print("changed Network")
        self.ids['wifi_connect'].text = "Connected"
        myip = socket.gethostbyname(socket.gethostname())
        print(myip)
        self.ids['ip'].text = myip

    def upload_file(self):

        IP = self.ids['server_ip'].text
        PORT = 4455
        file_loc = str(self.ids['file_location'].text)
        file_name = file_loc.split("/")
        print(file_name[len(file_name) - 1])
        print(file_name)
        ADDR = (IP, PORT)
        FORMAT = 'utf-8'
        SIZE = 10240
        print(self.ids['file_location'].text, self.ids['server_ip'].text)
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            file = open(self.ids['file_location'].text, "r")
            data = file.read()
            client.send(file_name[len(file_name) - 1].encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"server recived  {msg}")
            client.send(data.encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"server recived  {msg}")

            file.close()
            client.close()
        except Exception as err:
            if not self.fileError:
                self.fileError = MDDialog(
                    title="Connection Failed !",
                    text="verify the file / make sure the server is running",
                    buttons=[
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color,
                            on_release=lambda _: self.fileError.dismiss()
                        ),

                    ],
                )
            self.fileError.open()


class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (800, 480)
    Window.borderless = False
    # Window.size = (1366, 768)
    # loop.run_until_complete(
    #     async_runTouchApp(DemoApp().run(), async_lib='asyncio'))
    # loop.close()

    DemoApp().run()
    # MyLayout().run()
