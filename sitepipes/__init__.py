from sitepipes.config import init_config, init_log

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_migrate import Migrate
from flasgger import Swagger


config = init_config()
log = init_log('log')

cors = CORS()
db = PyMongo()
login_manager = LoginManager()
migrate = Migrate()
swagger = Swagger()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False, static_url_path='')

    app.config.from_object('sitepipes.config.AppConfig')

    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)
    swagger.init_app(app)

    with app.app_context():
        # MUST import libraries here to avoid circular dependencies
        from sitepipes.routes import models

        app.register_blueprint(models.models)

    return app
