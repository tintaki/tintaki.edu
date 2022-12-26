import json
from urllib import request
from configparser import ConfigParser

def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
    
class Weather:

 def __init__(self, city_name: str) -> None:
    self.api_key = _get_api_key()
    self.city_name = city_name
    self.weather = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"

 def get_weather_data(self):
    print(self.weather)
    response = request.urlopen(self.weather)
    data = response.read()
    return json.loads(data)