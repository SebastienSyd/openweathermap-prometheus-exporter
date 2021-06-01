## Description

Python implementation of a Prometheus exporter for the OpenWeatherMap service.

For this service to work, you need to sign up on the website and retrieve your API key.

## Build image

`docker build --tag openweathermap-prometheus-exporter .`

## Configuration

### Variables

The container accepts a few parameters to work:
| Name | Description | Required | Default |
|---|---|---|---|
|OPENWEATHERMAP_LATITUDE|Location latitude|Required (with OPENWEATHERMAP_LONGITUDE)|N/A|
|OPENWEATHERMAP_LONGITUDE|Location longitude|Required (with OPENWEATHERMAP_LATITUDE)|N/A|
|OPENWEATHERMAP_CITY|Location name |Required (not in conjunction with OPENWEATHERMAP_LONGITUDE/OPENWEATHERMAP_LATITUDE)|N/A|
|OPENWEATHERMAP_API_KEY|OpenWeatherMap API Key|Required|N/A|
|OPENWEATHERMAP_UNITS|Units (`standard`, `metric` and `imperial`)|Optional|`metric`|
|OPENWEATHERMAP_INTERVAL|Sampling time in seconds|Optional|`600`|
|OPENWEATHERMAP_PREFIX|Prefix of the metrics|Optional|`weather`|
||||

### Labels

| Name | Description |
|---|---|
|location_name|Name of the location|
|location_country|Name of the country|
|latitude|Latitude|
|longitude|Longitude|
|location_id|OpenWeatherMap location id|
|||

### Metrics

```
# HELP weather_current_temperature_celsius Current temperature in celsius provided by openweathermap
# TYPE weather_current_temperature_celsius gauge
weather_current_temperature_celsius{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 11.0
# HELP weather_feelslike_temperature_celsius Feels like temperature in celsius provided by openweathermap
# TYPE weather_feelslike_temperature_celsius gauge
weather_feelslike_temperature_celsius{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 10.3
# HELP weather_min_temperature_celsius Min temperature in celsius provided by openweathermap
# TYPE weather_min_temperature_celsius gauge
weather_min_temperature_celsius{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 6.7
# HELP weather_max_temperature_celsius Min temperature in celsius provided by openweathermap
# TYPE weather_max_temperature_celsius gauge
weather_max_temperature_celsius{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 13.6
# HELP weather_pressure_pa Temperature in celsius provided by openweathermap
# TYPE weather_pressure_pa gauge
weather_pressure_pa{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 1022.0
# HELP weather_humidity_percent Humidity in % provided by openweathermap
# TYPE weather_humidity_percent gauge
weather_humidity_percent{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 84.0
# HELP weather_weather_id Mapping provided by openweathermap at https://openweathermap.org/weather-conditions
# TYPE weather_weather_id gauge
weather_weather_id{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 800.0
# HELP weather_wind_speed Wind speed in m/s provided by openweathermap
# TYPE weather_wind_speed gauge
weather_wind_speed{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 3.1
# HELP weather_wind_deg Wind degree provided by openweathermap
# TYPE weather_wind_deg gauge
weather_wind_deg{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 300.0
# HELP weather_wind_gust Wind gust speed in m/s provided by openweathermap
# TYPE weather_wind_gust gauge
weather_wind_gust{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_clouds Cloudiness % provided by openweathermap
# TYPE weather_clouds gauge
weather_clouds{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_rain_1h 1h rain in mm provided by openweathermap
# TYPE weather_rain_1h gauge
weather_rain_1h{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_rain_3h 3h rain in mm provided by openweathermap
# TYPE weather_rain_3h gauge
weather_rain_3h{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_snow_1h 1h snow in mm provided by openweathermap
# TYPE weather_snow_1h gauge
weather_snow_1h{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_snow_3h 3h snow in mm provided by openweathermap
# TYPE weather_snow_3h gauge
weather_snow_3h{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 0.0
# HELP weather_visibility Visibility provided by openweathermap
# TYPE weather_visibility gauge
weather_visibility{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 10000.0
# HELP weather_sunrise Sunrise time provided by openweathermap
# TYPE weather_sunrise gauge
weather_sunrise{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 1.6224943e+09
# HELP weather_sunset Sunset time provided by openweathermap
# TYPE weather_sunset gauge
weather_sunset{latitude="-33.8679",location_country="AU",location_id="2010638",location_name="Sydney",longitude="151.2073"} 1.622530475e+09
```

## Run container

### Docker

You will need to build the image first, then:

```
docker run -d \
  -p 9200:9200 \
  -e OPENWEATHERMAP_LATITUDE=-33.8567844 \
  -e OPENWEATHERMAP_LONGITUDE=151.213108 \
  -e OPENWEATHERMAP_API_KEY=8454bcd.... \
  -e OPENWEATHERMAP_UNITS=metric \
  -e OPENWEATHERMAP_PREFIX=outside \
  --name openweathermap \
  openweathermap-prometheus-exporter
```

### Docker-compose

You will need to build the image first, then:

```
version: '3.4'
services:
  openweathermap:
    image: openweathermap-prometheus-exporter
    container_name: openweathermap
    restart: 'unless-stopped'
    ports:
    - "9200:9200"
    environment:
      OPENWEATHERMAP_LATITUDE: -33.8567844
      OPENWEATHERMAP_LONGITUDE: 151.213108
      OPENWEATHERMAP_API_KEY: 8454bcd....
      OPENWEATHERMAP_UNITS: metric
      OPENWEATHERMAP_PREFIX: outside
```
