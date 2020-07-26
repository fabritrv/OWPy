from weatherData import WeatherData


class ForecastData(WeatherData):
    def __init__(self, weather, unit):
        self._temp = weather.get_temperature(str(unit))["temp"]
        self._hum = weather.get_humidity()
        self._pres = weather.get_pressure()
        self._status = weather.get_status()
