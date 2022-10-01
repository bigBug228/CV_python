import unittest
import Weather
import WeatherModel
class MyTestCase(unittest.TestCase):
    def test_api(self):
        weather = Weather.Weather('dublin')
        api = weather.get_api()
        self.assertTrue(api.islower())
        self.assertEqual(api,"8f85fe04689c187c5fca4207c404609b")
    def test_url(self):
        weather = Weather.Weather('dublin')
        urlEndPoint = weather.get_url()
        self.assertTrue(urlEndPoint.islower())
        self.assertEqual(urlEndPoint,"https://api.openweathermap.org/data/2.5/weather?")
    def test_lat(self):
        weather =Weather.Weather('dublin')
        weather =weather.get_weather()
        weatherModel = WeatherModel.WeatherModel(weather)
        lat = weatherModel.get_lat()
        self.assertAlmostEqual(lat,37.7021)

    def test_lon(self):
        weather = Weather.Weather('dublin')
        weather = weather.get_weather()
        weatherModel = WeatherModel.WeatherModel(weather)
        lat = weatherModel.get_lon()
        self.assertAlmostEqual(lat, -121.9358)

if __name__ == '__main__':
    unittest.main()
