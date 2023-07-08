from flask import Response
from commonlib.initproperties import InitProperties, from_init
import json
import socket


def world():
    return from_init()


def create_json_response_object(body):
    response_object = Response(
        response=json.dumps(body),
        mimetype='application/json'
    )
    response_object.headers['Trace'] = socket.gethostname()
    return response_object



