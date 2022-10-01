from Weather import Weather
from WeatherModel import WeatherModel
# def main(name):
while True:
    user_answer = raw_input("Enter the city. If you want to exit, press 'q': ")
    if user_answer == "q":
        break
    weather = Weather(user_answer)
    weather.get_weather()
    weatherModel = WeatherModel(weather.get_weather())
    print("Temperature: " + str(weatherModel.get_temp()))
    print("Pressure: " + str(weatherModel.get_pressure()))
    print("Humidity: " + str(weatherModel.get_humidity()))
    print("Wind speed: " + str(weatherModel.get_windSpeed()))
    print("Wind direction: " + str(weatherModel.get_windDirection()))
    print("coordination lat: " + str(weatherModel.get_lat()))
    print("coordination lon: " + str(weatherModel.get_lon()))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')
