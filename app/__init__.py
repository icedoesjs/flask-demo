from flask import Flask
site = Flask(__name__)
from config import Config

configuration = Config()
site.config['FAVORITE_PEOPLE'] = configuration.favorite_people

from . import routes