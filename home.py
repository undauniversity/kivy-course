from kivy.app import App
from kivymd.app import MDApp

from kivy.properties import ObjectProperty
from kivy.lang import Builder

import urllib.request, json

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout



def cekLogin(username, password):
    with urllib.request.urlopen("http://localhost/lat/api.php?auth=888&perintah=loginMhs&user="+username+"&pass="+password) as json_url:
        data = json.loads(json_url.read())
        usernameTabel = data[0]["npm"]
        passwordTabel = data[0]["password"]


        #root.manager.current = 'Beranda'
        if username==usernameTabel and password==passwordTabel:
            print("Login Berhasil")
            data=1
        else:
            print("login gagal")
            data=0

    return data

class LoginScreen(Screen):
    def doLogin(self):
        #print("Halooo")
        cekLogin(self.txtUsername_.text,self.txtPassword_.text)


class HomeScreen(Screen):
    pass


class SignupScreen(Screen):
    pass

'''
class MylayoutForm(MDBoxLayout):
    def doLogin(self):
        #print("Explicit is better than implicit.")
        #self.txtPassword_.text="halo"
        cekLogin(self.txtUsername_.text,self.txtPassword_.text) #cek isi dari txtUsername_ dan txtPassword_
'''
'''
class LoginScreen(MDBoxLayout):
   def doLogin(self):
        print("Halooo")
'''

# penamaan class harus sama dengan file kv
# sim.kv
# nama class WAJIB SimApp
class SimApp(MDApp):
    pass
if __name__ == '__main__':
     def build(self):
        self.theme_cls.primary_palette = "Blue"
SimApp().run()
        