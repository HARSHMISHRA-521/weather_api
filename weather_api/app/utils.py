import requests
from flask import current_app
from . import db
from .models import Pincode, WeatherData
import logging

def get_lat_long(pincode):
    # Check if pincode exists in the database
    pincode_data = Pincode.query.filter_by(pincode=pincode).first()
    if pincode_data:
        return pincode_data.latitude, pincode_data.longitude

    # If not in DB, fetch from API
    api_key = current_app.config['OPENWEATHER_API_KEY']

    if not api_key:
        logging.error('OpenWeather API key is not set.')
        return None, None

    geocode_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={pincode},IN&appid={api_key}"
    response = requests.get(geocode_url)
    if response.status_code == 200:
        data = response.json()
        latitude = data.get('lat')
        longitude = data.get('lon')

        if latitude is None or longitude is None:
            logging.error('Latitude or Longitude not found in API response.')
            return None, None

        # Save to DB
        new_pincode = Pincode(pincode=pincode, latitude=latitude, longitude=longitude)
        db.session.add(new_pincode)
        db.session.commit()

        return latitude, longitude
    else:
        logging.error(f"Geocoding API failed with status code {response.status_code}")
        return None, None

def get_weather(latitude, longitude, date, pincode):
    # Check if weather data exists in the database
    weather_data = WeatherData.query.filter_by(pincode=pincode, date=date).first()
    if weather_data:
        return weather_data.weather_info

    # If not in DB, fetch from API
    api_key = current_app.config['OPENWEATHER_API_KEY']

    if not api_key:
        logging.error('OpenWeather API key is not set.')
        return None

    # OpenWeatherMap does not provide historical data for free, so we'll simulate this
    # For the purpose of this assignment, we'll fetch current weather data

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()

        # Save to DB
        new_weather = WeatherData(pincode=pincode, date=date, weather_info=data)
        db.session.add(new_weather)
        db.session.commit()

        return data
    else:
        logging.error(f"Weather API failed with status code {response.status_code}")
        return None
