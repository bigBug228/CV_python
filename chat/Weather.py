import requests
class Weather:
    __API = "8f85fe04689c187c5fca4207c404609b"
    __URL_endpoint = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, city):
        self.city = city

    def get_weather(self):
        params = {
            "q": self.city,
            "appid": self.__API,
            "units": "metric"
        }
        response = requests.get(self.__URL_endpoint, params)
        data = response.json()
        return data
    def get_api(self):
        return self.__API

    def get_url(self):
        return self.__URL_endpoint