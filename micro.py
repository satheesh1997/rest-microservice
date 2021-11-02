import os
import unittest


from app import blueprint
from app.main import create_app, db


app = create_app(os.getenv('ENV', 'development'))
app.register_blueprint(blueprint)
app.app_context().push()

