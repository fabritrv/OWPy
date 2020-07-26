from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pyowm

from dataClass.forecastHandler import ForecastHandler
from dataClass.locationData import Location
from dataClass.weatherData import WeatherData


def executor(key, loc, unit):
    owm = pyowm.OWM(key)
    location = Location(loc)
    meas = [WeatherData(location, owm, unit)]
    handler = ForecastHandler(location, owm, unit)
    meas = handler.get_full_data(meas)
    temps = []
    hums = []
    curr = datetime.now().strftime("%m/%d,%H")
    times = [curr]
    c = 0
    print(
        "\n\n----------------------------------------WEATHER FORECAST----------------------------------------\n"
    )
    for w in meas:
        if c > 12:
            break
        temps.append(w.get_temp())
        hums.append(w.get_hum())
        temporary = ""
        if c == 0:
            temporary = curr
        if c != 0:
            temporary = (datetime.now() + timedelta(hours=3) * c).strftime("%m/%d,%H")
            times.append(temporary)
        c += 1
        print(temporary + ":00 - " + w.get_status() + "\n")
    plot_creator(times, temps, hums, unit)


def plot_creator(times, temps, hums, unit):
    print("Check the plots for more in detail info.")
    plt.subplot(2, 1, 1)
    plt.plot(times, temps)
    plt.title("Temperature and humidity % in the next 36 hours")
    if unit == "celsius":
        plt.ylabel("Temperature " + "[°C]")
        plt.ylim([-5, 40])
    elif unit == "fahrenheit":
        plt.ylabel("Temperature " + "[°F]")
        plt.ylim([25, 104])
    plt.xlabel("Time")

    plt.subplot(2, 1, 2)
    plt.plot(times, hums)
    plt.ylabel("Humidity %")
    plt.xlabel("Time")
    plt.ylim([0, 100])

    plt.show()
