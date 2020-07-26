from forecastData import ForecastData


class ForecastHandler:

    _weathers = []

    def __init__(self, location, owm, unit):
        for f in (
            owm.three_hours_forecast_at_coords(location.get_lat(), location.get_lon())
            .get_forecast()
            .get_weathers()
        ):
            self._weathers.append(ForecastData(f, unit))

    def get_full_data(self, meas):
        for w in self._weathers:
            meas.append(w)
        return meas
