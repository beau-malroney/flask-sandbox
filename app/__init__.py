# app/__init__.py

# third-party imports
from flask import Flask, abort, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from utils import name_logger
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    logger = name_logger(__name__)
    app = Flask(__name__, instance_relative_config=True)
    try:
        app.config.from_object(app_config[config_name])
    except:
        logger.critical(f'Unable to locate config -- {config_name}')
        exit(1)
    try:
        app.config.from_pyfile('config.py')
    except:
        logger.critical(f"Unable to locate config.py")
        exit(1)

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    @app.route('/500')
    def error():
        abort(500)    
    
    return app