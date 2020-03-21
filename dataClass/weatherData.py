class WeatherData:

    _temp = 0
    _hum = 0
    _pres = 0

    def __init__(self, location, owm, unit):
        weather = owm.weather_at_coords(location.get_lat(), location.get_lon()).get_weather()
        self._temp = weather.get_temperature(str(unit))["temp"]
        self._hum = weather.get_humidity()
        self._pres = weather.get_pressure()
        self._status = weather.get_status()

    def get_temp(self):
        return self._temp

    def get_hum(self):
        return self._hum

    def get_status(self):
        return self._status

