from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()

def create_app(config_name):

	app=Flask(__name__)

	# Creating the app configurations
	app.config.from_object(config_options[config_name])

	# Initializing flask extensions
	bootstrap.init_app(app)

	#registering blue print
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .requests import configure_request
	configure_request(app)

	return app

# from app import views