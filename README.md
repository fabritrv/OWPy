# OWPy
Simple Python program that uses OpenWeatherMap's APIs to display temperature and humidity % for the next 36 hours, given a certain location.

#### HOW TO USE:
Insert in the main:
1. API key: get it at OpenWeatherMap's [website](openweathermap.org/api);
2. Location: using the format 'City, SC' where
    1. City = name of your city;
    2. SC= two letter state code, eg. US;
3. Unit of measurement: 'celsius' or 'fahreneit'.

#### NOTE:
pyowm - a library which OWPy relies on - went from version 2.x to version 3.x, and it wasn't a soft transition at all. It basically change all the previous code, forcing devs who use it to review all the project that include it. For this reason the project is currently WIP and will see some changes soon.
