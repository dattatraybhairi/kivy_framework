# code to show how to use nested boxlayouts.

# import kivy module
import kivy

# this restricts the kivy version i.e
# below this kivy version you cannot
# use the app or software
# kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size = (300, 100)


# class in which we are creating the button by using boxlayout
# defining the App class
class BoxLayoutApp(App):

    def build(self):
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets
        superBox = BoxLayout(orientation='vertical')

        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation='horizontal')

        btn1 = Button(text="One")
        btn2 = Button(text="Two")

        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(btn1)
        HB.add_widget(btn2)

        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = BoxLayout(orientation='vertical')

        btn3 = Button(text="Three")
        btn4 = Button(text="Four")

        # VB represents the vertical boxlayout orientation
        # declared above
        VB.add_widget(btn3)
        VB.add_widget(btn4)

        # superbox used to again align the orented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox


# creating the object root for BoxLayoutApp() class
root = BoxLayoutApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
