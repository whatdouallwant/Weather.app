from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class MainScr(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        Builder.load_file("style.kv")
        self.screen = MainScr(name="home")
        return self.screen


MainApp().run()