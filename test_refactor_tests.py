import unittest
import json
from app import create_app, new_endpoints


class StatusTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

    def test_status_code(self):
        for e in new_endpoints.endpoint_list:
            response = self.client().get(e.url)
            name = e.name
            with self.subTest(name=name):
                self.assertEqual(response.status_code, 200, name)

    def test_default_length(self):
        for e in new_endpoints.endpoint_list:
            response = self.client().get(e.url)
            name = e.name
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest(name=name):
                self.assertEqual(length, 100, name)

    def test_length_equals_10(self):
        for e in new_endpoints.endpoint_list:
            response = self.client().get("{}?limit=10".format(e.url))
            name = e.name
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest(name=name):
                self.assertEqual(length, 10, name)

    def test_length_past_max(self):
        for e in new_endpoints.endpoint_list:
            response = self.client().get("{}?limit=5001".format(e.url))
            name = e.name
            length = len(json.loads(response.get_data(as_text=True)))
            with self.subTest(name=name):
                self.assertEqual(length, 100, name)

    def test_properties(self):
        for e in new_endpoints.endpoint_list:
            name = e.name
            response = self.client().get(e.url)
            data = json.loads(response.get_data(as_text=True))
            keys = set(data[0].keys())
            with self.subTest(name=name):
                self.assertEqual(set(e.properties), keys, name)


if __name__ == '__main__':
    unittest.main()
