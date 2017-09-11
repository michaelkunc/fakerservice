from flask_api import FlaskAPI
from flask import jsonify, request, render_template
from faker import Faker
from flasgger import Swagger, swag_from

data = Faker()

from instance.config import app_config
from app import endpoints


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    swagger = Swagger(app)

    def _response(results):
        response = jsonify(results)
        response.status_code = 200
        return response

    def _limit():
        max_records = 5000
        requested_records = int(request.args.get('limit', 100))
        if requested_records <= max_records:
            return range(0, requested_records)
        else:
            return range(0, 100)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route(endpoints.addresses.url, methods=['GET'])
    @swag_from(endpoints.addresses.docs)
    def addresses():
        return _response([{'street_address': data.street_address(),
                           'city': data.city(), 'state_prov': data.state_abbr(),
                           'postal_code': data.postalcode(), 'country': data.country()} for i in _limit()])

    @app.route(endpoints.companies.url, methods=['GET'])
    @swag_from(endpoints.companies.docs)
    def companies():
        return _response([{'company_name': '{0} {1}'.format(data.company(), data.company_suffix()),
                           'slogan': data.catch_phrase()}
                          for i in _limit()])

    @app.route(endpoints.license_plates.url, methods=['GET'])
    @swag_from(endpoints.license_plates.docs)
    def license_plates():
        return _response([{'license_plate': data.license_plate()} for i in
                          _limit()])

    @app.route(endpoints.people.url, methods=['GET'])
    @swag_from(endpoints.people.docs)
    def people():
        return _response([data.profile(fields=['address', 'birthdate',
                                               'company', 'job', 'mail', 'name']) for i in _limit()])

    @app.route(endpoints.credit_cards.url, methods=['GET'])
    @swag_from(endpoints.credit_cards.docs)
    def credit_cards():
        return _response([{'full_card_detail': data.credit_card_full()} for i in _limit()])

    @app.route(endpoints.url.url, methods=['GET'])
    @swag_from(endpoints.url.docs)
    def url():
        return _response([{'url': data.url()} for i in _limit()])

    @app.route(endpoints.email.url, methods=['GET'])
    @swag_from(endpoints.email.docs)
    def email():
        return _response([{'email': data.email()} for i in _limit()])

    @app.route(endpoints.mac_address.url, methods=['GET'])
    @swag_from(endpoints.mac_address.docs)
    def mac_address():
        return _response([{'mac_address': data.mac_address()} for i in _limit()])

    @app.route(endpoints.username.url, methods=['GET'])
    @swag_from(endpoints.username.docs)
    def username():
        return _response([{'username': data.user_name()} for i in _limit()])

    @app.route(endpoints.image_url.url, methods=['GET'])
    @swag_from(endpoints.image_url.docs)
    def image_url():
        return _response([{'url': data.image_url()} for i in _limit()])

    @app.route(endpoints.ipv4.url, methods=['GET'])
    @swag_from(endpoints.ipv4.docs)
    def ipv4():
        return _response([{'ip': data.ipv4(network=False)} for i in _limit()])

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    return app
