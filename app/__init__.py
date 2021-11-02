import os

from flask_restx import Api
from flask import Blueprint

from .main.controller.service_controller import api as service_ns


blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title=os.getenv('MCS_SERVICE', 'MCS MicroService'),
    version=os.getenv('VERSION', '0.1'),
)


###################### Namespaces #########################
api.add_namespace(service_ns)
