#!/usr/bin/env python
import socket
import asyncio
from MySQLdb import IntegrityError
from kivy.config import Config
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
import MySQLdb
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.list import TwoLineIconListItem
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
        self.c.execute("SELECT * FROM demo")
        self.row = self.c.fetchall()
        print(self.row)
        # self.c.close()
        # self.db.close()
        return self.row

    def insert_query(self, query):
        self.c.execute(query)
        self.db.commit()


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
    db = DbCon()

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

    def inserting_into_database(self):
        if len(self.ids.RFID.text.strip()) != 0:
            print(self.ids.RFID.text.strip())
            try:
                query = f"insert into demo values ('{self.ids.RFID.text}'," \
                        f"'{self.ids.AssetSN.text}'," \
                        f"'{self.ids.DataCenter.text}'," \
                        f"'{self.ids.Description.text}'," \
                        f"'{self.ids.DeviceModel.text}'," \
                        f"'{self.ids.Floor.text}'," \
                        f"'{self.ids.Manufacturer.text}'," \
                        f"'{self.ids.AssetUnitUsage.text}'," \
                        f"'{self.ids.Room.text}'," \
                        f"'{self.ids.SerialNumber.text}'," \
                        f"'{self.ids.RackNo.text}'," \
                        f"'{self.ids.Column.text}'," \
                        f"'{self.ids.Supplier.text}'," \
                        f"'{self.ids.Address.text}'," \
                        f"'{self.ids.MacAddress1.text}'," \
                        f"'{self.ids.MacAddress2.text}'," \
                        f"'{self.ids.EquipmentCategory.text}'," \
                        f"'{self.ids.Weight.text}'," \
                        f"'{self.ids.InventoryCode.text}'," \
                        f"'{self.ids.LifeCycle.text}'," \
                        f"'{self.ids.Power.text}'," \
                        f"'{self.ids.LastMaintenanceStaff.text}'," \
                        f"'{self.ids.MaintenanceCycle.text}'," \
                        f"'{self.ids.Current.text}'," \
                        f"'{self.ids.NextMaintenanceStaff.text}'," \
                        f"'{self.ids.Principal.text}'," \
                        f"'{self.ids.Voltage.text}'," \
                        f"'{self.ids.LastUpdatedTime.text}'," \
                        f"'{self.ids.MaintenanceContact.text}'," \
                        f"'{self.ids.FirstUseTime.text}'," \
                        f"'{self.ids.NextUpdateTime.text}')"
                self.db.insert_query(query)
                self.change_screen("screen2")
                toast("Data Stor`ed Successfully !")
            except IntegrityError as err:
                print(err)
                toast("Alredy exists !")

        else:
            toast("Please enter proper data !")

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

    def clear_entries(self):
        self.ids.RFID.text = ""
        self.ids.AssetSN.text = ""
        self.ids.DataCenter.text = ""
        self.ids.Description.text = ""
        self.ids.DeviceModel.text = ""
        self.ids.Floor.text = ""
        self.ids.Manufacturer.text = ""
        self.ids.AssetUnitUsage.text = ""
        self.ids.Room.text = ""
        self.ids.SerialNumber.text = ""
        self.ids.RackNo.text = ""
        self.ids.Column.text = ""
        self.ids.Supplier.text = ""
        self.ids.Address.text = ""
        self.ids.MacAddress1.text = ""
        self.ids.MacAddress2.text = ""
        self.ids.EquipmentCategory.text = ""
        self.ids.Weight.text = ""
        self.ids.InventoryCode.text = ""
        self.ids.LifeCycle.text = ""
        self.ids.Power.text = ""
        self.ids.LastMaintenanceStaff.text = ""
        self.ids.MaintenanceCycle.text = ""
        self.ids.Current.text = ""
        self.ids.NextMaintenanceStaff.text = ""
        self.ids.Principal.text = ""
        self.ids.Voltage.text = ""
        self.ids.LastUpdatedTime.text = ""
        self.ids.MaintenanceContact.text = ""
        self.ids.FirstUseTime.text = ""
        self.ids.NextUpdateTime.text = ""

        self.ids.AssetSN2.text = ""
        self.ids.DataCenter2.text = ""
        self.ids.Description2.text = ""
        self.ids.DeviceModel2.text = ""
        self.ids.Floor2.text = ""
        self.ids.Manufacturer2.text = ""
        self.ids.AssetUnitUsage2.text = ""
        self.ids.Room2.text = ""
        self.ids.SerialNumber2.text = ""
        self.ids.RackNo2.text = ""
        self.ids.Column2.text = ""
        self.ids.Supplier2.text = ""
        self.ids.Address2.text = ""
        self.ids.MacAddress12.text = ""
        self.ids.MacAddress22.text = ""
        self.ids.EquipmentCategory2.text = ""
        self.ids.Weight2.text = ""
        self.ids.InventoryCode2.text = ""
        self.ids.LifeCycle2.text = ""
        self.ids.Power2.text = ""
        self.ids.LastMaintenanceStaff2.text = ""
        self.ids.MaintenanceCycle2.text = ""
        self.ids.Current2.text = ""
        self.ids.NextMaintenanceStaff2.text = ""
        self.ids.Principal2.text = ""
        self.ids.Voltage2.text = ""
        self.ids.LastUpdatedTime2.text = ""
        self.ids.MaintenanceContact2.text = ""
        self.ids.FirstUseTime2.text = ""
        self.ids.NextUpdateTime2.text = ""


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
        self.clear_entries()
        # self.ids.container.

    def open_data_table(self):
        if not self.database_key:
            self.rows = self.db.get_rows()
            self.database_key = True
            count = 0
            for i in self.rows:
                count = count + 1
                self.ids.container.add_widget(
                    ListItemWithCheckbox(text=f"{count}",
                                         on_release=self.click,
                                         secondary_text=f"{i[0]},{i[1]},{i[2]},{i[3]},{i[7]} ",
                                         )
                )
        else:
            # ListItemWithCheckbox.clear_widgets(self.ids.container)
            toast("Already Loaded")

    def cleardatabase(self):
        self.database_key = False
        self.clear_entries()
        ListItemWithCheckbox.clear_widgets(self.ids.container)

    def click(self, ListItemWithCheckbox):
        # print(str(ListItemWithCheckbox.text))
        print(self.rows[int(ListItemWithCheckbox.text) - 1])
        self.ids.RFID1.text = self.rows[int(ListItemWithCheckbox.text) - 1][0]
        self.ids.AssetSN2.text = self.rows[int(ListItemWithCheckbox.text) - 1][1]
        self.ids.DataCenter2.text = str(self.rows[int(ListItemWithCheckbox.text) - 1][2])
        self.ids.Description2.text = self.rows[int(ListItemWithCheckbox.text) - 1][3]
        self.ids.DeviceModel2.text = self.rows[int(ListItemWithCheckbox.text) - 1][4]
        self.ids.Floor2.text = self.rows[int(ListItemWithCheckbox.text) - 1][5]
        self.ids.Manufacturer2.text = self.rows[int(ListItemWithCheckbox.text) - 1][6]
        self.ids.AssetUnitUsage2.text = self.rows[int(ListItemWithCheckbox.text) - 1][7]
        self.ids.Room2.text = self.rows[int(ListItemWithCheckbox.text) - 1][8]
        self.ids.SerialNumber2.text = self.rows[int(ListItemWithCheckbox.text) - 1][9]
        self.ids.RackNo2.text = self.rows[int(ListItemWithCheckbox.text) - 1][10]
        self.ids.Column2.text = self.rows[int(ListItemWithCheckbox.text) - 1][11]
        self.ids.Supplier2.text = self.rows[int(ListItemWithCheckbox.text) - 1][12]
        self.ids.Address2.text = self.rows[int(ListItemWithCheckbox.text) - 1][13]
        self.ids.MacAddress12.text = self.rows[int(ListItemWithCheckbox.text) - 1][14]
        self.ids.MacAddress22.text = self.rows[int(ListItemWithCheckbox.text) - 1][15]
        self.change_screen("screen9")

    def update_database(self):
        print(self.ids.AssetSN2.text)
        query =f"update demo set AssetSN = '{self.ids.AssetSN2.text}'," \
               f"DataCenter = '{self.ids.DataCenter2.text}'," \
               f"Description = '{self.ids.Description2.text}'," \
               f"DeviceModel = '{self.ids.DeviceModel2.text}'," \
               f"Floor = '{self.ids.Floor2.text}'," \
               f"Manufacturer = '{self.ids.Manufacturer2.text}'," \
               f"AssetUnitUsage = '{self.ids.AssetUnitUsage2.text}'," \
               f"Room = '{self.ids.Room2.text}'," \
               f"SerialNumber = '{self.ids.SerialNumber2.text}'," \
               f"RackNo = '{self.ids.RackNo2.text}'," \
               f"Cols = '{self.ids.Column2.text}'," \
               f"Supplier = '{self.ids.Supplier2.text}'," \
               f"Address = '{self.ids.Address2.text}'," \
               f"MacAddress1 = '{self.ids.MacAddress12.text}'," \
               f"MacAddress2 = '{self.ids.MacAddress22.text}'," \
               f"EquipmentCategory = '{self.ids.EquipmentCategory2.text}'," \
               f"Weight = '{self.ids.Weight2.text}'," \
               f"InventoryCode = '{self.ids.InventoryCode2.text}'," \
               f"LifeCycle = '{self.ids.LifeCycle2.text}'," \
               f"Power = '{self.ids.Power2.text}'," \
               f"LastMaintenanceStaff = '{self.ids.LastMaintenanceStaff2.text}'," \
               f"MaintenanceCycle = '{self.ids.MaintenanceCycle2.text}'," \
               f"Current = '{self.ids.Current2.text}'," \
               f"NextMaintenanceStaff = '{self.ids.NextMaintenanceStaff2.text}'," \
               f"Principal = '{self.ids.Principal2.text}'," \
               f"Voltage = '{self.ids.Voltage2.text}'," \
               f"LastUpdatedTime = '{self.ids.LastUpdatedTime2.text}'," \
               f"MaintenanceContact = '{self.ids.MaintenanceContact2.text}',"\
               f"FirstUseTime = '{self.ids.FirstUseTime2.text}'," \
               f"NextUpdateTime = '{self.ids.NextUpdateTime2.text}' "\
               f"where RFID = '{self.ids.RFID1.text}'"
        print(query)
        self.db.insert_query(query)
        toast("Data Entry Updated !")

    def delete_entry(self):
        query = f"delete from demo where RFID = '{self.ids.RFID1.text}'"
        self.db.insert_query(query)
        toast("Data Entry Deleted!")
        self.change_screen("screen5")

    def delete_all_entries(self):
        query = f"delete from demo"
        self.db.insert_query(query)
        toast("All Entries Deleted!")
        # self.change_screen("screen5")

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
    DemoApp().run()
    # MyLayout().run()
