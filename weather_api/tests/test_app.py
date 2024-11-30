import unittest
import sys
import os

# Adjust the Python path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..app import create_app, db
from ..app.models import Pincode, WeatherData

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up a test client and an in-memory SQLite database for testing.
        """
        # Create an instance of the app for testing
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Clean up the database after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_missing_parameters(self):
        """
        Test the /weather endpoint with missing parameters.
        """
        response = self.client.get('/weather')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Please provide pincode and for_date parameters')

    def test_invalid_pincode(self):
        """
        Test the /weather endpoint with an invalid pincode.
        """
        response = self.client.get('/weather?pincode=000000&for_date=2020-10-15')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_valid_request(self):
        """
        Test the /weather endpoint with a valid request.
        """
        # Simulate a valid pincode and date
        pincode = '411014'
        for_date = '2020-10-15'

        # Mock data to simulate the database state
        with self.app.app_context():
            pincode_entry = Pincode(pincode=pincode, latitude=18.5204, longitude=73.8567)
            weather_entry = WeatherData(
                pincode=pincode,
                date=for_date,
                weather_info={'temp': 298.15, 'description': 'clear sky'}
            )
            db.session.add(pincode_entry)
            db.session.add(weather_entry)
            db.session.commit()

        # Send a request to the endpoint
        response = self.client.get(f'/weather?pincode={pincode}&for_date={for_date}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('weather', response.json)
        self.assertEqual(response.json['weather']['description'], 'clear sky')

    def test_nonexistent_pincode(self):
        """
        Test the /weather endpoint with a nonexistent pincode.
        """
        response = self.client.get('/weather?pincode=999999&for_date=2020-10-15')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
