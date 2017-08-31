from flask_api import FlaskAPI
from flask import jsonify, request
from faker import Faker

data = Faker()

from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/addresses/', methods=['GET'])
    def addresses():
        quantity = request.args.get('quantity', 100)
        results = [{'street_address': data.street_address(
        ), 'city': data.city(), 'state_prov': data.state_abbr(), 'postal_code': data.postalcode(), 'country': data.country()}
            for i in range(0, int(quantity))]
        response = jsonify(results)
        response.status_code = 200
        return response

    return app
