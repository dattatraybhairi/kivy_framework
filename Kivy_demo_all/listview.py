import MySQLdb
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem, IRightBodyTouch, TwoLineIconListItem

KV = '''
BoxLayout:
    orientation: "vertical"
    MDToolbar:
        md_bg_color: 0, 0, 1, 1
        id: toolbar
        title: "DataBase List"
        pos_hint:{"top": 1}
                   
    ScrollView:
        MDList:
            id: container
'''


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

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    db = DbCon()
    rows = db.get_rows()

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            self.root.ids.scroll.add_widget(
                TwoLineIconListItem(text=f"Item {i}", icon=icons[i])
            )


def click(self, OneLineListItem):
        print(str(OneLineListItem.text))
        print(self.rows[int(OneLineListItem.text)-1])

Test().run()
