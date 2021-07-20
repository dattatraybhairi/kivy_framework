from kivy.garden.cefpython import CefBrowser, cefpython
from kivy.app import App

class CefBrowserApp(App):
    def build(self):
        return CefBrowser(start_url='http://kivy.org')

CefBrowserApp().run()

cefpython.Shutdown()