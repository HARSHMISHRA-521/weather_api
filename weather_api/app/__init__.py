from flask import Flask
import sys
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Check if the OPENWEATHER_API_KEY is set
    if not app.config['OPENWEATHER_API_KEY']:
        sys.exit('Error: OPENWEATHER_API_KEY environment variable is not set.')

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .routes import weather_bp
    app.register_blueprint(weather_bp)

    with app.app_context():
        # Import models to register them with SQLAlchemy
        from . import models
        db.create_all()

    return app


# Expose db and create_app at the package level
__all__ = ['db', 'create_app']