class WeatherModel:

    def __init__(self, weathArr):
        self.__temp = weathArr["main"]["temp"]
        self.__pressure = weathArr["main"]["pressure"]
        self.__humidity = weathArr["main"]["humidity"]
        self.__windSpeed = weathArr["wind"]["speed"]
        self.__windDirection = weathArr["wind"]["deg"]
        self.__lat =weathArr["coord"]["lat"]
        self.__lon = weathArr["coord"]["lon"]


    def get_temp(self):
        return self.__temp

    def get_pressure(self):
        return self.__pressure

    def get_humidity(self):
        return self.__humidity

    def get_windSpeed(self):
        return self.__windSpeed

    def get_windDirection(self):
        return self.__windDirection

    def get_lat(self):
        return self.__lat

    def get_lon(self):
        return self.__lon
