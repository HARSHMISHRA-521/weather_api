# Weather Info API

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
  - [Endpoint: `/weather`](#endpoint-weather)
- [Testing](#testing)
- [Author](#author)
- [License](#license)

## Overview

The **Weather Info API** is a RESTful service that provides weather information for a given Indian pincode and specific date. The API optimizes external API calls by caching pincode-to-geolocation mappings and weather data in a relational database. This ensures efficient data retrieval and reduces the number of external API requests.

## Features

- **Single REST API Endpoint**: Fetch weather information based on pincode and date.
- **Caching Mechanism**: Stores pincode latitude and longitude, and weather data to minimize external API calls.
- **Database Integration**: Utilizes SQLite for data persistence.
- **Environment Variable Management**: Secures sensitive information using environment variables.
- **Unit Testing**: Ensures application reliability through comprehensive test cases.
- **Modular Code Structure**: Organized using Flask Blueprints for scalability and maintainability.

## Technologies Used

- **Python 3.8+**
- **Flask**
- **Flask SQLAlchemy**
- **Flask-Migrate**
- **SQLite**
- **Requests**
- **Python-dotenv**
- **Unittest**

## Project Structure

```doctest
weather_api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md

```

- **app/**: Contains the main application modules.
  - `__init__.py`: Initializes the Flask app, database, and migrations.
  - `config.py`: Handles configuration settings using environment variables.
  - `models.py`: Defines the database models.
  - `routes.py`: Contains the API endpoint routes.
  - `utils.py`: Includes utility functions for interacting with external APIs and the database.
- **tests/**: Contains unit tests for the application.
  - `__init__.py`: Marks the directory as a Python package.
  - `test_app.py`: Contains test cases for the API endpoints.
- **venv/**: Virtual environment directory (excluded from version control).
- **run.py**: Entry point to run the Flask application.
- **requirements.txt**: Lists all Python dependencies.
- **README.md**: Project documentation.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.env**: Stores environment variables (excluded from version control).

## Installation

### Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Git**: To clone the repository. Download Git from [here](https://git-scm.com/downloads).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/HARSHMISHRA-521/weather_api.git
   cd weather_api
   ```
## 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Unix or MacOS
python3 -m venv venv
source venv/bin/activate
```
## 3. Install Dependencies

With the virtual environment activated, install the required Python packages.

```doctest
pip install -r requirements.txt

```

## Configuration
The application uses environment variables to manage sensitive information like the secret key and OpenWeatherMap API key. These variables are stored in a .env file.

### Create a .env File
In the root directory of the project, create a .env file.

```doctest
touch .env

```
### Add Environment Variables
Open the .env file and add the following:

```doctest
SECRET_KEY=your_secret_key
OPENWEATHER_API_KEY=your_openweather_api_key

```
- SECRET_KEY: A secret key for Flask sessions. You can generate one using Python:
```doctest
import secrets
print(secrets.token_hex(16))

```
- OPENWEATHER_API_KEY: Your API key from [OpenWeatherMap](`https://home.openweathermap.org/api_keys`).

## Security Note
Do Not Commit `.env`: Ensure the `.env` file is included in .gitignore to prevent it from being pushed to version control.

```doctest
# .gitignore
venv/
__pycache__/
*.pyc
.env

```
## Running the Application
### Activate the Virtual Environment

```doctest
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate

```
### Run the Flask Application
```doctest
python run.py

```

The application will start on `http://127.0.0.1:5000/` by default.

## API Documentation

### Endpoint: `/weather`

- **Method**: GET

- **Description**: Fetches weather information for a specified pincode and date.

- **Parameters**:
  - `pincode` (string) - **Required**: The 6-digit Indian pincode.
  - `for_date` (string) - **Required**: The date for which weather information is requested in `YYYY-MM-DD` format.

- **Response**:

  - **Success (200 OK)**:

    ```json
    {
      "pincode": "411014",
      "date": "2020-10-15",
      "weather": {
        "coord": { "lon": 73.8567, "lat": 18.5204 },
        "weather": [
          {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
          }
        ],
        "base": "stations",
        "main": {
          "temp": 298.15,
          "feels_like": 298.15,
          "temp_min": 298.15,
          "temp_max": 298.15,
          "pressure": 1013,
          "humidity": 44
        },
        "visibility": 10000,
        "wind": { "speed": 1.5, "deg": 350 },
        "clouds": { "all": 1 },
        "dt": 1600000000,
        "sys": {
          "type": 1,
          "id": 9165,
          "country": "IN",
          "sunrise": 1600000000,
          "sunset": 1600000000
        },
        "timezone": 19800,
        "id": 1273294,
        "name": "Pune",
        "cod": 200
      }
    }
    ```

  - **Error Responses**:
    - **400 Bad Request**: Missing or invalid parameters.

      ```json
      {
        "error": "Please provide pincode and for_date parameters"
      }
      ```

      ```json
      {
        "error": "Invalid pincode or unable to fetch latitude and longitude"
      }
      ```

    - **500 Internal Server Error**: Unable to fetch weather information.

      ```json
      {
        "error": "Unable to fetch weather information"
      }
      ```

### Example Request

```bash
GET http://127.0.0.1:5000/weather?pincode=411014&for_date=2020-10-15
```
## Testing
The project includes unit tests to ensure the API functions as expected. Tests are written using Python's built-in` unittest` framework.

### Running Unit Tests
Ensure the Virtual Environment is Activated

```doctest
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate

```

### Run the Tests
Navigate to the project's root directory and execute:

```doctest
python -m unittest discover tests

```

### Expected Output:
```doctest
....
----------------------------------------------------------------------
Ran 4 tests in 0.123s

OK

```

## Test Cases Covered
- Missing Parameters: Ensures the API returns an error when required parameters are missing.
- Invalid Pincode: Tests the API's response to an invalid or nonexistent pincode.
- Valid Request: Checks if the API correctly returns weather information for valid inputs.
- Nonexistent Pincode: Verifies the API's behavior when the pincode does not exist in the database.

## Author

**Harsh Mishra**  
[GitHub](https://github.com/HARSHMISHRA-521) | [LinkedIn](http://www.linkedin.com/in/mishraharsh-hmc) | [Portfolio](https://harshmishra-521.github.io/MY-PORTFOLIO/) | [Resume](https://drive.google.com/drive/folders/1pGK1alOqsBhG7oRoVjr_QeOQf72o4TzL?usp=sharing) | [Medium](https://medium.com/@HARSHMISHRA_HMC) | [Replit](https://replit.com/@HARSHMISHRA34) | [Twitter](https://x.com/harsh_mishra___)

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note**: Replace `your_secret_key` and `your_openweather_api_key` in the `.env` file with your actual secret key and OpenWeatherMap API key, respectively.
