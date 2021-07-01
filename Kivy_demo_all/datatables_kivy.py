from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.logger import Logger

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

kv = '''
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        id:button_tab
        size_hint_y:None
        height: dp(48)

        MDFlatButton:
            text: "Hello <3"
            on_release:
                app.update_row_data()

    BoxLayout:
        id:body

'''

class Example(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            # MDDataTable allows the use of size_hint
            size_hint=(0.8, 0.7),
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60), self.sort_on_signal),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30), self.sort_on_schedule),
                ("Team Lead", dp(30), self.sort_on_team)
            ],
            row_data=[
                ("1", ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                 "Astrid: NE shared managed", "Medium", "Triaged", "0:33",
                 "Chase Nguyen"),
                ("2", ("alert-circle", [1, 0, 0, 1], "Offline"),
                 "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
                 "Brie Furman"),
                ("3", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Phoenix: prod shared lyra-lists", "Minor",
                 "Not Triaged", "3:12", "Jeremy lake"),
                ("4", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Sirius: NW prod shared locations",
                 "Negligible",
                 "Triaged", "13:18", "Angelica Howards"),
                ("5", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Sirius: prod independent account",
                 "Negligible",
                 "Triaged", "22:06", "Diane Okuma"),

            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        root = Builder.load_string(kv)
        root.ids.body.add_widget(self.data_tables)
        return root

    def update_row_data(self, *dt):
        self.data_tables.row_data = [
        (
            "21",
            ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
            "Astrid: NE shared managed",
            "Medium",
            "Triaged",
            "0:33",
            "Chase Nguyen"
        ),
        ("32", ("alert-circle", [1, 0, 0, 1], "Offline"),
        "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
        "Brie Furman"),
        ("43", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Phoenix: prod shared lyra-lists", "Minor",
        "Not Triaged", "3:12", "Jeremy lake"),
        ("54", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: NW prod shared locations",
        "Negligible",
        "Triaged", "13:18", "Angelica Howards"),
        ("85", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: prod independent account",
        "Negligible",
        "Triaged", "22:06", "Diane Okuma"),
        ("85", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: prod independent account",
        "Negligible",
        "Triaged", "22:06", "John Sakura"),
        ]


    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    # Sorting Methods:
    # Since the # 914 Pull request, the sorting method requires you to sort
    # out the indexes of each data value for the support of selections

    # The most common method to do this is with the use of the bult-in function
    # zip and enimerate, see the example below for more info.

    # the result given by these funcitons must be a list in the format of
    # [Indexes, Sorted_Row_Data]


    def sort_on_signal(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][2]
            )
        )

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [int(l[1][-2].split(":")[0])*60,
                    int(l[1][-2].split(":")[1])]
                )
            )
        )

    def sort_on_team(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][-1]
            )
        )

Example().run()