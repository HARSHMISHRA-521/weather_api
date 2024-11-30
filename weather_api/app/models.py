from . import db

class Pincode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pincode = db.Column(db.String(10), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pincode = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    weather_info = db.Column(db.JSON, nullable=False)
