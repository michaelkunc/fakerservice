import unittest
import os
import json
from app import create_app


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

    def test_addresses(self):
        response = self.payload('/addresses/')
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(100, response['length'])
        self.assertEqual(
            set(['city', 'state_prov', 'postal_code', 'country', 'street_address']), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])
        response = self.payload('/addresses/?quantity=10')
        self.assertEqual(10, response['length'])

    def test_companies(self):
        response = self.payload('/companies/')
        self.assertEqual(response['status_code'], 200)
        self.assertEqual(100, response['length'])
        self.assertEqual(
            set(['company_name']), response['keys'])
        self.assertTrue(response['data'][0] != response['data'][1])
        response = self.payload('/companies/?quantity=10')
        self.assertEqual(10, response['length'])


if __name__ == '__main__':
    unittest.main()
