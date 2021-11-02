from datetime import datetime

from flask import request
from flask_restx import Namespace, Resource


api = Namespace('service', description='service related operations')


@api.route("/ping/")
class Ping(Resource):
    def get(self):
        return {"status": "OK"}
