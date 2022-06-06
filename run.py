# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")
    
# @app.route("/about")
# def about():
#     return render_template("about.html")
    
# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)

# run.py

from os import getenv
from utils import init_logging, name_logger

from app import create_app

config_name = getenv('FLASK_CONFIG')

# create logger
logger = init_logging(True, 10, __name__)

logger.debug(f"Current FLASK_CONFIG: {config_name}")

app = create_app(config_name)

if __name__ == '__main__':
    #Should never get here - remove this
    if(config_name != 'production'):
        logger.warn("Time to app.run")
    app.run()