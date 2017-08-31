import unittest
import os
import json
from app import create_app


class FakerServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

    def test_addresses(self):
        response = self.client().get('/addresses/')
        keys = set(json.loads(response.get_data(as_text=True))[0].keys())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(100, len(json.loads(response.get_data(as_text=True))))
        self.assertEqual(
            set(['city', 'state_prov', 'postal_code', 'country', 'street_address']), keys)

    def test_addresses_with_quantity(self):
        response = self.client().get('/addresses/?quantity=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(10, len(json.loads(response.get_data(as_text=True))))

    def test_addresses_return_unique_results(self):
        response = self.client().get('/addresses/?quantity=2')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data[0] == data[1])

if __name__ == '__main__':
    unittest.main()
