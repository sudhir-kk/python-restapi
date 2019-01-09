"""/src/app.py"""
import socket
import os
from flask import Flask
from flasgger import Swagger
from werkzeug.routing import BaseConverter
from .config import app_config
from .models import db, bcrypt
from .globalconfigviews.globalconfigview import globalconfig_api


class ListConverter(BaseConverter):
    """List Converter"""
    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)for value in values)


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
port = os.getenv('PORT')
var = IPAddr + ":" + port

template = {"swagger": "2.0",
            "info": {"title": "GlobalConfig API with Python",
                     "description": "API for ICP Ancillary services",
                     "version": "0.0.1"}, "host": var,
            "schemes": ["http", "https"],
            "operationId": "globalConfigId"}


def create_app(env_name):
    """
  Create application
  """
    # app initiliazation
    app = Flask(__name__)
    Swagger(app, template=template)
    app.config.from_object(app_config[env_name])
    app.url_map.converters['list'] = ListConverter

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)
    app.register_blueprint(globalconfig_api, url_prefix='/globalconfig')

    @app.route('/actuator/health', methods=['GET'])
    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
    """
        return 'Welcome to Python Flask Microservice API for Global Config Service' + str(
            hostname) + ' IP Addr is ' + str(IPAddr)

    return app
