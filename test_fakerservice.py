import unittest
import json
from app import create_app
import collections

Endpoint = collections.namedtuple('Endpoint', 'url properties')
addresses = Endpoint(url='/addresses/',
                     properties=('city', 'state_prov', 'postal_code', 'country', 'street_address'))
companies = Endpoint(url='/companies/',
                     properties=('company_name', 'slogan'))
license_plates = Endpoint(url='/license_plates/',
                          properties=(['license_plate']))
people = Endpoint(url='/people/',
                  properties=('address', 'birthdate', 'company', 'mail', 'name', 'job'))


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
        self.case(addresses.url, addresses.properties)

    def test_companies(self):
        self.case(companies.url, companies.properties)

    def test_license_plates(self):
        self.case(license_plates.url, license_plates.properties)

    def test_people(self):
        self.case(people.url, people.properties)

    def test_docs(self):
        response = self.client().get('/apidocs/#')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
