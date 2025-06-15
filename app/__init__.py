import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

# Initialize extensions
wvar_db = SQLAlchemy()
wvar_login_manager = LoginManager()
wvar_login_manager.login_view = 'wr_auth.login'

def wfun_create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    wvar_db.init_app(app)
    wvar_login_manager.init_app(app)
    
    # Setup logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(
        app.config['LOG_FILE'],
        maxBytes=10240,
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Application startup')
    
    # Register blueprints
    from .main import wvar_main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import wvar_auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    # Add security headers
    @app.after_request
    def wfun_add_security_headers(response):
        for header, value in app.config['SECURITY_HEADERS'].items():
            response.headers[header] = value
        return response
    
    # Error handlers
    @app.errorhandler(404)
    def wfun_not_found_error(error):
        return 'Page not found', 404
    
    @app.errorhandler(500)
    def wfun_internal_error(error):
        wvar_db.session.rollback()
        return 'Internal server error', 500
    
    return app 