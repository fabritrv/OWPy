from geopy.geocoders import Nominatim


class Location:
    _lat = 0
    _lon = 0

    def __init__(self, loc):
        locator = Nominatim(user_agent="owp")
        location = locator.geocode(loc)
        self._lat = location.latitude
        self._lon = location.longitude

    def get_lat(self):
        return self._lat

    def get_lon(self):
        return self._lon
