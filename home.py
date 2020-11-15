from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import urllib.request, json


class MylayoutForm(MDBoxLayout):
    def doLogin(self):
        #print("Explicit is better than implicit.")
        self.txtPassword_.text="halo"

class MylayoutApp(MDApp):
    pass
if __name__ == '__main__':
     def build(self):
        self.theme_cls.primary_palette = "Blue"
MylayoutApp().run()
        