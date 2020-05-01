import os
import sys
from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'messae': 'pong!'
        }


print(app.config, file=sys.stderr)
api.add_resource(Ping, '/ping')