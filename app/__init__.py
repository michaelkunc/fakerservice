from flask_api import FlaskAPI
from flask import jsonify, request
from faker import Faker

data = Faker()

from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    def _response(results):
        response = jsonify(results)
        response.status_code = 200
        return response

    def _quantity():
        return range(0, int(request.args.get('quantity', 100)))

    @app.route('/addresses/', methods=['GET'])
    def addresses():
        return _response([{'street_address': data.street_address(),
                           'city': data.city(), 'state_prov': data.state_abbr(),
                           'postal_code': data.postalcode(), 'country': data.country()}
                          for i in _quantity()])

    @app.route('/companies/', methods=['GET'])
    def companies():
        return _response([{'company_name': '{0} {1}'.format(data.company(), data.company_suffix()),
                           'slogan': data.catch_phrase()}
                          for i in _quantity()])

    @app.route('/license_plates/', methods=['GET'])
    def license_plates():
        return _response([{'license_plate': data.license_plate()} for i in _quantity()])

    @app.route('/people/', methods=['GET'])
    def people():
        return _response([data.profile(fields=['address', 'birthdate', 'company', 'job', 'mail', 'name']) for i in _quantity()])
    return app
