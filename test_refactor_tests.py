import unittest
import json
from app import create_app, endpoints


class StatusTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

    def test_status_code(self):
        for e in endpoints.endpoint_list:
            response = self.client().get(e.url)
            with self.subTest():
                self.assertEqual(response.status_code, 200, e.name)

    def test_default_length(self):
        for e in endpoints.endpoint_list:
            response = self.client().get(e.url)
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest():
                self.assertEqual(length, 100, e.name)

    def test_length_equals_10(self):
        for e in endpoints.endpoint_list:
            response = self.client().get("{}?limit=10".format(e.url))
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest():
                self.assertEqual(length, 10, e.name)

    def test_length_past_max(self):
        for e in endpoints.endpoint_list:
            response = self.client().get("{}?limit=5001".format(e.url))
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest():
                self.assertEqual(length, 100, e.name)

    def test_properties(self):
        for e in endpoints.endpoint_list:
            response = self.client().get(e.url)
            data = json.loads(response.get_data(as_text=True))
            keys = set(data[0].keys())
            with self.subTest():
                self.assertEqual(set(e.properties), keys, e.name)

    def test_unique_values(self):
        for e in endpoints.endpoint_list:
            response = self.client().get(e.url)
            data = json.loads(response.get_data(as_text=True))
            values = [d.values() for d in data]
            with self.subTest():
                self.assertTrue(len(set(values)) > 1, e.name)

if __name__ == '__main__':
    unittest.main()
