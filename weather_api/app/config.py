import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenWeatherMap API Key
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
