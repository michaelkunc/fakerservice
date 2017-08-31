import unittest
import os
import json
from app import create_app


endpoints = {'addresses': {'url': '/addresses/',
                           'properties': ['city', 'state_prov', 'postal_code', 'country', 'street_address']},
             'companies': {'url': '/companies/',
                           'properties': ['company_name']}}


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

    def endpoint_test(self, url, properties):
        response = self.payload(url)
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(100, response['length'])
        self.assertEqual(
            set(properties), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])
        response = self.payload("{}?quantity=10".format(url))
        self.assertEqual(10, response['length'])

    def test_addresses(self):
        self.endpoint_test(
            endpoints['addresses']['url'], endpoints['addresses']['properties'])

    def test_companies(self):
        self.endpoint_test(endpoints['companies']['url'], endpoints[
                           'companies']['properties'])

if __name__ == '__main__':
    unittest.main()
