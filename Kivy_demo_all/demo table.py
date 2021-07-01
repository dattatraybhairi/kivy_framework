from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
import MySQLdb
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

class DbCon:

    def __init__(self):
        self.db = MySQLdb.connect(user="vacus",passwd="vacus321",db="vacus")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM taginfo" )
        self.row = self.c.fetchall()
        # print(self.row)

        return self.row


class Example(MDApp):

    def build(self):
        self.db = DbCon()
        self.rows = self.db.get_rows()
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            #use_pagination=True,
            rows_num=100,
            column_data=[
                ("No.", dp(40)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (f"{row[0] }", row[1], row[2], "3", "4", "5") for row in self.rows
            ],
        )

        print(self.rows[0][2])

        layout.add_widget(data_tables)
        return layout

Example().run()