from kivymd.uix.backdrop.backdrop import MDCard
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from settings import *
import requests
from kivymd.uix.card import MDCard

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
    def create_card(self, data):
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        if 'dt_txt' in data:
            date = data['dt_txt'][5:-3]
        else:
            date = 'Зараз'
        new_card = MyMDCard(date, icon, temp, feels, description, wind_speed, humidity)
        self.ids.carousel.add_widget(new_card)

    def searching(self):
        self.ids.carousel.clear_widgets()
        city = self.ids.find_city.text.lower().strip()
        print(city)
        current_weather = self.get_data(WEATHER_URL, city)
        self.create_card(current_weather)

        forecast_weather = self.get_data(FORECAST_URL, city)
        for period in forecast_weather['list']:
            self.create_card(period)





class MyMDCard(MDCard):
    def __init__(self, date, image, curr_temp, feelslike, description, wind, wet, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.time.text = date
        self.ids.image.source = f'https://openweathermap.org/img/wn/{image}@2x.png'
        self.ids.curr_temp.text = f'{curr_temp}°C'
        self.ids.feelslike.text = f'Відчувається як {feelslike}°C'
        self.ids.description.text = f'{description}'
        self.ids.wind.text = f'Швидкість вітру: {wind} м/с'
        self.ids.wet.text = f'Вологість: {wet}%'

class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        Builder.load_file("style.kv")
        self.screen = MainScr(name="home")
        return self.screen


MainApp().run()