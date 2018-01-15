# -*- coding = utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string

from config import Config


def create_app():

    app = Flask("demo")

    app.config.from_object(Config)
    config_blueprint(app)

    return app


def config_blueprint(application):

    """

    :type application: Flask
    """
    for bp in Config.BLUEPRINTS:
        bp = import_string(bp)
        application.register_blueprint(bp)
