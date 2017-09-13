import unittest
import json
from app import create_app, endpoints


class FakerServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

    def payload(self, url):
        response = self.client().get(url)
        data = json.loads(response.get_data(as_text=True))
        keys = set(data[0].keys())
        length = len(json.loads(response.get_data(as_text=True)))
        return {'response': response, 'keys': keys, 'length': length, 'data': data, 'status_code': response.status_code}

    def case(self, url, properties):
        response = self.payload(url)
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(100, response['length'])
        self.assertEqual(
            set(properties), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])

        response = self.payload("{}?limit=10".format(url))
        self.assertEqual(10, response['length'])

        response = self.payload("{}?limit=5001".format(url))
        self.assertEqual(100, response['length'])

    def test_addresses(self):
        self.case(endpoints.addresses.url, endpoints.addresses.properties)

    def test_addresses_country_codes(self):
        self.case(endpoints.country_code.url,
                  endpoints.country_code.properties)

    def test_addresses_military_state(self):
        response = self.payload(endpoints.military_state.url)
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(3, response['length'])
        self.assertEqual(
            set(endpoints.military_state.properties), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])

    def test_addresses_military_ship(self):
        response = self.payload(endpoints.military_ship.url)
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(4, response['length'])
        self.assertEqual(
            set(endpoints.military_ship.properties), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])

    def test_companies(self):
        self.case(endpoints.companies.url, endpoints.companies.properties)

    def test_license_plates(self):
        self.case(endpoints.license_plates.url,
                  endpoints.license_plates.properties)

    def test_people(self):
        self.case(endpoints.people.url, endpoints.people.properties)

    def test_credit_cards(self):
        self.case(endpoints.credit_cards.url,
                  endpoints.credit_cards.properties)

    def test_internet_url(self):
        self.case(endpoints.url.url,
                  endpoints.url.properties)

    def test_internet_email(self):
        self.case(endpoints.email.url,
                  endpoints.email.properties)

    def test_internet_mac_addresses(self):
        self.case(endpoints.mac_address.url,
                  endpoints.mac_address.properties)

    def test_internet_usernames(self):
        self.case(endpoints.username.url,
                  endpoints.username.properties)

    def test_internet_image_urls(self):
        self.case(endpoints.image_url.url,
                  endpoints.image_url.properties)

    def test_internet_ipv4(self):
        self.case(endpoints.ipv4.url,
                  endpoints.ipv4.properties)

    def test_internet_passwords(self):
        self.case(endpoints.password.url,
                  endpoints.password.properties)

    def test_docs(self):
        response = self.client().get('/apidocs/#')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
