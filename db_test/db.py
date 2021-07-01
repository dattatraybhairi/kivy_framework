from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable

KV = """
MDScreen:
    MDRaisedButton:
        id: btn
        text: "Open DataTables"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            app.open_data_table()

    AnchorLayout:
        id: container

"""


class Example(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)

    def open_data_table(self):
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.95, 0.3),
            # use_pagination=True,
            rows_num=10,
            column_data=[
                ("Subject", dp(25)),
                ("Enrll", dp(13)),
                ("Online", dp(13)),
                ("No Device", dp(15)),
                ("Reached", dp(15)),
                ("N.Cntct", dp(15)),
            ],
        )
        self.data_tables.ids.container.add_widget(
            MDRaisedButton(
                text="CLOSE",
                pos_hint={"right": 1},
                on_release=self.close_data_table,
            )
        )
        self.root.ids.btn.disabled = True
        self.root.ids.container.add_widget(self.data_tables)

    def close_data_table(self, *args):
        self.root.ids.btn.disabled = False
        self.root.ids.container.remove_widget(self.data_tables)


Example().run()