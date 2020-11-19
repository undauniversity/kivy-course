from kivy.app import App
from kivymd.app import MDApp

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.properties import ObjectProperty
from kivy.lang import Builder

import urllib.request, json


def cekLogin(username, password):
    with urllib.request.urlopen("http://localhost/lat/api2.php?auth=888") as json_url:
        data = json.loads(json_url.read().decode())
        #print(data)
        print(json.dumps(data, indent=3, sort_keys=True))
        print("isi data=" +username +", " +password)
    return data


class MylayoutForm(MDBoxLayout):
    def doLogin(self):
        #print("Explicit is better than implicit.")
        self.txtPassword_.text="halo"
        cekLogin(self.txtUsername_.text,self.txtPassword_.text) #cek isi dari txtUsername_ dan txtPassword_

#penamaan class harus sama dengan file kv
# mylayout.kv
# nama class WAJIB MylayoutApp
class MylayoutApp(MDApp):
    pass
if __name__ == '__main__':
     def build(self):
        self.theme_cls.primary_palette = "Blue"
MylayoutApp().run()
        