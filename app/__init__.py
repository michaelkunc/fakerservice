
from flask_api import FlaskAPI
from flask import jsonify, request, render_template
from faker import Faker
from flasgger import Swagger, swag_from

data = Faker()

from instance.config import app_config, swagger_template
from app import endpoints as ep


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    swagger = Swagger(app, template=swagger_template)

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

    def _single_field(property, data):
        return _response([{property[0]: data()} for i in _limit()])

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/whoami')
    def whoami():
        return render_template('whoami.html')

    @app.route(ep.addresses.url, methods=['GET'])
    @swag_from(ep.addresses.docs)
    def addresses():
        return _response([{'street_address': data.street_address(),
                           'city': data.city(), 'state_prov': data.state_abbr(),
                           'postal_code': data.postalcode(), 'country': data.country()} for i in _limit()])

    @app.route(ep.country.url, methods=['GET'])
    @swag_from(ep.country.docs)
    def country():
        return _single_field(ep.country.properties,
                             ep.country.data)

    @app.route(ep.country_code.url, methods=['GET'])
    @swag_from(ep.country_code.docs)
    def country_code():
        return _single_field(ep.country_code.properties,
                             ep.country_code.data)

    @app.route(ep.military_state.url, methods=['GET'])
    @swag_from(ep.military_state.docs)
    def military_state():
        return _single_field(ep.military_state.properties, ep.military_state.data)

    @app.route(ep.military_ship.url, methods=['GET'])
    @swag_from(ep.military_ship.docs)
    def military_ship():
        return _single_field(ep.military_ship.properties, ep.military_ship.data)

    @app.route(ep.state_abbr.url, methods=['GET'])
    @swag_from(ep.state_abbr.docs)
    def state_abbr():
        return _single_field(ep.state_abbr.properties, ep.state_abbr.data)

    @app.route(ep.street_address.url, methods=['GET'])
    @swag_from(ep.street_address.docs)
    def street_address():
        return _single_field(ep.street_address.properties, ep.street_address.data)

    @app.route(ep.companies.url, methods=['GET'])
    @swag_from(ep.companies.docs)
    def companies():
        return _response([{'company_name': '{0} {1}'.format(data.company(), data.company_suffix()),
                           'slogan': data.catch_phrase()}
                          for i in _limit()])

    @app.route(ep.license_plates.url, methods=['GET'])
    @swag_from(ep.license_plates.docs)
    def license_plates():
        return _single_field(ep.license_plates.properties, ep.license_plates.data)

    @app.route(ep.people.url, methods=['GET'])
    @swag_from(ep.people.docs)
    def people():
        return _response([data.profile(fields=['address', 'birthdate',
                                               'company', 'job', 'mail', 'name']) for i in _limit()])

    @app.route(ep.credit_cards.url, methods=['GET'])
    @swag_from(ep.credit_cards.docs)
    def credit_cards():
        return _single_field(ep.credit_cards.properties, ep.credit_cards.data)

    @app.route(ep.credit_card_security_code.url, methods=['GET'])
    @swag_from(ep.credit_card_security_code.docs)
    def credit_card_security_code():
        return _single_field(ep.credit_card_security_code.properties, ep.credit_card_security_code.data)

    @app.route(ep.credit_card_expire.url, methods=['GET'])
    @swag_from(ep.credit_card_expire.docs)
    def credit_card_expire():
        return _single_field(ep.credit_card_expire.properties, ep.credit_card_expire.data)

    @app.route(ep.url.url, methods=['GET'])
    @swag_from(ep.url.docs)
    def url():
        return _single_field(ep.url.properties, ep.url.data)

    @app.route(ep.email.url, methods=['GET'])
    @swag_from(ep.email.docs)
    def email():
        return _single_field(ep.email.properties, ep.email.data)

    @app.route(ep.mac_address.url, methods=['GET'])
    @swag_from(ep.mac_address.docs)
    def mac_address():
        return _single_field(ep.mac_address.properties, ep.mac_address.data)

    @app.route(ep.username.url, methods=['GET'])
    @swag_from(ep.username.docs)
    def username():
        return _single_field(ep.username.properties, ep.username.data)

    @app.route(ep.image_url.url, methods=['GET'])
    @swag_from(ep.image_url.docs)
    def image_url():
        return _single_field(ep.image_url.properties, ep.image_url.data)

    @app.route(ep.ipv4.url, methods=['GET'])
    @swag_from(ep.ipv4.docs)
    def ipv4():
        return _response([{'ip': data.ipv4(network=False)} for i in _limit()])

    @app.route(ep.password.url, methods=['GET'])
    @swag_from(ep.password.docs)
    def password():
        return _response([{'password': data.password(length=10, special_chars=True, digits=True,
                                                     upper_case=True, lower_case=True)} for i in _limit()])

    @app.route(ep.rgb_color.url, methods=['GET'])
    @swag_from(ep.rgb_color.docs)
    def rgb_color():
        return _single_field(ep.rgb_color.properties, ep.rgb_color.data)

    @app.route(ep.color_name.url, methods=['GET'])
    @swag_from(ep.color_name.docs)
    def color_name():
        return _single_field(ep.color_name.properties, ep.color_name.data)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    return app
