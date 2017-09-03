import unittest
import json
from app import create_app


endpoints = {'addresses': {'url': '/addresses/',
                           'properties': ['city', 'state_prov', 'postal_code', 'country', 'street_address']},
             'companies': {'url': '/companies/',
                           'properties': ['company_name', 'slogan']},
             'license_plates': {'url': '/license_plates/', 'properties': ['license_plate']},
             'people': {'url': '/people/', 'properties': ['address', 'birthdate', 'company', 'mail', 'name', 'job']}}


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
        response = self.payload("{}?quantity=10".format(url))
        self.assertEqual(10, response['length'])

    def test_addresses(self):
        self.case(
            endpoints['addresses']['url'], endpoints['addresses']['properties'])

    def test_companies(self):
        self.case(endpoints['companies']['url'], endpoints[
            'companies']['properties'])

    def test_license_plates(self):
        self.case(endpoints['license_plates']['url'], endpoints[
            'license_plates']['properties'])

    def test_people(self):
        self.case(endpoints['people']['url'], endpoints[
            'people']['properties'])

    def test_docs(self):
        response = self.client().get('/apidocs/#')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
