from flask import Flask

from commonlib.initproperties import InitProperties
from foobar.hello import world, create_json_response_object

app_prop = InitProperties('WebApp.ini')
app = Flask(__name__)


@app.route("/")
def index():
    return "some landing page"


@app.route("/foobar")
def foobar_page():
    dummy_json = {
        'key1': 'value1',
        'key2': 2
    }
    json_response = create_json_response_object(dummy_json)
    return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
