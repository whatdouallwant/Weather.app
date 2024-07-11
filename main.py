from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from settings import *
import requests

class MainScr(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_data(self, url, city):
        api_par = {
            "q": city, 
            "appid": API_KEY,

        }
        data = requests.get(url, api_par)
        response = data.json()
        print(response)
        return response
    def searching(self):
        city = self.ids.find_city.text.lower().strip()
        print(city)
        current_weather = self.get_data(WEATHER_URL, city)
        temp = current_weather['main']['temp']
        self.ids.content.text = f"{temp}°C"


class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        Builder.load_file("style.kv")
        self.screen = MainScr(name="home")
        return self.screen


MainApp().run()