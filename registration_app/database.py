from kivy.app import App
import MySQLdb
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class DbCon:

    def __init__(self):
        self.db = MySQLdb.connect(user="vacus",passwd="vacus321",db="vacus")
        self.c = self.db.cursor()

    def get_rows(self,search = ""):
        self.c.execute("SELECT * FROM taginfo WHERE assettag REGEXP '.*%s.*' LIMIT 3" % search)
        return self.c.fetchall()


class Table(BoxLayout):

    def __init__(self,**kwargs):
        super(Table,self).__init__(**kwargs)

        self.orientation = "vertical"

        self.search_field = BoxLayout(orientation="horizontal")

        self.search_input = TextInput(text='search',multiline=False)
        self.search_button = Button(text="search",on_press=self.search)

        self.search_field.add_widget(self.search_input)
        self.search_field.add_widget(self.search_button)

        self.add_widget(self.search_field)

        self.add_widget(Label(text="table"))

        self.table = GridLayout(cols=2,rows=4)
        self.table.add_widget(Label(text="Fruit"))
        self.table.add_widget(Label(text="Price"))

        self.rows = [[Label(text="item"),Label(text="price")],
                     [Label(text="item"),Label(text="price")],
                     [Label(text="item"),Label(text="price")]]

        for item,price in self.rows:
            self.table.add_widget(item)
            self.table.add_widget(price)

        self.add_widget(self.table)


        self.db = DbCon()
        self.update_table()


    def update_table(self,search=""):
        for index,row in enumerate(self.db.get_rows(search)):
            self.rows[index][0].text = row[1]
            self.rows[index][1].text = str(row[2])

    def clear_table(self):
        for index in range(3):
            self.rows[index][0].text = ""
            self.rows[index][1].text = ""


    def search(self, *args):
        self.clear_table()
        self.update_table(self.search_input.text)


class MyApp(App):
    def build(self):
        return Table()


MyApp().run()