from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.graphics import Color
from kivy.metrics import dp
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """

Screen:
    NavigationLayout:
        ScreenManager:
            id : scrn_manager
            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        text: 'Meine Einkaufsliste'

                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: "center"
                    RecycleView:
                        id: rv
                        key_viewclass: 'viewclass'
                        key_size: 'height'

                        RecycleBoxLayout:
                            id: rbl
                            orientation: 'vertical'
                            height: dp(650)
                            width: dp(250)

                    MDBottomAppBar:
                        MDToolbar:
                            title: 'Tools'
                            icon: "git"
                            type: "bottom"
                            md_bg_color: app.theme_cls.primary_color
                            specific_text_color: app.theme_cls.accent_color
                            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                            #on_action_button: app.navigation_draw()
                            elevation: 10
                            MDIconButton:
                                icon: 'magnify'
                            MDTextField:
                                id: search_field
                                hint_text: 'Search icon'
        MDNavigationDrawer:
            id: nav_drawer             
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                MDLabel:
                    text: 'Tools'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:    
                    MDList:
                        OneLineIconListItem:
                            on_release: app.new_item()
                            text: 'Neuer Artikel'
                            IconLeftWidget:
                                icon: 'camera-plus'
                        OneLineIconListItem:
                            on_release: app.item_upload()
                            text: 'Synchro auf Server'
                            IconLeftWidget:
                                icon: 'file-upload'

"""


class ShoppinglistApp(MDApp):
    column_data = ListProperty([])
    row_data = ListProperty([])

    def build(self):
        self.screen = Builder.load_string(screen_helper)
        self.data_table()

        return self.screen

    def data_table(self):
        self.datatable = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                     size_hint=(0.9, 0.6),
                                     check=True,
                                     rows_num=10,
                                     column_data=[("Artikel", dp(30)),
                                                  ("Menge", dp(15)),
                                                  ("Geschäft", dp(30))
                                                  ],
                                     row_data=[("Tee: Earl Gray", "1", "Kaufland"),
                                               ("Kartoffeln", "2,5 kg", "Kaufland"),
                                               ("CW Obst&Sahne", "1", "Kaufland"),
                                               ("Bananen etwas grün ", "5", "Aldi"),
                                               ("Mangosaft ", "1", "Kaufland"),
                                               ("Pizateig von Omas Kühltruhe ", "1", "Edeka"),
                                               ("Rinderrouladen Oberschale", "4", "Edeka"),
                                               ("Joghurt 4er ", "2", "Kaufland")
                                               ]
                                     )
        self.datatable.bind(on_check_press=self.check_press)
        self.datatable.bind(on_row_press=self.row_press)
        self.screen.ids.rbl.add_widget(self.datatable)

    def navigation_draw(self):
        print("NAV")

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def new_item(self):
        print('Neuer Artikel')

    def item_upload(self):
        print('Hochladen')


ShoppinglistApp().run()