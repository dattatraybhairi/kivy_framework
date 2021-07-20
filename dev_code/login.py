#!/usr/bin/env python
import socket
import asyncio

from kivy.app import async_runTouchApp
import subprocess
from kivy.config import Config
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
from kivy.uix.textinput import TextInput
from self import self

login_key = False
Config.set('kivy', 'keyboard_mode', 'dock')
loop = asyncio.get_event_loop()


class Calc(TextInput):
    def _keyboard_close(self):
        pass

    def setup_keyboard(self):
        kb = Window.request_keyboard(self._keyboard_close, self)
        if kb.widget:
            # kb.widget.layout = 'numeric.json'
            kb.widget.font_size = 38
            kb.widget.height = 350
            # kb.widget.width = 100


class DbCon:

    def __init__(self):
        self.db = MySQLdb.connect(user="vacus", passwd="vacus321", db="vacus")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM taginfo")
        self.row = self.c.fetchall()
        print(self.row)
        self.c.close()
        return self.row


class Tab(FloatLayout, MDTabsBase):
    pass


class MyLayout(BoxLayout, MDApp):
    dialog = None
    fileError = None
    wifi = None
    cam_error = None
    key = Calc()

    # theme_cls = ThemeManager()
    def __init__(self, **kwargs):
        # self.key.setup_keyboard()
        super().__init__(**kwargs)
        self.manager_open = False
        self.login_key = False
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

    def open_data_table(self):
        self.db = DbCon()
        self.rows = self.db.get_rows()
        # print(len(self.rows))
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0, "center_y": 0},
            size_hint=(1, 1),
            # use_pagination=True,
            # check=True,
            # rows_num=100,
            column_data=[
                # page1
                ("No.", dp(15)),  # 0
                ("Physical", dp(25)),  # 1
                ("Data Center", dp(25)),  # 2
                ("Description", dp(25)),  # 3
                ("Device Model", dp(25)),  # 4
                ("Floor", dp(30), self.sort_on_team),  # 5
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
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                 row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16],
                 #
                 row[17], row[18], row[19], row[20], row[21], row[22], row[23],
                 row[24], row[25], row[26], row[27], row[28], row[29],
                 row[30],  # row[31],

                 ) for row in self.rows
            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2
        )
        Config.set('kivy', 'keyboard_mode', 'system')
        self.ids.container.add_widget(self.data_tables)
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)

    def sort_on_signal(self, data):
        return sorted(data, key=lambda l: l[2])

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    def sort_on_signal(self, data):
        return sorted(data, key=lambda l: l[2])

    def sort_on_schedule(self, data):
        return sorted(data, key=lambda l: sum([int(l[-2].split(":")[0]) * 60, int(l[-2].split(":")[1])]))

    def sort_on_team(self, data):
        return sorted(data, key=lambda l: l[-1])

    def close_data_table(self, *args):
        self.ids.container.remove_widget(self.data_tables)

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
    loop.run_until_complete(
        async_runTouchApp(DemoApp().run(), async_lib='asyncio'))
    loop.close()

    # DemoApp().run()
    # MyLayout().run()
