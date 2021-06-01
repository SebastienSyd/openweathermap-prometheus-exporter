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
|OPENWEATHERMAP_LATITUDE|Location latitude|Required|N/A|
|OPENWEATHERMAP_LONGITUDE|Location longitude|Required|N/A|
|OPENWEATHERMAP_API_KEY|OpenWeatherMap API Key|Required|N/A|
|OPENWEATHERMAP_UNITS|Units (`standard`, `metric` and `imperial`)|Optional|`metric`|
|OPENWEATHERMAP_INTERVAL|Sampling time in seconds|Optional|`600`|
|OPENWEATHERMAP_PREFIX|Prefix of the metrics|Optional|`weather`|

### Metrics

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 89.0
python_gc_objects_collected_total{generation="1"} 260.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 53.0
python_gc_collections_total{generation="1"} 4.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="3",version="3.7.3"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 5.5156736e+07
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.882112e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.62255300689e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.51
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 9.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP weather_current_temperature_celsius Current temperature in celsius provided by openweathermap
# TYPE weather_current_temperature_celsius gauge
weather_current_temperature_celsius{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 11.3
# HELP weather_feelslike_temperature_celsius Feels like temperature in celsius provided by openweathermap
# TYPE weather_feelslike_temperature_celsius gauge
weather_feelslike_temperature_celsius{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 10.7
# HELP weather_min_temperature_celsius Min temperature in celsius provided by openweathermap
# TYPE weather_min_temperature_celsius gauge
weather_min_temperature_celsius{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 7.5
# HELP weather_max_temperature_celsius Min temperature in celsius provided by openweathermap
# TYPE weather_max_temperature_celsius gauge
weather_max_temperature_celsius{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 13.7
# HELP weather_pressure_pa Temperature in celsius provided by openweathermap
# TYPE weather_pressure_pa gauge
weather_pressure_pa{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 1022.0
# HELP weather_humidity_percent Humidity in % provided by openweathermap
# TYPE weather_humidity_percent gauge
weather_humidity_percent{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 85.0
# HELP weather_weather_id Mapping provided by openweathermap at https://openweathermap.org/weather-conditions
# TYPE weather_weather_id gauge
weather_weather_id{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 800.0
# HELP weather_wind_speed Wind speed in m/s provided by openweathermap
# TYPE weather_wind_speed gauge
weather_wind_speed{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 2.2
# HELP weather_wind_deg Wind degree provided by openweathermap
# TYPE weather_wind_deg gauge
weather_wind_deg{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 5.0
# HELP weather_wind_gust Wind gust speed in m/s provided by openweathermap
# TYPE weather_wind_gust gauge
weather_wind_gust{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 2.7
# HELP weather_clouds Cloudiness % provided by openweathermap
# TYPE weather_clouds gauge
weather_clouds{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 0.0
# HELP weather_rain_1h 1h rain in mm provided by openweathermap
# TYPE weather_rain_1h gauge
weather_rain_1h{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 0.0
# HELP weather_rain_3h 3h rain in mm provided by openweathermap
# TYPE weather_rain_3h gauge
weather_rain_3h{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 0.0
# HELP weather_snow_1h 1h snow in mm provided by openweathermap
# TYPE weather_snow_1h gauge
weather_snow_1h{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 0.0
# HELP weather_snow_3h 3h snow in mm provided by openweathermap
# TYPE weather_snow_3h gauge
weather_snow_3h{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 0.0
# HELP weather_visibility Visibility provided by openweathermap
# TYPE weather_visibility gauge
weather_visibility{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 10000.0
# HELP weather_sunrise Sunrise time provided by openweathermap
# TYPE weather_sunrise gauge
weather_sunrise{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 1.622494299e+09
# HELP weather_sunset Sunset time provided by openweathermap
# TYPE weather_sunset gauge
weather_sunset{latitude="-33.8637711",location_country="AU",location_name="Sydney",longitude="151.2061033"} 1.622530475e+09
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
