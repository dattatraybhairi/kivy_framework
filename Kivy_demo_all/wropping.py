import socket
import sys
import os
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
class TextInputApp(App):
    def build(self):

        layout = BoxLayout(padding=10, orientation='vertical')
        # Second boxlayout
        layout2 = BoxLayout()
        # Add BoxLayout do main layout
        layout.add_widget(layout2)

        # Drop old size and pos_hints
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        # Add Button to secondary boxlayout
        layout2.add_widget(btn1)
        self.txt1 = TextInput(multiline=False, text='',
                                           size_hint=(0.5, 0.1))
        layout.add_widget(self.txt1)
        # Drop size_hint
        self.lbl1 = Label(text="Write your guess in the blank text box")
        layout2.add_widget(self.lbl1)

        return layout
    def buttonClicked(self,btn):
        print( "hi")

TextInputApp().run()