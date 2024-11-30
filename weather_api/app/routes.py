from flask import Blueprint, request, jsonify
from .utils import get_lat_long, get_weather

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/weather', methods=['GET'])
def get_weather_info():
    pincode = request.args.get('pincode')
    date = request.args.get('for_date')

    if not pincode or not date:
        return jsonify({'error': 'Please provide pincode and for_date parameters'}), 400

    latitude, longitude = get_lat_long(pincode)
    if latitude is None or longitude is None:
        return jsonify({'error': 'Invalid pincode or unable to fetch latitude and longitude'}), 400

    weather_info = get_weather(latitude, longitude, date, pincode)
    if weather_info is None:
        return jsonify({'error': 'Unable to fetch weather information'}), 500

    return jsonify({'pincode': pincode, 'date': date, 'weather': weather_info})
