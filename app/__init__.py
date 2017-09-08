from flask_api import FlaskAPI
from flask import jsonify, request
from faker import Faker
from flasgger import Swagger, swag_from
import collections

data = Faker()

from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    swagger = Swagger(app)
    Endpoint = collections.namedtuple('Endpoint', 'url docs')
    addresses = Endpoint(url='/addresses/', docs='../docs/addresses.yml')
    companies = Endpoint(url='/companies/', docs='../docs/companies.yml')
    license_plates = Endpoint(url='/license_plates/',
                              docs='../docs/license_plates.yml')
    people = Endpoint(url='/people/', docs='../docs/people.yml')

    def _response(results):
        response = jsonify(results)
        response.status_code = 200
        return response

    def _quantity():
        max_records = 5000
        requested_records = int(request.args.get('quantity', 100))
        if requested_records <= max_records:
            return range(0, requested_records)
        else:
            return range(0, 100)

    @app.route(addresses.url, methods=['GET'])
    @swag_from(addresses.docs)
    def addresses():
        return _response([{'street_address': data.street_address(),
                           'city': data.city(), 'state_prov': data.state_abbr(),
                           'postal_code': data.postalcode(), 'country': data.country()}
                          for i in _quantity()])

    @app.route(companies.url, methods=['GET'])
    @swag_from(companies.docs)
    def companies():
        return _response([{'company_name': '{0} {1}'.format(data.company(), data.company_suffix()),
                           'slogan': data.catch_phrase()}
                          for i in _quantity()])

    @app.route(license_plates.url, methods=['GET'])
    @swag_from(license_plates.docs)
    def license_plates():
        return _response([{'license_plate': data.license_plate()} for i in _quantity()])

    @app.route(people.url, methods=['GET'])
    @swag_from(people.docs)
    def people():
        return _response([data.profile(fields=['address', 'birthdate', 'company', 'job', 'mail', 'name']) for i in _quantity()])

    return app
