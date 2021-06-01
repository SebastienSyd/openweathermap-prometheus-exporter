#!/usr/bin/env python3
import time
from prometheus_client import Gauge, start_http_server
from dotenv import load_dotenv
import requests
import logging
import os

logging.basicConfig(format='<%(asctime)s> <%(levelname)s> <%(message)s>', level=logging.INFO)

load_dotenv()

LATITUDE = os.environ.get("OPENWEATHERMAP_LATITUDE")
LONGITUDE = os.environ.get("OPENWEATHERMAP_LONGITUDE")
API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")
UNITS = os.environ.get("OPENWEATHERMAP_UNITS")
INTERVAL = os.environ.get("OPENWEATHERMAP_INTERVAL")
PREFIX = os.environ.get("OPENWEATHERMAP_PREFIX")

if LATITUDE is None:
  raise "OPENWEATHERMAP_LATITUDE var is empty"
if LONGITUDE is None:
  raise "OPENWEATHERMAP_LONGITUDE var is empty"
if API_KEY is None:
  raise "OPENWEATHERMAP_API_KEY var is empty"
if UNITS is None:
  UNITS = "metric"
if INTERVAL is None:
  INTERVAL = 600
if PREFIX is None:
  PREFIX = "weather"

params = {
  "lat": LATITUDE,
  "lon": LONGITUDE,
  "units": UNITS,
  "appid": API_KEY
}
baseurl = "https://api.openweathermap.org/data/2.5/weather"
content_type = str('text/plain; version=0.0.4; charset=utf-8')

labels = ["location_name", "location_country", "latitude", "longitude"]

# Create a metric to track time spent and requests made.
outside_current_temperature_celsius = Gauge('%s_current_temperature_celsius' % PREFIX,
          'Current temperature in celsius provided by openweathermap', labels)
outside_feelslike_temperature_celsius = Gauge('%s_feelslike_temperature_celsius' % PREFIX,
          'Feels like temperature in celsius provided by openweathermap', labels)
outside_min_temperature_celsius = Gauge('%s_min_temperature_celsius' % PREFIX,
          'Min temperature in celsius provided by openweathermap', labels)
outside_max_temperature_celsius = Gauge('%s_max_temperature_celsius' % PREFIX,
          'Min temperature in celsius provided by openweathermap', labels)
outside_pressure_pa = Gauge('%s_pressure_pa' % PREFIX,
          'Temperature in celsius provided by openweathermap', labels)
outside_humidity_percent = Gauge('%s_humidity_percent' % PREFIX,
          'Humidity in % provided by openweathermap', labels)
outside_weather_id = Gauge('%s_weather_id' % PREFIX,
          'Mapping provided by openweathermap at https://openweathermap.org/weather-conditions', labels)
outside_wind_speed = Gauge('%s_wind_speed' % PREFIX,
          'Wind speed in m/s provided by openweathermap', labels)
outside_wind_deg = Gauge('%s_wind_deg' % PREFIX,
          'Wind degree provided by openweathermap', labels)
outside_wind_gust = Gauge('%s_wind_gust' % PREFIX,
          'Wind gust speed in m/s provided by openweathermap', labels)
outside_clouds = Gauge('%s_clouds' % PREFIX,
          'Cloudiness % provided by openweathermap', labels)
outside_rain_1h = Gauge('%s_rain_1h' % PREFIX,
          '1h rain in mm provided by openweathermap', labels)
outside_rain_3h = Gauge('%s_rain_3h' % PREFIX,
          '3h rain in mm provided by openweathermap', labels)
outside_snow_1h = Gauge('%s_snow_1h' % PREFIX,
          '1h snow in mm provided by openweathermap', labels)
outside_snow_3h = Gauge('%s_snow_3h' % PREFIX,
          '3h snow in mm provided by openweathermap', labels)
outside_visibility = Gauge('%s_visibility' % PREFIX, 
          'Visibility provided by openweathermap', labels)
outside_sunrise = Gauge('%s_sunrise' % PREFIX, 
          'Sunrise time provided by openweathermap', labels)
outside_sunset = Gauge('%s_sunset' % PREFIX, 
          'Sunset time provided by openweathermap', labels)

def get_weather_data():
  response = requests.get(url=baseurl, params=params)
  response.raise_for_status()
  logging.info("Data fetched successfully, setting data in exporter")
  weather = response.json()
  loc_name = weather['name']
  loc_country = weather['sys']['country']

  if weather.get('main'):
    outside_current_temperature_celsius.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['temp']))
    outside_feelslike_temperature_celsius.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['feels_like']))
    outside_min_temperature_celsius.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['temp_min']))
    outside_max_temperature_celsius.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['temp_max']))
    outside_pressure_pa.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['pressure']))
    outside_humidity_percent.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['main']['humidity']))
  if weather.get('wind'):
    outside_wind_speed.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['wind']['speed']))
    outside_wind_deg.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['wind']['deg']))
    outside_wind_gust.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['wind']['gust']))
  if len(weather['weather']) > 0:
    outside_weather_id.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:d}'.format(weather['weather'][0]['id']))
  if weather.get('visibility'):
    outside_visibility.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['visibility']))
  if weather.get('clouds'):
    outside_clouds.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['clouds']['all']))
  if weather.get('sys'):
    outside_sunrise.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['sys']['sunrise']))
    outside_sunset.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['sys']['sunset']))
  if weather.get('rain'):
    if weather['rain'].get('1h'):
        outside_rain_1h.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['rain']['1h']))
    if weather['rain'].get('3h'):
        outside_rain_3h.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['rain']['3h']))
  else:
    outside_rain_1h.labels(loc_name, loc_country, LATITUDE, LONGITUDE).set(0)
    outside_rain_3h.labels(loc_name, loc_country, LATITUDE, LONGITUDE).set(0)
  if weather.get('snow'):
    if weather['snow'].get('1h'):
      outside_snow_1h.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['snow']['1h']))
    if weather['snow'].get('3h'):
      outside_snow_3h.labels(loc_name, loc_country, LATITUDE, LONGITUDE)\
          .set('{0:0.1f}'.format(weather['snow']['3h']))
  else:
    outside_snow_1h.labels(loc_name, loc_country, LATITUDE, LONGITUDE).set(0)
    outside_snow_3h.labels(loc_name, loc_country, LATITUDE, LONGITUDE).set(0)

if __name__ == '__main__':
  start_http_server(9200)
  logging.info("Server listening on port 9200")

  while True:
    logging.info("Fetching data from Weathermap...")
    get_weather_data()
    logging.info("Now sleeping for %d seconds" % INTERVAL)
    time.sleep(INTERVAL)