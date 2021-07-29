from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.list import MDList, OneLineListItem,TwoLineListItem
from kivy.lang import Builder
from kivymd.label import MDLabel
from kivymd.button import MDFlatButton,MDRaisedButton
import threading
from models_sql import *
from kivy.properties import ObjectProperty
from kivymd.textfields import SingleLineTextField
from kivymd.spinner import MDSpinner
from kivy.uix.floatlayout import FloatLayout
session = Session()


kv = ''' 
Testimonies:
    Button:

        text: " Testify"
        size_hint: None, None
        size: 4 * dp(40), dp(40)
        pos_hint: {'center_x': 0.2, 'center_y': 0.3}
        font_name: 'Roboto-Regular'
        on_release: root.share();



<F>:
    name: name
    message: message

    id: sub_button
    title: 'Share Your Testimony'
    markup: True
    size_hint: .9, None
    height: dp(300)
    pos_hint:{'center_x': 0.5, 'center_y': 0.65}
    FloatLayout:
        SingleLineTextField:
            id: name
            hint_text: 'Name'
            multiline: False
            pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        SingleLineTextField:
            id: message
            hint_text: 'Message'
            multiline: True
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}

        MDFlatButton:
            text: 'ShieeeeeeM)'
            pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            on_press: root.shiemor()


<DBScroll>:
    id: dbscroll
    title: ''
    size_hint: None, None
    size: 400,100
    FloatLayout:
        Label:
            text: 'Sending'
            pos_hint:{'center_x': 0.8, 'center_y': 0.7}
            size_hint: None, None
            size: 50,100

        MDSpinner:
            size_hint: None,None
            size: dp(30),dp(30)
            pos_hint:{'center_x': 0.2, 'center_y': 0.7}

'''



class DBScroll(Popup):
    pass

class F(Popup):
    stop = threading.Event()
    name = ObjectProperty(None)
    message = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(F, self).__init__(**kwargs)

    def start_second_thread(self):
        threading.Thread(target=self.popman()).start()

    def shiemor(self):
        self.start_second_thread()
        print('starting thread')
        add_testimony = Testify(name=self.ids.name.text, message=self.ids.message.text)
        session.add(add_testimony)
        print(' connecting to external db')

        session.commit()
        self.ids.name.text= ""
        self.ids.message.text= ''
        print('done ')
        #self.dismiss() use this to close the popUp


    def popman(self):
        pop = DBScroll(auto_dismiss=True)
        pop.open()





class Testimonies(BoxLayout):
    def __init__(self, **kwargs):
        super(Testimonies, self).__init__(**kwargs)

    def share(self):
        pop = F()
        pop.open()



class Stack(App):
    def build(self):
        #return Testimonies()
        return Builder.load_string(kv)


if __name__=="__main__":
    Stack().run()